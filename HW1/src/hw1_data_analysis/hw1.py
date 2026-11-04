import numpy as np 
import matplotlib.pyplot as plt  
import pandas as pd

bike_data = pd.read_csv('/Users/toireasa.marie/cse583/CSE-583-HW/HW1/src/hw1_data_analysis/bicycle_data.csv')
df = pd.DataFrame(bike_data)
print(df.columns.tolist())
#Columns : dtype 
#'Date'   : datetime64[ns]
#'Fremont Bridge Sidewalks, south of N 34th St Total' : float64
#'Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk' : float64
#'Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk' : float64

df['Total'] = (df['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk']
                + df['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk'])
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p')
df['Hour'] = df['Date'].dt.hour
df['Year'] = df['Date'].dt.year
#print(df.head())
#print(df.dtypes)
df_2016 = df[df['Year'] == 2016]
print(f'amount of missing data in 2016 is: {df_2016.isna().sum()}')
#There is 1 number of points of missing data for 2016 


#plot of hour of the day vs daily counts 
plt.figure(figsize=(8,6))
hour_totals = df_2016.groupby('Hour')['Total'].sum()
plt.plot(hour_totals.index, hour_totals.values, marker = '.')
plt.xlabel('Hour of the day')
plt.ylabel('Total Bicycle Counts')
plt.title('Total Bicycle Count vs Hour of Day')
plt.savefig('counts_by_hour.png', dpi = 500)
#plt.show()

#deciding what is the busiest hour of the day 
# Find the busiest hour of the day
hour_total_max =hour_totals.max()
hour_total_max_index =hour_totals.idxmax()

print('max bicycle count:', hour_total_max)
print('busiest hour:', hour_total_max_index)
#print(hour_totals)
#the busiest hour is 17 or 5pm 