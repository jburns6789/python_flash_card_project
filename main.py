from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ----------------- UI ------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.geometry("1000x900")

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263,  image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

language_label = Label(window, text="Language", font=("Ariel", 40, "italic"), fg="black", bg="white")
language_label.grid(row=0, column=0, columnspan=2, padx=400, pady=150, sticky="n")

word_label = Label(window, text="Word", font=("Ariel", 60, "bold"), fg="black", bg="white")
word_label.grid(row=0, column=0, columnspan=2, pady=263, padx=400, sticky="w")

# base_canvas = Canvas(width=800, height=526)
# base_canvas.grid(column=0, row=0, columnspan=2)
#
# card_front = PhotoImage(file='images/card_front.png')
# card_back = PhotoImage(file='images/card_back.png')
#
# base_canvas.create_image(400, 263, image=card_back)
# front_canvas = base_canvas.create_image(400, 263, image=card_front)

known = PhotoImage(file='images/right.png')
known_button = Button(image=known, bd=0, width=96, height=96)
known_button.grid(row=3, column=1, pady=50)

unknown = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=unknown, bd=0, width=95, height=95)
unknown_button.grid(row=3, column=0, pady=50)

window.mainloop()