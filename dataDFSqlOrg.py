"""
Clean and load steps for Org data
"""

import numpy as np
import pandas as pd

import os
os.getcwd() # get current working directory


# update this to your file path:
os.chdir('C:/Users/DElbert/Desktop/coLab')

os.getcwd() # confirm working directory changed successfully

organization = pd.read_csv('data/orgBODescription.csv', encoding='latin1')


organization.columns
organization.dtypes
organization.shape
organization.head()

organization = organization.rename(columns = {'Ord Code' : 'orgCode', 'Bureau/Office' : 'bo', 'Descr' : 'orgName'})


#dealing with missing data, NAN
organization_cleaned = organization.dropna(how='all')

#adding string to NAN rows in HAB orgNAme
organization = organization_cleaned.fillna('HAB')


#any duplicates
organization.duplicated('orgCode').sum()

organization['orgCode'].nunique()


#load steps
import mysql.connector
"""
dbconn = mysql.connector.connect(user='root',
                                  password='root',
# leave password blank if you didn't create one
                                  host='127.0.0.1',
                                  database='mydb')
"""


from sqlalchemy import create_engine

dbconn = create_engine('mysql+mysqlconnector://root:root@localhost/talentdataone')

organization.to_sql("organization", dbconn, index=False, if_exists='append')
