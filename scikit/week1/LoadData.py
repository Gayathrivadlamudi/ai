from sklearn import datasets
import pandas as pd
iris_data=datasets.load_iris()
print(iris_data.data)
print("feature names",iris_data.feature_names)
print("feature target",iris_data.target_names)
df=pd.DataFrame(iris_data.data,columns=iris_data.feature_names)

#the conversion from text (categories) → numbers is already done automatically by Scikit-learn when you load the dataset.
print(iris_data.target,'\n')
print(iris_data.target_names,'\n')
#It gives you:

# iris_data.target → [0, 0, 1, 1, 2, ...]

# iris_data.target_names → ['setosa', 'versicolor', 'virginica']
#adding a column
df['target']=iris_data.target
df['species']=df['target'].apply(lambda x: iris_data.target_names[x])
print(df.head())


#the above thing we did is manual this only we can do with simple steps
load_data_digits=datasets.load_digits
digitsData=load_data_digits(as_frame=True)
df=digitsData.frame
print(df.head())

#explanation
#when we have load_digits that means we get dicitionary like object in that we have lot of info
#digits=load_digits()
#print(digits.key())
#output: dict_keys(['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])
# data → the input features (like pixel values)
# target → the labels (numbers 0–9)
# images → the 8×8 images
# feature_names → names of the features (like pixel_1_1, pixel_1_2…)
# DESCR → description text


#digits.data is numpy array so to represent them in table we use as_frame=True
# Converts digits.data into a DataFrame (table)
# ✅ Converts digits.target into a column in that table
# ✅ Adds column names automatically

#after loading the scikit-learn stores the table in digit.frame so we store that in df