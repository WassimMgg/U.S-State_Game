import turtle
import pandas

# -------------------- Screen setup --------------------

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# -------------------- Data --------------------

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
num_of_correct_guesses = 0

# -------------------- state turtle --------------------
state = turtle.Turtle()
state.hideturtle()
state.penup()

# -------------------- Create Guess_state function  --------------------
def guess_state(answer_state, num_of_correct_guesses, all_states, data, guessed_states):
        
    if answer_state.title() in all_states:
        if answer_state.title() not in guessed_states:
            guessed_states.append(answer_state.title())
            num_of_correct_guesses += 1
            state_data = data[data.state == answer_state.title()]
            state.goto(int(state_data.x), int(state_data.y))
            state.write(answer_state.title())
            
    return num_of_correct_guesses

# -------------------- Game loop --------------------

game_is_on = True
while game_is_on:
    if num_of_correct_guesses == 50:
        game_is_on = False
        
    answer_state = screen.textinput(title = f"{num_of_correct_guesses}/50 correct states", prompt = "What is another state's name ?")
    
    if answer_state.lower() == "exit":
        game_is_on = False
        break
    
         
    num_of_correct_guesses = guess_state(answer_state, num_of_correct_guesses, all_states, data, guessed_states)
        
        
# -------------------- End --------------------
screen.exitonclick()