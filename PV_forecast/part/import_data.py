# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:05:59 2019

@author: todayfirst
"""
import numpy as np
import pandas as pd

def run(test_mode, comsset, plant_id, minute, weather_ele):
    Pbasic_data = []
    
    path_crop = ".\\data\\"+plant_id
    
    basic_data=pd.read_csv(path_crop+"\\"+plant_id+'_dataset_with_coms_pixel.csv',sep=",", header=0)
    basic_data["coms_index"] = basic_data.index[:]
    
    if test_mode[0] ==1:
        Pbasic_data=pd.read_csv(path_crop+"\\"+plant_id+'_dataset_with_coms_pixel_predict.csv',sep=",", header=0)
        Pbasic_data["coms_index"] = Pbasic_data.index[:]
        
    path_weather = path_crop + "\\"+ plant_id +"_weather_data_new.csv"
    path_weather_predict = path_crop + "\\"+  plant_id +"_weather_data_new_pred.csv"
    
    weather = pd.read_csv(path_weather,sep=",",header=0)
    weather = weather[240:]
    weather.reset_index(inplace = True)
    if(len(weather)>len(basic_data)):
        weather = weather[:len(basic_data)] 
    else:
        basic_data = basic_data[:len(weather)]
    
    for i in weather_ele:
        basic_data[plant_id+"_"+str(i)] =weather[plant_id+"_"+str(i)]
    
    
    if test_mode[0] == 1:
        
        Pweather = pd.read_csv(path_weather_predict,sep=",",header=0)
        Pweather = Pweather[240:]
        Pweather.reset_index(inplace = True)
        #print(Pweather.head(10))


        if(len(Pweather)>len(Pbasic_data)):
            Pweather = Pweather[:len(Pbasic_data)] 
        else:
            Pbasic_data = Pbasic_data[:len(Pweather)]
            
        for i in weather_ele:
            Pbasic_data[plant_id+"_"+str(i)] =Pweather[plant_id+"_"+str(i)]
    
    if not test_mode[0]==1:
        Pbasic_data = []
    return (basic_data, Pbasic_data)
   