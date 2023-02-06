# -*- coding: utf-8 -*-
"""

@author: UTHMAN OYEBANJI
"""
import requests
import pandas as pd

def Stop_and_Search_Data(force, date):
    '''
    This function gets the stop and search data from the police API "https://data.police.uk/docs/method/stops-force/".
    Clean data is returned in a pandas dataframe.
    
    Args:
    force: string. The force ID of the force to get stop and searches for. IDs can be found here: https://data.police.uk/api/crimes-street-dates.
    date: string. The year and month data needed in the format YYYY-MM.
    
    Returns:
    df_raw_data: the data in pandas data frame.
    '''
    
    force_response = requests.get(f'https://data.police.uk/api/stops-force?force={force}&date={date}')

    force_json = force_response.json()
    df_raw_data = pd.json_normalize(force_json)
    
    df_raw_data['datetime'] = pd.to_datetime(df_raw_data['datetime'])
    df_raw_data['datetime'] = df_raw_data['datetime'].dt.date
    
    df_useful = df_raw_data.loc[:,['age_range', 'outcome', 'involved_person',
       'gender', 'datetime', 'officer_defined_ethnicity', 'type', 
       'object_of_search']]
    
    df_clean = df_useful.rename({'officer_defined_ethnicity': 'ethnicity'}, axis=1)
    df_clean[['age_range','gender', 'ethnicity']] = df_clean[['age_range','gender', 'ethnicity']].fillna('Unspecified')
    df_clean['object_of_search'] = df_clean['object_of_search'].fillna('Others')
    
    return df_clean

import matplotlib.pyplot as plt


def BarPlot(x_column, y_column, title, ylabel, color = "b", fontsize =30, fontweight='bold'):
    plt.rcParams.update({'font.family':'fantasy'})
    plt.figure(figsize = (25,13))
    plt.bar(x = x_column, height=y_column, color = color)
    plt.xticks(rotation=45)
    plt.title(title, fontsize = fontsize, fontweight=fontweight)
    plt.ylabel(ylabel, fontsize = fontsize, fontweight=fontweight)
    plt.xlabel('Date', fontsize = fontsize, fontweight='bold')
    plt.xticks(size= 15)
    plt.yticks(size= 15)
    
def LinePlot(y_column, title, ylabel, color = "b", fontsize =30, fontweight='bold'):
    plt.rcParams.update({'font.family':'fantasy'})
    plt.figure(figsize = (25,13))
    plt.plot(y_column, color = color, linewidth = 3)
    plt.xticks(rotation=45)
    plt.title(title, fontsize = fontsize, fontweight=fontweight)
    plt.ylabel(ylabel, fontsize = fontsize, fontweight=fontweight)
    plt.xlabel('Date', fontsize = fontsize, fontweight='bold')
    plt.xticks(size= 15)
    plt.yticks(size= 15)

    