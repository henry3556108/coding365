import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from io import StringIO
from sklearn import preprocessing

def foo(x):
    return 1.2 * x + 0.8 + 0.5  * np.random.randint(10)
x = np.linspace(50,100,50).reshape(50,1)
y = np.array(list(map(foo,x))).reshape(50,1)
data=np.concatenate((x,y),axis=1)
df= pd.DataFrame(data)
X = df.iloc[:,0].values
y = df.iloc[:,1].values
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)
regressor = LinearRegression()
regressor.fit(X_train,y_train)
print(y_test)
print(regressor.predict(X_test))
print(regressor.score(X_test,y_test))
plt.scatter(X_test,y_test,color= 'black')
plt.xlabel("a")
plt.ylabel("b")
plt.title( 'no idea what am i doing' )
plt.savefig(r'C:\Users\user\Desktop\機器學習\腋毛.png')
plt.plot(X_test,regressor.predict(X_test),'r')
plt.show()