import tkinter as tk
from tkinter import ttk as tkk
root = tk.Tk()
#this is a funtion to get entry text 
def get_entry():
    # not all widgets have a get method
    entry_text = entry.get()
    #print(f"Entry text: {entry_text}")
    # updating the label with entry text 
    #label.config(text=entry_text) Old
    label['text'] = entry_text  # Updated to use dictionary-style access
root.title("Simple Tkinter App")
root.geometry("300x200")
# Create a label
label = tk.Label(master=root, text="Hello, Tkinter!")
label.pack(pady=5)

# Create an entry field
entry= tkk.Entry(master=root,)
entry.pack(pady=5)
#create a button
button = tkk.Button(master=root, text="Button", command=get_entry)
button.pack(pady=5)
# creat button for label rest
button_reset = tkk.Button(master=root, text="Reset",command=lambda: label.config(text=""))
button_reset.pack(pady=5)



root.mainloop()
# This is a simple tkinter application that creates a window.