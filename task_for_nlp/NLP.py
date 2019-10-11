from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

import re
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


#  Using Facebook Dataset to find which category(economy, microsoft, obama, palestine) the news article belong 

#Loading Facebook Economy Dataset
fb_economy = pd.read_csv('Facebook_Economy.csv')

fb_economy.isnull().any().any()

fb_economy.shape


#Loading Facebook Microsoft Dataset
fb_microsoft = pd.read_csv('Facebook_Microsoft.csv')

fb_microsoft.isnull().any().any()

fb_microsoft.shape


#Loading Facebook Obama Dataset
fb_obama = pd.read_csv('Facebook_Obama.csv')

fb_obama.isnull().any().any()

fb_obama.shape


#Loading Facebook Palestine Dataset
fb_palestine = pd.read_csv('Facebook_Palestine.csv')

fb_palestine.isnull().any().any()

fb_palestine.shape


#Concatenating all the types of facebook data to fb_data
fb_data = pd.concat([fb_economy, fb_microsoft,
                    fb_obama, fb_palestine], ignore_index = True)

fb_data.head()

fb_data.shape


#Final News Dataset
data = pd.read_csv('News_Final.csv')

data.head()

data.info()


#Merging all FAcebook data with Final News Data on IDLink column
facebook = pd.merge(data, fb_data, on = "IDLink")

facebook.head()

facebook.shape

facebook['Headline'].isnull().sum()

facebook['Topic'].isnull().sum()

facebook = facebook.dropna()

facebook.shape

facebook.head()

#Setting the index value of dataframe to 0 as after dropping the null values the index values of the dataframe start from 6
facebook.reset_index(inplace = True) 

facebook.head()

#Dropping the index column 
facebook.drop(['index'], axis =1, inplace = True)

facebook.head()

facebook.isnull().any().any()

facebook.shape


# Using the headline as feature and Topic as label

corpus_headline = [ ]


#Data Preprocessing
for i in range(82929):
    headline = re.sub('[^a-zA-Z]+', ' ', facebook['Headline'][i])
    headline = re.sub('\s+', ' ', headline).lower()
    
    stemmer = PorterStemmer()
    headline = [stemmer.stem(w) for w in word_tokenize(headline) if w not in stopwords.words('english')]
    headline = ' '.join(headline)
    
    corpus_headline.append(headline)


len(corpus_headline)


# Applying label Encoding on topics column of data

lb = LabelEncoder()
y =lb.fit_transform(facebook['Topic'])

# Reduced the Features 30587 from to 5000 as memory is insufficient to handle shape of (82929,30587) sparse matrix
cv = CountVectorizer(max_df = 0.90, min_df = 2, max_features = 5000)

x = cv.fit_transform(corpus_headline).toarray()
x.shape


#Splitting Data in to train and test
x_train = x[:20000]
x_test = x[20000:40000]
y_train = y[:20000]
y_test = y[20000:40000]

x_train.shape, x_test.shape, y_train.shape, y_test.shape


# Applying different classifiers to predict the category of news article


# Using Gaussian Naive Bayes

nb = GaussianNB()
nb.fit(x_train, y_train)



y_pred_nb = nb.predict(x_test)


f1_score_nb = f1_score(y_test, y_pred_nb, average = 'weighted')
score_nb = accuracy_score(y_test, y_pred_nb)
matrix_nb = confusion_matrix(y_test, y_pred_nb)
print('F1 Score-:', f1_score_nb)
print('Accuracy Score-:', score_nb)
print('Confusion Matrix-:', matrix_nb)

y_pred_nb


# Using Logistic Regression


lr = LogisticRegression()
lr.fit(x_train, y_train)

y_pred_lr = lr.predict(x_test)

f1_score_lr = f1_score(y_test, y_pred_lr, average = 'weighted')
score_lr = accuracy_score(y_test, y_pred_lr)
matrix_lr = confusion_matrix(y_test, y_pred_lr)
print('F1 Score-:', f1_score_lr)
print('Accuracy Score-:', score_lr)
print('Confusion Matrix-:', matrix_lr)

y_pred_lr[0:50]


# The headlines are now classified in to topics('economics', 'microsoft', 'palestine', 'obama') in y_pred_nb.
# Using y_pred_nb as the input and TS144(Final level of popularity after 2 days upon publication) as the output
# With this and using Simple Linear Regression we can predict the popularity of the news headline


popularity = facebook['TS144'].iloc[20000:40000]
popularity.shape

features = {'News_Categories':y_pred_nb, 'Popularity':popularity}


df = pd.DataFrame(features)

df.head()

df.shape


# importing the library for linear regression

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = df.iloc[:, 0:1].values
Y = df.iloc[:,-1:].values
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
x_train.shape, x_test.shape, y_train.shape, y_test.shape


classifier = LinearRegression()
classifier.fit(x_train, y_train)

y_pred_linear = classifier.predict(x_test)

mse = mean_squared_error(y_test, y_pred_linear)
rmse = np.sqrt(mse)
print('MSE:-', mse)
print('RMSE:-', rmse)

# Using Logistic Regression predictions

features_lr = {'News_Categories':y_pred_lr, 'Popularity':popularity}
df_lr = pd.DataFrame(features_lr)

df_lr.head()
df_lr.shape

X_lr = df.iloc[:, 0:1].values
Y_lr = df.iloc[:,-1:].values

x_train, x_test, y_train, y_test = train_test_split(X_lr, Y_lr, test_size = 0.2, random_state = 0)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

classifier_lr = LinearRegression()
classifier_lr.fit(x_train, y_train)
y_pred_lr = classifier_lr.predict(x_test)

mse = mean_squared_error(y_test, y_pred_lr)
rmse = np.sqrt(mse)
print('MSE:-', mse)
print('RMSE:-', rmse)