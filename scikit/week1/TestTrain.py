#in scikit there is package called model_selection in that there is a function called train_test_split

#what is splitting
#when we have dataset we dont train full data on the model
#we take 80% of data for training and 20% for testing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

data=load_iris(as_frame=True) #here it loads a bunch of data like  ['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])
df=data.frame

#we store inputs and labels in X and Y
X=df[data.feature_names] #so here we call data.feature_names
Y=data.target
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=14)
print(x_train.shape,x_test.shape)
 #X and Y are inputs
 #test_size=0.2 means its saying 20 % of data is for testing
 #random_state=14 means every time we run the same data should be divided into train data and test data