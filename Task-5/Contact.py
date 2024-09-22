import tkinter as tk
from tkinter import messagebox
import sqlite3
import re


def main():
    root = tk.Tk()
    root.title("Contact Management System")
    root.geometry('400x600')
    root.minsize(width=400,height=600)
    root.maxsize(width=600, height=800)

    global search_box
    search_canvas = tk.Canvas(root, highlightthickness=0)
    search_canvas.pack(pady=15)
    search_box = tk.Entry(search_canvas, width=35, borderwidth=0)
    search_box.insert(0, "Search Contact")
    search_button = tk.Button(search_canvas, text='Search', command= lambda: show_contacts(search=search_box))
    search_box.bind('<FocusIn>', on_entry_click)  
    search_box.bind('<FocusOut>', on_focus_out)
    search_box.grid(row=0, column=0)
    search_button.grid(row=0, column=1, padx=10)

    canvas = tk.Canvas(root, height=400, width=400, highlightthickness=0)
    canvas.propagate(False)
    canvas.pack()

    global contact_frame, contact_canvas
    contact_canvas = tk.Canvas(canvas, height=400, width=300, bg='white', highlightthickness=2,highlightbackground='black',borderwidth=2)
    contact_canvas.pack_propagate(False)
    contact_canvas.pack(padx=5)

    my_scrollbar = tk.Scrollbar(contact_canvas, orient="vertical", command=contact_canvas.yview, width=20)
    my_scrollbar.pack(side='right', fill='y', padx=2, pady=2)

    contact_canvas.configure(yscrollcommand=my_scrollbar.set)
    contact_frame = tk.Frame(contact_canvas, bg="white", padx=5, pady=0)
    contact_canvas.bind("<Configure>", lambda e: contact_canvas.configure(scrollregion=contact_canvas.bbox('all')))
    contact_canvas.create_window((0, 10), window=contact_frame, anchor="nw")

    show_contacts()

    button_frame = tk.Canvas(root, height=30, width=300)
    button_frame.pack(pady=20)

    add_button = tk.Button(button_frame, text='Add Contact', command=lambda: add_contact(contact_canvas, canvas))
    add_button.pack(pady= 10)

    delete_button = tk.Button(button_frame, text='Delete Contact')
    delete_button.pack(side=tk.BOTTOM, padx=5)

    root.mainloop()

def show_contacts(add_canvas=None, search = 'afzal'):
    if add_canvas != None:
        add_canvas.pack_forget()
        contact_canvas.pack()
        contact_canvas.delete('all')
    
    cursor.execute('Select *from contacts')

    conn.commit()
    for row in cursor.fetchall():
        create_contact_frame(contact_frame,row[1], row[0], row[2], row[3])

    

def on_entry_click(event):
    if search_box.get() == "Search Contact":
        search_box.delete(0, tk.END) 
        search_box.config(fg='black')  

def on_focus_out(event):
    if search_box.get() == "": 
        search_box.insert(0, "Search Contact")
        search_box.config(fg='grey')

def create_contact_frame(parent, name, phone_number, email, address):
    contact_frame1 = tk.Frame(parent,width=250,height=110, bd=2,relief="solid", padx=10, pady=10)
    contact_frame1.grid_propagate(False)
    contact_frame1.pack(pady=5, padx=10)

    label_name = tk.Label(contact_frame1, text=f"{name}", font=("Arial", 12, "bold"))
    label_name.grid(row=0, column=0, sticky="w", padx=5)

    label_phone = tk.Label(contact_frame1, text=f"Phone: {phone_number}", font=("Arial", 10))
    label_phone.grid(row=1, column=0, sticky="w", padx=5)

    label_email = tk.Label(contact_frame1, text=f"Email: {email}", font=("Arial", 10))
    label_email.grid(row=2, column=0, sticky="w", padx=5)

    label_address = tk.Label(contact_frame1, text=f"Address: {address}", font=("Arial", 10))
    label_address.grid(row=3, column=0, sticky="w", padx=5)

def add_contact(contact_canvas, canvas):
    contact_canvas.pack_forget()

    add_canvas = tk.Canvas(canvas, height= 200,width=350, background='white')
    add_canvas.pack(pady=40)

    tk.Label(add_canvas, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    name_entry = tk.Entry(add_canvas, width=30, borderwidth=1, relief="solid")
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(add_canvas, text="Phone Number:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    phone_entry = tk.Entry(add_canvas, width=30, borderwidth=1, relief="solid")
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(add_canvas, text="Address:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    address_entry = tk.Entry(add_canvas, width=30, borderwidth=1, relief="solid")
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(add_canvas, text="Email:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    email_entry = tk.Entry(add_canvas, width=30, borderwidth=1, relief="solid")
    email_entry.grid(row=3, column=1, padx=5, pady=5)


    submit_button = tk.Button(add_canvas, text="Submit", command=lambda: add_information(name_entry, phone_entry, email_entry, address_entry, contact_canvas, add_canvas))
    submit_button.grid(row=4, columnspan=2,padx= 10, pady=10)

    see_button = tk.Button(add_canvas, text="Contacts", command=lambda: show_contacts(add_canvas))
    see_button.grid(row=4,column=1, columnspan=2, padx=10, pady=10)
  
def add_information(name , phone , email, add, contact_canvas, add_canvas):
    if phone.get and name.get():
        cursor.execute('''
        Insert into contacts(phone, name, email, address) Values (?,?,?,?)
        ''' , (phone.get(), name.get(), email.get(), add.get()))
        conn.commit()
    else:
        messagebox.showerror("Error", "Name and Phone number can not be empty!!")

if __name__ == '__main__':
    global conn, cursor
    conn = sqlite3.connect('contact_database.db')
    cursor = conn.cursor()
    main()
    conn.close()