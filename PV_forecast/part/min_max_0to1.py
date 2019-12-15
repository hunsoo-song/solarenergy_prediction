# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:43:53 2019

@author: todayfirst
"""

def run(training_data, P_data, test_mode ):
    scaled_features = {}
    for each in training_data:
        if each == "test":
            continue

        #print(each)
        maxx1, minn1 = training_data[each].max(), training_data[each].min()
        if test_mode[0] ==1:
            
            maxx2, minn2 = P_data[each].max(),P_data[each].min()
            if maxx1>maxx2:
                maxx = maxx1
            else:
                maxx = maxx2
            if minn1<minn2:
                minn = minn1
            else:
                minn = minn2
        else:
            maxx = maxx1
            minn = minn1
        
        scaled_features[each] = [maxx, minn]
        training_data.loc[:, each] = (training_data[each] - minn)/(maxx-minn)
        if test_mode[0] ==1:
            
            P_data.loc[:, each] = (P_data[each] - minn)/(maxx-minn)
        
        if each == "2h":
            forevalmax = maxx
            forevalmin = minn
    return (training_data, P_data,forevalmax, forevalmin,scaled_features)