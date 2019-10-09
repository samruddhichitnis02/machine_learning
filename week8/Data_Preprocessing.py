import pandas as pd
import numpy as np



class Data_Preprocessing:
    def __init__(self):
        pass
    
    
    def problem1(self):
    
        ############################ Data Preprocessing For Problem1 ###############################
        data = pd.read_csv('bank.csv', delimiter = ';')

        data_num = data.select_dtypes(include = [np.number]) #will consider the columns which has numeric data
        data_num = (data_num - data_num.mean()) / (data_num.std())
        data[data_num.columns] = data_num        

        data = pd.get_dummies(data = data, drop_first = True)
        
        n = float(input('Enter a float value to split-'))
        Training_data = int(n * len(data))
        x_train, y_train, x_test, y_test = np.array(data.iloc[0:Training_data, 0:-1]), np.array(data.iloc[0:Training_data,-1:]), np.array(data.iloc[Training_data:, 0:-1]), np.array(data.iloc[Training_data:, -1:])

        return x_train, y_train, x_test, y_test 

    def problem2(self):
    
        ############################ Data Preprocessing For Problem1 ###############################
        data = pd.read_csv('Churn_Modelling.csv')
        o_data = data.iloc[:, -1:]
        data.drop(['Surname','Exited'], axis = 1, inplace = True)

        #Feature Scaling
        data_num = data.select_dtypes(include = [np.number]) #will consider the columns which has numeric data
        data_num = (data_num - data_num.mean()) / (data_num.std())
        data[data_num.columns] = data_num  


        #one hot encoding
        data = pd.get_dummies(data = data, drop_first = True)
        o_data = pd.get_dummies(data = o_data, drop_first = True)


        #Splitting data
        n = float(input('Enter a float value to split data-'))
        Training_data = int(n * len(data))

        x_train, x_test = np.array(data.iloc[0:Training_data, :]), np.array(data.iloc[Training_data:, :])

        y_train, y_test = np.array(o_data.iloc[0:Training_data, :]), np.array(o_data.iloc[Training_data:, :])
    
        return x_train, y_train, x_test, y_test


    def choice(self):
        choice = int(input('Enter 1 to solve problem 1 & 2 to solve problem2-'))
        if choice == 1:
            x_train, y_train, x_test, y_test = self.problem1()
            return x_train, y_train, x_test, y_test
        elif choice == 2:
            x_train, y_train, x_test, y_test = self.problem2()
            return x_train, y_train, x_test, y_test