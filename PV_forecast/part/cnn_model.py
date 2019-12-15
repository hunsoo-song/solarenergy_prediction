# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:00:39 2019

@author: todayfirst
"""
from tensorflow import keras




from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Add
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import concatenate

lossfunc = 'mean_absolute_error'
opt = Adam(lr =0.001, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-8, decay = 0.0)


def create_cnn(width, height, depth, cnn_layers, case):

            inputShape = (height, width, depth)
            chanDim = -1

            inputs = Input(shape=inputShape)
            
            x = inputs

            for (i, f) in enumerate(cnn_layers):
                if f[0] == 'I':
                    x1 = Conv2D(f[1], (1, 1), padding='same')(x)
                    x1 = Activation("relu")(x1)
                    x1 = Conv2D(f[1], (3, 3), padding='same')(x1)
                    x1 = Activation("relu")(x1)
                    
                    x2 = Conv2D(f[1], (1, 1), padding='same')(x)
                    x2 = Activation("relu")(x2)
                    x2 = Conv2D(f[1], (5, 5), padding='same')(x2)
                    x2 = Activation("relu")(x2)
                    
                    x3 = AveragePooling2D(pool_size=(3, 3),strides=(1,1),padding='same')(x)
                    x3 = Conv2D(f[1], (1, 1), padding='same')(x3)
                    x3 = Activation("relu")(x3)
                    
                    x4 = Conv2D(f[1], (1, 1), padding='same')(x)
                    x4 = Activation("relu")(x4)
                    
                    x = keras.layers.concatenate([x1, x2, x3,x4], axis = 3)

                if f[0] =='C':
                    if len(f)==5:
                        x = Conv2D(f[2], (f[1], f[1]), strides = f[4], padding=f[3])(x)
                    else:
                        x = Conv2D(f[2], (f[1], f[1]), padding=f[3])(x)
                    #x = BatchNormalization(axis=chanDim)(x)
                    x = Activation("relu")(x)
                    x = BatchNormalization(axis=chanDim)(x)
           # CONV => RELU => BN => POOL 이 기본
                if f[0] == 'A':
                    x = AveragePooling2D(pool_size=(f[1], f[1]))(x)
                if f[0] == 'M':
                    x = MaxPooling2D(pool_size=(f[1], f[1]))(x)

                print(x)

            x = Flatten()(x)

            x = BatchNormalization()(x)
           # x = Dropout(0.2)(x)

            # CNN
            model = Model(inputs, x)

            # return the CNN
            return model