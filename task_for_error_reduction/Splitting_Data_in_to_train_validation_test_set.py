
import os
import glob
import pandas
directory1 = '/home/admin1/Downloads/machine_learning/task_for error_reduction/Datasets_Healthy_Older_People/S1_Dataset/'
file1 = glob.glob(directory1 + '/*')

directory2 = '/home/admin1/Downloads/machine_learning/task_for error_reduction/Datasets_Healthy_Older_People/S2_Dataset/'
file2 = glob.glob(directory2 + '/*')


files = file1 + file2


print(len(files))


#combining all the data from datsetS1 and DatasetS2
with open('dataset.txt','w') as outfile:
    for names in files:
        if names.endswith('.txt'):
            continue
        with open(names) as infile:
            for line in infile:
                outfile.write(line)


import pandas as pd
data = pd.read_csv('dataset.txt', header = None)



print(data.head())


print(data.shape)

#Renaming the columns of dataframe
data.columns = ['Time(secs)', 'Acceleration reading in G(frontal axis)',
                          'Acceleration reading in G (vertical axis)',
                          'Acceleration reading in G(lateral axis)',
                          'Id of antenna reading sensor',
                          'Received signal strength indicator (RSSI)',
                          'Phase','Frequency', 'Label of activity']


#Dividing the dataset in to Training Datset, Cross Validation Dataset and Test Dataset
import numpy as np
train, validate, test = np.split(data.sample(frac = 1), [ int(0.6*len(data)), int(0.8*len(data))])


print(train.head())


print(train.shape)


print(test.head())


print(test.shape)


print(validate.head())


print(validate.shape)


#Training Dataset
train.to_csv('train.csv', index = False)


#Cross Validatoin Dataset
validate.to_csv('cross_validation.csv', index = False)

#Test Dataset
test.to_csv('test.csv', index = False)

