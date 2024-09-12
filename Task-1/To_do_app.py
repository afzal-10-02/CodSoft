from tkinter import * 
from tkinter import messagebox
from sqlite3 import *

def main():

    # Create the main window
    global root
    root = Tk()
    root.geometry('510x675')
    root.minsize(510, 675)
    root.title("To-Do Application")
    root.iconbitmap('codesoft.ico')

    #frame for the content
    global frame
    frame = Frame(root)
    frame.pack()

    # #enter task label.
    label_enter = Label(frame, text='Enter your task...', font=("Georgia", 14, 'italic'))

    #task entry box.
    global task_box
    task_box = Entry(frame, width=30, borderwidth=1, relief='solid', font=("Georgia", 14))


    global label
    label =Label(frame, text='To Do', font=("Georgia", 16, 'bold'))

    
    #list of tasks
    global task_list
    task_list = Listbox(frame, width=45, height=25, border=0, font=('Georgia', 12), selectforeground='black')
    todo_task(task_list)    #showing all the data from the database to the list_box

    #frame for task,completed and done button
    frame1 = Frame(frame)
    #frame for the clear and delete button
    frame2 = Frame(frame)
    
    #buttons
    add_button = Button(frame, text='Add', relief="solid", padx=10, borderwidth=2, font=('Times New Roman', 12, 'bold'), command=add_task)
    delete_button = Button(frame2, text='Delete', relief="solid", padx=5, borderwidth=2, font=('Times New Roman', 12, 'bold'), command=delete_task)
    clear_button = Button(frame2, text='Reset', relief="solid", padx=5, borderwidth=2, font=('Times New Roman', 12, 'bold'), command=clear_task)
    done_button = Button(frame1, text='Done', relief="solid", padx=5, borderwidth=2, font=('Times New Roman', 12, 'bold'), command=complete_task)
    completed_button = Button(frame1, text='Completed', relief="solid", padx=5, borderwidth=2, font=('Times New Roman', 12, 'bold'), command=completed_task)
    task_button = Button(frame1, text='Tasks', relief="solid", padx=5, borderwidth=2, font=('Times New Roman', 12, 'bold'), command=to_dotask)

    #placing the content of the frame
    label_enter.grid(column=0, row=0)
    task_box.grid(column=0 , row=1 )
    add_button.grid(column=1, row=1 )
    label.grid(column=0, row=2, columnspan=2)
    task_list.grid(column=0, row=3, padx=14, pady=10, columnspan=2)
    frame1.grid(column=0 , row=4, columnspan=2, pady=2)
    frame2.grid(column=0 , row=5, columnspan=2, pady=2)


    done_button.grid(column=0, row=0, padx= 0)  
    completed_button.grid(column=2, row=0, padx=0)
    task_button.grid(column=1 , row=0, padx= 40)

    delete_button.grid(column=0 , row=0)
    clear_button.grid(column=1 , row= 0, padx=40)

    root.bind('<Key>', on_key_press)
    
    #GUI loop
    root.mainloop()

#add task Functions:
def add_task():
    task = task_box.get().strip()

    #checking the task it is neither empty or nor already in the table 
    if task in task_list.get(0, END):  
        messagebox.showerror("warning" , 'Task already exits.')
    elif task != '':    
        task_list.insert(END, task)
        task_box.delete(0, END)
        query = 'insert into task_table(task) values (?)'
        update_db(query , task)

#delete task function
def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        data = task_list.get(selected_task_index)
        task_list.delete(selected_task_index)
        query = 'Delete from task_table where task = ?'
        update_db(query  , data)

    except:
        messagebox.showerror("Warning", "Select your task.")

#complete the task
def complete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        data = task_list.get(selected_task_index)
        task_list.delete(selected_task_index)
        query = 'UPDATE task_table SET status = 1 WHERE task = ?'
        update_db(query  , data)
    except:
        messagebox.showerror("Warning", "Select your task.")

#completed task function
def completed_task():
    label.config(text='Completed Task')
    task_list.delete(0 , END)
    task_c = c.execute('select task from task_table where status =1')
    for task in task_c:
        task_s = ''.join(map(str , task))
        task_list.insert(END , task_s)
    conn.commit()

#to_dotask
def to_dotask():
    label.config(text='To Do')
    task_list.delete(0 , END)
    task_c = c.execute('select task from task_table where status is NULL')
    for task in task_c:
        task_s = ''.join(map(str , task))
        task_list.insert(END , task_s)
    conn.commit()

#clear task function  
def clear_task():
    confirm = messagebox.askyesno("confirmation" , '''Clicking yes will clear all your completed task and uncompleted task.
This action cannot be undone. Are you sure you want to proceed?''')
    if confirm:
        task_list.delete(0, END)
        query = 'delete from task_table'
        update_db(query ,None)
    
#Print the task from the database.
def todo_task(task_list):
    tasks_l = c.execute('select task from task_table where status is NULL')
    for task in tasks_l:
        task_s = ''.join(map(str , task))
        task_list.insert(END , task_s)
    conn.commit()

#executing the query and uploading it to the database
def update_db(query , data):
    if data == None:
        c.execute(query)
    else:
        c.execute(query , [data])
    conn.commit()

#staring the connection to the database
def start_conn():
    global conn
    global c
    conn = connect("to_do.db")
    c = conn.cursor()

#onkeyboard press
def on_key_press(event):
    if event.keysym == 'Return':
        add_task()
    elif event.keysym == 'Delete':
        delete_task()

if __name__ == "__main__":
    start_conn()
    main()
    conn.close()