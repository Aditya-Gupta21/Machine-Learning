
# creating the pmf of the rolling of the two dice 
# and calculate their sums 

# importing the library 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import random

# creating the empty list 
L = []

# Perform a loop 
for i  in range(10000):
    
    # Rolling the 2 dice name as a and b 
    a = random.randint(1,6)
    b = random.randint(1,6)
    
    L.append(a + b)
    
    
print(L[:6])

# Making the overall valeus of the list in the series framework 
pmf = (pd.Series(L).value_counts()/pd.Series(L).value_counts().sum()).sort_index()
print(pmf)

# Plotting the graph 
plt.bar(pmf.index,pmf.values)

plt.xlabel("Sum of numbers of dice")
plt.ylabel("Probability")
plt.show()