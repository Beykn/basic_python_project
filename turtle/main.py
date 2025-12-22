from turtle import Turtle 
from turtle import Screen
import random

timmy_to_turtle = Turtle()
"""
for i in range(4):
    timmy_to_turtle.forward(100)
    timmy_to_turtle.right(90)
    
    
    ---------------------
for _ in range(15):
    timmy_to_turtle.forward(10)
    timmy_to_turtle.penup()
    timmy_to_turtle.forward(10)
    timmy_to_turtle.pendown()  
    
    
    ---------------------
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_to_turtle.forward(100)
        timmy_to_turtle.right(angle)

for shape_side_n in range(3,9):
    timmy_to_turtle.color(random.choice(colors))
    draw_shape(shape_side_n) 
    
    ---------------------
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
directions = [0, 90 , 180, 270]
timmy_to_turtle.pensize(20)
timmy_to_turtle.speed("fastest")

for _ in range(200):
    timmy_to_turtle.color(random.choice(colors))
    timmy_to_turtle.forward(20)
    timmy_to_turtle.setheading(random.choice(directions))
    
    -----------------------
    
        
"""
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy_to_turtle.pensize(20)
directions = [0, 90 ,180, 270]
timmy_to_turtle.speed("fastest")

for _ in range(200):
    timmy_to_turtle.color(random_color())
    timmy_to_turtle.forward(20)
    timmy_to_turtle.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()