#%% Select rows 

import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\nUse == operator\n")
print(employees.loc[employees['Age'] == 23])

print("\nUse < operator\n")
print(employees.loc[employees['Age'] > 30])

print("\nUse != operator\n")
print(employees.loc[employees['Occupation'] != 'Statistician'])

print("\nMultiple Conditions\n")
mycon = 'Occupation != "Statistician" & Name == "John"'
employees.query(mycon)

#%% .isin

print("\nUse query operator\n")
mycon = 'Occupation in ["Chemist", "Programmer"]'
print(employees.query(mycon))
print("\nAlternatively, use isin operator\n")
print(employees.loc[employees['Occupation'].isin(['Chemist'])])

#%%
print("\n Example itterrows \n")
for index, col in employees.iterrows():
    print(col['Name'], "--", col['Age'])


#%%
