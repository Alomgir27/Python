import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('mtcars.csv')

# d = pd.DataFrame(df.isna().sum(), columns=['count'])
# d.index.name = 'column'
# d = d.reset_index()
# d = d[d['count'] >= 0]
# d = d.sort_values(by='count', ascending=False)
# d = d.reset_index(drop=True)
# d['percent'] = d['count'] / len(df)
# d['percent'] = d['percent'].apply(lambda x: '{:.2%}'.format(x))
# d['count'] = d['count'].apply(lambda x: '{:,}'.format(x))
# d = d[['column', 'count', 'percent']]

print(len(df))
d = df.dropna(axis=0, how='any')
df = df.interpolate(method='linear', axis=0, limit_direction='forward').fillna(method='bfill', axis=0).fillna(method='ffill', axis=0)
print(len(df) - len(d))
print(df.isna().sum())
print(df.describe())

df = df.dropna()
print(len(df))
print(df)
    
df = df.dropna(axis=0, how='any')
df = df.interpolate(method='linear', axis=0, limit_direction='forward').fillna(method='bfill', axis=0).fillna(method='ffill', axis=0)
print(df.isna().sum())
print(df.describe())





# print(d, df)



# for i in range(len(df.columns)):
#     df = df.rename(columns={'Unnamed: ' + str(i): df.columns[i]})

# x = df['mpg'].values
# y = df['wt'].values

# print(df.head())

# plt.figure(figsize=(10, 6))
# plt.scatter(x, y, c='red', alpha=0.5, s=100)
# plt.xlabel('mpg')
# plt.ylabel('wt')
# plt.title('Scatter plot of mpg vs wt')

# plt.show()

# plt.figure(figsize=(10, 6))
# plt.scatter(df['mpg'], df['wt'], c='red', alpha=0.5, s=100)
# plt.xlabel('mpg')
# plt.ylabel('wt')

# plt.show()



# print(df.head())





