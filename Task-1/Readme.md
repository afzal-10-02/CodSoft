# To-Do Application

This is a simple To-Do application built with Python using [Tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical user interface (GUI) 
and [SQLite3](https://docs.python.org/3/library/sqlite3.html) for data storage.

The application allows users to `Add` `delete a task` `mark as done` `view completed task`.

## *Features / Buttons*:

`Add task`:  Easily add new tasks to your to-do list.

`Delete`:  Remove the selected tasks from your list once completed or no longer needed.

`Done`:  Mark tasks as done and move them to the completed tasks section.

`completed`:  View all tasks that have been marked as completed.

`Reset`:  Clear all tasks from the list (both completed and uncompleted).


**Keyboard Shortcuts** :  Quickly add or delete tasks using keyboard shortcuts (`Enter` and `Delete` keys).

## Technologies Used
***Python:*** The core programming language used for application logic.

***Tkinter:*** Python’s standard GUI library for creating the application interface.

***SQLite:*** A lightweight, file-based database used to store tasks persistently.


## How to Use:

<mark>Add a Task:</mark>

Enter your task in the "Enter your task..." text box. 
Click the `Add Task` button or press the `Enter` key to add the task to your to-do list.



<mark>Delete a Task:</mark>

Select the task from the list.
Click the `Delete` button or press the `Delete` key to remove the selected task.

<mark>Mark a Task as Completed:</mark>

Select the task you want to mark as completed.
Click the `Done` button to mark the task as completed.

<mark>View Completed Tasks:</mark>

Click the `Completed` button to view all tasks marked as completed.

<mark>View Tasks to do:</mark>

Click the `Tasks` button to view all tasks that are not completed.

<mark>Reset All Tasks:</mark>

Click the `Reset` button to clear all tasks from the list. You will be prompted with a confirmation dialog.

## Database
The application uses SQLite as the database to store the tasks. A database file named **to_do.db** is created in the same directory as the script. The database includes a table named **task_table** with the following structure:

<mark>task:</mark> The text of the task.
<mark>status:</mark> Indicates whether the task is completed (1 for completed, NULL for not completed).


## Code Overview
***Main Window Setup:*** The main window is created using Tkinter's Tk class, and various frames, labels, buttons, and entry widgets are added to it.

***Database Functions:*** Functions such as start_conn(), update_db(query, data), and todo_task(task_list) handle the database operations using SQLite.

***Task Management Functions:*** Functions like add_task(), delete_task(), complete_task(), completed_task(), and clear_task() provide functionality for managing tasks in the to-do list.

***Keyboard Event Handling:*** The on_key_press(event) function allows users to use keyboard shortcuts to interact with the to-do list.


### Acknowledgments
- This project was developed as part of the CodSoft internship program.
