# import necessary modules to build the analogue clock

import turtle
import time
# create the canvas
turtle.Screen()
turtle.bgcolor("#00000f")
turtle.setup(width=800,height=600)
turtle.title("የግድግዳ ሰአት")
turtle.tracer(0)

# create a drawing pen for lines,numbers and clock hands
ብእር = turtle.Turtle()
ብእር.hideturtle()
ብእር.speed(0)
# draw the frame of the clock
turtle.up()
turtle.goto(0,240)
turtle.setheading(180)
turtle.color('#0000ff')
turtle.down()
turtle.pensize(8)
turtle.circle(240)

# define a function that adds lines,numbers and clock hands in the frame
def ሳል_ሰአት(ሰአት,ደቂቃ,ሰከንድ,ብእር):
    # draw lines for the hours
    ብእር.penup()
    ብእር.goto(0,0)
    ብእር.setheading(90)
    for ቆጣሪ in range(12):
        ብእር.forward(205)
        ብእር.pendown()
        ብእር.color("#006400")
        ብእር.pensize(5)
        ብእር.forward(25)
        ብእር.penup()
        ብእር.goto(0,0)
        ብእር.right(30)

    # draw lines for the minutes and seconds
    ብእር.penup()
    ብእር.goto(0, 0)
    ብእር.setheading(90)
    for ቆጣሪ in range(60):
        ብእር.forward(220)
        ብእር.pendown()
        ብእር.color("#006400")
        ብእር.pensize(3)
        ብእር.forward(15)
        ብእር.penup()
        ብእር.goto(0, 0)
        ብእር.right(6)

    # draw the hour hand
    ብእር.penup()
    ብእር.goto(0,0)
    ብእር.color('#008000')
    ብእር.setheading(90)
    angle= (ሰአት/12)*360
    ብእር.right(angle)
    ብእር.pendown()
    ብእር.pensize(7)
    ብእር.forward(90)

    # draw the minute hand
    ብእር.penup()
    ብእር.goto(0, 0)
    ብእር.color('#ffff00')
    ብእር.setheading(90)
    angle = ( ደቂቃ/ 60) * 360
    ብእር.right(angle)
    ብእር.pendown()
    ብእር.pensize(5)
    ብእር.forward(155)

    # draw the second hand
    ብእር.penup()
    ብእር.goto(0, 0)
    ብእር.color('#ff0000')
    ብእር.setheading(90)
    angle = (ሰከንድ / 60) * 360
    ብእር.right(angle)
    ብእር.pendown()
    ብእር.pensize(2)
    ብእር.forward(185)

    # draw the numbers on the clock
    # draw number 3
    ብእር.up()
    ብእር.hideturtle()
    ብእር.goto(180,-25)
    ብእር.color("#FFD700")
    ብእር.write(3,align="left",font=("Cambria",30,"normal"))

    # draw number 6
    ብእር.up()
    ብእር.hideturtle()
    ብእር.goto(0, -205)
    ብእር.write(6, align="center", font=("Cambria", 30, "normal"))
    # draw number 9
    ብእር.up()
    ብእር.hideturtle()
    ብእር.goto(-175, -25)
    ብእር.write(9, align="right", font=("Cambria", 30, "normal"))
    # draw number 12
    ብእር.up()
    ብእር.hideturtle()
    ብእር.goto(0, 160)
    ብእር.write(12, align="center", font=("Cambria", 30, "normal"))

    # draw the vertex of the clock hands
    ብእር.penup()
    ብእር.goto(20,-20)
    ብእር.setheading(90)
    ብእር.forward(20)
    ብእር.pendown()
    ብእር.color("#c0c0c0")
    ብእር.begin_fill()
    ብእር.circle(20)
    ብእር.end_fill()
    ብእር.penup()
    ብእር.goto(-3,-8)
    ብእር.pencolor("black")
    ብእር.write("ኢ",font=("arial",14))

    # write name and UGR
    ብእር.penup()
    ብእር.goto(210,230)
    ብእር.color("#FFD700")
    ብእር.write("made by:Abe",font=("Cambria",16))

while 1:
    ሰአት = int(time.strftime("%I"))
    ደቂቃ = int(time.strftime("%M"))
    ሰከንድ = int(time.strftime("%S"))
    ሳል_ሰአት( ሰአት,ደቂቃ,ሰከንድ,ብእር)
    turtle.update()
    time.sleep(1)
    ብእር.clear()
turtle.done()
