# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:32:12 2019

@author: todayfirst
"""
from tensorflow.keras.layers import concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import Adam


lossfunc = 'mean_absolute_error'
opt = Adam(lr =0.001, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-8, decay = 0.0)



def run(model_mlp, model_cnn, combine_layers):
    
    combinedInput = concatenate([model_mlp.output, model_cnn.output])
    
    for i, f in enumerate(combine_layers):
        if f[0] == 'F':
            if i ==0:
                x = Dense(f[1])(combinedInput)
            else: 
                x = Dense(f[1])(x)
                
        if f[0] == 'R':
            if i ==0:
                x = Activation('relu')(combinedInput)
            else: 
                x = Activation('relu')(x)
                
        if f[0] == 'D':
            if i==0:
                x = Dropout(f[1])(combinedInput)
            else:
                x = Dropout(f[1])(x)

        if f[0] == 'B':
            if i==0:
                x = BatchNormalization()(combinedInput)
            else:
                x = BatchNormalization()(x)
    x = Dense(1, activation="linear")(x)

    model = Model(inputs=[model_mlp.input, model_cnn.input], outputs=x)
    model.compile(loss=lossfunc,
            optimizer=opt,
            metrics=['mean_absolute_error', 'mean_squared_error'])
    
    return model