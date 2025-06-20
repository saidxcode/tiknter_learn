import tkinter as tk
import ttkbootstrap as ttk
#functions
def convert():
    miles = entry_number.get()
    kilometers = miles * 1.60934  # Convert miles to kilometers
    output_string.set(f"{miles} miles = {kilometers:.2f} km")
#root
#use ttkbootstrap with dark mode using new windows methode 
root = ttk.Window(themename='darkly')
root.title("My App")
root.geometry("300x200")


title_lable=ttk.Label(master=root,text='Miles to Km', font=('Arial', 22))
title_lable.pack(pady=10)
#input field
input_field=ttk.Frame(master=root)
#storing entry data
entry_number=tk.DoubleVar()
entry=ttk.Entry(master=input_field,textvariable=entry_number)
button=ttk.Button(master=input_field,command=convert,text='convert')
entry.pack(side='left')
button.pack(side='right',padx=10)
input_field.pack(pady=10)
#output field 
#adding text var for label
output_string=tk.StringVar()
output_label=ttk.Label(master=root,text='Output', font='Calibri 24',textvariable=output_string)
output_label.pack(pady=5)
#running the app
root.mainloop()