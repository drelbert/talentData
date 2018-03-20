"""
tasks to be completed on this df
split PO Name into two columns

"""


import numpy as np
import pandas as pd

import os
os.getwd()



os.chdir('C:/Users/DElbert/Desktop/coLab')

#cleaning the PO list
poTemp = pd.read_csv('data/poListJan30.csv', encoding='latin1')


poTemp.columns
poTemp.dtypes

poTemp['PO Name'].unique()
poTemp['PO Name'].nunique()
#448

#creataing and renaming the df
projectOfficers = poTemp[['Bureau/ Office', 'PO Name', 'PO Email',  'PO Phone']]

projectOfficers = projectOfficers.rename(columns = {'Bureau/ Office' : 'bo', 'PO Name' : 'name', 'PO Email' : 'pOEmail', 'PO Phone' : 'pOPhone' })

#removing duplicates on email
projectOfficers.duplicated('pOEmail').sum()
#6211
projectOfficers = projectOfficers.drop_duplicates('pOEmail')
#resulted in 448



#separating first and last names into diff columns

projectOfficers[['firstName','lastName']] = projectOfficers['name'].loc[projectOfficers['name'].str.split().str.len() == 2].str.split(expand=True)

#re build df to have remove the name column
projectOfficers = projectOfficers[[ 'pOEmail', 'lastName', 'firstName', 'bo', 'pOPhone']]

#code to save as .csv for sharing w HLI
projectOfficers.to_csv('projectOfficers.csv')


#pre load code to change name
project_officers = projectOfficers[[ 'pOEmail', 'lastName', 'firstName', 'bo', 'pOPhone']]

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

project_officers.to_sql("project_officers", dbconn, index=False, if_exists='append')







  