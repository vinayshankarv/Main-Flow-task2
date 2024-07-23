import pandas as pd
data = pd.read_csv('D:\\Main Flow\\Tasks\\01.Data Cleaning and Preprocessing.csv')
type(data)
data.info
data.describe()
data = data.drop_duplicates()
data
data.isnull()
data.isnull().sum()
data.isnull().sum().sum()
data2 = data.fillna(value=0)
data2
data3 = data.fillna(method='pad')
data3 
data4 = data.fillna(method='bfill')
data4
import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats
data2.columns
data2.drop(['Observation'], axis=1, inplace=True)
data2.columns
Q1= data2.quantile(0.25)
Q3= data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)
data2=data2[~((data2<(Q1-1.5*IQR))| (data2>(Q3+1.5*IQR))).any(axis=1)]
data2
data2.describe()







