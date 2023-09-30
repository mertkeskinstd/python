import pandas as pd
import numpy as np

data_frame=pd.read_excel("C:\\Users\\tahak\\Desktop\\piton\\modul_paket\\pandaslib\\27-SalarySheet.xlsx")
group_ones=data_frame.groupby("Department")
group_two=data_frame.groupby("Title")
print(group_ones.mean())
print(data_frame.describe())
print(data_frame["Salary"].mean())
print(group_two.mean())
print(data_frame.loc[data_frame["Department"] == "Software Development"].groupby("Title").mean())


