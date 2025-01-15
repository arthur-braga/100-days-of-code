from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

def random_word(df):
    random_row = df.sample()
    french = random_row["French"].to_string(index=False)
    english = random_row["English"].to_string(index=False)
    return french, english

def update_word():
    global french_word, english_word, flip_timer
    window.after_cancel(flip_timer)
    french, english = random_word(french_words_data)
    french_word = french
    english_word = english
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(language_title, text=french_words_data.columns[0], fill="black")
    canvas.itemconfig(word_title, text=french, fill="black")

    flip_timer = window.after(3000, change_card)

def right():
    global french_word, french_words_data
    french_words_data = french_words_data[french_words_data['French'] != french_word]
    french_words_data.to_csv("data/words_to_learn.csv", index=False)
    update_word()


def change_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(language_title, text=french_words_data.columns[1], fill="white")
    canvas.itemconfig(word_title, text=english_word, fill="white")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)

try:
    french_words_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words_original = pd.read_csv("data/french_words.csv")
    french_words_data = french_words_original.copy()
    french_words_data.to_csv("data/words_to_learn.csv", index=False)

french_word, english_word = random_word(french_words_data)

language_title = canvas.create_text(400, 150, text=f"{french_words_data.columns[0]}", font=FONT_LANGUAGE)
word_title = canvas.create_text(400, 263, text=f"{french_word}", font=FONT_WORD)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, command=right, highlightthickness=0)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, command=update_word, highlightthickness=0)
wrong_button.grid(row=1, column=0)

flip_timer = window.after(3000, change_card)

window.mainloop()
