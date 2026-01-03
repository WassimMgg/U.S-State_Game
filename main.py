import turtle

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
answer_state = screen.textinput(title = "Guess the State", prompt = "What is another state's name?")

import pandas

screen.exitonclick()