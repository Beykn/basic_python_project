from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    color = (r,g,b)
    
    return color

def draw_spirograph(size_of_graph):
    for _ in range(int(360/size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_graph)
        
draw_spirograph(10)
screen.exitonclick()

        