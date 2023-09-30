import numpy as np
"""
#numpy array

list=[10,20,30,40,50,60]
print(type(list))
np_list=np.array(list)
print(type(np_list))            #numpy matrislerle calisan birkutuphaneden bu islemin tek farki daha fazla özelliginin olmasi....

list2=[[1,0,0],[0,1,0],[0,0,1],[0,0,0]]
np_list2=np.array(list2)
print(np_list2)
print(np_list2.shape)           #matrisin kaca kaclik oldgunu soyler....
print(np_list2.mean())

print([*range(0,10)])

print(np.arange(0,10,2))
print(np.zeros((10,10)))
print(np.ones((10,10)))



print(np.linspace(0,10,100))        #0 dan 10 a kadar giden bir liste olusturur ancak bir sonraki elemana belirttigin deger kadar arttirarak ilerler
                                        #yani 1.10 1.20 vs.....

print(np.random.randint(1,100,3))   #1 den 100 e kaadar 3 tane rastgele sayi goster..


np_list3=np.arange(0,20)
print(np_list3[4:9:2])

list3=[*range(0,20)]
#list3[4:9:2]=10        hata aliriz
(np_list3[5:14:2])=10
print(np_list3[5:14:2])
"""

x=np.random.randint(10,100,25)
print(x)

result=x>50
print(result)

print(x[result])   #50 den buyuk sayilaari burada gosteririr...
