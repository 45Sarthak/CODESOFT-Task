import tkinter as tk
from tkinter import messagebox 
from tkinter import *

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")
        
        self.tasks = []

        self.task_entry = tk.Entry(master, width=70)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(master, width=70)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
            messagebox.showinfo("Info", f"Task '{task}' removed successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def display_tasks(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()