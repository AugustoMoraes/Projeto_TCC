import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('../dataset/dataset.csv')

print(df)
#print(df.head(4))
#print(df.describe())

