# when our model predicts we need to check how accurate are those
# we can check by using metrics
# like
# accuracy
# precision
# recall
# f1 score


# Accuracy:
# how many predictions are correct out of all predictions

# Example:
# If the model predicted 90 correct out of 100 → 90% accuracy

# precision:
# out of all positive predicts how many are actually positive
# like
# suppose Example
#     model said 10 people got gold
# but only 5 got gold so precision is 7/10 i.e70%


# Recall:
# out of all actual positvies(not predicted ones) how many did the model predicted
# model said 10 people have gold
# but actually there are only 7

# f1-score: is both combinatin of precision and Recall
# that is it balances both precision and Recall it tell both value in single digit
# If you want one score that tells:
# how accurate positive predictions are (precision)
# how many positives detected (recall)
# Then use F1-score.

# confusion matrix :this matrix shows how many correct and wrong predctions for each class

# | **Actual / Predicted** | **setosa (0)** | **versicolor (1)** | **virginica (2)** |
# | ---------------------- | -------------- | ------------------ | ----------------- |
# | **setosa (0)**         | 10             | 0                  | 0                 |
# | **versicolor (1)**     | 0              | 8                  | 1                 |
# | **virginica (2)**      | 0              | 1                  | 9                 |

# Example readings:

# 10 setosa were correctly predicted as setosa
# 8 versicolor were correctly predicted
# 1 versicolor was wrongly predicted as virginica
# 1 virginica was wrongly predicted as versicolor
# 9 virginica were correct


# classification report gives
# precision
# Recall
# f1 score
# support


from  sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(confusion_matrix,ConfusionMatrixDisplay,classification_report)
import matplotlib.pyplot as plt

#load the data
data=load_iris()
X=data.data
Y=data.target
#splitting
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=14)

#scalling
scaler=StandardScaler()
x_trainScaled=scaler.fit_transform(x_train)
x_testScaled=scaler.transform(x_test)

#training the model
model=DecisionTreeClassifier(max_depth=3)
model.fit(x_trainScaled,y_train)

#predictions
y_pred=model.predict(x_testScaled)

#confusion matrix
cfm=confusion_matrix(y_test,y_pred)
print(cfm)

#plot confusion matrix
disp=ConfusionMatrixDisplay(cfm)
disp.plot()
plt.show()

#classification report
print('cr',classification_report(y_test,y_pred,target_names=load_iris().target_names ))
