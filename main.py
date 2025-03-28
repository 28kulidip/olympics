import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")
t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-80,15)
t.setheading(0)
t.pendown()
t.pencolor("blue")
t.circle(35)
t.setheading(90)

t.penup()
t.goto(0,15)
t.setheading(0)
t.pendown()
t.pencolor("black")
t.circle(35)
t.setheading(90)

t.penup()
t.goto(80,15)
t.setheading(0)
t.pendown()
t.pencolor("red")
t.circle(35)
t.setheading(90)

t.penup()
t.goto(-40,-22)
t.setheading(0)
t.pendown()
t.pencolor("yellow")
t.circle(35)
t.setheading(90)


t.penup()
t.goto(40,-22)
t.setheading(0)
t.pendown()
t.pencolor("green")
t.circle(35)
t.setheading(90)

t.penup()
t.goto(0,120)
t.pendown()
t.pencolor("purple")
t.write("Winter Olympics",font=("Arial",25),align="center")

t.penup()
t.goto(0,-90)
t.pendown()
t.pencolor("purple")
t.write("2026",font=("Arial",25),align="center")


turtle.done()

