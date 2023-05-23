# single dimention is called series and multidimentional is called dataframe
import pandas as pd

# -------------------create series of list
s1 = pd.Series([1,2,43,4,3])
# print(s1)
# print(type(s1))
s2 = pd.Series([1,2,43,4,3],index=['a','b','c','d','e'])
# print(s2)

# -------------------create series of dict
s_d = pd.Series({'a':1,'d':3,'f':3})
s_d = pd.Series({'a':1,'d':3,'f':3},index=['a','f','d']) # change index
# print(s_d)


# ---------------extract indivisual element from series by using indexing like list
in_s_d = s_d[:2]
# print(in_s_d)

# arthmatic operation
# print(s_d+3)
# print(s_d-3)
# print(s_d*3)
# print(s_d/3)
# print(s_d+in_s_d)