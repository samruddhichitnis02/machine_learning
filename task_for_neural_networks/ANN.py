from keras.models import Sequential
from keras.layers import Dense

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv('crx.data', header = None)


# In[3]:


data.head()


# In[4]:


data.columns = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
               'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'classes']


# In[5]:


data.head()


# In[70]:


sb.countplot(data['classes'])
plt.show()


# In[6]:


data.head().isnull().any().any()


# In[7]:


data['A1'].value_counts()


# In[8]:


data[(data == '?')].any()


# In[36]:


df = pd.read_csv('crx.data', na_values=['?'], header = None)


# In[37]:


df.head()


# In[38]:


df.columns = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
               'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'classes']


# In[39]:


df.head()


# In[40]:


df.isnull().any()


# In[41]:


df['A1'].unique()


# In[42]:


df.shape


# # Handling Missing Values

# In[43]:


df['A2'].fillna(df['A2'].mean(), inplace=True)
df['A14'].fillna(df['A14'].mean(), inplace = True)


# In[44]:


df=df.fillna(method='ffill')


# In[45]:


df.isnull().any()


# In[46]:


df.dtypes


# # Applying Standard Scalar

# In[47]:


sc = StandardScaler()
for col in df:
    if (df[col].dtype == 'float64') or (df[col].dtype == 'int64'):
        df[[col]]=sc.fit_transform(df[[col]])


# In[48]:


df.head()


# # Applying label Encoding

# In[49]:


le = LabelEncoder()
for col in df:
    if df[col].dtype == 'object':
        df[[col]] = le.fit_transform(df[[col]])


# In[50]:


df.head()


# In[51]:


fig = plt.figure(figsize = (10,4))
f1 = fig.add_subplot(1,2,1)
f2 = fig.add_subplot(1,2,2)
sb.countplot(df['A1'], ax = f1)
sb.countplot(df['A4'], ax = f2)
plt.show()


# In[52]:


fig = plt.figure(figsize = (10,4))
f1 = fig.add_subplot(1,2,1)
f2 = fig.add_subplot(1,2,2)
sb.countplot(df['A5'], ax = f1)
sb.countplot(df['A6'], ax = f2)
plt.show()


# In[53]:


fig = plt.figure(figsize = (10,4))
f1 = fig.add_subplot(1,2,1)
f2 = fig.add_subplot(1,2,2)
sb.countplot(df['A10'], ax = f1)
sb.countplot(df['A12'], ax = f2)
plt.show()


# In[54]:


sb.countplot(df['A13'])
plt.show()


# # Applying One Hot Encoding

# From the above graphs we can see that only columns A4, A5, A6, A7 and A13 have more than 2 categories 

# In[55]:


X = df.iloc[:, 0:-1]
Y = df.iloc[:,-1:]


# In[56]:


X.shape, Y.shape


# In[61]:


ohe = OneHotEncoder(categorical_features = [3, 4, 5, 6, 12])
X = ohe.fit_transform(X).toarray()


# In[62]:


X[0]


# In[63]:


X.shape


# # Splitting data in to training and testing

# In[64]:


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


# In[65]:


x_train.shape, x_test.shape, y_train.shape, y_test.shape


# # Initialising the ANN

# In[69]:


model = Sequential()


# # Adding Hidden Layers

# In[71]:


model.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 42))
model.add(Dense(output_dim = 6, init = 'uniform', activation = 'sigmoid'))


# # Adding Output Layer

# In[72]:


model.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))


# # Compile the Artificial Neural network

# In[73]:


model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# In[74]:


model.summary()


# # Fitting the ANN to the training set 

# In[75]:


model.fit(x_train, y_train, batch_size = 20, nb_epoch = 100)


# # Predicting the Test set Result

# In[76]:


y_pred = model.predict_classes(x_test)


# In[78]:


y_pred[0:5]


# In[81]:


score = accuracy_score(y_test, y_pred)
score


# In[82]:


print(classification_report(y_test, y_pred))


# In[83]:


cm = confusion_matrix(y_test, y_pred)
cm


# # Predicting the result for one input example

# In[92]:


df.iloc[45, -1:]


# # Applying one hot encoding to row number 45 as the values are already scaled and label encoded. Also the output value is 0.0 i.e class '+'

# In[95]:


example = df.iloc[45, 0:-1].values


# In[96]:


example


# In[98]:


example = ohe.transform([example]).toarray()


# In[99]:


example


# In[100]:


example.shape


# In[101]:


prediction = model.predict_classes(example)


# In[102]:


prediction


# In[104]:


if prediction:
    print('The class is -')
else:
    print('The class is +')


# In[ ]:




