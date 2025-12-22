# both logistic and decision tree are same they are used for predicint categories

# Use Logistic Regression when:

# ✔ Data is simple
# ✔ Features are clearly separated
# ✔ You want a stable, low-overfitting model

# Use Decision Tree when:

# ✔ You want easy-to-read rules
# ✔ Data has complex patterns
# ✔ You don’t want to scale features

# Final Simple Summary
# Both predict categories, but they think differently.
# Logistic Regression draws a line.
# Decision Tree makes rules.

# what is decision tree
# a decision tree is a machine learning model that works like a flowchart
# example
# is it raining?
#             YES?then dont play
#             NO?then is it windy?
#                                 YES?maybe dont play
#                                 NO?then play

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split    
from sklearn.tree import DecisionTreeClassifier

#load iris data
irisData=load_iris()
X=irisData.data
Y=irisData.target

#splitting
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=14)

#create model
model=DecisionTreeClassifier(max_depth=3)
#why we use max_depth
#some times model learn too much that they work fine on testing data but they dont work on testing data
#this is called overfitting to avoid this we set limit by using max_depth so the tree can't go too much learning
model.fit(x_train,y_train)
accuracy=model.score(x_test,y_test)
print(accuracy)