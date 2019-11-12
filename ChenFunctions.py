import turtle
turtle.colormode(255)
bob = turtle.Turtle()
bob.speed(0)

def spikeFlower(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 36)
    
def spike(distance):
    for times in range(20):
        c  = times * 12
        bob.color(c,c,c)
        bob.width(times*2)
        bob.forward(distance)
        bob.left(10)

def tile(c):
    polygon(4,200,c)
    for times in range(4):
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        bob.left(90)

def rowtile(c):
    for times in range(4):
        tile(c)
        bob.forward(200)
        
def polygon(sides, distance,c):
    bob.color( c )
    angle = 360 / sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance, c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
    bob.end_fill()

def explosion(distance, c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.left(135)
    bob.end_fill()

def figure1(distance,size,c):
    bob.color(c)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()

def monster(color):
    bob.color(color)
    bob.begin_fill()
    bob.left(90)
    bob.forward(100)
    bob.circle(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(135)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.left(90)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.end_fill()
    
