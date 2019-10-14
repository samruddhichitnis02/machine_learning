from Multilayer_Utility import Multilayer_Trainer
from Data_Preprocessing import Data_Preprocessing


obj = Data_Preprocessing()
x_train, y_train, x_test, y_test = obj.choice()
obj1 = Multilayer_Trainer()

new_parameters, cost_list = obj1.nn_model(x_train, y_train)
A3, y = obj1.multi_layer(x_test, y_test, new_parameters, cost_list)

accuracy = obj1.accuraccy(A3, y)
print(accuracy)