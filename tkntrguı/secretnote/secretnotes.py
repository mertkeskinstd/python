from tkinter import *
import base64
from tkinter import messagebox
from PIL import ImageTk, Image


#gorun
wn=Tk()
wn.title("Secret Notes")
wn.minsize(width=500,height=800)
wn.configure(bg="black")
frame1 = Frame(wn, width=500, height=800, relief=SUNKEN,bg="black")
frame1.pack()
frame=Frame(wn,width=600,height=400)
frame.pack()
frame.place(anchor=N ,relx=0.5,rely=-0.0001   )
img=ImageTk.PhotoImage(Image.open("C:\\Users\\tahak\\Desktop\\piton\\modul_paket\\tkntrguı\\secretnote\\topsc.jpg"))
lb= Label(frame,image=img)
lb.pack()


mode=StringVar()
gizli=StringVar()
pasw=StringVar()
result=StringVar()


#encode cryptolamak icin... ASCII kodlarına donusturulur ve veriyi base64 sayesinde dizeye donusturur...
def encode(key,cl):
    enc=[]
    for i in range(len(cl)):
        key_ek=key[i % len(key)]
        enc_ek=chr((ord(cl[i]) +ord(key_ek))%256)
        enc.append(enc_ek)
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def decode(key,enc):
    dec=[]
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_ek=key[i%len(key)]
        dec_ek=chr((256 + ord(enc[i]) - ord(key_ek)) % 256)
        dec.append(dec_ek)
    return "".join(dec)

def reset():
    gizli.set("")
    pasw.set("")
    mode.set("")
    result.set("")

def bind():
    print(f"Your message: {en1.get()}")
    cl=en1.get()
    key=en2.get()
    m=en3.get()
    if cl=="" or key=="" or m=="":
        messagebox.showinfo(title="İnformation",message="PLEASE DON'T :)")
    else:
        if (m=="e"):
            result.set(encode(key,cl))
        else:
            result.set(decode(key,cl))

#IO.......................................................................
lb1=Label(frame1,text="MESSAGE: ",bg="red",fg="white",font=("arial",8,"bold italic"))
lb1.place(x=60,y=285)
en1=Entry(frame1,width=40,textvariable=gizli)
en1.place(x=200,y=285)
lb2=Label(frame1,text="KEY: ",bg="red",fg="white",font=("arial",8,"bold italic"),padx=30)
lb2.place(x=60,y=390)
en2=Entry(frame1,width=40,textvariable=pasw)
en2.place(x=200,y=390)
lb3=Label(frame1,text="MODE(e for encode\n d for decode):  ",bg="red",fg="white",font=("arial",8,"bold italic"))
lb3.place(x=60,y=485)
en3=Entry(frame1,width=40,textvariable=mode)
en3.place(x=200,y=485)
lb4=Label(frame1,text="THE RESULT:  ",bg="red",fg="white",font=("arial",8,"bold italic"))
lb4.place(x=60,y=590)
en4=Entry(frame1,width=40,textvariable=result)
en4.place(x=200,y=590)




#button
but1=Button(frame1,text="Show message",command=bind).place(x=60,y=650)
but2=Button(frame1,text="clear",command=reset).place(x=60,y=700)










wn.mainloop()
