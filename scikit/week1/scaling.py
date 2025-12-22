#why do we scale
# What happens in real time if we don’t scale data

# Let’s say you’re building a model to predict house prices.
# You feed in features like:

# Feature	Typical Range
# Number of rooms	1 → 10
# House size (sqft)	500 → 5000
# Distance to city (km)	1 → 50
# Price	target (prediction)

# Now look — “house size” values (500–5000) are much larger
# than “number of rooms” (1–10).

# ⚠️ If you don’t scale:

# The model will think “house size” is 100× more important than rooms.

# It will completely ignore smaller-scale features (like distance, rooms).

# Your predictions become biased and unstable



#Standard scaler means it converts all the features to same unit by removing mean and scaling by standard deviation
# When you apply StandardScaler, it transforms every number using this formula:
# z=(z-mean)/standarddeviation
#  so it converts all by [-1.22, 0, 1.22]
# so after scaling we get mean =0 and standard devaition ~ =1
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# here we are scaling the data by  doing two things
# learn how to scale (from traing data only)
# i.e

# Step 1: fit_transform(X_train)
# The scaler first learns from training data:
# Mean = 170
# Standard deviation ≈ 14.14
# Then it transforms it using:
# z=(x-mean)/sd
# So training data becomes:[-1.41, -0.71, 0, 0.71, 1.41]
# ✅ That’s what .fit_transform() does → learn + scale


# Step 2: transform(X_test)
# Now, we use the same mean (170) and std (14.14)
# to scale the test data.
# That’s what .transform() does → scale using training’s values

# and most important thing we should not perform fit on testing data which may give results unaccurately
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#load data
iris_data=load_iris(as_frame=True) #this returns dictonary of values
df=iris_data.frame

#split features and target
X=df[iris_data.feature_names]
Y=iris_data.target

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=14)

#scaling
scaler=StandardScaler() #it just first caluclates the means and sd after it transforms the data points
x_trainScaled=scaler.fit_transform(x_train)
x_testScaled=scaler.transform(x_test)
print("Before scaling \n",x_train)
print("after scalings hi  hi i am going to learn \n",x_testScaled)