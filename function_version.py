#!/usr/bin/env python
# coding: utf-8

# #### Airline Passenger Flow:
# ##### This program analyzes data from the San Fransisco Airport to identify airlines that could benefit from increasing/decreasing checkout counters, based on the number of passengers using a terminal over time.
# 
# ##### Through the view_airline_flow function, a user can input the relevant data file name ('Air_Traffic_Passenger_Statistics.csv'), airline code (e.g. 'TZ'), activity (e.g., 'Enplaning'), and terminal (e.g., 'Terminal 1'). The function outputs a line plot of the passenger flow by month, per the given parameters.
# 
# ###### Generally, a recent, sharp increase in passengers indicates that the airline would benefit from increasing the number of check-in counters in the terminal. Conversely, a sharp decrease would suggest the airline would benefit from less check-in counters.
# 
# ### General form:
# 
# #### view_airline_flow('Air_Traffic_Passenger_Statistics.csv', 'Airline code', 'Activity Code', 'Terminal' [or 'All'])

# In[ ]:


import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


# In[ ]:


def view_airline_flow(filename, airline, activity, terminal):
    # read in data
        air=pd.read_csv(filename)  
        
        # Extract month and year from Activity Period
        air['Activity Period'] = air['Activity Period'].apply(str)
        air['year'] = air['Activity Period'].str.slice(0,4)
        air['month'] = air['Activity Period'].str.slice(4,6)
        
        # Drop unnecessary cols and rename w/out spaces
        air2 = air.drop(['Operating Airline','Published Airline','Published Airline IATA Code','GEO Summary','GEO Region','Price Category Code','Boarding Area'], axis=1)
        air2 = air2.rename(columns={'Activity Period':'activity_period', 'Terminal':'terminal', 'Operating Airline IATA Code':'airline_code', 'Activity Type Code':'activity_code', 'Passenger Count':'passenger_flow'})
        
        # create airline, activity, and terminal variables
        airline = airline
        activity = activity
        terminal = terminal
        
        # query data by airline code, activity code, and terminal
        if terminal == 'All':
            air2 = air2.query('airline_code == @airline and activity_code == @activity')
        else:
            air2 = air2.query('airline_code == @airline and activity_code == @activity and terminal == @terminal ')
        
        air2 = air2.drop_duplicates()
        
        # group and sort by month
        air2.groupby(['activity_period']).sum()
        air2.sort_values(by=['activity_period'])
        
        # plot passenger flow over time
        return air2.plot(x = 'activity_period', y = 'passenger_flow', kind = 'line')
        


# In[ ]:


view_airline_flow('Air_Traffic_Passenger_Statistics.csv', '9W', 'Enplaned', 'All')

