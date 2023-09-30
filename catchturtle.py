import turtle 
import math
import random
#ekran goster
wsn=turtle.Screen()
wsn.bgcolor("black")
wsn.title("Catch The Turtle")

score=0
print("\n "*40)
print("your score:\n0")

#baslik
t=turtle.Turtle()                   
t.pencolor("purple")
t.hideturtle()
t.penup()
t.setposition(-70,350)
t. write("kaplumagayi yakala",font=("Fantasy",18))

#tip
ti=turtle.Turtle()
ti.pencolor("red")
ti.hideturtle()
ti.penup()
ti.setposition(-70,-350)
ti. write("duvar kenarlarina carpma!!!",font=("Bold İtalic",18))



#draw border
kalem=turtle.Turtle()
kalem.penup()
kalem.speed(10)
kalem.hideturtle()
kalem.setposition(-10,-390)
kalem.pendown()
kalem.pensize(3)  
for side in range(4):
    kalem.pencolor("yellow")
    kalem.forward(395)
    kalem.pencolor("white")
    kalem.left(90)
    kalem.forward(395)
    
#player
pl=turtle.Turtle()
pl.pencolor("orange")
pl.shape("arrow")
pl.penup()
pl.speed(0)
#tosbik
tt=turtle.Turtle()
tt.pencolor("brown")
tt.shape(   "turtle")
tt.penup()
tt.speed(0)
tt.setposition(50,0)


speed=1

def leftt():
    pl.left(30)
def rightt():
    pl.right(30)
def hiz():
    global speed
    speed +=0.5
def fren():
    global speed
    speed-=1
turtle.listen()
turtle.onkey(fun=leftt,key="Left")
turtle.onkey(fun=rightt,key="Right")
turtle.onkey(fun=hiz,key="Up")
turtle.onkey(fun=fren,key="Down")

while True:
    #duvara carpasa(boundary check)
    pl.forward(speed)
    if pl.xcor()<-405 or pl.xcor()>385:
        print("siktir git")
        quit()
    if pl.ycor()<-390 or pl.ycor()>390:
        print("siktir git")
        quit()
    #catch turtle
    d= math.sqrt(math.pow(pl.xcor()-tt.xcor(),2) + math.pow(pl.ycor()-tt.ycor(),2))
    if d < 20 :
        tt.setposition(random.randint(-300,300), random.randint(-300, 300))
        score +=1
        print("/n"*40)
        print(f"Your Score : {score}")
    
    






    
