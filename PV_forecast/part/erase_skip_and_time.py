# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:54:33 2019

@author: todayfirst
"""
import numpy as np

## skip 값 지우기

def run(training_data, Ptraining_data,cnn_mode, test_mode, cap, comsset, hours, minute,time_start, time_end ):
    cntout = len(comsset)
    for_delete_skip =[]
    
    for i in hours:
        #print(i)
        if not i==0:
    
            comscnt = 0
            while(comscnt<cntout):
                if (2 in hours) and not(i ==2):
                    break
                for m_i, m in enumerate(minute):
                    for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(training_data[training_data[comsset[comscnt]+"_"+str(i)+"."+str(m)] == 'skip'].index))
                comscnt = comscnt+1
                
        if i==0:
    
            comscnt = 0
            while(comscnt<cntout):
                for m_i, m in enumerate(minute):
                    for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(training_data[training_data[comsset[comscnt]+"."+str(m)] == 'skip'].index))
                comscnt = comscnt+1

##영상이 없으므로 인해 삭제되는 데이터들 
    print(len(for_delete_skip))
    training_data.drop(for_delete_skip, inplace = True)
    training_data=training_data.reset_index()
    training_data.drop("index", axis=1,inplace = True)

    if test_mode[0] ==1:
        ## skip 값 지우기
        for_delete_skip =[]
        
        for i in hours:
            #print(i)
            if not i==0:
        
                comscnt = 0
                while(comscnt<cntout):
                    if (2 in hours) and not(i ==2):
                        break
                    for m_i, m in enumerate(minute):
                        for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(Ptraining_data[Ptraining_data[comsset[comscnt]+"_"+str(i)+"."+str(m)] == 'skip'].index))
                    comscnt = comscnt+1
                    
            if i==0:
        
                comscnt = 0
                while(comscnt<cntout):
                    for m_i, m in enumerate(minute):
                        for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(Ptraining_data[Ptraining_data[comsset[comscnt]+"."+str(m)] == 'skip'].index))
                    comscnt = comscnt+1
        
           ##영상이 없으므로 인해 삭제되는 데이터들 
     
        Ptraining_data.drop(for_delete_skip, inplace = True)
        Ptraining_data=Ptraining_data.reset_index()
        
        Ptraining_data.drop("index", axis=1,inplace = True)
    
    

## part  9 : 시간 설정

    print(np.shape(training_data))

    ## 두 개수가 같아야함.
    
    print(np.shape(Ptraining_data))

    ## 두 개수가 같아야함.
    
    
    
    ## 시간 솎아주기
    for_delete_skip =[]
    
    
    for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(training_data[training_data["Khour"] <time_start-2].index))
    #print(for_delete_skip )
    for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(training_data[training_data["Khour"] >time_end - 2].index))
    for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(training_data[training_data["2h"] >cap].index))
    for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(training_data[training_data["2h"] <0].index))
    
    for i in hours:
        if i==2:
            continue
        for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(training_data[training_data[str(i)+"h"] >cap].index))
        for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(training_data[training_data[str(i)+"h"] <0].index))
    
    training_data.drop(for_delete_skip, inplace = True)
    training_data=training_data.reset_index()
    training_data.drop("index", axis=1,inplace = True)
    
    
    ## 시간 솎아주기
    if test_mode[0]==1:
        for_delete_skip =[]
        
        
        for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(Ptraining_data[Ptraining_data["Khour"] <time_start-2].index))
        #print(for_delete_skip )
        for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(Ptraining_data[Ptraining_data["Khour"] >time_end-2].index))
        for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(Ptraining_data[Ptraining_data["2h"] >cap].index))
        for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(Ptraining_data[Ptraining_data["2h"] <0].index))
        
        for i in hours:
            if i==2:
                continue
            for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(Ptraining_data[Ptraining_data[str(i)+"h"] >cap].index))
            for_delete_skip = list(dict.fromkeys(for_delete_skip))+list(dict.fromkeys(Ptraining_data[Ptraining_data[str(i)+"h"] <0].index))
        
        Ptraining_data.drop(for_delete_skip, inplace = True)
        
        Ptraining_data=Ptraining_data.reset_index()
      
        Ptraining_data.drop("index", axis=1,inplace = True)
    
    
    training_data=training_data.astype(float)
    print("drop na : "+ str(np.shape(training_data)))

    training_data=training_data.dropna()
    print(np.shape(training_data))
    
    if test_mode[0] == 1:
        Ptraining_data=Ptraining_data.astype(float)
        print("drop na : "+ str(np.shape(Ptraining_data)))

        Ptraining_data=Ptraining_data.dropna()
        print(np.shape(Ptraining_data))

    return training_data, Ptraining_data