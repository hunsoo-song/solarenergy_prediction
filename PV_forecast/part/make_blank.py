# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:05:36 2019

@author: todayfirst
"""
def run(comsset, minute, test_mode):

    #zero_time_iamge : [coms 종류][minute]순으로 인덱싱 

    zero_time_image = []
    Pzero_time_image = []
    
    comscnt = 0
    cntout = len(comsset)

    while(comscnt<cntout):

        zero_time_image.append([])
        if test_mode[0]==1:
            Pzero_time_image.append([])
        for m in minute:
            zero_time_image[comscnt].append([])
            if test_mode[0]==1:
                Pzero_time_image[comscnt].append([])
        comscnt = comscnt+1

    return (zero_time_image, Pzero_time_image)


