# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:16:24 2019

@author: todayfirst
"""

import numpy as np

def run(zero_time_image, Pzero_time_image,patch_size, comsset, hours, minute, test_mode, len_basic_data,len_Pbasic_data):

    start = 30-int(patch_size/2)
    end = 30+int(patch_size/2)
    if patch_size%2 ==0:
        end = end-1
    
    max_hour = max(hours)
    min_hour = min(hours)
    if min_hour == max_hour:
        min_hour=0
        
    coms_training_data = []
    
    if max_hour>2:
        len_for_max = max_hour
    else :
        len_for_max = 2

    cntout = len(comsset)

    for i in range(-min_hour,len_basic_data-len_for_max):
        outImage = np.zeros(( patch_size,patch_size,cntout*len(hours)*len(minute) ))

        for index,h in enumerate(hours):
            comscnt = 0
            while(comscnt<cntout):
                for m_i, m in enumerate(minute):

                    outImage[:,:,index*cntout*len(minute)+len(minute)*comscnt+m_i] = zero_time_image[comscnt][m_i][i+h][start:end+1,start:end+1]
                    #print(i+h)
                comscnt = comscnt+1

        coms_training_data.append(outImage)

##cnn을 위한 영상 stack

            
    coms_P_data = []
    if test_mode[0] == 1:
        if max_hour>2:
            len_for_max = max_hour
        else :
            len_for_max = 2
    
        
        for i in range(-min_hour,len_Pbasic_data-len_for_max):
            outImage = np.zeros(( patch_size,patch_size,cntout*len(hours)*len(minute) ))
    
            for index,h in enumerate(hours):
                comscnt = 0
                while(comscnt<cntout):
                    for m_i, m in enumerate(minute):
                        outImage[:,:,index*cntout*len(minute)+len(minute)*comscnt+m_i] = Pzero_time_image[comscnt][m_i][i+h][start:end+1,start:end+1]

                    comscnt = comscnt+1
    
            coms_P_data.append(outImage)
    return(coms_training_data, coms_P_data)