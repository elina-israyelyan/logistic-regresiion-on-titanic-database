#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# uncomment the next line if you need the heatmap
# import seaborn as sns

df = pd.read_csv("titanic.csv")  # reading the database
# in the next two lines we convert the string values two numbers
df.Sex[df.Sex == "male"] = 1
df.Sex[df.Sex == "female"] = 0

# uncomment the next two lines if you need the heatmap of corellation between the variables corr = df.corr()
# sns.heatmap(corr) # there is no corellation between independent variables

x = df[["Age", "Sex", "Pclass"]]  # these are the variables that will predict the outcome
y = df["Survived"]  # this is the outcome

# we split the data to train and test datas 30 percent is the test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
model = LogisticRegression().fit(x_train, y_train)  # we do a logistic regression on x and y
y_pred = model.predict(x_test)
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)  # this outputs the confussion matrix


# uncomment the next three lines to see the accuracy, precision and the recall score of the model
# print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
# print("Precision:", metrics.precision_score(y_test, y_pred))
# print("Recall:", metrics.recall_score(y_test, y_pred))

class Surviving:
    """this class gets 3 variables as inputs and has a function which evaluates if the person
    that has the inputed characteristics will survive."""
    data = df
    model_s = model

    def __init__(self, age, sex, p_class):
        self.age = age
        self.p_class = p_class
        self.sex = 0
        if sex == "male":
            self.sex = 1

    def will_survive(self):
        survive = model.predict(np.array([[self.age, self.sex, self.p_class]]).astype(np.float64))
        return survive
