import turtle
import math
ob=turtle.Turtle()
ob.hideturtle()
wn=turtle.Screen()
wn.bgcolor("black")
ob.pencolor("light green")
ob.speed(100)
ob.left(90)
def tree(d,ob,angle):
  if d>5:
    ob.forward(d)
    ob.right(angle)
    tree(d/math.sqrt(2),ob,angle)
    ob.left(2*angle)
    tree(d/math.sqrt(2),ob,angle)
    ob.right(angle)
    ob.backward(d)
    
tree(100,ob,20)