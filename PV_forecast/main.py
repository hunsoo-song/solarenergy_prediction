# -*- coding: utf-8 -*-

import os


from part import config
from part import make_blank
from part import import_data
from part import import_coms
from part import make_multitemporal_data
from part import make_multitemporal_coms
from part import erase_skip_and_time
from part import erase_coms
from part import min_max_0to1
from part import make_name
from part import set_train_data
from part import set_train_coms
from part import mlp_model
from part import cnn_model
from part import combine_model
from part import fit_model
from part import test_model
from part import write_evaluation_result

import pandas as pd
import numpy as np

all_case_number = len(config.all_case)
NMAE = pd.DataFrame()
for case, each_case in enumerate(config.all_case):
    (plant_id, cap, weather_ele, comsset, cnn_mode, hours, no_coms, patch_size, layers, combine_layers, numofex, test_mode )=config.iterate(0)
    minute = [0]
    NMAE[str(case)] = np.zeros(numofex)
    if cnn_mode==1:
        (zero_time_image, Pzero_time_image) = make_blank.run(comsset, minute, test_mode)
        (zero_time_image, Pzero_time_image) = import_coms.run(zero_time_image, Pzero_time_image, test_mode, comsset, plant_id, minute)
    
    basic_data, Pbasic_data = import_data.run(test_mode, comsset, plant_id, minute, weather_ele)
    
    training_data, Ptraining_data = make_multitemporal_data.run(basic_data, Pbasic_data, test_mode, comsset,hours, minute, weather_ele, plant_id)
    
    if cnn_mode==1:
        coms_training_data, coms_P_data = make_multitemporal_coms.run(zero_time_image, Pzero_time_image,patch_size, comsset, hours, minute, test_mode, len(basic_data),len(Pbasic_data))

    training_data, Ptraining_data = erase_skip_and_time.run(training_data, Ptraining_data,cnn_mode, test_mode, cap, comsset, hours, minute,6, 20 )

    if cnn_mode==1:
        coms_training_data, coms_P_data = erase_coms.run(list(Ptraining_data["coms_index"].astype(int)),list(training_data["coms_index"].astype(int)),
                                                         coms_training_data, coms_P_data,test_mode)
    
        print(str(len(training_data))+" : "+str(len(coms_training_data)))
        print(str(len(Ptraining_data))+" : "+str(len(coms_P_data)))

    if test_mode[0]==1:
        Pindex = Ptraining_data.pop("coms_index")
    training_data.pop("coms_index")  


    training_data, Ptraining_data,forevalmax, forevalmin,scaled_features = min_max_0to1.run(training_data, Ptraining_data, test_mode )

    for_name = make_name.run(cnn_mode, no_coms, comsset, weather_ele, hours)

    

    for ex_case in range(numofex):
        
        if cnn_mode ==1:
            train_dataset, test_dataset, train_labels, test_labels, for_name1 = set_train_coms.make_for_cnn(coms_training_data, coms_P_data, test_mode, training_data, Ptraining_data,hours,minute,comsset,cnn_mode,ex_case,for_name)
        
        else : 
            train_dataset, test_dataset, train_labels, test_labels, for_name1 = set_train_data.make_for_mlp(test_mode, training_data, Ptraining_data,hours,minute,comsset,cnn_mode,ex_case,for_name)
        
        #if 'A' in df.columns:
        
        if cnn_mode ==1:
            model_cnn = cnn_model.create_cnn(np.shape(train_dataset[1])[1],np.shape(train_dataset[1])[2],
                             np.shape(train_dataset[1])[3], layers,  ex_case)
            model_mlp = mlp_model.create_mlp(np.shape(train_dataset[0])[1],[], False)
            
            model = combine_model.run(model_mlp, model_cnn, combine_layers)            
        else:
            model = mlp_model.create_mlp(train_dataset.shape[1],layers, True)

            
        history = fit_model.run(model, train_dataset, train_labels,case,ex_case,early_p = 15, val_split = 0.2)
        
        #print(test_model.run(ex_case, case, model,history, test_dataset, test_labels,forevalmax, forevalmin, cap))
        NMAE[str(case)][ex_case] = test_model.run(ex_case, case, model,history, test_dataset, test_labels,forevalmax, forevalmin, cap)
    NMAE.to_csv("./result"+"//"+plant_id+"//"+plant_id+"_Result.csv", mode='w')
