from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MAke your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


y = -100
for index in range(6):
    y += 30
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=y)




screen.exitonclick()