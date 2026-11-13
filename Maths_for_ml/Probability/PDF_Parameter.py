
# here we have to calculate the pdf --> probability density function for the data 

# importing the library 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.stats import norm 

# Generating an sample '
sample = np.random.normal(loc=50,scale=5,size=1000)

# Plotting an histogram 
# plt.hist(sample,bins=10)
# plt.show()

# find the mean and the standard deviation 
mean =  np.mean(sample)
std =  np.std(sample,ddof=1)

# find the density of the valeus 
x = np.linspace(20,100,200)
y = norm.pdf(x,mean,std)

# Drwating the histrogram 
plt.hist(sample,bins=5,density=True)

# plotting the graph 
plt.plot(x,y)

plt.xlabel("x axis ")
plt.ylabel("density values ")
plt.title("probability density function")
plt.show()