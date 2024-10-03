import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle


df = pd.read_csv('../datasets/StudentsPerformance[1].csv')
df = df.drop('race/ethnicity', axis=1)
df = df.drop('lunch', axis=1)
df = df.drop('parental level of education', axis=1)
df['gender'].replace('male', 1, inplace=True)
df['gender'].replace('female', 0, inplace=True)
df['test preparation course'].replace('completed', 1, inplace=True)
df['test preparation course'].replace('none', 0, inplace=True)
print(df.columns.tolist())

X = df.drop('gender', axis=1)
y = df['gender']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LogisticRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
filename = '../../models/model.pkl'
pickle.dump(regressor, open(filename, 'wb'))
