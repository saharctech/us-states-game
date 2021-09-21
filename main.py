import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# create dataframe
data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()
print(state_list)

guessed_state = []

while len(guessed_state) < 51:

    answer_state = screen.textinput(title=f"Guess the state {len(guessed_state)}/50", prompt="What's another state's name?").title()

    # exit
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_state:
                missing_states.append(state)
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        state_data = data[data.state == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(answer_state, font=("Arial", 10))
        guessed_state.append(answer_state)




screen.exitonclick()