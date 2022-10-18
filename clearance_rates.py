import pandas as pd
import zipfile
from io import BytesIO
import numpy as np
import os


def get_file(fnombre):
    location = data_path + fnombre
    filenames = [y for y in os.listdir(location)]
    df_outcome = []
    df_street = []
    for file in filenames:
        if file.endswith('outcomes.csv'):
            df_outcome.append(pd.read_csv(os.path.join(location, file)))
        elif file.endswith('street.csv'):
            df_street.append(pd.read_csv(os.path.join(location, file)))
    return pd.concat(df_outcome, ignore_index=True), pd.concat(
        df_street, ignore_index=True)

def appended_df():
    df_outcome = []
    df_street = []
    for year in years:
        df_outcome.append(get_file(fnombre=year)[0])
        df_street.append(get_file(fnombre=year)[1])
    df_outcome = pd.concat(df_outcome)
    df_outcome.rename(columns={
        'Month': 'date',
        'Reported by': 'agency_name',
        'Longitude': 'lon',
        'Latitude': 'lat',
        'LSOA code': 'lad',
        'Outcome type': 'outcome'
    }, inplace=True)
    df_outcome = df_outcome[['lad', 'lon', 'lat',
                             'agency_name', 'date', 'outcome']]
    df_outcome = df_outcome.dropna().reset_index(drop=True)
    df_street = pd.concat(df_street)
    df_street.rename(columns={
        'Month': 'date',
        'Reported by': 'agency_name',
        'Longitude': 'lon',
        'Latitude': 'lat',
        'LSOA code': 'lad',
        'Crime type': 'crime_type',
        'Last outcome category': 'last_outcome'
    }, inplace=True)
    df_street = df_street[['lad', 'lon', 'lat', 'agency_name',
                           'date', 'crime_type', 'last_outcome']]
    df_street = df_street.dropna().reset_index(drop=True)
    return df_outcome, df_street


if __name__ == '__main__':

    data_path = '/Users/schin/clearance-rates-uk/data/'

    years = ['2014-01', '2014-02', '2014-03', '2014-04', '2014-05', '2014-06',
             '2014-07', '2014-08', '2014-09', '2014-10', '2014-11', '2014-12',
             '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06',
             '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12',
             '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06',
             '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12',
             '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',
             '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
             '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06',
             '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12',
             '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06',
             '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12']

    df_outcome, df_street = appended_df()
