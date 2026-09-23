
# Import numpy and pandas 
import numpy as np 
import pandas as pd 


# TOPIC WE HAVE TO LEARN IN MISSING DATA 
"""
1 --> FINDING THE MISSING DATA 
2 --> REMOVING THE MISSING DATA 
3 --> FILLING THE MISSING DATA 
"""

data = {
    'A' : [1,2,np.nan,4,5],
    'B' : [1,2,3,4,5],
    'C' : [1,2,3,np.nan,np.nan],
    'D' : [1,np.nan,np.nan,np.nan,5]
}

df = pd.DataFrame(data)
print(df)

# STEP --> FINDING THE NAN VALUES 
print(df.isna())
print(df.isna().sum())   # used to findout which row have more NAN values 
print(df.isna().any())    # USED TO FIND ALL COLUMNS HAVE NAN VALUES OR NOT 

# REMOVING THE NAN VALUES --> work on basis on rows 
print(df)
print(df.dropna())   

#  jo row me null value nhi hogi usko print mar dega 

print(df.dropna(thresh=1))    # Means row me 1 rnda chaiye 

# for the filling 
print(df.fillna(0))

# Agr alg alg columns me alg alg values dalna hai toh 
values = {
    'A':0,
    'B':100,
    'C':400,
    'D':800
}
print(df.fillna(value=values,inplace=True))
print(df)