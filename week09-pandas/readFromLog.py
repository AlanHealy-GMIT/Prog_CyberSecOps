# messingWithPandas.py
# This program uses pandas to read from a file.
# Author: Alan Healy
# Date Created: 27-APR-2021

import pandas as pd
import regex as re
import matplotlib.pyplot as plt

path = './data/'
logFilename = path + 'access.log'

colNames = ('IP','Dash1','UserID','Time','URL','Status Code','Size of Response','Referrer','User Agent','Dunno')


df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)

df.drop(columns=['Dash1','UserID'], inplace=True)

# remove [] from time
df['Time'] = df['Time'].apply(lambda x: re.search('[\w:/]+', x).group())

# change Time type to time
df['Time'] = pd.to_datetime(df['Time'], format='%d/%b/%Y:%H:%M:%S')

#print(df)

#print(df.iloc[0])

#print(df.dtypes)

start_date = '2021/02/15 18:00:00'
end_date   = '2021/02/15 18:59:59'

# way one of loc
#newdf = df.loc[(df['Time'} > start_date) & (df['Time'] < end_date)]]

# way 2
#newdf = df[df.Time.between(start_date, end_date)]

# way 3, sets index to date column
df = df.set_index(['Time'])
newdf = df['2021/02/15 18:00:00':'2021/02/15 18:59:59']

#newdf = df.between_time('23:00', '23:59') # this is times every day

print(newdf)

downloadSamples = df['Size of Response'].resample(rule='10Min').mean()
print(downloadSamples)

downloadSamples.plot()

plt.title("readFromLog.py", loc='center')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()

plt.show()
