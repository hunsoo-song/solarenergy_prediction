# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:22:20 2019

@author: todayfirst
"""
import pandas as pd

def run(plant_id,Pindex):
        
    writethis = pd.read_csv("./data//"+plant_id+"//"+plant_id+"_1_day_ahead_forecasting_result.csv",sep=",",header=0)



