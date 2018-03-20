import numpy as np
import pandas as pd
import os
os.getcwd() # get current working directory


# update this to your file path:
os.chdir('C:/Users/DElbert/Desktop/dev')

os.getcwd() # confirm working directory changed successfully

hrsaList = pd.read_csv('talApp/data/hrsaList.csv', encoding='latin1')



# find the most common Descr value
grouped_df = hrsaList.groupby('Descr')
type(grouped_df)

grouped_df.sum()


#create a new df based in Descr
descr = hrsaList.groupby(['Descr'], as_index=False).count()




