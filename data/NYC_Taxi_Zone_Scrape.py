import os
import pandas as pd

print(os.getcwd())

taxi_zones_df = pd.read_csv(r"C:\Users\alden\Desktop\UCSD_Course_Private\UCSD_Course_Private\16_Data_Wrangling_&_Exploration\taxi_zones.csv", encoding= "utf-8")
print(taxi_zones_df.columns)

taxi_zones_df = taxi_zones_df[["zone", "LocationID"]]

taxi_zones_dict = dict(zip(taxi_zones_df["LocationID"], taxi_zones_df["zone"]))
print(taxi_zones_dict)
                       