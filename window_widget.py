import tkinter as tk
from tkinter import ttk
#creating a function to be called when the button is clicked

root = tk.Tk()
#adding a title to the window
root.title("My Window")
#adding geometry to the window 
#this will set the size of the window to 500*500 pixels
root.geometry("600x700")
#creating widgets 
#there are two types of widgets tk and ttk(newer)
tk.Text(master=root).pack(padx=10,pady=10)

#ttk entry widget
entry = ttk.Entry(master=root)
entry.pack()
#adding text label between the entry area and the button
label=tk.Label(master=root,text='the world')
label.pack()
#ttk button widget
#by adding command=function_name, we can call the function when the button is clicked
button = ttk.Button(master=root,text="Click me",command=lambda:print(entry.get()))
button.pack()
#adding a checkbutton
check_var = tk.BooleanVar()
check_button = ttk.Checkbutton(
    root,
    text='check me',
    variable = check_var,
    onvalue=True,
    offvalue=False)
check_button.pack()

#creating a radio button
radio_var = tk.StringVar()
radio_button = ttk.Radiobutton(root,text='option-1',value=1,variable=radio_var)
radio_button.pack()
radio_button_2 = ttk.Radiobutton(root,text='option-2',value='s',variable=radio_var)
radio_button_2.pack()


root.mainloop()
#everying that comes after this is won't be executed until the window is closed