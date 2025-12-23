
##pip install colorgram.py##
"""
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

"""
import turtle as t
import random
tim_dot = t.Turtle()
tim_dot.speed("fastest")
tim_dot.hideturtle()
tim_dot.penup()
t.colormode(255)
colors = [
          (202, 164, 109),  (150, 75, 49), 
          (52, 93, 124),   (172, 154, 40), 
          (140, 30, 19),   (133, 163, 185), (198, 91, 71), 
          (46, 122, 86),   (72, 43, 35),    (145, 178, 148), 
          (13, 99, 71),    (233, 175, 164), (161, 142, 158), 
          (105, 74, 77),   (55, 46, 50),    (183, 205, 171), 
          (36, 60, 74),    (18, 86, 90),    (81, 148, 129), 
          (148, 17, 20),   (14, 70, 64),    (30, 68, 100), 
          (107, 127, 153), (174, 94, 97),   (176, 192, 209)
        ]
tim_dot.setheading(225)
tim_dot.forward(300)
tim_dot.setheading(0)
number_of_dots = 100

for dot_count in range (1, number_of_dots + 1):
        tim_dot.dot(20, random.choice(colors))
        tim_dot.forward(50)
        
        if dot_count %10 ==0:
            tim_dot.setheading(90)
            tim_dot.forward(50)
            tim_dot.setheading(180)
            tim_dot.forward(500)
            tim_dot.setheading(0)
    
        
    
   
    
t.exitonclick()