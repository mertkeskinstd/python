from tkinter import *

wn=Tk()
wn.title("BMI")
wn.minsize(width=400,height=400)
wn.config(padx=20,pady=20)
wn.configure(bg="yellow")

def hesap1():
    kilo=en1.get()
    boy=en.get()
    hesap=float(kilo)/((float(boy)**2)*10000)
    #int(en2.insert(0,hesap))
    
    if en=="" or en1 =="":
        lb3.config(text= "lutfen deger giriniz ")
    else:
        try:
            
            gir=yazdir(hesap)
            lb3.config(text=gir)
        except:
            lb3.config(text="lutfen sayi girin...")
    
    

def yazdir(hesap):
    
    if hesap<18.5:
        lb5.config(text="İdeal kilonun altinda")
    elif 18.5<hesap<24.9:
        lb5.config(text="İdeal kiloda")
    elif 25<hesap<29.9:
        lb5.config(text="İdeal kilonun ustunde")
    elif 30<hesap<39.9:
        lb5.config(text="obezsin")
    elif 40<hesap:
        lb5.config(text="molbid obezsin")
            
    

lb1=Label(text="Lutfen Boyunuzu Giriniz: ",bg="black",fg="white",font=( "arial",8 ," bold italic"))
lb1.config(padx=10,pady=5)
lb1.place(x=0,y=90)
lb2=Label(text="Lutfen Kilonuzu Giriniz: ",bg="black",fg="white",font=( "arial",8 ," bold italic"))
lb2.config(padx=10,pady=5)
lb2.place(x=0,y=220)
lb3=Label(bg="yellow",font=( "arial",8 ," bold italic"))
lb3.config(padx=10,pady=5)
lb3.place(x=115,y=315)
lb4=Label(bg="yellow",font=( "arial",8 ," bold italic"))
lb4.config(padx=10,pady=5)
lb4.place(x=115,y=315)
lb5=Label(bg="yellow",font=( "arial",8 ," bold italic"))
lb5.config(padx=10,pady=5)
lb5.place(x=115,y=315)




en=Entry(width=20)
en.place(x=200,y=92)
en1=Entry(width=20)
en1.place(x=200,y=222)
#en2=Entry(width=20)
#en2.place(x=200,y=325)

but=Button(text="Hesapla",command=hesap1,bg="red")
but.place(x=150,y=270)






wn.mainloop()