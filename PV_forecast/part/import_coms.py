# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:05:59 2019

@author: todayfirst
"""
import numpy as np

def run(zero_time_image, Pzero_time_image, test_mode, comsset, plant_id, minute):

    cntout = len(comsset)
    path_crop = ".\\data\\"+plant_id
    
    comscnt = 0    
    while(comscnt<cntout):
        for i,m in enumerate(minute):

            zero_time_image[comscnt][i] =np.load(path_crop+"\\"+plant_id+"_"+comsset[comscnt]+"_"+"dataset_with_coms_pixel_"+str(m)+".npy")
                
        ##영상 min-max normalization
            if comsset[comscnt]=="le2_ins":
                zero_time_image[comscnt][i] = zero_time_image[comscnt][i]/960
            else:
                zero_time_image[comscnt][i] =zero_time_image[comscnt][i]/255
        comscnt = comscnt+1
        
        
    if test_mode[0] ==1:
        comscnt = 0
        while(comscnt<cntout):
            for i,m in enumerate(minute):
                Pzero_time_image[comscnt][i] =np.load(path_crop+"\\"+plant_id+"_"+comsset[comscnt]+"_"+"dataset_with_coms_pixel_predict_"+str(m)+".npy")
                    
            ##영상 min-max normalization
                if comsset[comscnt]=="le2_ins":
                    Pzero_time_image[comscnt][i] = Pzero_time_image[comscnt][i]/960
                else:
                    Pzero_time_image[comscnt][i] =Pzero_time_image[comscnt][i]/255
            comscnt = comscnt+1
    return (zero_time_image, Pzero_time_image)