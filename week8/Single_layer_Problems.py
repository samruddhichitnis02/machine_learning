from Single_Utility import Single_Trainer
from Data_Preprocessing import Data_Preprocessing



obj = Data_Preprocessing()
x_train, y_train, x_test, y_test = obj.choice()
obj1 = Single_Trainer()

new_parameters, cost_list = obj1.learning_model(x_train, y_train)
A1, y = obj1.single_layer(x_test, y_test, new_parameters, cost_list)

accuracy = obj1.accuraccy(A1, y)
print(accuracy)
