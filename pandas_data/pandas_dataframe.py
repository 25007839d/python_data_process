import pandas as pd

# key like a column and value like a cilumn value(rows)
df= pd.DataFrame({"name":['rahul','ritu','monty'],'city':['pune','delhi','kashipur']})
# print(df)

# -------------sahpe() for know the row and column, head() for top 5 row, describe() for general info , tail() for last record
# print(df.describe())
# print(df.head(1))
# print(df.tail(1))
# print(df.shape)

#--------create df by csv file

# df1 = pd.read_json(r'C:\Users\Dell\OneDrive\Desktop\dag.json',lines=True)
# print

df2 = pd.read_excel(r'C:\Users\Dell\OneDrive\Desktop\z.xlsx')
print(df2)

# print(df1.shape)

# ---------iloc[1,4] function for fetch value by slicing
# print(df1.iloc[2:6,0:3])

# --------loc[1:4,('id','first_name')] fetch by column name
# print(df1.loc[0:5,('id','first_name')])

#---------drop the column by 1-axis and drop rows by 0-axis (pass index value)
# print(df1.drop('id',axis=1))     # drop column

# print(df1.drop([0,4,2],axis=0))   # drop rows

#---------aggrigate functions (min,max,mean, etc)
# print(df1.max())
"""
result:----------
first_name                 Vallie
last_name                Wilkison
email         vskitt1@state.tx.us
salary                         43
gender                       Male
ip_address          84.54.102.193
"""

#------------function apply on df columns
def upper(x):

    return x+1000
# print(df1[['id']].apply(upper))

#------------value_counts() as like group by count
# print(df1[['first_name']].value_counts())

#---------sort column byse
# print(df1.sort_values(by="first_name"))

#---------join df

# df.set_index('key').join(other.set_index('key'))

