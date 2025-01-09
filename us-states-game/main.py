import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)

df = pd.read_csv('50_states.csv')
df_states = df.state.str.lower().to_list()

try:
    list_correct_states = pd.read_csv("list_correct_states.csv").state.str.lower().to_list()
except:
    list_correct_states = []

for state in list_correct_states:
    print_state_name = turtle.Turtle()
    print_state_name.hideturtle()
    print_state_name.penup()
    x_cor = int(df[(df.state.str.lower() == state)]['x'])
    y_cor = int(df[(df.state.str.lower() == state)]['y'])
    print_state_name.goto(x_cor, y_cor)
    print_state_name.write(state)

while len(list_correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(list_correct_states)}/50 States Correct",
                                    prompt="What's another state's name?").lower()

    if answer_state == "exit":
        break

    if answer_state in df_states:
        print("you got it!")
        df_states.remove(answer_state)
        list_correct_states.append(answer_state)
        print_state_name = turtle.Turtle()
        print_state_name.hideturtle()
        print_state_name.penup()
        x_cor = int(df[(df.state.str.lower() == answer_state)]['x'])
        y_cor = int(df[(df.state.str.lower() == answer_state)]['y'])
        print_state_name.goto(x_cor,y_cor)
        print_state_name.write(answer_state)

    pd.DataFrame(df_states, columns=["state"]).to_csv("missing_states.csv")
    pd.DataFrame(list_correct_states, columns=["state"]).to_csv("list_correct_states.csv")

