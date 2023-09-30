import numpy as np
import matplotlib.pyplot as plt
"""""
age_list = [20,25,30,35,40,45,50,55,60]
weight_list = [70,75,73,85,89,90,75,84,90]

age_list_numpy = np.array(age_list)

weight_list_numpy = np.array(weight_list)

plt.plot(age_list_numpy,weight_list_numpy,"black")
plt.xlabel("age")
plt.ylabel("weight")
plt.title("age-weight grabh")
plt.show()  

np_list=np.linspace(0,15,25)
np_list2=np_list**3

plt.plot(np_list,np_list2,"y--")
#plt.show()

plt.subplot(1,2,2)          #satırlar 1 arak-lıklı sutunlar 2 aralıklı 2. gafik olucak sekildee.......
plt.plot(np_list,np_list2,"b*")

plt.subplot(1,2,1)
plt.plot(np_list2,np_list,"c--")

my_figure = plt.figure()
my_axes = my_figure.add_axes([0.1,0.1,0.5,0.5])
my_axes.plot(np_list,np_list2,"g*")
my_axes.set_xlabel("X Data")
my_axes.set_ylabel("Y Data")
my_axes.set_title("Graph Title")

my_figure2 = plt.figure()


my_axes3 = my_figure2.add_axes([0.1,0.1,0.9,0.9])
my_axes3.plot(np_list,np_list2,"r*-")
my_axes3.set_xlabel("X Data Large")
my_axes3.set_ylabel("Y Data Large")
my_axes3.set_title("Large Graph")

my_axes2 = my_figure2.add_axes([0.25,0.4,0.3,0.3])
my_axes2.plot(np_list,np_list2,"g*")
my_axes2.set_xlabel("X Data Small")
my_axes2.set_ylabel("Y Data Small")
my_axes2.set_title("Small Graph")
plt.show()

(my_fig, my_axe) = plt.subplots()
my_numpy3 = np.linspace(0,15,20)
my_numpy4 = my_numpy3 ** 2
my_axe.plot(my_numpy3,my_numpy4, color="#CD621D", alpha=1)
my_axe.plot(my_numpy4,my_numpy3, color="#B81DCD", alpha=0.9)


(new_fig, new_axe) = plt.subplots()
new_axe.plot(my_numpy3, my_numpy3 + 2, color="#B81DCD", linewidth = 2.4)
new_axe.plot(my_numpy3, my_numpy3 + 3, color="#1DCDCA", linewidth = 1.4)
new_axe.plot(my_numpy3, my_numpy3 + 4, color="blue", linewidth = 1.4, linestyle="-.")
new_axe.plot(my_numpy3, my_numpy3 + 5, color="#fff435", linewidth = 1.4, linestyle=":")
new_axe.plot(my_numpy3, my_numpy3 + 6, color="red", linewidth = 1.4, linestyle="--", marker="o")
new_axe.plot(my_numpy3, my_numpy3 + 7, color="black", linewidth = 1.4, linestyle="--", marker="+", markersize=8)


plt.scatter(my_numpy3, my_numpy4)

#histogram

new_numpy = np.random.randint(0,100,40)
plt.hist(new_numpy)
plt.show()
"""