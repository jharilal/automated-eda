import pandas as pd
import os

# a = os.path.abspath('sources')
op = pd.read_csv(os.path.abspath('sources/testdata/vHoneyNeonic_v02.csv'))

op2 = op.copy()

for col in op.columns:
    try:
        op2[col] = pd.to_datetime(op2[col])
    except:
        continue

print(op2.info())

print(op2['year'].head())

# print(op['name'].isnull().sum())
