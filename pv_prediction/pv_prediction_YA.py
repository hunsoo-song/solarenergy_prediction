#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import absolute_import, division, print_function, unicode_literals
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import os
os.chdir("C:\\Users\\Hunsoo\\Desktop\\regression_practice\\Data")
dataset_path = os.path.join(os.getcwd(),"pvprediction_yeongam")
dataset_path


# In[2]:


raw_dataset = pd.read_csv('pvprediction_yeongam.txt',sep="\t", header=0)
raw_dataset.head()


# In[3]:


raw_dataset.shape


# In[4]:


raw_dataset.drop(raw_dataset[raw_dataset.clock<9].index,inplace=True)
raw_dataset.drop(raw_dataset[raw_dataset.clock>19].index,inplace=True)


# In[5]:


raw_dataset.shape


# In[6]:


raw_dataset.head()


# In[7]:


fields_to_drop = ['windspeed','cloud','lowcloud','pv-2h','pv+1h','pv+5h','pv+3h','pv+4h','point','year','sunshine','locarpressure','temp','irradiation','lst','snow','pv-3h','winddirection','humidity','vaporpressure','dewpointtemperature','seasurfacepressure','sijung','temp5cm','temp10cm','temp20','temp30cm','pv-5h','pv-4h']

data = raw_dataset.drop(fields_to_drop, axis=1)
data.head()

dataset = data.copy()
dataset.tail()


# In[8]:


dataset.shape


# In[9]:


dataset=dataset.dropna()


# In[10]:


quant_features = ['day365','clock','pv-1h','pv+0h','pv+2h']

scaled_features = {}

#for each in quant_features:
#    mean, std = data[each].mean(), data[each].std()
#    scaled_features[each] = [mean, std]
#    data.loc[:, each] = (data[each] - mean)/std

for each in quant_features:
    maxx, minn = dataset[each].max(), dataset[each].min()
    scaled_features[each] = [maxx, minn]
    dataset.loc[:, each] = (dataset[each] - minn)/(maxx-minn)


# In[11]:


dataset.shape


# In[12]:


train_dataset = dataset.sample(frac=0.975,random_state=0)
test_dataset = dataset.drop(train_dataset.index)


train_labels = train_dataset.pop('pv+2h')
test_labels = test_dataset.pop('pv+2h')


# In[13]:


train_dataset.head()


# In[14]:


def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation=tf.nn.relu, input_shape=[dataset.shape[1]-1]),
    layers.Dense(64, activation=tf.nn.relu),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mean_squared_error',
                optimizer=optimizer,
                metrics=['mean_absolute_error', 'mean_squared_error'])
  return model

model = build_model()


# In[15]:


# 에포크가 끝날 때마다 점(.)을 출력해 훈련 진행 과정을 표시합니다
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 1 == 0: print('')
    print('.', end='')

EPOCHS = 100

early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=15)

history = model.fit(train_dataset, train_labels, epochs=EPOCHS,
                    validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])


# In[16]:


hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()


# In[17]:


import matplotlib.pyplot as plt

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch
  
  plt.figure(figsize=(8,12))
  
  plt.subplot(2,1,1)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [pv+2h]')
  plt.plot(hist['epoch'], hist['mean_absolute_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
           label = 'Val Error')
  plt.ylim([0,0.5])
  plt.legend()
  
  plt.subplot(2,1,2)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$pv+2h^2$]')
  plt.plot(hist['epoch'], hist['mean_squared_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_squared_error'],
           label = 'Val Error')
  plt.ylim([0,0.05])
  plt.legend()
  plt.show()

plot_history(history)


# In[18]:


loss, mae, mse = model.evaluate(test_dataset, test_labels, verbose=0)

print("테스트 세트의 평균 절대 오차: {:5.2f} pv+2h".format(mae))


# In[19]:


test_predictions = model.predict(test_dataset).flatten()

plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [pv+2h]')
plt.ylabel('Predictions [pv+2h]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0,plt.xlim()[1]])
plt.ylim([0,plt.ylim()[1]])
_ = plt.plot([-100, 5000], [-100, 5000])


# In[20]:


error = test_predictions - test_labels
plt.hist(error, bins = 25)
plt.xlabel("Prediction Error [pv+2h]")
_ = plt.ylabel("Count")


# In[21]:


array_test_labels=pd.Series(test_labels).values
array_test_predictions=pd.Series(test_predictions).values


# In[22]:


rss=((array_test_labels-array_test_predictions)**2).sum()
mse=np.mean((array_test_labels-array_test_predictions)**2)
print("Final rmse value is =",np.sqrt(np.mean((array_test_labels-array_test_predictions)**2)))


# In[23]:


print(np.corrcoef(array_test_labels,array_test_predictions))


# In[24]:


def mape_vectorized_v2(a, b): 
    mask = a != 0
    return (np.fabs(a - b)/a)[mask].mean()

mape_vectorized_v2(array_test_labels,array_test_predictions)


# In[25]:


max(test_labels)


# In[26]:


def nmae(a, b, c): 
    mask = a != 0
    return (np.fabs(a - b)/max(c)/9)[mask].mean()

nmae(array_test_labels,array_test_predictions,test_labels)


# In[27]:


def nmae_wo_mask(a, b, c): 
    return (np.fabs(a - b)/max(c)/9).mean()

nmae_wo_mask(array_test_labels,array_test_predictions,test_labels)


# In[28]:


from sklearn.metrics import mean_squared_error
from math import sqrt

rms = sqrt(mean_squared_error(array_test_labels, array_test_predictions))
print(rms)


# In[26]:


array_test_labels


# In[27]:


array_test_predictions


# In[28]:


mape_vectorized_v2(array_test_labels*100,array_test_predictions*100)


# In[ ]:




