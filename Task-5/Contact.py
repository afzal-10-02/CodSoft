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

    contact_canvas = tk.Canvas(root, height=370, width=300, bg='white', highlightthickness=2,highlightbackground='black')
    contact_canvas.pack_propagate(False)
    contact_canvas.pack(padx=5)
    my_scrollbar = tk.Scrollbar(contact_canvas, orient="vertical", command=contact_canvas.yview)
    my_scrollbar.pack(side='right', fill='y', padx=2, pady=2)
    contact_canvas.configure(yscrollcommand=my_scrollbar.set)
    contact_frame = tk.Frame(contact_canvas, bg="white", padx=5, pady=10)
    contact_canvas.bind("<Configure>", lambda e: contact_canvas.configure(scrollregion=contact_canvas.bbox("all")))
    contact_canvas.create_window((0, 10), window=contact_frame, anchor="nw")


    for i in range(10):
        create_contact_frame(contact_frame,f'Afzal{i}', '8092155146', 'afzalj_jamal@srmus.edu.in', 'gangtok')

    

    
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


def create_contact_frame(parent, name, phone_number, email, address):
    contact_frame = tk.Frame(parent, bd=2, relief="solid", padx=10, pady=10)
    contact_frame.pack(pady=5, padx=10)

    label_name = tk.Label(contact_frame, text=f"{name}", font=("Arial", 12, "bold"))
    label_name.grid(row=0, column=0, sticky="w", padx=5)

    label_phone = tk.Label(contact_frame, text=f"Phone: {phone_number}", font=("Arial", 10))
    label_phone.grid(row=1, column=0, sticky="w", padx=5)

    label_email = tk.Label(contact_frame, text=f"Email: {email}", font=("Arial", 10))
    label_email.grid(row=2, column=0, sticky="w", padx=5)

    label_address = tk.Label(contact_frame, text=f"Address: {address}", font=("Arial", 10))
    label_address.grid(row=3, column=0, sticky="w", padx=5)


def add_contact(name, phone, email, address):
    pass



if __name__ == '__main__':
    conn = sqlite3.connect('contact_database.db')
    cursor = conn.cursor()
    main()
    conn.close()