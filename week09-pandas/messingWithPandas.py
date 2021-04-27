# messingWithPandas.py
# This program tests out different pandas capabilities.
# Author: Alan Healy
# Date Created: 27-APR-2021

import pandas as pd

listData = [
    ['John', 'Math', 23],
    ['John', 'Programming', 66],
    ['Mary', 'Math', 45],
    ['Mary', 'Programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'Programming', 70],
    ['Mark', 'Math', 73],
    ['John', 'Programming', 61]
]

df = pd.DataFrame(listData, columns=['Name','Subject','Grade'])
print(df.head(3))

print(df.describe())
print(type(df.describe()))

path = "./data/"
csvFilename = path + 'grades.csv'
df.to_csv(csvFilename)

excelFilename = path + 'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")


mean = df.describe().loc['mean','Grade']
print(mean)
# or
mean = df['Grade'].mean()
print(mean)

