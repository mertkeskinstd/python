import turtle

ws=turtle.Screen()
ws.bgcolor("light blue")
ws.title("metingotten")

t=turtle.Turtle()
t.color("green")

def ic_ice_kare(size):

    for i in range(40):
        t.left(90)
        t.forward(size)
        size -=5
        
    size +=100
    for i in range(40):
        t.left(90)
        t.backward(size)
        size -=5
    return i

for i in range(2):
    ic_ice_kare(300)