# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:54:48 2019

@author: todayfirst
"""
def run(cnnmode, no_coms, comsset, weather_ele, hours):
    for_name="("
    if cnnmode==0:
        if no_coms==0:
            for each in comsset:
                for_name = for_name+each+", "
            
            for_name = for_name+")_("
        else:
            for_name = for_name+"no_coms)_("
    if cnnmode==1:
        for_name = for_name+"cnn)_("
    else:
        for_name = for_name+"fnn)_("
        
    if len(weather_ele)>0:
        for_name = for_name+"weather__"
        for i,c in enumerate(weather_ele):
            for_name = for_name+str(c)
            if i==len(weather_ele)-1:
                continue
            for_name = for_name+", "
        for_name = for_name+")_("
    else:
        for_name = for_name+"no_weather)_("
    for i,c in enumerate(hours):
        for_name = for_name+str(c)+"h"
        if i==len(hours)-1:
            continue
        for_name = for_name+", "
    
    for_name = for_name+")_("
    
    return for_name