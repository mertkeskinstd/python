from tkinter import *

wn=Tk()
wn.title("hojgeldinzzzz")
wn.minsize(width=600,height=600)
wn.config(padx=20,pady=20)
def buton_click():
    
    print( text.get("1.0",END))     #1 LİNE DEMEK O KAREKTER DEMEK....
    
    
    
label1=Label(text="murs3l",bg="blue",fg="white",font=("Arial",50,"bold italic"))
label1.config(padx=20,pady=20)
label1.pack()
buton1=Button(text="bascan",command=buton_click,bg="purple",font=("arial",10,"italic"))
buton1.pack()
#entry
entry=Entry(width=20,bg="black",fg="white")
entry.pack()
#multiline
text=Text(width=30)
text.focus()
text.pack()
#scale

def bu(x):
    print(x)
    
my_scale=Scale(from_=0,to=50,command=bu)
my_scale.pack()

#spin box
def sp():
    print(my_spinbox.get())
    
my_spinbox=Spinbox(from_=0,to=50,command=sp )

my_spinbox.pack()
#checkbutton
def ck():
    print(check_status.get())
    

check_status=IntVar()

check=Checkbutton(text="check",variable=check_status,command=ck)
check.pack()
#radio button
def radio_selected():
    print(radio_state.get())
radio_state=IntVar()
my_radio_button=Radiobutton(text="1 option",value=10,variable=radio_state,command=(radio_selected))
my_radio_button2=Radiobutton(text=" option",value=20,variable=radio_state,command=(radio_selected))
my_radio_button.pack()
my_radio_button2.pack()
#listbox
def slect(event):
    print(lb.get(lb.curselection()))

lb=Listbox()
isim=["murs","fewef","fgs","gdgd","erfge","fdfsgde"]
for i in range(len(isim)):
    lb.insert(i,isim[i])
lb.bind('<<ListboxSelect>>',slect)
lb.pack()
    

wn.mainloop()