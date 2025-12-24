# random forest classifier
# it is many decision trees combination
# and each decision tree makes an predcition and the random forest considers all the predictions and choose the majority decision 
# #which helps the predction to be accurate
# we use random forest mainly when we want to classify something
# | Question                           | Type        |
# | ---------------------------------- | ----------- |
# | Will customer buy or not buy?      | Yes/No      |
# | Is the email spam or not?          | Yes/No      |
# | Is this image a cat, dog, or bird? | Multi-class |
# | Will student pass or fail?         | Yes/No      |

#lets see an example
#predict if a person if he or she have diabetes

#import dataset
from sklearn.datasets import load_diabetes
#need to split the data for traing and testing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
#this ensemble is sub module for skcikit where it contains ensemble learning algorithms
#randomforestclassifer is one of those algo
#in this ensembel module it contains algorithms which contain multiple models to make a stronger model
#so example multiple decision trees are combined to make one stronger model that is random decsion model
# | Algorithm                    | Meaning                                           |
# | ---------------------------- | ------------------------------------------------- |
# | `RandomForestClassifier`     | Many decision trees work together → majority vote |
# | `RandomForestRegressor`      | Same as above but for regression                  |
# | `AdaBoostClassifier`         | Weak learners combined with boosting              |
# | `GradientBoostingClassifier` | Trees added one by one to reduce error            |
# | `BaggingClassifier`          | Same model trained on random sample subsets       |
# | `VotingClassifier`           | Combine predictions of different models           |
 
from sklearn.metrics import accuracy_score
#to get the performance of the model
diabetes=load_diabetes()
x=diabetes.data #this are Features
#diabetes.target this is target values
y=(diabetes.target>140).astype(int) #here we are checking if the diabetes is higher than 140 them we convert to 1 or else we keep it as 0 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=14)
model=RandomForestClassifier(n_estimators=100) #here n_estimatores means the random forest will create 100 descision trees and all these treees wil be trained on different sample data
#train the model
model.fit(x_train,y_train) #we are training the model will traing data
#prediction
pred=model.predict(x_test)
#accuracy score
print("accuracy",accuracy_score(y_test,pred))