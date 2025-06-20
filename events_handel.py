import tkinter as tk
from tkinter import ttk as ttk
window = tk.Tk()
window.title('Events Handeling')
window.geometry('500x300')
Text = tk.Text(master=window, width=30, height=10)
Text.pack()

entry = ttk.Entry(master=window, width=30)
entry.pack()

btn = ttk.Button(master=window, text='Button')
btn.pack()

#adding a event to it that will capture the text in the text area
#window.bind('<Button-1>', lambda event: print('Left click at', event.x, event.y))
#this will capture the text in the entry field
#Text.bind('<Motion>', lambda event: print('Mouse moved to', event.x, event.y))
# debending on what you bind to the event you can get different information or effects
#btn.bind('<FocusIn>', lambda event: print('Button focused'))
#exercise: print 'Mouse wheel' when the user hold shift and scroll the mouse on the text area
Text.bind('<Shift-MouseWheel>', lambda event: print(f'Mouse wheel scrolled with shift held down at {event.x} {event.y}'))

window.mainloop()

