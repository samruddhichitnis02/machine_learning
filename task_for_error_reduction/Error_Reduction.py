#Importing Libraries

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import  OneHotEncoder, StandardScaler
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')



data = pd.read_csv('train.csv')


print(data.info())

print(data.describe())


#Checking For null Values if any
print(data.isnull().any())


#Checking for unique values in column Id of antenna reading sensor
print(data['Id of antenna reading sensor'].unique())


#Plotting the number of occurences of classes for target variable
sb.countplot(data['Label of activity'])
plt.show()



#Visualising the distribution of dataset
data.hist(figsize = (15, 8))
plt.show()



sb.pairplot(data)
plt.show()


#Visualising the corelation through heatmaps
fig, ax = plt.subplots(figsize = (10,10))
sb.heatmap(data.corr(), annot = True)
plt.show()


# Applying KNearest Neighbours for the 1st time 

#data is Training data set
x = data.iloc[:,0:-1]
y = data.iloc[:, -1:].values



ohe = OneHotEncoder(categorical_features = [4])
x = ohe.fit_transform(x).toarray()



kn = KNeighborsClassifier()
kn.fit(x,y)


#cv_data is the cross validation dataset
cv_data = pd.read_csv('cross_validation.csv')


cv_x = cv_data.iloc[:, 0:-1]
cv_y = cv_data.iloc[:, -1:].values


cv_x = ohe.transform(cv_x).toarray()


# accuracy = cross_val_score(kn, x, y, cv = 3)
# accuracy

# accuracy.mean()

#applying the model->knn and cross validation on cross validation dataset
y_pred_1 = cross_val_predict(kn, cv_x, cv_y, cv = 3)

#Classification of the model without any error reduction techniques
cr = classification_report(cv_y, y_pred_1)
print(cr)


#Applying Standard Scalar to check  if accuracy increases

#data is Training Data
x_1 = data.iloc[:,0:-1]
y_1 = data.iloc[:,-1:].values


standard = StandardScaler()
x_1.iloc[:,[0,5,7]] = standard.fit_transform(x_1.iloc[:,[0,5,7]])


x_1 = ohe.transform(x_1).toarray()

kn_1 = KNeighborsClassifier()
kn_1.fit(x_1, y_1)


#cv_data --> Cross Validation Dataset
cv_data.head()

cv_x1 = cv_data.iloc[:,0:-1]
cv_y1 = cv_data.iloc[:,-1:].values


cv_x1.iloc[:,[0,5,7]] = standard.transform(cv_x1.iloc[:,[0,5,7]])


#Applying Cross Validation 
cv_x1 = ohe.transform(cv_x1).toarray()



y_pred_2 = cross_val_predict(kn_1, cv_x1, cv_y1, cv = 3)

#Checking classificication report of cross validation dataset after using Standard Scalar
cr1 = classification_report(cv_y1, y_pred_2)
print(cr1)

cm2 = confusion_matrix(cv_y1, y_pred_2)
print(cm2)


score1 = accuracy_score(cv_y1, y_pred_2)
print(score1)


#Applying Grid Search

#Training Dataset
x_2 = data.iloc[:,0:-1]
y_2 = data.iloc[:,-1:].values


x_2.iloc[:,[0,5,7]] = standard.transform(x_2.iloc[:,[0,5,7]])


x_2 = ohe.transform(x_2).toarray()


kn_2 = KNeighborsClassifier()
kn_2.fit(x_2, y_2)


parameters = [{'n_neighbors': [3,5,7], 'metric': ['minkowski'], 'p':[2]},
             {'n_neighbors' : [3,5,7], 'metric': ['minkowski'], 'p':[1]}]

grid_search = GridSearchCV(estimator = kn_2,
                          param_grid = parameters,
                          scoring = 'accuracy',
                          cv = 3)

grid_search = grid_search.fit(x_2, y_2)


#Grid Search Accuracy
accuracy = grid_search.best_score_

print(accuracy)

#Tuned Hyperparameters from grid search
print(grid_search.best_params_)


#Fitting the dataset by using the hyperparameters tuned by grid search 
kn_2 = KNeighborsClassifier(n_neighbors = 3, metric = 'minkowski', p = 1)
kn_2.fit(x_2, y_2)


# cv_data --> Cross Validation Dataset
cv_x2 = cv_data.iloc[:,0:-1]
cv_y2 = cv_data.iloc[:,-1:].values

cv_x2.iloc[:,[0,5,7]] = standard.transform(cv_x2.iloc[:,[0,5,7]])


cv_x2.head()

cv_x2 = ohe.transform(cv_x2).toarray()

#Applying Cross Validation 
y_pred_3 = cross_val_predict(kn_2, cv_x2, cv_y2, cv = 3)


#Checking classificication report of cross validation dataset after using Grid Search
cr2 = classification_report(cv_y2, y_pred_3)
print(cr2)

score2 = accuracy_score(cv_y2, y_pred_3)
score2

matrix = confusion_matrix(cv_y2, y_pred_3)

matrix = pd.DataFrame(matrix)


sb.heatmap(matrix, annot = True, cmap = 'Blues',fmt='.6g')
plt.show()


import pickle

objects = {'standard':standard, 'ohe':ohe, 'kn_2':kn_2}
pickle.dump(objects,open('model.pkl', 'wb'))



obj = pickle.load(open('model.pkl','rb'))
standard1 = obj['standard']
ohe1 = obj['ohe']
model = obj['kn_2']
