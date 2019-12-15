# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:44:41 2019

@author: todayfirst
"""

import pandas as pd
import numpy as np

## part 6 : 파일화, 데이터 생성하기, 다시기로 


## 불러온 데이터(basic_data)를 training에 사용할 데이터만 넣음.
##modify : 다른 데이터를 사용하려면 이 단계에서 입력해야함 
def run(basic_data, Pbasic_data, test_mode, comsset,hours, minute, weather_ele, plant_id):
    
    training_data = pd.DataFrame()
    training_data["2h"] = np.zeros((len(basic_data)))
    training_data["2h"][0:len(basic_data)-2] = basic_data["0h"][2:len(basic_data)]
    
    training_data["Khour"]=basic_data["Khour"]
    if test_mode[0] == 2:
        training_data["test"]=np.zeros((len(basic_data)))
        
        cnt =0
        while(cnt<len(basic_data)):
            training_data.iloc[cnt:cnt+24]["test"] = int(cnt/24)
            cnt = cnt+24
        
    training_data["10sum"]=basic_data["10sum"]
    training_data["azimuth_2"] = np.zeros((len(basic_data),1))
    training_data["azimuth_2"][0:len(basic_data)-2] = basic_data["azimuth"][2:len(basic_data)]
    training_data["elevation_2"] = np.zeros((len(basic_data),1))
    training_data["elevation_2"][0:len(basic_data)-2] = basic_data["elevation"][2:len(basic_data)]
    training_data["azimuth_1"] = np.zeros((len(basic_data),1))
    training_data["azimuth_1"][0:len(basic_data)-1] = basic_data["azimuth"][1:len(basic_data)]
    training_data["elevation_1"] = np.zeros((len(basic_data),1))
    training_data["elevation_1"][0:len(basic_data)-1] = basic_data["elevation"][1:len(basic_data)]
    training_data["azimuth_1_0.2"] = np.zeros((len(basic_data),1))
    training_data["azimuth_1_0.2"][0:len(basic_data)-1] = basic_data["azimuth_0.2"][1:len(basic_data)]
    training_data["elevation_1_0.2"] = np.zeros((len(basic_data),1))
    training_data["elevation_1_0.2"][0:len(basic_data)-1] = basic_data["elevation_0.2"][1:len(basic_data)]
    training_data["azimuth_1_0.4"] = np.zeros((len(basic_data),1))
    training_data["azimuth_1_0.4"][0:len(basic_data)-1] = basic_data["azimuth_0.4"][1:len(basic_data)]
    training_data["elevation_1_0.4"] = np.zeros((len(basic_data),1))
    training_data["elevation_1_0.4"][0:len(basic_data)-1] = basic_data["elevation_0.4"][1:len(basic_data)]
    training_data["0h"] = basic_data["0h"]
    training_data["coms_index"] = basic_data["coms_index"]

    for w in weather_ele:
        training_data[plant_id+"_"+str(w)+"_2"] =np.zeros((len(basic_data),1))
        training_data[plant_id+"_"+str(w)+"_2"][:len(basic_data)-2]=basic_data[plant_id+"_"+str(w)][2:len(basic_data)]
    for w in weather_ele:
        training_data[plant_id+"_"+str(w)+"_1"] =np.zeros((len(basic_data),1))
        training_data[plant_id+"_"+str(w)+"_1"][:len(basic_data)-1]=basic_data[plant_id+"_"+str(w)][1:len(basic_data)]
    
    cntout = len(comsset)
        
    for i in hours:
        if i<0:
            training_data[str(i)+"h"] = np.zeros((len(basic_data),1))
            training_data[str(i)+"h"][-i:len(basic_data)] = basic_data["0h"][0:len(basic_data)+i]
            if not(2 in hours): 
                comscnt = 0
                while(comscnt<cntout):
                    for m_i,m in enumerate(minute):
                        training_data[comsset[comscnt]+"_"+str(i)+"."+str(m)] = np.zeros((len(basic_data),1))
                        training_data[comsset[comscnt]+"_"+str(i)+"."+str(m)][-i:len(basic_data)] =basic_data[comsset[comscnt]+"."+str(m)][0:len(basic_data)+i]
    
                    comscnt = comscnt+1
    
        if i==0:
            comscnt = 0
            while(comscnt<cntout):
                for m_i, m in enumerate(minute):
                    training_data[comsset[comscnt]+"."+str(m)] =basic_data[comsset[comscnt]+"."+str(m)]
                comscnt = comscnt+1
            #나중에#basic_data = basic_data[0:len(basic_data)-2]
            continue
            
        if i>0:
    
            if i==1:
                training_data[str(i)+"h"] = np.zeros((len(basic_data),1))
                training_data[str(i)+"h"][0:len(basic_data)-i] = basic_data["0h"][i:len(basic_data)]
    
            comscnt = 0
            while(comscnt<cntout):
                for m_i, m in enumerate(minute):
                    training_data[comsset[comscnt]+"_"+str(i)+"."+str(m)] = np.zeros((len(basic_data),1))
                    training_data[comsset[comscnt]+"_"+str(i)+"."+str(m)][0:len(basic_data)-i] = basic_data[comsset[comscnt]+"."+str(m)][i:len(basic_data)]
                comscnt = comscnt+1


    if test_mode[0] == 1:  
        
        Ptraining_data = pd.DataFrame()
        Ptraining_data["2h"] = np.zeros((len(Pbasic_data)))
        Ptraining_data["2h"][0:len(Pbasic_data)-2] = Pbasic_data["0h"][2:len(Pbasic_data)]
        
        Ptraining_data["Khour"]=Pbasic_data["Khour"]
        
        Ptraining_data["10sum"]=Pbasic_data["10sum"]
        Ptraining_data["azimuth_2"] = np.zeros((len(Pbasic_data),1))
        Ptraining_data["azimuth_2"][0:len(Pbasic_data)-2] = Pbasic_data["azimuth"][2:len(Pbasic_data)]
        Ptraining_data["elevation_2"] = np.zeros((len(Pbasic_data),1))
        Ptraining_data["elevation_2"][0:len(Pbasic_data)-2] = Pbasic_data["elevation"][2:len(Pbasic_data)]
        Ptraining_data["azimuth_1"] = np.zeros((len(Pbasic_data),1))
        Ptraining_data["azimuth_1"][0:len(Pbasic_data)-1] = Pbasic_data["azimuth"][1:len(Pbasic_data)]
        Ptraining_data["elevation_1"] = np.zeros((len(Pbasic_data),1))
        Ptraining_data["elevation_1"][0:len(Pbasic_data)-1] = Pbasic_data["elevation"][1:len(Pbasic_data)]
        Ptraining_data["azimuth_1_0.2"] = np.zeros((len(Pbasic_data),1))
        Ptraining_data["azimuth_1_0.2"][0:len(Pbasic_data)-1] = Pbasic_data["azimuth_0.2"][1:len(Pbasic_data)]
        Ptraining_data["elevation_1_0.2"] = np.zeros((len(Pbasic_data),1))
        Ptraining_data["elevation_1_0.2"][0:len(Pbasic_data)-1] = Pbasic_data["elevation_0.2"][1:len(Pbasic_data)]
        Ptraining_data["azimuth_1_0.4"] = np.zeros((len(Pbasic_data),1))
        Ptraining_data["azimuth_1_0.4"][0:len(Pbasic_data)-1] = Pbasic_data["azimuth_0.4"][1:len(Pbasic_data)]
        Ptraining_data["elevation_1_0.4"] = np.zeros((len(Pbasic_data),1))
        Ptraining_data["elevation_1_0.4"][0:len(Pbasic_data)-1] = Pbasic_data["elevation_0.4"][1:len(Pbasic_data)]
        Ptraining_data["0h"] = Pbasic_data["0h"]
        Ptraining_data["coms_index"] = Pbasic_data["coms_index"]
        for w in weather_ele:
            Ptraining_data[plant_id+"_"+str(w)+"_2"] =np.zeros((len(Pbasic_data),1))
            Ptraining_data[plant_id+"_"+str(w)+"_2"][:len(Pbasic_data)-2]=Pbasic_data[plant_id+"_"+str(w)][2:len(Pbasic_data)]
        for w in weather_ele:
            Ptraining_data[plant_id+"_"+str(w)+"_1"] =np.zeros((len(Pbasic_data),1))
            Ptraining_data[plant_id+"_"+str(w)+"_1"][:len(Pbasic_data)-1]=Pbasic_data[plant_id+"_"+str(w)][1:len(Pbasic_data)]

            
        for i in hours:
            if i<0:
                Ptraining_data[str(i)+"h"] = np.zeros((len(Pbasic_data),1))
                Ptraining_data[str(i)+"h"][-i:len(Pbasic_data)] = Pbasic_data["0h"][0:len(Pbasic_data)+i]
                if not(2 in hours): 
                    comscnt = 0
                    while(comscnt<cntout):
                        for m_i,m in enumerate(minute):
                            Ptraining_data[comsset[comscnt]+"_"+str(i)+"."+str(m)] = np.zeros((len(Pbasic_data),1))
                            Ptraining_data[comsset[comscnt]+"_"+str(i)+"."+str(m)][-i:len(Pbasic_data)] =Pbasic_data[comsset[comscnt]+"."+str(m)][0:len(Pbasic_data)+i]
        
                        comscnt = comscnt+1
        
            if i==0:
                comscnt = 0
                while(comscnt<cntout):
                    for m_i, m in enumerate(minute):
                        Ptraining_data[comsset[comscnt]+"."+str(m)] =Pbasic_data[comsset[comscnt]+"."+str(m)]
                    comscnt = comscnt+1
                #나중에#Pbasic_data = Pbasic_data[0:len(Pbasic_data)-2]
                continue
                
            if i>0:
        
                if i==1:
                    Ptraining_data[str(i)+"h"] = np.zeros((len(Pbasic_data),1))
                    Ptraining_data[str(i)+"h"][0:len(Pbasic_data)-i] = Pbasic_data["0h"][i:len(Pbasic_data)]
        
                comscnt = 0
                while(comscnt<cntout):
                    for m_i, m in enumerate(minute):
                        Ptraining_data[comsset[comscnt]+"_"+str(i)+"."+str(m)] = np.zeros((len(Pbasic_data),1))
                        Ptraining_data[comsset[comscnt]+"_"+str(i)+"."+str(m)][0:len(Pbasic_data)-i] = Pbasic_data[comsset[comscnt]+"."+str(m)][i:len(Pbasic_data)]
                    comscnt = comscnt+1
    
    
    
    


    
    #전후 시간 shift한 걸로인한 nan값 지워주기
    print("before : "+str(np.shape(training_data)))
    max_hour = max(hours)
    min_hour = min(hours)
    if min_hour == max_hour:
        min_hour=0
        
    if max_hour>2:
        training_data = training_data[0:len(training_data)-max_hour]
    else : 
        training_data = training_data[0:len(training_data)-2]
    
    training_data = training_data[-min_hour:len(training_data)]
    training_data=training_data.reset_index()
    training_data.drop("index", axis=1,inplace = True)
    print("after :"+str(np.shape( training_data)))
    
    #전후 시간 shift한 걸로인한 nan값 지워주기
    if test_mode[0] == 1:
        print("before :"+str(np.shape( Ptraining_data)))
        if max_hour>2:
            Ptraining_data = Ptraining_data[0:len(Ptraining_data)-max_hour]
    
        else : 
            Ptraining_data = Ptraining_data[0:len(Ptraining_data)-2]
        
        Ptraining_data = Ptraining_data[-min_hour:len(Ptraining_data)]
    
        Ptraining_data=Ptraining_data.reset_index()
        Ptraining_data.drop("index", axis=1,inplace = True)
        print("after :"+str(np.shape( Ptraining_data)))
    

    if not test_mode[0]==1:
        Ptraining_data = []
            
    return (training_data, Ptraining_data)
                    