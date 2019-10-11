from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings('ignore')
import pickle
import pandas as pd
from prettytable import PrettyTable


import glob
import os


#Getting files from dataset1

s1_directory = '/home/admin1/machine_learning/Task_for_Classification/Datasets_Healthy_Older_People/S1_Dataset'
s1_filename = glob.glob(s1_directory + '/*')


files = [ ]
for name in s1_filename:
    if name.endswith('.txt'):
        continue
    data = pd.read_csv(name, header = None, index_col = None)
    files.append(data)

s1_data = pd.concat(files, axis = 0, ignore_index = True)



s2_directory = '/home/admin1/machine_learning/Task_for_Classification/Datasets_Healthy_Older_People/S2_Dataset'
s2_filename = glob.glob(s2_directory + '/*')


#Getting Files from Dataset2

files = [ ]
for name in s2_filename:
    if name.endswith('.txt'):
        continue
    data = pd.read_csv(name, header = None, index_col = None)
    files.append(data)

s2_data = pd.concat(files, axis = 0, ignore_index = True)



s1_data.shape


s2_data.shape

#Concatinating Dataset1 and Dataset2

new_data = pd.concat([s1_data,s2_data], axis = 0, ignore_index = True)



new_data.shape


new_data.head()


#Assigning column names to the dataset
new_data.columns = ['Time(secs)', 'Acceleration reading in G(frontal axis)',
                          'Acceleration reading in G (vertical axis)',
                          'Acceleration reading in G(lateral axis)',
                          'Id of antenna reading sensor',
                          'Received signal strength indicator (RSSI)',
                          'Phase','Frequency', 'Label of activity']



new_data.head()


x = new_data.iloc[:, 0:-1].values
y = new_data.iloc[:, -1:].values



standard_x = StandardScaler()
x = standard_x.fit_transform(x)



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)



y_train.shape

#Applying all the Classification Algorithms on the dataset

algorithms = {'LogisticRegression':LogisticRegression(),
              'KNearestNeighbours':KNeighborsClassifier(n_neighbors = 3, metric='minkowski', p = 2),
              'SupportVectorMachine':SVC(kernel = 'linear'), 
              'DecisionTree':DecisionTreeClassifier(criterion = 'entropy', max_depth = 3), 
              'RandomForest':RandomForestClassifier(n_estimators = 10, criterion = 'entropy', max_depth = 3)}
    
p = PrettyTable(["Algorithm", "AccuracyScore(test)", "AccuracyScore(train)"])

for key,value in algorithms.items():
    value.fit(x_train, y_train)
    y_pred_train = value.predict(x_train)
    y_pred_test = value.predict(x_test)
    p.add_row([key, value.score(x_test, y_test), value.score(x_train, y_train)])
    
print(p)
        



model = algorithms['SupportVectorMachine']




objects = {'standard_x':standard_x, 'model': model}
pickle.dump(objects, open('model.pkl','wb'))





a = new_data.iloc[:1,0:-1].values


a = standard_x.transform(a)



a.shape


model.predict(a)
