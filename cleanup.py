import pandas as pd
import numpy as np
import os

os.chdir('C:/Users/ejl9900/Desktop/Data Science/MSDS434/GCP Survey Project')

#import open text survey responses from Learning Mangagement System
data=pd.read_csv('EJL Survey Essay Results with Sent Score v2 - UTF8.csv', encoding='utf-8')

#Write to .csv in utf-8 format for upload to GCP Storage

data.to_csv('Survey Results to GCP.csv', encoding='utf-8')
