""" 
Using the two blocks of code below, create a window that creates a folder, and creates a file with content from the window.

"""
# https://automatetheboringstuff.com/2e/chapter9/

# Using pathlib and OS to create directories and add files
from pathlib import Path
import os
print(Path.cwd())
# changes directory to github folder
os.chdir('C:/githubstuff')

# using tkinter to create a usable window
#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")

#Define a function to show a message
def myclick():
    # displayes message with chosen folder name
    message= "Your Folder " + entry.get()
    label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
    # make directory with entry.get() as the folder name
    os.makedirs('C:/githubstuff/' + entry.get())
    # switches the directory to the created one
    os.chdir('C:/githubstuff/' + entry.get())
    entry.delete(0, 'end')
    label.pack(pady=30)
    
    # displayes message with chosen file name
    message1= "Your File " + entry1.get()
    label= Label(frame, text= message1, font= ('Times New Roman', 14, 'italic'))
    # makes a file with the inputted name and appends the .txt extention to it
    p = Path(entry1.get() + '.txt')
    entry1.delete(0, 'end')
    label.pack(pady=30)
    
    # displayes message with chosen content
    message2= "Your Content " + entry2.get()
    label= Label(frame, text= message2, font= ('Times New Roman', 14, 'italic'))
    # writes the inputted content in
    p.write_text(str(entry2.get()))
    p.read_text()
    entry2.delete(0, 'end')
    label.pack(pady=30)
    


#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an Entry widget in the Frame
# duplicated for different entries
entry = ttk.Entry(frame, width= 40)
entry.insert(INSERT, "Enter Your Folder Name")
entry.pack()
entry1 = ttk.Entry(frame, width= 40)
entry1.insert(INSERT, "Enter Your File Name")
entry1.pack()
entry2 = ttk.Entry(frame, width= 40)
entry2.insert(INSERT, "Enter Your File Content")
entry2.pack()


#Create a Button
ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
win.mainloop()