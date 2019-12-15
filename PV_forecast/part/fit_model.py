# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:59:41 2019

@author: todayfirst
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras


def run(model, train_dataset, train_labels,case,ex_case,early_p = 15, val_split = 0.2):

    class PrintDot(keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs):
            if epoch % 50 == 0: print('')
            print('.', end='')
            
    early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=early_p)
    history=model.fit(train_dataset, train_labels, epochs=100,
        validation_split =val_split,callbacks=[early_stop,PrintDot()],verbose=0)
    
    dirname = "./result"+"//"+str(case)
    if not os.path.isdir(dirname): 
        os.mkdir(dirname)
    model.save(dirname+"//"+str(ex_case)+'_model1.h5')
    return history
