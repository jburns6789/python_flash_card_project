from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}
# ----------------- DATA ----------------

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    initial_data = pd.read_csv("data/french_words.csv")  # read csv file
    words_to_learn = initial_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")  # convert csv to a dictionary

# ----------------- METHODS ----------------

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(words_to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def remove_from_list():
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



    # try:
    #     remaining_words_data = pd.read_csv("data/words_to_learn.csv")
    #     remaining_words = remaining_words_data.to_dict(orient="records")
    # except FileNotFoundError:
    #     remaining_words_df = pd.DataFrame()
    #     words_remaining_to_learn = 'words_to_learn.csv'
    #     remaining_words_df.to_csv(words_remaining_to_learn, index=False)
    # else:
    #
    # words_to_learn.remove(current_card)




# ----------------- UI ------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.geometry("1000x900")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas.create_image(400, 263, image=card_front_img)
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

known = PhotoImage(file='images/right.png')
known_button = Button(image=known, bd=0, width=96, height=96, command=remove_from_list)
known_button.grid(row=3, column=1, pady=50)

unknown = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=unknown, bd=0, width=95, height=95, command=next_card)
unknown_button.grid(row=3, column=0, pady=50)

next_card()

window.mainloop()
