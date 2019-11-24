# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19T7upbyJGa_B9CcfglIR7SHvdcH5_RMK
"""

train = '/content/drive/My Drive/Colab Notebooks/datasets/zhengqi_pred/zhengqi_train.txt'
test = '/content/drive/My Drive/Colab Notebooks/datasets/zhengqi_pred/zhengqi_test.txt'

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import lightgbm as lgb
import matplotlib.pyplot as plt
from scipy.special import jn
from IPython.display import display, clear_output
import time

# %matplotlib inline

train_data = pd.read_csv(train, sep='\t')
test_data = pd.read_csv(test, sep='\t')

train_data.head()

# 分别显示38个属性在训练集与测试集上的分布
plt.figure(figsize=[6,120])
for i in range(38):
    ax = plt.subplot(38,1,i+1)
    pd.DataFrame(train_data).iloc[:,i].plot(kind='kde',ax=ax,color="red")
    pd.DataFrame(test_data).iloc[:,i].plot(kind='kde',ax=ax)
    ax.set_title(test_data.columns[i])

# 通过观察，删除分布差异较大的属性
drop_columns = ['V5','V9','V17','V19','V20', 'V21', 'V22', 'V27','V35']
train_data.drop(columns=drop_columns,inplace=True)
test_data.drop(columns=drop_columns,inplace=True)

# 查看各个属性之间的相关性
t = train_data.corr()

# 删除相关性较低的属性
drop_columns = t[(np.abs(t["target"])<0.05)].index
train_data.drop(columns=drop_columns,inplace=True)
test_data.drop(columns=drop_columns,inplace=True)

# 数据分割
from sklearn.model_selection import train_test_split
X = train_data.iloc[:,:-1]
y = train_data['target']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

# 生成训练数据
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

# 设置模型参数
params = {
      'task': 'train',
      'boosting_type': 'gbdt',
      'objective': 'regression',
      'metric': {'l2', 'auc'},
      'num_leaves':31 ,
      'learning_rate': 0.01,
      'feature_fraction': 0.9,
      'bagging_fraction': 0.7,
      'bagging_freq': 2,
      'header': True
}

# 训练模型
gbm = lgb.train(params,
         lgb_train,
         num_boost_round=10000,
         valid_sets=lgb_eval,
         early_stopping_rounds=200)

# 预测测试数据
y_pred = gbm.predict(test_data, num_iteration=gbm.best_iteration)
y_pred

# 生成提交文件
df = pd.DataFrame(y_pred)
df.to_csv('submit.txt', index=False)

