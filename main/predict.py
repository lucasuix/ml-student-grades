# Here we make a simple prediction of a random set of data to compare the results, using the Linear Model Pickle file saved

import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("../student/student-mat.csv", sep=";") #The csv file is separated by ;
data = data[["G1", "G2", "G3", "studytime", "absences", "failures"]]
predict = "G3"
attribute_data = np.array(data.drop(columns=[predict])) # We gonna put the data, without the G3, in an array, contains our attributes
label_data = np.array(data[predict]) # This array will contain the data the we actually want to predict, known as labels

tr_att_data, att_test, tr_label_data, label_test =  sklearn.model_selection.train_test_split(attribute_data, label_data, test_size = 0.1)

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# To make a prediction ###

# On this point our code already has the the linear model done and trained, so we can make predictions:
# we can print all the predictions of the model with a data array that contains. of course, the data the model is expecting to work on

predictions = linear.predict(att_test) # So we store all of the predictions results here

# Printing the results of the predictions and the correspondent input data (att_test) along with the following results (label_test).
for i in range(len(predictions)):
    print("Prediction: ", predictions[i], "; Datainfo:", att_test[i], "; Actual Student Grade:", label_test[i])
