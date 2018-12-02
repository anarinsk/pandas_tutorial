#%% 
import pandas as pd
ser1 = pd.Series([1.5, 2.5, 3, 4.5, 5.0, 6])
print(ser1)

#%%
ser2 = pd.Series(['India', 'US', 'Korea'], name='Countries')
print(ser2)


#%%
ser4 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})
print(ser4)

#%%
import pandas as pd
import numpy as np

ser1 = pd.Series(np.linspace(1, 10, 5))
print(ser1)
ser2 = pd.Series(np.random.normal(size=5))
print(ser2)

#%%
import pandas as pd
import numpy as np
 
ser1 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})
 
print(ser1.values)
print(ser1.index)

#%%
import pandas as pd

values = ['India', 'Canada', 'Australia', 'Japan', 'Germany', 'France']
code = ['IND', 'CAN', 'AUS', 'JAP', 'GER', 'FRA']

ser1 = pd.Series(values, index=code)
print(ser1)

#%%
print(len(ser1))
print(ser1.shape)
print(ser1.size)

#%%
import pandas as pd
 
num = [000, 100, 200, 300, 400, 500, 600, 700, 800, 900]
idx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

series = pd.Series(num, index=idx)
series[2:6] 
print(series[1:6:2])
print(series[:6])
print(series[4:])
#%%
import pandas as pd
 
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

employees.loc[employees['Occupation'].isin(['Chemist','Programmer'])]

#%% column to list 
print(list(employees))
print(employees.columns.values)
print(employees['Age'].tolist())

#%% Bunch of 

employees[['EmpCode', 'Name', 'Age']]
import pandas as pd

#%% dict into Df 
 
data = ({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   })

print(data)
type(data)

df = pd.DataFrame(data)
df


#%% index and column 

values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]

df = pd.DataFrame(values, index=code, columns=['Countries'])

df
#%%
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
print(df)
print("\n -- Selecting a single row with .iloc with an integer -- \n")
print(df.iloc[4])
print("\n -- Selecting multiple rows with .iloc with a list of integers -- \n")
print(df.iloc[[2, -2]])
print("\n -- Selecting multiple rows with .iloc with slice notation -- \n")
print(df.iloc[:5:3])

#%% loc vs iloc 
print("\n -- loc -- \n")
print(df.loc[df['Age'] < 30, ['Color', 'Height']])
print(df.iloc[(df['Age'] < 30).values, [1,3]])
(df['Age'] < 30).values
#%% change order of columns 
print("\n -- Change order using columns -- \n")
new_order = [3, 2, 1, 4, 5, 0]
print(df)
df[df.columns[new_order]]
print("\n -- Change order using reindex -- \n")
df.reindex(['State', 'Color', 'Age', 'Food', 'Score', 'Height'], axis=1)
#%%
import pandas as pd
 
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df.dtypes)

#%% 

#%%