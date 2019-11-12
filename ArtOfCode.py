from ChenFunctions import*

turtle.bgcolor("black")
bob.speed(0)
bob.color("cyan")
turtle.tracer(False)
for times in range(180):
    bob.forward(200)
    bob.right(30)
    bob.forward(20)
    bob.left(60)
    bob.forward(50)
    bob.right(30)
    bob.penup()
    bob.setposition(0, 0)
    bob.pendown()
    bob.right(2)
bob.home()

for times in range(8):
    monster("red")
    bob.left(90)

spikeFlower(10)

turtle.tracer(True)
