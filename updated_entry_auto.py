import tkinter as tk 
from tkinter import ttk as ttk
#function that get the entry 
def outer_button_print(paramater=None):
    def inner_button_print():
        print(string_var.get())
    return inner_button_print
    
    
# this will incheck the radio button through the checkbutton
def check_button():
    if check_var.get():
       radio_var.set('-1') # uncheck the radio button
def uncheck_button():
    if radio_var.get() != '-1':
        check_var.set(False)  # uncheck the checkbutton if a radio button is selected
    
    
#creating windows or root 
window = tk.Tk()
window.title('Tiknter Variables')
window.geometry("500x300")
#creating string var to connect the entry to label through the shared var
string_var=tk.StringVar()
#creating label
label = ttk.Label(master=window,text='Hello', textvariable=string_var)
label.pack()
#creating entry area
entry =  ttk.Entry(master=window,textvariable=string_var)
entry.pack()
#adding a button to it 
button =ttk.Button(master=window,text='Button',command=outer_button_print(string_var))
button.pack()
radio_var= tk.StringVar()
#checkbutton 
check_var = tk.BooleanVar()
check_btn =  ttk.Checkbutton(master=window,text='Check Button',command=check_button,variable=check_var)
check_btn.pack()
#radiobuttons

radio_btn1 = ttk.Radiobutton(master=window,text='A',value='1',variable=radio_var,command=uncheck_button)
radio_btn1.pack()
radio_btn2 = ttk.Radiobutton(master=window,text='B',value='2',variable=radio_var,command=uncheck_button)
radio_btn2.pack()
#run window
window.mainloop()