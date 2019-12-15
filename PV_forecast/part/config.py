# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:50:43 2019

@author: todayfirst
"""
import pandas as pd

##all_case에, 
# 1. site : 평창("pch"), 고창("gch"), 창녕("chn"), 익산("iksan"), 
#           함안("ham"), 증평("jp"), 창원("chw"),
#           영암("yy"), 진도("JD")
#           중 하나 입력
#           ex) "jp"

# 2. 기상 데이터 중 사용할 데이터 선택 : 1~9중 선택, 중복선택 가능
#           ex)[1] or [1,2,3,4,6,7,9]

# 3. 사용할 위성 영상 선택 : 가시광선 영상("le1b_vis"), 적외선영상("le1b_ir01"),
#           표면도달 일사량 영상("le2_ins") 중 선택, 중복선택가능
#           ex) ["le1b_vis","le1b_ir01"]

# 4. cnn인지 fnn인지 선택 : "CNN" or "FNN"

# 5. 사용할 시간대 선택 : input으로 사용할 영상과 pv자료 사용할 시간대 선택
#           ex) 3시간전, 2시간전, 1시간전, 0시간의 자료를 사용하고 싶으면
#               [-3,-2,-1,0]을 선택

# 6. FNN사용시 위성영상의 픽셀을 사용하려면 True, 아니면 False
#    CNN사용시 상관없음

# 7. CNN사용시 위성영상의 patch 크기

# 8. FNN, CNN사용시 레이어 구성
#   1)FNN일때
#       'F' : Fully connected layers
#           [1요소] = 노드수
#       ex) ['F', 128]
#       
#       'R' : relu Activation
#       ex) ['R']
#
#       'D' : DropOut
#           [1요소] = dropout rate
#       ex) ['D',0.2] : 20%를 무시하는 dropout레이어 추가
#
#       'B' : BatchNormalization
#       ex) ['B']       


#
#   2)CNN : 
#       'R' : relu Activation
#       ex) ['R']
#
#       'D' : DropOut
#           [1요소] = dropout rate
#       ex) ['D',0.2] : 20%를 무시하는 dropout레이어 추가
#
#       'B' : BatchNormalization
#       ex) ['B']
#
#       'C' : 2D Convolutional Layer
#           [1요소] = filter 사이즈
#           [2요소] = filter 개수
#           [3요소] = 패딩방법,('same', 'valid'중 하나)
#           optional [4요소] = strides
#       ex) ['C', 3,16,'same']
#
#       'I' : Inception layer
#       ex) ['I']
#
#
# 9. cnn사용시, cnn feature와 fnn feature를 어떻게 결합할지,Fnn레이어와 같은 방법으로 구성
#
# 10. 케이스당 실험 반복횟수
#
# 11. 테스트를 어떤 방식으로 진행 할지, 1이면 test할 파일 따로 존재하고 그 파일의 데이터로 테스트함
#                       2이면 test할 파일이 따로 없고 랜덤한 날짜를 선택하여 테스트함. 테스트할 날짜의 수도 기입해야함.
#                       3이면 test할 파일이 따로 없고 랜덤한 데이터를 선택하여 테스트함.2와 다른 점은 시간도 날짜도 랜덤임. 테스트 데이터로 쓸 데이터 비율도 기입해야함.
#   ex) test할 파일이 존재 : [1]
#       training data의 일부로 test함. 한 날짜의 모든 발전량을 예측함. 20일을 사용 : [2,20]
#       training data의 일부로 test함. training data의 20%를 랜덤하게 뽑아 트레이닝 데이터로 사용 : [3,0.2]
##
##ex) = ["yy", [1,2,4,7,8], ["le1b_vis","le1b_ir01","le2_ins"], "CNN", [-3,-2,-1,0],
#           True, 0, [ ["C",3,16,"same"]],[['F', 64],['F',128],['F',64]], 10, [1]]]
#

all_case =[
        ["yy", [1,2,4,7,8], ["le1b_vis","le1b_ir01","le2_ins"], "CNN", [-3,-2,-1,0],
          True, 11,[ ["C",3,16,"same"]], [['F', 64],['F',128],['F',64]], 1, [1]]
        ]
        


df = pd.read_csv(".\\data\\plant_info.csv")
df.index = df.iloc[:,0]
def iterate( _case ):
    numofex = len(all_case)
  
    plant_id, weather_ele, comsset, str_cnn_mode, hours, use_image_fnn, patch_size, layers_cnn, combine_layers, numofex, test_mode = all_case[_case] 
    
    if str_cnn_mode == "FNN" or str_cnn_mode =="fnn":
        cnn_mode = 0
    elif str_cnn_mode == "CNN" or str_cnn_mode =="cnn":
        cnn_mode = 1
    
    if use_image_fnn:
        no_coms = 0
    else:
        no_coms = 1
    

    cap = df.loc[plant_id,"cap"]
        
    return (plant_id, cap, weather_ele, comsset, cnn_mode, hours, no_coms, patch_size, layers_cnn,combine_layers, numofex, test_mode )
    
