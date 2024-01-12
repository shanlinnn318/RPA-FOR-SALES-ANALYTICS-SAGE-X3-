import pandas as pd
from pandas import DataFrame

a = pd.read_csv("/Users/shanlin/Downloads/Invoice inquiry.csv")  #Change the directory
b = pd.read_csv("/Users/shanlin/Downloads/Invoice inquiry (1).csv")   #Change the directory
c = pd.read_csv("/Users/shanlin/Downloads/Invoice inquiry (2).csv")   #Change the directory
frames=[a,b,c]
mergedFrames=pd.DataFrame()
mergedFrames=pd.concat(frames, sort=False)
mergedFrames.to_csv("/Users/shanlin/Downloads/RPA_Invoice/Pending/Merged_files.csv")   #Change the directory

