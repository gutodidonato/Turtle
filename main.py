from turtle import *
import random

colors = ["red", "blue", "green", "purple", "orange", "gray"]
timot = Turtle()
screen = Screen()
screen.colormode(255)



def limite_de_cores():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    random_color = (r,g,b)
    print(random_color)
    return random_color

timot.shape(name="circle")

def triangulo():
    timot.color(random.choice(colors))
    for i in range (3):
        timot.forward(100)
        timot.right(120)
        
def square():
    timot.color(random.choice(colors))
    for i in range (4):
        timot.forward(100)
        timot.right(90)

def pentagon():
    timot.color(random.choice(colors))
    for i in range (5):
        timot.forward(100)
        timot.right(72)
        
def hexagon():
    timot.color(random.choice(colors))
    for i in range (6):
        timot.forward(100)
        timot.right(60)
        

def dashed_line():
    for b in range(15):
        timot.forward(10)
        timot.color("white")
        timot.forward(10)
        timot.color("black")
        


def random_walk(walks):
    moves = [0,90,180,270]
    timot.pensize(15)
    timot.speed("fastest")
    for i in range(walks):
        timot.color(limite_de_cores())
        timot.right(random.choice(moves))
        timot.forward(50)
        
def spirograph():
    timot.speed("fastest")
    for i in range(100):
        timot.color(limite_de_cores())
        timot.circle(100)
        timot.left(5)    

spirograph()


screen.exitonclick()