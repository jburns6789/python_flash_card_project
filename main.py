from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ----------------- UI ------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.geometry("1000x800")

base_canvas = Canvas(width=800, height=526)
base_canvas.grid(column=0, row=0, columnspan=2)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

base_canvas.create_image(400, 263, image=card_back)
front_canvas = base_canvas.create_image(400, 263, image=card_front)

language_label = Label(window, text="Language", font=("Ariel", 40, "italic"))
language_label.grid(row=0, column=0, columnspan=2, padx=400, pady=150, sticky="n")

word_label = Label(window, text="Word", font=("Ariel", 60, "bold"))
word_label.grid(row=0, column=0, columnspan=2, pady=263, padx=400, sticky="w")

# flash_card_front =
# flash_card_back =

right = PhotoImage(file='images/right.png')
right_button = Button(image=right, highlightthickness=0)
right_button.grid(row=3, column=1, pady=50)

wrong = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(row=3, column=0, pady=50)

window.mainloop()