import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("cyan")  
t.pencolor("black")  
  
a = 0  
b = 0  
t.speed(200)  
t.penup()  
t.goto(0,250)  
t.pendown()  
while(True):  
    t.forward(a)  
    t.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break  
    t.hideturtle()  
  
turtle.done()  