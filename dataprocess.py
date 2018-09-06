#!/usr/bin/python3
#-*- coding=utf-8 -*-
"""
Created on 03-09-2018  22:44:25 
@author: crunch
"""

import numpy as np
import pandas as pd
from collections import Counter
import os
WORKSPACE = os.getcwd()

HEADER = ['frame_id','Q1','a1_1','a1_2','a1_3','Q2','a2_1','a2_2','a2_3','Q3','a3_1','a3_2','a3_3','Q4','a4_1','a4_2','a4_3','Q5','a5_1','a5_2','a5_3']
QUESTION = ['Q1','Q2','Q3','Q4','Q5']
ANSWER = ['a1_1','a1_2','a1_3','a2_1','a2_2','a2_3','a3_1','a3_2','a3_3','a4_1','a4_2','a4_3','a5_1','a5_2','a5_3']

#### 得到所有的解
traintxt = pd.read_csv(os.path.join(WORKSPACE,'datas','train.txt'), header=None, names=HEADER, index_col=None) #### encoding='gb2312':其他编码中文显示错误  index_col=0:设置第1列数据作为index
all_answers = traintxt[ANSWER]
#print(all_answers.shape) #### (3325, 15)


#### 得到答案词频
ans_freq = Counter()
for ans in ANSWER:
    ans_freq += Counter(all_answers[ans])
#ans_freq = dict(ans_freq)
#print(len(list(ans_freq)))  #### 4744
#print(ans_freq.most_common(100))
print(ans_freq)
ans_file = os.path.join(WORKSPACE,'results','ans_freq.txt')
_f = open(ans_file,'w')
for i in ans_freq:
    _write_str = str(i) + ',' + str(ans_freq[i]) + '\n'
    _f.write(_write_str)
_f.close()
