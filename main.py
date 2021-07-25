import pandas as pd
import csv

df = pd.read_csv("Data.csv")

column = ["Star_name", "Distance", "Mass", "Radius"]

for i in range(0, len(column)):
    df = df[df[column[i]].notna()]

unwanted_column = ["index", "index_temp", "dawf_Star_name",
                   "dawf_Star_Distance", "temp_Mass", "temp_Radius"]


for i in range(0, len(unwanted_column)):
    del df[unwanted_column[i]]

df.drop([518,519,520,521,522,523,524,525,526,527,528,529,530,531], inplace=True)

df.to_csv("Final_Star_data.csv")
