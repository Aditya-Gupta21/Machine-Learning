
# here we learn how to use the PDF in data science 

# Import the libray 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Load the data set of the seaborn 
df = sns.load_dataset('iris')

# View data set 
print(df.head())

# plotting the kde and plot  for  petal length 
sns.kdeplot(data=df,x= 'petal_length',hue='species')
sns.ecdfplot(data = df,x ='petal_length',hue='species')

plt.show()

# Plotting the kde and cdf plot for petal width 
sns.kdeplot(data = df,x = 'petal_width',hue='species')
sns.ecdfplot(data = df,x='petal_width',hue='species')
plt.show()

# plotting kde and cdf plot for the sepal length 
sns.kdeplot(data=df,x = 'sepal_length',hue='species')
sns.ecdfplot(data=df,x= 'sepal_length',hue='species')

plt.show()

# Plotting kde and cdf plot for the sepal width 
sns.kdeplot(data=df,x= 'sepal_width',hue='species')
sns.ecdfplot(data=df,x= 'sepal_width',hue='species')

plt.show()