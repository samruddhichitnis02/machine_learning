import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle


class Single_Trainer:
    def __init__(self):
        pass
    
    def shapes(self,x):
        transform_x = x.shape[0]
        transform_w = x.shape[1]
        
        return transform_x, transform_w
    
    def initialize(self,transform_x, transform_w, x, y):
        x = np.reshape(x,(transform_w,transform_x))
        y = np.reshape(y,(1,transform_x))
        
        np.random.seed(0)
        W = np.random.randn(1,transform_w) * 0.01
        b = np.zeros((1,1))
        
        parameters = {'W':W, 'b':b}
        return x, y, parameters
    
    def forward_propagation(self, x, parameters):
        W = parameters['W']
        b = parameters['b']
        
        Z = np.dot(W, x) +b
        return  Z
    
    def sigmoid(self, Z):
        sigmoid = 1 / (1 + np.exp(-Z))
        return sigmoid
    
    def backward_propagation(self, A, x, y):
        dz = A - y
        m = x.shape[1]
        dw = (np.dot(x, dz.T)) / m
        db = np.sum(dz) / m
        db = np.reshape(db,(1,1))
        
        grads = {'dw':dw, 'db':db}
        
        return grads
    
    def update(self,parameters, grads,learning_rate):
        W = parameters['W']
        b = parameters['b']
        
        dw = grads['dw']
        db = grads['db']
        
        W = W - (learning_rate * dw.T)
        b = b- (learning_rate * db)
        
        parameters = {'W':W, 'b':b}
        return parameters
    
    def compute_cost(self,A, x, y):
        m = x.shape[1]
        L = (y * np.log(A)) + ((1-y)  * np.log(1-A))
        cost = - (np.sum(L) / m)
        return cost
    
    def learning_model(self, x_train, y_train):
        epoch = int(input('Enter the number of iterations-'))
        learning_rate = float(input('Enter the learning rate-'))
        cost_list = [ ]
        transform_x, transform_w = self.shapes(x_train)
        x, y, parameters = self.initialize(transform_x, transform_w, x_train, y_train)
        
        for i in range(epoch):
            Z = self.forward_propagation(x, parameters)
            A = self.sigmoid(Z)
            cost = self.compute_cost(A, x, y)
            cost_list.append(cost)
            grads = self.backward_propagation(A, x, y)
            parameters = self.update(parameters, grads, learning_rate)
            pickle_out = open("singlelayer_parameters.pickle","wb")
            pickle.dump(parameters, pickle_out)
            pickle_out.close()
        return parameters, cost_list
    
    def single_layer(self,x_test, y_test, new_parameters, cost_list):
        plt.plot(cost_list)
        plt.show()
    
        transform_x, transform_w = self.shapes(x_test)
        x, y, para = self.initialize(transform_x, transform_w, x_test, y_test)
    
        Z1 = self.forward_propagation(x, new_parameters)
        A1 = self.sigmoid(Z1)
    
        return A1,y
    
    
    def accuraccy(self,A1,y):
        accuracy = 0
        predictions = [ ]
        [predictions.append(1) if A1[0][i] > 0.5 else predictions.append(0) for i in range(len(A1[0]))]

        for i in range(len(predictions)):
            if predictions[i] == y[0][i]:
                accuracy += 1
        acc = (accuracy / len(predictions)) * 100
        return acc