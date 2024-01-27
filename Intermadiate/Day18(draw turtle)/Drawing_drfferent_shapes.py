from turtle import Turtle, Screen 
import random 

turtle1 = Turtle() 
turtle1.shape("turtle")
shapes = [3,4,5,6,7,8,9,10]
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple", "pink", "brown", "black", "gray", "cyan", "magenta"]


for numbers in shapes: 
    turtle1.color(random.choice(colours))
    for i in range(numbers):
        angles = int(360 / numbers)
        turtle1.forward(100)
        turtle1.right(angles)

