import numpy as np
import pandas as pd


dataset = pd.read_csv('~/Documents/GitHub/100-Days-of-ML/100-Days-Of-ML-Code/datasets/Data.csv')
print(dataset)
print('=========================')

# loc[列,欄] 應用於文字
# df.loc[行index,[column name]]
X = dataset.iloc[ 0:1 , :]
print(X)
print('=========================')

# iloc[列,欄] 應用於數字
# df.iloc[行index,列index]
Y = dataset.iloc[ 0:1, 1]
print(Y)
print('=========================')


# List不支持 element-wise 運算
list1 = [46, 8, 11, 11, 4, 56]
print(list1*5)
print('=========================')

# Numpy支持 element-wise 運算
# Numpy的ndarray只允許一種資料類型

list1_np = np.array([46, 8, 11, 11, 4, 56])
print(list1_np*5)


# print('=========================')
# print(dataset['Age']*dataset.index*dataset['Salary'])











