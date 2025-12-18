# goal
# train two models
# !)logestic regresion)
# 2)DescisionTreeClassifier

# compare them using
# accuracy
# precision,recall ,f1score
# confusion matrices


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)
import matplotlib.pyplot as plt

# ------------------------------
# 1. Load dataset
# ------------------------------
iris = load_iris()
X = iris.data
y = iris.target


# ------------------------------
# 2. Train-Test Split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------
# 3. Scaling (important for LogisticRegression)
# ------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


#training models
#logestic regression
logesticModel=LogisticRegression(max_iter=300)
logesticModel.fit(X_train_scaled,y_train)

#decsion 
descisionModel=DecisionTreeClassifier(max_depth=3,random_state=14)
descisionModel.fit(X_train_scaled,y_train)


#predictions
logesticPrediction=logesticModel.predict(X_test_scaled)
decisionPredction=descisionModel.predict(X_test_scaled)

#printing reports
print("logestic clasifciatin report.",)
print(classification_report(y_test,logesticPrediction,target_names=iris.target_names))

print("decsinprediction, is good ")
print(classification_report(y_test,decisionPredction,target_names=iris.target_names))

#confusion matrix plots

fig,axes=plt.subplots(1,2,figsize=(10,4))
ConfusionMatrixDisplay(confusion_matrix(y_test,logesticPrediction)).plot(ax=axes[0])
print(axes[0])
axes[0].set_title("logestic")
ConfusionMatrixDisplay(confusion_matrix(y_test,decisionPredction)).plot(ax=axes[1])
axes[1].set_title('decision')
# ax=axes[0]
# → Tells matplotlib:
# “Draw this inside first box (left plot)”
plt.show()



