# Normal Standard Variate --> here it is the special Normal distribution 
# where mean --> 0 and standard deviation is 1 

# importing the libary 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# importing the titanic datatset 
df = sns.load_dataset("titanic")
print("dataset loaded successfully!!!")

# printing the data set 
print(df.head())

# Printing the age column
print(df["age"])

# Plotting the kde plot 
sns.kdeplot(df['age'])
plt.show()

# find the mean and the standard variation 
mean = df["age"].mean()
print(mean)
std = df["age"].std()
print(std)

# formula to convert the standard normal variate 
s = (df['age'] - mean)/std
print(s)

# plotting the graph for the normal standard variate 
sns.kdeplot(s)
plt.show()