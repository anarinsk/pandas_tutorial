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

#%% astype
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
df['Age'] = df['Age'].astype('str')
print(df.dtypes)

#%% to int 

import pandas as pd
 
df = pd.DataFrame({'DailyExp': [75.7, 56.69, 55.69, 96.5, 84.9, 110.5,
                                58.9],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df.dtypes)
df['DailyExp'] = df['DailyExp'].astype('int')
print(df.dtypes)

#%% datetime64
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],                   
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df.dtypes)
df['DateOfBirth'] = df['DateOfBirth'].astype('datetime64')
print(df.dtypes)

#%% append df 

df1 = pd.DataFrame({'Age': [30, 20, 22, 40], 'Height': [165, 70, 120, 80],
                    'Score': [4.6, 8.3, 9.0, 3.3], 'State': ['NY', 'TX',
                                                             'FL', 'AL']},
                   index=['Jane', 'Nick', 'Aaron', 'Penelope'])
 
df2 = pd.DataFrame({'Age': [32, 28, 39], 'Color': ['Gray', 'Black', 'Red'],
                    'Food': ['Cheese', 'Melon', 'Beans'],
                    'Score': [1.8, 9.5, 2.2], 'State': ['AK', 'TX', 'TX']},
                   index=['Dean', 'Christina', 'Cornelia'])
 

df3 = df1.append(df2, sort=True)
df3


#%%

cols = ['Zip']
lst = []
zip = 1000 

for a in range(10): 
    lst.append(zip)
    zip += 1

lst
#%%
import pandas as pd
 
df = pd.DataFrame(columns=['Name', 'Age'])
 
df.loc[1, 'Name'] = 'Rocky'
df.loc[1, 'Age'] = 21
 
df.loc[2, 'Name'] = 'Sunny'
df.loc[2, 'Age'] = 22
 
df.loc[3, 'Name'] = 'Mark'
df.loc[3, 'Age'] = 25
 
df.loc[4, 'Name'] = 'Taylor'
df.loc[4, 'Age'] = 28

line = pd.DataFrame({'Name':'FUCK', 'Age':1000}, index=[2.5])
df = df.append(line)
df.sort_index().reset_index(drop=True)
#%%
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
df['mean basket'] = df.mean(axis=1)
df.loc['mean fruits'] = df.mean(axis=0)
df
#%% Use of any()

import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
 
if df['State'].str.contains('TX').any():
    print("TX is there")


#%% remove duplicated 

import pandas as pd
import numpy as np
 
df = pd.DataFrame({'Age': [30, 30, 22, 40, 20, 30, 20, 25],
                   'Height': [165, 165, 120, 80, 162, 72, 124, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])
 
print("\n -------- Duplicate Rows ----------- \n")
print(df)
df.reset_index().drop_duplicates(subset=['index'], keep='first')
df.loc[df['Age']>20, 'Height'].values
#%%
import pandas as pd
 
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
df.sort_index(ascending=True) 

#%%

import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
 
print("\n--------- DataFrame Values--------\n")
print(df)
 
print("\n--------- DataFrame Values by Rank--------\n")
print(df.rank(ascending=False))

#%%
import pandas as pd
 
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
 
pidx = pd.period_range('6/1/2006', '11/1/2006', freq='M')
 
df = pd.DataFrame(values, index=pidx, columns=['Country'])
 
print(df)

#%%
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n----------- Calculate Mean -----------\n")
print(df.mean())
 
print("\n----------- Calculate Median -----------\n")
print(df.median())
 
print("\n----------- Calculate Mode -----------\n")
print(df.mode())

#%%
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n----------- Calculate Mean -----------\n")
print(df.mean())
 
print("\n----------- Calculate variance -----------\n")
print(df.cov())
 

#%%
import pandas as pd
 
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n------ Percent change at each cell of a Column -----\n")
print(df[['Apple']].pct_change()[:3])
 
print("\n------ Percent change at each cell of a DataFrame -----\n")
print(df.pct_change()[:5])

#%%

import pandas as pd
 
df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
 
print("\n------ DataFrame-----\n")
print(df)
 
print("\n------ Unstacking DataFrame -----\n")
print(df.stack(level=-1))
print(df.unstack(level=-1))

#%%
