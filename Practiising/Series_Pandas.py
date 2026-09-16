# Importing Numpy and pandas 
import numpy as np 
import pandas as pd 

# Making the series ---> FROM THE LIST 
data = [10,20,30,40,50,60,70]
s1 = pd.Series(data)
# print(s1)

# Accesing the element from the list by the indexing 
# print(s1.iloc[0])   # Acces the 0 index element 
# print(s1.iloc[4])    # Acess the 4 index element 
# print(s1.iloc[[0,3]])    # Acees the 0 and 3 index element

# Adding the labels to the data 
label = ['a','b','c','d','e','f','g']
s2 = pd.Series(data,index = label)

# Accesing the element from the list by using the labels 
# print(s2.loc['a'])      # Acces the elemnt by using the lables 
# print(s2.loc['e'])       # Acces the element by using the lables 
# print(s2.loc[['a','d']])


# Making the Series  --> FROM THE Dictionary 
my_data = {
    1 : 'Aditya',
    2 : 'Chandan',
    3 : 'Harsh',
    4 : 'Saurabh',
    5 : 'Omakr',
    6 : 'Chandru',
    7 : 'Aryan'
}
s3 = pd.Series(my_data)
# print(s3)


# BASIC mathematical operations 
d1 = [10,20,30,40,None]
l1 = ['a','b','c','d','e']
s4 = pd.Series(d1,index = l1)
print(s4)

# # SOME IMPORTANT FUNCTION 
# print(s4.head(3))   # Starting ke 3 values chaiye 
# print(s4.tail(2))   # ENDING Ke 2 values chaiye
# print(s4.shape)   # Give shape in the tuples 
# print(s4.size)     # Give the size means 5 rows 
# print(s4.ndim)    # Give the dimensions 
# print(s4.index)      # Give the index or if labels are given so its give the labels 
# print(s4.values)     # Gives the values of the list 


# # some mathematical function 
# print(s4.sum())
# print(s4.mean())
# print(s4.median())
# print(s4.mode())
# print(s4.max())
# print(s4.min())
# print(s4.prod())
# print(s4.count())


# # CREATING THE NEW DATA 
# d2 = [50,20,20,30,40,None]
# l3 = ['a','b','c','d','e','f']
# s6 = pd.Series(d2,index = l3)
# print(s6)

# # First function 
# print(s6.describe())

# # Second function 
# print(s6.unique())

# # Second function 
# print(s6.nunique())

# # Values count 
# print(s6.value_counts())

# # Sort index 
# print(s6.sort_index())

# # Sort values 
# print(s6.sort_values())

# # Use of the aggre fucntion 
# print(s6.agg(['sum','mean','max']))


#  BOOLEAN INDEXING 

d5 = [10, 25, 30, 45, 60, 75, 90, -5, 100]
s5 = pd.Series(d5)
print(s5)

# Question numnber 1 
print(s5[s5 > 50])

# Question number 2 
print(s5[(s5 > 20) & (s5 < 80) ])

# Question 3 
print(s5[s5 % 2 != 0])

# Question 4 
print(s5[s5 <0])

# Question 6 
print(s5[s5.isin([10,30,100])])

# Question 7 
print(s5[~(s5 == 100)])

# Question 8 
print(s5[(s5 < 20) & (s5 > 80)])

# Question 9 
print(s5[s5 % 5 == 0])