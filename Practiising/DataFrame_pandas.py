
import numpy as np 
import pandas as pd
# DATAFRAME --> WHICH CONSIST MANY SERIES 

# CREATION OF DATAFRAME 
# 1 --> by using dictionary 
# 2 -->  by using nested list 


# USING BY USING DICTIONARY 
employees = {
"EMPID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
"Name": ["Amit", "Neha", "Rahul", "Priya", "Vikas", "Sneha", "Arjun", "Pooja", "Rohit",
"Kiran"],
"DOB": ["1995-02-10", "1996-07-15", "1994-03-22", "1997-11-05", "1993-08-18",
"1998-01-30", "1992-12-12", "1996-05-25", "1994-09-09", "1997-04-14"],
"Address": ["Delhi", "Mumbai", "Patna", "Kolkata", "Lucknow",
"Chennai", "Bangalore", "Hyderabad", "Pune", "Jaipur"],
"Dept": ["IT", "HR", "Finance", "IT", "Marketing",
"HR", "Finance", "IT", "Sales", "Marketing"],
"Post": ["Developer", "Manager", "Accountant", "Tester", "Executive",
"HR Executive", "Analyst", "Developer", "Sales Officer", "Manager"],
"Sal": [50000, 60000, 55000, 48000, 52000,
58000, 62000, 51000, 47000, 59000]
}

df = pd.DataFrame(employees)
# print(df)

# Creation of dataframe by using nested list 
# my_List = [
#         [101, "Amit", "1995-02-10", "Delhi", "IT", "Developer", 50000],
#         [102, "Neha", "1996-07-15", "Mumbai", "HR", "Manager", 60000],
#         [103, "Rahul", "1994-03-22", "Patna", "Finance", "Accountant", 55000],
#         [104, "Priya", "1997-11-05", "Kolkata", "IT", "Tester", 48000],
#         [105, "Vikas", "1993-08-18", "Lucknow", "Marketing", "Executive", 52000]
# ]

# df1 = pd.DataFrame(my_List)
# print(df1)

# # Adding column in the above table 
# column = ['EMPID','Name','D.O.B.','Addresh','Dept','Post','Sal']
# df2 = pd.DataFrame(my_List,columns=column)
# print(df2)

# Working on the dictionary data 
# print(df)

# Access the columns 
# Acces the single column 
# print(df['Name'])
# print(df['Sal'])

# # Acces the multipl columns 
# print(df[['Name','Dept','Sal']])
# print(df[['EMPID','Name','DOB']])

# # ACCES THE MULTIPLE ROWS BY USING index 
# # ROW INDEXING 
# print(df.iloc[0])
# print(df.iloc[5])

# # ROW SLICING 
# print(df.iloc[0 : 5])
# print(df.iloc[:4])

# print(df.iloc[[0,4,7]])

# # Slicing in row amd columns 
# print(df.loc[1:4:2,['Name','Post','Sal']])

# emp_data = {
# "Empid": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
# "Name": ["Amit", "Ravi", "Sita", "Neha", "Rahul", "Priya", "Ankit", "Pooja", "Vikas", "Kiran"],
# "City": ["Patna", "Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore", "Hyderabad",
# "Pune",
# "Jaipur", "Lucknow"],
# "Dept": ["HR", "IT", "Finance", "IT", "Sales", "HR", "IT", "Finance", "Sales", "HR"],
# "Post": ["Manager", "Developer", "Analyst", "Developer", "Executive", "Manager", "Tester",
# "Analyst", "Executive", "Manager"],
# "Sal": [50000, 60000, 55000, 62000, 45000, 52000, 48000, 53000, 47000, 51000]
# }

# df3 = pd.DataFrame(emp_data)
# print(df3)

# # Question no 1 
# print(df3[df3['Sal'] > 50000])

# # Question 2 
# print(df3[df['Dept'] == 'IT'])

# # Question 3 
# print(df3[df3['City'] == 'Patna'])

# # Question 4 
# print(df3[df3['Sal'] < 48000])

# # Question 5 
# print(df3[df3['Name'] == 'Ravi'])

# #Question 6
# print(df3[(df3['Sal'] > 45000) & (df3['Sal'] < 55000)])

# # Question 7 
# print(df3[(df3['Dept'] == 'HR') & (df3['Sal'] > 50000)])

# # Question 8 
# print(df3[(df3['City'] == 'Delhi') | (df3['City'] == 'Mumbai')])

# # Question 10 
# print(df3[df3['Sal'].isin([45000,47000,60000])])


# QUERY BASED CONDITION 
data = {
"Name": ["Ravi", "Amit", "Sita", "Rahul", "Ankit", "Riya", "Sumit", "Neha", "Karan", "Pooja"],
"Age": [25, 30, 28, 35, 27, 24, 32, 29, 31, 26],
"City": ["Patna", "Delhi", "Patna", "Mumbai", "Delhi", "Patna", "Kolkata", "Mumbai", "Delhi",

"Patna"],
"Department": ["IT", "HR", "Finance", "IT", "HR", "IT", "Finance", "HR", "IT", "Finance"],
"Salary": [50000, 60000, 45000, 70000, 40000, 55000, 48000, 52000, 65000, 43000],
"Email": [
"ravi@gmail.com", "amit@yahoo.com", "sita@gmail.com",
"rahul@outlook.com", "ankit@gmail.com", "riya@yahoo.com",
"sumit@gmail.com", "neha@gmail.com", "karan@yahoo.com", "pooja@gmail.com"
]
}

df2 = pd.DataFrame(data)
print(df2)

# Question 1 
print(df2.query("Salary > 50000"))

# Question 2 
print(df2.query("City == 'Patna'"))