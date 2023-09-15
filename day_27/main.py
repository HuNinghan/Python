import tkinter
from tkinter import *
import turtle

# Open window

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)



#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()



# Turtle

# tim = turtle.Turtle()
# tim.write("Some text", font=("Times New Roman", 20, "bold"))



# Label text

my_label.config(text = "New Text")
# my_label["text"] = "New text"

# add space around
my_label.config(padx=50, pady=50)
# adjust position
# my_label.grid(column=0, row=0)



# Button

def button_clicked():
    print("I got clicked")

    new_text = input.get()
    if len(new_text) > 0:
        my_label.config(text=new_text)
    else:
        my_label.config(text="Button Got Clicked")

button = Button(text = "Click Me", command=button_clicked)
button.pack()
# can not use grid and pack at the same time
# button.grid(column=1, row=1)


    

# Entry box

input = Entry(width=10)
input.pack()
# can not use grid and pack at the same time
# input.grid(column=2, row=2)



# Text

text = Text(height=5, width=30)
# puts cursor in textbox
text.focus()
# adds some text to begin with
text.insert(END, "Example of multi-ine text entry")
# gets current value in textbox at line 1, character 0
text.get("1.0", END)
text.pack()



# Spinbox

def spinbox_used():
    # gets the current value in spinbox
    spinbox.get()

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()



# Scale

def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()



# checkbutton

def checkbutton_used():
    checked_state.get()

# a variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()



# radio button

def radio_used():
    print(radio_state.get())

# a variable to hold on to which radio button value is checked. Only one button can be check at one time
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()



# list

def listbox_used(event):
    listbox.get(listbox.curselection())

listbox = Listbox(height=4)
fruits = ["apple", "pear", "orange", "banana"]
for item in fruits:
        listbox.insert(fruits.index(item), item)
listbox.bind("ListboxSelect", listbox_used)
listbox.pack()




# keep the windoe open

window.mainloop() 