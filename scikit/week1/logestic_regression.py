from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
data = load_iris()
X = data.data
y = data.target     # 0,1,2 classes

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features (important for logistic regression)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create model
model = LogisticRegression(max_iter=200)
#max_iter is for the algorithm to find the best weights
# A logistic regression model predicts using:
# z = w1*x1 + w2*x2 + w3*x3 + ... + b
# Where:
# w1, w2, w3 ... = weights
# x1, x2, x3 ... = values of features
# b = bias (intercept)
# Train
model.fit(X_train, y_train)

# Accuracy
print("Accuracy:", model.score(X_test, y_test)) #model.score() gives us the performance of the model
