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
