import tkinter

wn=tkinter.Tk()
wn.title("python tkk")
wn.minsize(width=450,height=450)

def click_button():
    print(my_entry.get())
#labell
my_label=tkinter.Label(
    text="this is a label",             #    . sonrdan degistirmek istersen .config yapman yeterli...
    font=("Arial",40,"bold"),
    bg="black",
    fg="white"   
)
#my_label.pack(side="top")
#my_label.place(x=100,y=100)
my_label.grid(row=1,column=1)

#button
my_button=tkinter.Button(text="Buton",command=click_button)
#my_button.pack(side="top")
my_button.grid(row=1,column=0)
#entry
my_entry=tkinter.Entry(width=50)
#my_entry.pack(side="top")
my_entry.grid(row=0,column=2)
    







wn.mainloop()