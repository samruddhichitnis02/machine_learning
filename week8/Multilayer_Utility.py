import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle 


class Multilayer_Trainer:
    def __init__(self):
        pass
    
    def shapes(self,x):
        transform_x = x.shape[0]
        transform_w = x.shape[1]
        return transform_x, transform_w
    
    def initialize(self,transform_x, transform_w, x, y):
        x = np.reshape(x, (transform_w,transform_x))
        y = np.reshape(y, (1,transform_x))
    
        np.random.seed(0)
        W1 = np.random.randn(5,transform_w) * 0.01
        b1 = np.zeros((5,1))
    
        W2 = np.random.randn(3,5) * 0.01
        b2 = np.zeros((3,1))
    
        W3 = np.random.randn(1,3) * 0.01
        b3 = np.zeros((1,1))
    
        parameters = {'W1':W1,'b1':b1, 'W2':W2, 'b2':b2, 'W3':W3, 'b3':b3}
    
        return x, y, parameters
    
    def sigmoid(self,Z):
        sigmoid = 1 / (1 + np.exp(-Z))
        return sigmoid
    
    def forward_propagation(self,x, parameters):
        W1 = parameters['W1']
        b1 = parameters['b1']
     
        W2 = parameters['W2']
        b2 = parameters['b2']
    
        W3 = parameters['W3']
        b3 = parameters['b3']
    
    
        Z1 = np.dot(W1,x) + b1
        A1 = np.tanh(Z1)
    
        Z2 = np.dot(W2,A1) + b2
        A2 = self.sigmoid(Z2)
    
        Z3 = np.dot(W3,A2) + b3
        A3 = self.sigmoid(Z3)
    
        cache = {'A1': A1, 'A2':A2, 'A3':A3}
    
        return cache
    
    def backward_propagation(self,parameters, cache, x, y):
        A1 = cache['A1']
        A2 = cache['A2']
        A3 = cache['A3']
    
        W2 = parameters['W2']
        m  = x.shape[1]
    
        dZ3 = A3 - y
        dW3 = (1 / m) * np.dot(dZ3, A2.T)
        db3 = (1 / m) * np.sum(dZ3, axis=1, keepdims=True)
    
    
        dZ2 = A2 - y
        dW2 = (1 / m) * np.dot(dZ2, A1.T)
        db2 = (1 / m) * np.sum(dZ2, axis = 1, keepdims = True)
    
        dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2))
        dW1 = (1 / m) * np.dot(dZ1,x.T)
        db1 = (1 / m) * np.sum(dZ1, axis = 1, keepdims = True)
    
        grads = {'dW3':dW3, 'db3':db3, 'dW2':dW2, 'db2':db2, 'dW1':dW1, 'db1':db1}
        return grads
    
    def update(self,parameters, grads, learning_rate):
        W1 = parameters['W1']
        b1 = parameters['b1']
    
        W2 = parameters['W2']
        b2 = parameters['b2']
    
        W3 = parameters['W3']
        b3 = parameters['b3']
    
    
        dW1 = grads['dW1']
        db1 = grads['db1']
    
        dW2 = grads['dW2']
        db2 = grads['db2']
    
        dW3 = grads['dW3']
        db3 = grads['db3']
    
        W1 = W1 - (learning_rate * dW1)
        b1 = b1 - (learning_rate * db1)
    
        W2 = W2 - (learning_rate * dW2)
        b2 = b2 - (learning_rate * db2)
    
        W3 = W3 - (learning_rate * dW3)
        b3 = b3 - (learning_rate * db3)
    
    
        parameters = {'W1':W1,'b1':b1, 'W2':W2, 'b2':b2, 'W3':W3, 'b3':b3}
        return parameters
    
    def compute_cost(self,cache, x, y):
        A3 = cache['A3']
        m = x.shape[1]
        L = (y * np.log(A3)) +((1-y) * np.log(1-A3))
        cost = - ( np.sum(L) / m)
        return cost
    
    def nn_model(self,x1, y1):
        epoch = int(input('Enter the number of iterations-'))
        learning_rate = float(input('Enter the learning rate-'))
        cost_list = [ ]
        transform_x, transform_w = self.shapes(x1)
        x, y, parameters = self.initialize(transform_x, transform_w, x1, y1)
        for i in range(epoch):
            cache = self.forward_propagation(x, parameters)
            cost = self.compute_cost(cache, x, y)
            cost_list.append(cost)
            grads = self.backward_propagation(parameters, cache, x, y)
            parameters = self.update(parameters, grads, learning_rate)
            pickle_out = open("multilayer_parameters.pickle","wb")
            pickle.dump(parameters, pickle_out)
            pickle_out.close()
        return parameters, cost_list
    

    def multi_layer(self,x_test, y_test, new_parameters, cost_list):
        plt.plot(cost_list)
        plt.show()
    
        transform_x, transform_w = self.shapes(x_test)
        x, y, para = self.initialize(transform_x, transform_w, x_test, y_test)
    
        cache = self.forward_propagation(x, new_parameters)
        A3 = cache['A3']
    
        return A3,y

    def accuraccy(self,A3,y):
        accuracy = 0
        predictions = [ ]
        [predictions.append(1) if A3[0][i] > 0.5 else predictions.append(0) for i in range(len(A3[0]))]

        for i in range(len(predictions)):
            if predictions[i] == y[0][i]:
                accuracy += 1
        acc = (accuracy / len(predictions)) * 100
        return acc
