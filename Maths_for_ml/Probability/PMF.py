# here we learn the how to do pmf in the python and the numpy 


# importing the library 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# also importing the random 
import random

# creating the empty list 
L  = []

# Apply the loop 
for i in range(10000):
    L.append(random.randint(1,6))
    
# length of the List 
print(len(L))

# Print the element of the list 
print(L[:6])

# find the values count 
pmf = (pd.Series(L).value_counts()/pd.Series(L).value_counts().sum()).sort_index()
print(pmf)

# Plotting the graph 
plt.bar(pmf.index,pmf.values)

plt.xlabel("Dice Values ")
plt.ylabel("probability")
plt.title("PMF of the Dice ")

plt.show()