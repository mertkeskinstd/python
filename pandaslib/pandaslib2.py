import pandas as pd
import numpy as np
"""""
dic={"serhat":[40,30,np.nan],"mursel":[20,np.nan,50],"berat":[10,20,30]}

data_frame=pd.DataFrame(dic)
print(data_frame)
print(data_frame.dropna())
print(data_frame.dropna(axis=1))

dic={"serhat":[40,30,np.nan],"mursel":[20,np.nan,50],"berat":[10,20,30],"ali":[45,np.nan,np.nan]}
data_frame=pd.DataFrame(dic)
print(data_frame)
print(data_frame.dropna(axis=1,thresh=2))           #nan degerinden kolondan 2 tane varsa cikar demek oluyor....
print(data_frame.fillna(205))


dic={"programing language":["python","python","python","java","java","swift"],"name":["a","b","c","d","e","f"],"salary":[100,90,80,70,60,50]}
salary_frame=pd.DataFrame(dic)
print(salary_frame)
group_object=salary_frame.groupby("programing language")
print(group_object.count())
print(group_object.mean())
print(group_object.min())
print(group_object.max())
print(group_object.min(numeric_only=True))      #sadece numara olan seylerin ustunden min bulur...
print(group_object.describe())                  #herseyi yazdrır 

"""
dic1={"Name" : ["A","B","C","D"],
    "Sports" : ["Basketball", "Football", "Tennis", "Running"],
    "Calories" : [100,200,300,400]
    }
frame1=pd.DataFrame(dic1,index=[0,1,2,3])
#print(frame1)
dic2 = {"Name" : ["E","F","G","H"],
        "Sports" : ["Basketball", "Football", "Tennis", "Running"],
        "Calories" : [200,50,330,440]
        }
frame2=pd.DataFrame(dic2,index=[4,5,6,7])
#print(frame2)
dic3={"Name" : ["I","J","K","L"],
    "Sports" : ["Basketball", "Football", "Tennis", "Running"],
    "Calories" : [300,150,320,410]
    }
frame3=pd.DataFrame(dic3,index=[8,9,10,11])
#print(frame3)


#concatenation.....BİRLESTİRR....

print(pd.concat([frame1,frame2,frame3]))

#MERGE

print(pd.merge(frame1,frame2,on="Sports"))


söz={"name":["serhat","berat","mursel"],"salary":[10000,61000,75000],"age":[25,21,22]}
new_data=pd.DataFrame(söz)
print(new_data)

print(new_data["name"].unique())
print(new_data["name"].nunique())
def grosstonet(x):
    return x*0.65

print(new_data["salary"].apply(grosstonet))



