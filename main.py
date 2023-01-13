import tkinter
import pandas
import random
data_for_learn = {}


BACKGROUND_COLOR = "#B1DDC6"
random_num = 0
#-------------------------Data-----------------------------#

try:
    data = pandas.read_csv("/Users/programing/Desktop/programing/flash-card-project-start/word_for_learn.csv")
    data_dict = data.to_dict(orient="records")
except:
    data = pandas.read_csv("/Users/programing/Desktop/programing/flash-card-project-start/data/french_words.csv")
    data_dict = data.to_dict(orient="records")
finally:
    print(len(data_dict)) 


#-------------------------Button Commands-----------------------------#


def next_function():
    global random_num
    random_num = random.randint(0, len(data_dict) - 1)
    canvas.itemconfig(canvas1, text = "French", fill = "black")
    canvas.itemconfig(canvas2, text = data_dict[random_num]["French"], fill = "black")
    canvas.itemconfig(canvas_img, image = img)
    window.after(3000,func = change_language)
    
def change_language():
    global random_num
    canvas.itemconfig(canvas1, text = "English", fill = "white")
    canvas.itemconfig(canvas2, text = data_dict[random_num]["English"], fill = "white")
    canvas.itemconfig(canvas_img, image = img2)

def know_word():
    global random_num, data_for_learn   

    data_dict.remove(data_dict[random_num])
    print(data_for_learn)
    data_for_learn = pandas.DataFrame(data_dict)
    data_for_learn.to_csv("word_for_learn.csv", index = False)
    next_function()
    




#--------------------------Display-------------------------#
window = tkinter.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.title("Learn French")
canvas = tkinter.Canvas(height=526,width=800)
img = tkinter.PhotoImage(file='/Users/programing/Desktop/programing/flash-card-project-start/images/card_front.png')
img2 = tkinter.PhotoImage(file='/Users/programing/Desktop/programing/flash-card-project-start/images/card_back.png')
#canvas
canvas_img = canvas.create_image(400, 263, image = img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas1 = canvas.create_text(400,150,text="Title", font=("ariel",40,"italic"))
canvas2 = canvas.create_text(400,263,text="Word", font=("ariel",60,"bold"))

canvas.grid(column=0,row=0,columnspan=2)

#button
cross = tkinter.PhotoImage(file="/Users/programing/Desktop/programing/flash-card-project-start/images/wrong.png")
unknow_but = tkinter.Button(image=cross, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_function)
unknow_but.grid(column = 0,row = 1)

check = tkinter.PhotoImage(file="/Users/programing/Desktop/programing/flash-card-project-start/images/right.png")
know_but = tkinter.Button(image=check, bg=BACKGROUND_COLOR, highlightthickness=0, command= know_word)
know_but.grid(column = 1,row = 1)
  


next_function()


window.mainloop()