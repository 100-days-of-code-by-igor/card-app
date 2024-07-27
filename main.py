import csv
from tkinter import *
from random import *
from csv import *
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

#load data

try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


# functions
def remove_word():
    to_learn.remove(current_card)
    words_to_learn = DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv",index=False)
    change_word()


def change_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(image_id, image=front_image)
    canvas.itemconfig(title_id,text="French",fill="black")
    canvas.itemconfig(word_id,text=current_card["French"],fill="black")
    flip_timer= window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_id, text="English")
    canvas.itemconfig(word_id,text=current_card["English"],fill="white")
    canvas.itemconfig(image_id,image=back_image)

#UI----------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)
#images
back_image = PhotoImage(file="images\\card_back.png")
front_image = PhotoImage(file="images\\card_front.png")
right_image = PhotoImage(file="images\\right.png")
wrong_image = PhotoImage(file="images\\wrong.png")

#canvas
canvas = Canvas(height=526,width=800)
image_id = canvas.create_image(400,263,image=front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title_id = canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
word_id = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
#buttons
know_button = Button(image=right_image,highlightthickness=0,command=remove_word)
know_button.grid(row=1,column=0)
unknown_button = Button(image=wrong_image,highlightthickness=0,command=change_word)
unknown_button.grid(row=1,column=1)



#set initial word
change_word()

window.mainloop()