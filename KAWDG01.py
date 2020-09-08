import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import datetime



# .csv files headers = ['Date','Water Levels (m)']

# point code to the data.
cwd = os.chdir("/Users/abigailmccarthy/Desktop/the real desktop/thesis/KAWDG01") 

field_data = pd.read_excel('Field_measurements.xlsx', parse_dates = ['Date'])

# figure handle to change properties more easily
field_data_fig = plt.figure(figsize = (15, 6))

plt.plot(field_data['Date'], field_data['Water Levels (m)'], color='green') 

plt.ylabel('Water Levels (m)')
plt.title('Field Measurements')

field_data_fig.tight_layout() # <-- extends plot to the border of the figure window
# field_data_fig.savefig('Field Data.png', dpi = 300) # <-- to save figures as a .png file



#stacked plots: groundwater level timeseries, 3 month SPEI, 12 month SPEI

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize = (10, 6))
plt1 = fig.add_subplot(3,1,1)
plt2 = fig.add_subplot(3,1,2)
plt3 = fig.add_subplot(3,1,3)

#groundwater level timeseries
SPEI = pd.read_excel('SPEI_1-24mo.xlsx', parse_dates = ['Date_start'])

plt1.plot(field_data['Date'], field_data['Water Levels (m)'], color ='green')
plt1.set_title('Groundwater Level (Field Measurements)')
plt1.set_xlim([datetime.date(1952, 2, 1), datetime.date(2020, 2, 1)])
plt1.axes.xaxis.set_ticklabels([])

#3 month SPEI
plt2.plot(SPEI['Date_start'], SPEI['SPEI_3mo'], color ='blue')
plt2.set_title('3-Month SPEI')
plt2.set_xlim([datetime.date(1952, 2, 1), datetime.date(2020, 2, 1)])
plt2.axes.xaxis.set_ticklabels([])
# if you want to remove x axis completely, use plt2.axes.get_xaxis().set_visible(False)

#12 month SPEI
plt3.plot(SPEI['Date_start'], SPEI['SPEI_12mo'], color ='purple')
plt3.set_xlim([datetime.date(1952, 2, 1), datetime.date(2020, 2, 1)])
plt3.set_title('12-Month SPEI')


fig.subplots_adjust(hspace=0.2,wspace=0.5)
plt.show()

#%%
#field_data remove outliers
#Data set not good when filtered.

#where to add parse_dates = ['Date'] ?

#test_windows=field_data.iloc[:,1].rolling(2).median()

#threshold = 0.02
#difference = np.abs(field_data['Water Levels (m)'] - test_windows)
#outlier_idx = difference < threshold 

#field_data['Water Levels (m)'][outlier_idx].plot(figsize = (15,6), color='green')
#plt.title('Field Data, outliers removed')
#plt.show()

#%% KGS Index Well Plot

kgs_data = pd.read_excel('Index_well_hourly.xlsx', parse_dates = ['Date for Average'])

kgs_data_fig = plt.figure(figsize = (15,6))

# Hourly data
#plt.plot(kgs_data['Date'], kgs_data['Water Levels (m)'], color='purple') 

#Index Well hourly data to daily average
plt.plot(kgs_data['Date for Average'], kgs_data['Daily Average'], color='purple') 

plt.ylabel('Water Levels (m)')
plt.title('KGS Index Well')
plt.xticks(rotation = 90)

plt.show()


#%%  
# The index well data cnverted to daily does not need this filter anymore.

#Index well smoothing outlier points using rolling median filter
#test_windows=kgs_data.iloc[:,1].rolling(10).median()
#48 was a good rolling number for hourly data.

#test_windows.plot(figsize = (15,6), color='purple')
#plt.ylabel('Water Levels (m)')
#plt.title('KGS Index Well Filtered')
#plt.xticks(rotation = 90)
#plt.title('Index Well, outliers smoothed')


#Removing outliers from Index Well

# Smoothness increases by increasing the rolling median number below.
#test_windows = kgs_data.iloc[:,1].rolling(30).median()

#for hourly data, lower threshold number (0.01) looked similar to the original data. 
#Using a higher threshold number 0.05 looks more jagged, fewer outlier points. Used 0.02 for hourly data.
#Does not remove clusters of very high or low points
#threshold = 0.03
#difference = np.abs(kgs_data['Daily Average'] - test_windows)
#outlier_idx = difference < threshold 
# If difference in values is over the threshold, then the point is removed. Note: If you make difference greater than threshold by reversing inequality sign, the result is a jagged graph.
#np.max(difference) in console: 0.67055... the same for any threshold value

#kgs_data['Daily Average'][outlier_idx].plot(figsize = (15,6), color='purple')
#plt.title('Index Well, outliers removed')
#plt.xticks(rotation = 90)
#plt.show()

#This looks loopy because smoothing data and then removing outliers
#test_windows[outlier_idx].plot(figsize = (15,6), color='purple')
#plt.xticks(rotation = 90)
#plt.title('Index Well, outliers smoothed then removed')



#%% USGS Daily Data Plot

usgs_data = pd.read_excel('USGS_Daily_data.xlsx', parse_dates = ['Date'])

usgs_data_fig = plt.figure(figsize = (15,6))

plt.plot(usgs_data['Date'], usgs_data['Water Levels (m)']) 

plt.ylabel('Water Levels (m)')

plt.title('USGS Daily Data Filtered')
plt.show()

#%% 
#rolling mean filter for Daily Data Plot, smoothing only

#test_windows=usgs_data.iloc[:,1].rolling(15).median()
#test_windows.plot(figsize = (15,6))
#plt.ylabel('Water Levels (m)')
#plt.title('USGS Daily Data')
#plt.show()

#%% Daily data, smooth and remove outliers

#where to add parse_dates = ['Date'] ?

test_windows=usgs_data.iloc[:,1].rolling(18).median()

threshold = 0.02
difference = np.abs(usgs_data['Water Levels (m)'] - test_windows)
outlier_idx = difference < threshold 


usgs_data['Water Levels (m)'][outlier_idx].plot(figsize = (15,6))
plt.title('Daily Data, outliers removed')
plt.show()


#%%
#stack three plots, (#rows,#columns,plot#)
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize = (6, 8))
plt1 = fig.add_subplot(3,1,1)
plt2 = fig.add_subplot(3,1,2)
plt3 = fig.add_subplot(3,1,3)

field_data = pd.read_excel('Field_measurements.xlsx', parse_dates = ['Date'])
plt1.plot(field_data['Date'], field_data['Water Levels (m)'], color ='green')
plt1.set_title('Field Measurements')

kgs_data = pd.read_excel('Index_well_hourly.xlsx', parse_dates = ['Date'])
plt2.plot(kgs_data['Date'], kgs_data['Water Levels (m)'], color ='blue')
plt2.set_title('Index Well')

usgs_data = pd.read_excel('USGS_Daily_data.xlsx', parse_dates=['Date'])
plt3.plot(usgs_data['Date'], usgs_data['Water Levels (m)'], color ='purple')
plt3.set_title('USGS Daily Data')
fig.subplots_adjust(hspace=1,wspace=1)
plt.show()

#%% 
#All lines on the same graph

# figure handle to change properties more easily
combined_fig = plt.figure(figsize = (15, 6))

plt.plot(field_data['Date'], field_data['Water Levels (m)'], color ='green', label = "Field Measurements")
plt.plot(kgs_data['Date'], kgs_data['Water Levels (m)'], color ='blue', label = "KGS Index Well")
plt.plot(usgs_data['Date'], usgs_data['Water Levels (m)'], color ='purple', label = "USGS Daily Data")

#using rows from csv file or from dataframe (row 3260), bracket in this range
#plt.xlim(field_data.iloc[3260,0],field_data.iloc[3357,0])

# name y axis 
plt.ylabel('Water Levels (m)')
# title to my graph 
plt.title('Well Data')
plt.legend(loc='upper left', bbox_to_anchor=(0, 1.08)) 
#combined_fig.savefig('Field Data.png', dpi = 300)

plt.show()

  
                  
#%%

#Meteorological data
#It says invalid syntax but it still works anyways.
climate_data = pd.read_excel('Climate_onlycombineddata.xlsx', parse_dates = ['Date for monthly sum'])

# figure handle to change properties more easily
climate_data_fig = plt.figure(figsize = (15, 6))

plt.plot(climate_data['Date for monthly sum'], climate_data['PRECIP MONTHLY SUM'], color='green') 

plt.ylabel('Precipitation (mm)')
plt.title('Precipitation')
climate_data_fig.tight_layout() # <-- extends plot to the border of the figure window
#climate_data_fig.savefig('Field Data Precip.png', dpi = 300) # <-- to save figures as a .png file
plt.show()

#plotTmax

plt.plot(climate_data['Date for monthly sum'], climate_data['TMAXMONTHLY'], color='pink') 

plt.ylabel('Maximum Temperature (C)')
plt.title('Maximum Temperature')
climate_data_fig.tight_layout() # <-- extends plot to the border of the figure window
#climate_data_fig.savefig('Field Data Tmax.png', dpi = 300) # <-- to save figures as a .png file
plt.show()

#plot Tmin
plt.plot(climate_data['Date for monthly sum'], climate_data['TMINMONTHLY'], color='orange') 

plt.ylabel('Minimum Temperature (C)')
plt.title('Minimum Temperature')
climate_data_fig.tight_layout() # <-- extends plot to the border of the figure window
#climate_data_fig.savefig('Field Data Tmin.png', dpi = 300) # <-- to save figures as a .png file
plt.show()

#%% 
#Evapotranspiration with two outliers removed
#Hargreaves-Samani method for evapotranspiration

#Evap = pd.read_excel('Evap.xlsx', parse_dates = ['Date'])
Evap = pd.read_excel('Evap.xlsx', parse_dates = ['Date for monthly sum'])

Evap_fig = plt.figure(figsize = (15,6))

#plt.plot(Evap['Date'], Evapo['ETo'], color='red')
# ^to plot with the two negative values included

removeoutlier_idx = Evap['EVAP MONTHLY SUM'] > 0

Evap['EVAP MONTHLY SUM'][removeoutlier_idx].plot(figsize = (15,6), color = 'red')

plt.ylabel('Evapotranspiration (mm/day)')
plt.title('Evapotranspiration')
plt.xticks(rotation = 90)

plt.show()

