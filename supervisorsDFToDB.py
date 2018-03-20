import numpy as np
import pandas as pd
import os
os.getcwd() # get current working directory


# update this to your file path:
os.chdir('C:/Users/DElbert/Desktop/coLab')

os.getcwd() # confirm working directory changed successfully

tempsupervisors = pd.read_csv('data/supervisorsJan18.csv', encoding='latin1')


tempsupervisors.columns
supervisors.dtypes
tempsupervisors.shape


supervisors = tempsupervisors [['DeptID', 'Name', 'name 2', 'Descr', 'Mgr Level']]


#groupby for summarization
grouped_df = tempsupervisors.groupby('DeptID')
type(grouped_df)
#creates a DataFrameGroupBy object to do the aggregation method like .size()
grouped_df.sum()



#rename cols to match the those of the tables
supervisors = supervisors.rename(columns = { 'DeptID' : 'orgCode', 'Name' : 'lastName', 'name 2' : 'firstName', 'Descr' : 'title', 'Mgr Level' : 'mngrLevel'})


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

supervisors.to_sql("supervisors", dbconn, index=True, if_exists='replace')





#