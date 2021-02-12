from sklearn.neighbors import  NearestNeighbors, KNeighborsClassifier, KNeighborsRegressor 
from sklearn.datasets import load_iris
iris_data=load_iris()
iris_data.data
from sklearn.model_selection import cross_val_predict
x=iris_data.data
y=iris_data.target
knn = KNeighborsClassifier(n_neighbors=10)
y_pred= cross_val_predict(knn, x, y, cv=5)
y_pred
from sklearn.metrics import mean_squared_error, r2_score
error = []
for k in range (1,51):
    knn =KNeighborsClassifier(n_neighbors=k)
    y_pred = cross_val_predict(knn, x, y, cv=5)
    error.append(mean_squared_error(y,y_pred))
import matplotlib.pyplot as plt
plt.plot(range(1,51),error)
from sklearn.datasets import load_boston
boston_data= load_boston()
boston_data.data
boston_data.target

x=boston_data.data
y=boston_data.target
knn= KNeighborsRegressor(n_neighbors=10)
y_pred = cross_val_predict(knn, x, y, cv=5)

y_pred
x=boston_data.data
y=boston_data.target
knn=KNeighborsRegressor(n_neighbors=10)
y_pred =cross_val_predict(knn, x, y, cv=5)
y_pred

from math import sqrt
print(mean_squared_error(y,y_pred))
print(r2_score(y,y_pred))

error = []
for k in range(1,51):
    knn=KNeighborsRegressor(n_neighbors=k)
    y_pred = cross_val_predict(knn, x, y, cv=5)
    error.append(mean_squared_error(y,y_pred))
plt.plot(range(1,51),error)

from sklearn.preprocessing  import StandardScaler
from sklearn.pipeline   import make_pipeline

classifier_pipeline = make_pipeline(StandardScaler(), KNeighborsRegressor(n_neighbors=10))

y_pred=cross_val_predict(classifier_pipeline, x, y, cv=5)
print(mean_squared_error(y,y_pred))
print(r2_score(y,y_pred))

error =[]
for k in range (1,51):
    classifier_pipeline= make_pipeline(StandardScaler(), KNeighborsRegressor(n_neighbors=k))
    y_pred = cross_val_predict(classifier_pipeline, x, y, cv=5)
    error.append(mean_squared_error(y,y_pred))
    
plt.plot(range(1,51), error)

from sklearn.model_selection import KFold
cv =KFold(n_splits=5 ,random_state=0, shuffle=False)

classifier_pipeline=make_pipeline(StandardScaler(),KNeighborsRegressor(n_neighbors=10))
y_pred = cross_val_predict(classifier_pipeline, x, y, cv=cv)
print(mean_squared_error(y,y_pred))
print(r2_score(y,y_pred))



