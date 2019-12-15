# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:17:21 2019

@author: todayfirst
"""
import numpy as np

def run(Pindex,Tindex,coms_training_data, coms_P_data,test_mode):
    coms_training_data = np.asarray(coms_training_data)
    coms_training_data = coms_training_data[Tindex]
    
    if test_mode[0] == 1:
        coms_P_data = np.asarray(coms_P_data)
        coms_P_data = coms_P_data[Pindex]
    
    return (coms_training_data, coms_P_data)
