
df= pd.DataFrame(data)
X = df.iloc[:,0].values
y = df.iloc[:,1].values
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)
regressor = LinearRegression()
regressor.fit(X_train,y_train)
print(regressor.predict(X_test))