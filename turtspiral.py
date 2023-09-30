import turtle
ws=turtle.Screen()
ws.bgcolor("black")
ws.title("spiral")

t=turtle.Turtle()
t.color("white")
tc=["red","purple","blue","pink","yellow","cyan","white","brown","orange"]
turtle.speed(0)



for i in range(28):
    t.color(tc[i%9])
    t.circle(10*i)
    t.circle(-10*i)
    t.left(i)




turtle.done()


def git():
    t.forward(100)
def gitclear():
    t.clear()

def git3():
    t.left(90)
def git4():
    t.left(45)
def git5():
    t.home()

    
    

ws=turtle.Screen()
ws.bgcolor("black")
ws.title("spiral")

t=turtle.Turtle()
t.color("white")

ws.onkeypress(fun=git,key="a")
ws.onkeypress(fun=gitclear,key="c")
ws.onkeypress(fun=git4,key="w")
ws.onkeypress(fun=git3,key="s")
turtle.listen()

turtle.mainloop()
