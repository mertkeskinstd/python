import pandas as pd
import numpy as np
"""""

my_dict={"mursel":50,"omer":100,"ali":43,"mehmet":65}
print(pd.Series(my_dict))

#liste icin ayni islem....
yas=[50,100,43,65]
name=["mursel","omer","ali","mehmet"]

print(pd.Series(data=yas,index=name))


np_array=np.arange(10,20)
print(pd.Series(np_array))
"""
my_data=np.array([[10,20,30],[50,60,80],[70,90,40],[65,72,63]])
names=np.array(["serhat","ali","veli","memet"])
month=np.array(["oct","apr","may"])
data_frame=pd.DataFrame(data=my_data,index=names,columns=month)
print(data_frame["apr"])
print(data_frame)

"""""
apr_mean=data_frame["apr"]
print(apr_mean.mean())
print(apr_mean.serhat)
print(apr_mean.max())

print(data_frame[["oct","may"]])

print(data_frame.loc["serhat"].mean())    
print(data_frame.iloc[3])

data_frame["june"]=data_frame["apr"]*2
print(data_frame)

print(data_frame.drop("serhat",axis=0))   #orjinal kod deismiyor axis 0 ve 1 degeri alır satir 0 sutun 1....
print(data_frame)
#eger serhati cikarmak istiyorsam kod su sekil olucak:
#data_frame.drop("june",axis=1,inplace=True)
#print(data_frame)
"""
#boolean_frame=data_frame>60
#print(boolean_frame)
#print(data_frame[boolean_frame])
print(data_frame[      data_frame["apr"]  >   50    ])

print(data_frame.reset_index())

data_frame["newindex"]=["ser","a,","ve","me"]
print(data_frame.set_index("newindex"))