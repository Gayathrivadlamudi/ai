#regression is used to predict continous numeric value
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
#this r2_score tells how well the regression line fits the data
#     Higher R² means better model performance.
# | R² Score     | Meaning                                              |
# | ------------ | ---------------------------------------------------- |
# | **1.0**      | Perfect model — predicts everything accurately       |
# | **0 to 1**   | Good model — the closer to 1, the better             |
# | **0**        | Model is no better than guessing the average         |
# | **Negative** | Very bad model — worse than predicting just the mean |

#load dataset
diabeticData=load_diabetes()
X=diabeticData.data
Y=diabeticData.target 

#split data
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=14)
 
#creating model
model=LinearRegression()
 
#traing model
model.fit(x_train,y_train)

#predicing

y_pred=model.predict(x_test)

#printing r2

print("r2_score",   r2_score(y_test,y_pred))