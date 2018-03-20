import numpy as np
import pandas as pd



import os
os.getcwd() # get current working directory


# update this to your file path:
os.chdir('C:/Users/DElbert/Desktop/coLab')

os.getcwd() # confirm working directory changed successfully

tablestemp = pd.read_csv('data/evaluations.csv', encoding='latin1')


#explore the DF
tablestemp.dtypes
tablestemp.shape

tablestemp.describe()

#summarization
grouped_df = tablestemp.groupby('Respondent')
type(grouped_df)
grouped_df.size()

#creation of a three column df
respondent = tablestemp[['Respondent', 'Question', 'Response']]



#making an HHS ID column
def get_hhsid(respondent):
    if respondent is None:
        return None
    hhsids = ['']
    
    for hhsid in hhsids:
        if respondent.find(hhsid) != -1:
            return hhsid
        return''
        
        