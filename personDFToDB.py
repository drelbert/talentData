
import numpy as np
import pandas as pd
import os
os.getcwd() # get current working directory


# update this to your file path:
os.chdir('C:/Users/DElbert/Desktop/coLab')

os.getcwd() # confirm working directory changed successfully

tablestemp = pd.read_csv('data/learnerTranscripts2017.csv', encoding='latin1')


tablestemp.columns
tablestemp.dtypes
tablestemp.shape

#drop the NAN's



#groupby for summarization
grouped_df = tablestemp.groupby('TITLE')
type(grouped_df)
#creates a DataFrameGroupBy object to do the aggregation method like .size()
grouped_df.sum()


#to compare org code and b/o code
tablestemp['HHSID'].unique()
#reuse code above but add b/o code


#initial creation of the person df
person = tablestemp[['FNAME', 'LNAME', 'HHSID',  'ORG']]



#rename cols to match the those of the  tables
person = person.rename(columns = {'FNAME' : 'firstName', 'LNAME' : 'lastName', 'HHSID' : 'hhsId', 'ORG' : 'orgCode' })

#clean
##deleting the duplicate HHSID rows

#use read steps above and then
person.head()


#check for duplicates
person.duplicated()

#or check for duplicates in a particular column

# using
person.duplicated('hhsId').sum()

# shows that there are 18424 hhsId duplicates
# need to remove these duplicates to get a true list of HRSA employees who have completed offerings

# view the duplicated rows
person.loc[person.duplicated(), :]

#to update the actual df run
person = person.drop_duplicates('hhsId')
len(person)
#this results in 2210 unique hhsIds





#initial creation of course_offering
#this has only been done for CY 17 data set
#need to complete for CY 18

tablestemp.columns
tablestemp.dtypes
tablestemp.shape



course_offering = tablestemp [[ 'TITLE', 'NAME', 'OFFERING_TEMPLATE_NO',  'PART_NO', 'FOS_NAME', 'DURATION' ]]

#dropping Nan's 

#returns 5862 rows so this seems to remove too many
course_offering = course_offering.dropna(axis=0, how='any', thresh=5, subset=None, inplace=False )



#this code dropped rows after 19296 which was 1408 fully NAN rows
course_offering = course_offering[:19296]
#returns shape of 19296
course_offering.shape



course_offering = course_offering.rename(columns = {'TITLE' : 'courseTitle', 'OFFERING_TEMPLATE_NO' : 'courseId', 'PART_NO' : 'offeringId', 'FOS_NAME' : 'program', 'NAME' : 'deliveryType', 'DURATION' : 'duration' })


#dropping dups
#needed to define what was unique about this df vs the course df in order to drop the right dups
course_offering.duplicated('offeringId').sum()
#dups are
#for courseTitle  = 18511
#for courseId  =  18511
#for offeringId =  18040 

#WHY?  courseTitle and courseId are a one to one
#While offeringId represents many to one, there can be more than one offering for one courseId  

#Is dropping duplicates valid?  Is it neccessary?  
#No, because each row in the course_offering df represents one hhsId completing an offering 

#but if need to drop, here is the code
course_offering = course_offering.drop_duplicates('courseId')
len(course_offering)

#results in a df with 758 rows  




#splitting the course_offering DF since 19,296 returned a mysql timeout
group_one = pd.DataFrame()
group_two = pd.DataFrame()



if course_offering.shape[0] < 10000:
    group_one = course_offering[:10000]
    group_two = course_offering[10000:]

#this resulted in two df's one with 10000 and one 9296  
    




#initial creaation of the transcript df
transcript = tablestemp[['HHSID', 'OfferingId']]

transcript = transcript.rename(columns = {'HHSID' : 'hhsId', 'OfferingId' : 'offeringId'})




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

#confirm append or replace
group_two.to_sql("course_offering", dbconn, index=False, if_exists='replace')
