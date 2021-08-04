import turtle

board=turtle.Screen()
pen=turtle.Turtle()
pen.shape("classic")
pen.width(6)
pen.speed(10)
pen.color('red')
pen.fillcolor("green")
pen.begin_fill()
pen.right(90)
pen.stamp()
pen.forward(300)
pen.left(90)
pen.width(20)

pen.width(5)
for i in range(100,400,50):
    pen.circle(i)
    pen.circle(i+i)
pen.end_fill()
pen.penup()
pen.goto(-200,-200)
pen.pendown()
pen.forward(100)
turtle.circle(100)

pen.up()
pen.home()



turtle.done()