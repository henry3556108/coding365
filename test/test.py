import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pprint import * 
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import tree
import random
import sqlite3
import datetime

iris = datasets.load_iris()
data_x = iris.data
data_y = iris.target
data_x = preprocessing.scale(data_x)
X_train, X_test, y_train, y_test = train_test_split(data_x,data_y, test_size=0.3)
model= svm.LinearSVC()
model.fit(X_train,y_train)
print(y_test[:5])
print(model.predict(X_test[:5]))
print(np.rint(model.predict(X_test[:5])))
print(model.score(X_test,y_test))
















# dataset = pd.read_csv("C:\\Users\\user\\Desktop\\dataset.csv")
# print(dataset)
# x=dataset.iloc[2:5,1].values
# print(x)


# X = dataset.iloc[2:5,0].values
# y = dataset.iloc[2:5,1].values

# #資料視覺化
# plt.scatter(x,y, color='blue')
# plt.plot(x,y, color='red')
# plt.title( 'YearsExperience & Salary' )
# plt.xlabel('YearsExperience')
# plt.ylabel('Salary')
# plt.savefig(r'C:\\Users\\user\\Desktop\\dataset.png')
# plt.show()



