# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:30:00 2019

@author: todayfirst
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def make_for_cnn(coms_training_data, coms_P_data, test_mode, training_data, Ptraining_data,hours,minute,comsset,cnn_mode,ex_case,for_name):
  
    if test_mode[0] == 1:
        test_coms_dataset = coms_P_data[:]
        test_dataset = Ptraining_data[:]
        train_coms_dataset = coms_training_data[:]
        train_dataset = training_data[:]
    if test_mode[0] == 2:
        test_dataset.pop('test')
        train_dataset.pop('test')
    if test_mode[0] == 3:
        train_dataset = training_data[:]
        train_coms_dataset = coms_training_data[:]
        train_dataset.reset_index(inplace = True)
        train_dataset.drop("index", axis=1,inplace = True)

        split = train_test_split(train_dataset, train_coms_dataset , test_size=test_mode[1])
        (train_dataset, test_dataset, train_coms_dataset, test_coms_dataset) = split

    train_labels = train_dataset.pop('2h')
    test_labels = test_dataset.pop('2h')
    cntout = len(comsset)
    if cnn_mode==1:
        
        for i in hours:
            if not (i==0):
                comscnt = 0
                while(comscnt<cntout):
                    for m_i, m in enumerate(minute):
                        train_dataset.pop(comsset[comscnt]+"_"+str(i)+"."+str(m))
                        test_dataset.pop(comsset[comscnt]+"_"+str(i)+"."+str(m))
                    comscnt = comscnt+1
            if i==0:
                comscnt = 0
                while(comscnt<cntout):
                    for m_i, m in enumerate(minute):
                        train_dataset.pop(comsset[comscnt]+"."+str(m))
                        test_dataset.pop(comsset[comscnt]+"."+str(m))
                    comscnt = comscnt+1
                continue
                
    if ex_case==0:
        num0ffeature=0
        for each in train_dataset:
            print(each)
            num0ffeature = num0ffeature+1
        for_name1 = for_name+"num of features__"+str(num0ffeature)+")"
        
        print("number of features : "+str(num0ffeature))
        print("test data #: "+str(len(test_dataset)))
        print("train data #: "+str(len(train_dataset)))


    train_dataset = np.asarray(train_dataset)
    test_dataset  = np.asarray(test_dataset)
    test_labels = np.asarray(test_labels)
    train_labels = np.asarray(train_labels)

    train_dataset = [train_dataset, train_coms_dataset]
    test_dataset = [test_dataset, test_coms_dataset]
    
    return train_dataset, test_dataset, train_labels, test_labels, for_name1