import tkinter as tk
from tkinter import messagebox
import sqlite3


def main():
    root = tk.Tk()
    root.title("Contact Management System")
    root.geometry('400x600')
    root.minsize(width=400,height=600)
    root.maxsize(width=600, height=800)

    global search_box
    search_box = tk.Entry(root, width=35, borderwidth=0)
    search_box.insert(0, "Search Contact")  
    search_box.bind('<FocusIn>', on_entry_click)  
    search_box.bind('<FocusOut>', on_focus_out)
    search_box.pack(pady=10)

    contact_frame = tk.Canvas(root, height=350, width=300, bg='white', highlightbackground="black", highlightthickness=2)
    contact_frame.pack(padx=5)

    button_frame = tk.Canvas(root, height=30, width=300)
    button_frame.pack(pady=20)

    add_button = tk.Button(button_frame, text='Add Contact')
    add_button.pack()

    delete_button = tk.Button(button_frame, text='Delete Contact')
    delete_button.pack(side=tk.BOTTOM, padx=5)

    



    root.mainloop()


def on_entry_click(event):
    if search_box.get() == "Search Contact":
        search_box.delete(0, tk.END) 
        search_box.config(fg='black')  

def on_focus_out(event):
    if search_box.get() == "": 
        search_box.insert(0, "Search Contact")
        search_box.config(fg='grey')


if __name__ == '__main__':
    main()