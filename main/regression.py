# Linear Regression Algorithm and data treatment is done here

import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn import linear_model
from sklearn.utils import shuffle


data = pd.read_csv("../student/student-mat.csv", sep=";") #The csv file is separated by ;

# print(data.head()) # -- Print the 5 first DATA elements



# Trimming the data by especific attributes
data = data[["G1", "G2", "G3", "studytime", "absences", "failures"]]

# G3 is the students final GRADE, the thing we want to predict
predict = "G3" # Known as label, you can predict one, or more


attribute_data = np.array(data.drop(columns=[predict])) # We gonna put the data, without the G3, in an array, contains our attributes
label_data = np.array(data[predict]) # This array will contain the data the we actually want to predict, known as labels


# tr_att_data and tr_label_data, sections of the respective datas
# att_test, label_test, data for the model to test the accuracy on, which corresponds to 10% of the original data (0.1)
# The reason for this split is to separate the correct prediction of it's corralated data, to avoid the model to just memorize what answer to give based on input values
# that only exists in our dataset

# This section of the code that trains the model ###
# 50 times and saves the best one

# Best accuracy starts at 0
best = 0

# Model for saving
linear_to_save = linear_model.LinearRegression()

for i in range(50):
    tr_att_data, att_test, tr_label_data, label_test =  sklearn.model_selection.train_test_split(attribute_data, label_data, test_size = 0.1)
    # Start a linear regression model
    linear = linear_model.LinearRegression()
    # It's gonna find which is the best fit line for this data aggregate
    linear.fit(tr_att_data, tr_label_data)
    # We gonna know if the best fit line actually compares well with the test arrays, that the training model had no access to
    acc = linear.score(att_test, label_test)
    
    # print("Accuracy", acc, "\n")
    
    if acc > best:
        best = acc
        linear_to_save = linear
        
        print("New best accuracy found:", best, "\n")

###


# Saving a model ###

with open("studentmodel.pickle", "wb") as f:
    pickle.dump(linear_to_save, f)

'''
# Loading the model ###
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)
'''

'''
# To make a prediction ###

# On this point our code already has the the linear model done and trained, so we can make predictions:
# we can print all the predictions of the model with a data array that contains. of course, the data the model is expecting to work on

predictions = linear.predict(att_test) # So we store all of the predictions results here

# Printing the results of the predictions and the correspondent input data (att_test) along with the following results (label_test).
for i in range(len(predictions)):
    print(predictions[i], att_test[i], label_test[i])
'''
