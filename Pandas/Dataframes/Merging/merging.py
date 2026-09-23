
#   merging the data frame 

# Importing numpy and pandas 
import numpy as np 
import pandas as pd 

# Creating two dataframes 
employess ={
    'employee_id' : [1,2,3,4,5],
    'name' : ['John','Anna','Peter','Linda','Bob'],
    'department' : ['HR','IT','Finance','IT','HR']
}

df = pd.DataFrame(employess)
print(df)

salaries = {
    'employee_id':[1,2,3,6,7],
    'Salary' : [60000,80000,65000,70000,90000],
    'bonus' : [5000,10000,7000,8000,12000]
} 
df2 = pd.DataFrame(salaries)
print(df2)

print(pd.merge(df,df2,on='employee_id',how='inner'))

# use of the outer 
print(pd.merge(df,df2,on='employee_id',how='outer'))

