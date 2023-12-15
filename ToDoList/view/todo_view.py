# Tkinter-based view
import tkinter as tk
from tkinter import filedialog
import os

class ToDoView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()

        # Set window title and size 
        self.root.title("My To-Do List")
        self.root.geometry("400x400")

        # Set window color
        self.root.configure(bg="#FFFFED")

        # Set window icon
        try:
        	icon_path = os.path.join(os.path.dirname(__file__),"icons","icon.ico")
        	self.root.iconbitmap(icon_path)
        except tk.TclError:
        	print("Icon file not found")

        self.create_widgets()

    def create_widgets(self):
        self.task_input = tk.Entry(self.root, width=40)
        self.task_input.pack(pady=20)

        self.add_task_button = tk.Button(self.root, text="Add task", command=self.add_task)
        self.add_task_button.pack(pady=5)
        self.add_task_hover(self.add_task_button)
        
        # self.update_task_button = tk.Button(self.root, text="Update task", command=self.update_tasks)
        # self.update_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=5)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5)

        self.edit_task_button = tk.Button(self.button_frame, text="Edit task", command=self.edit_task)
        self.edit_task_button.pack(side=tk.LEFT,padx=5)
        self.add_hover_effect(self.edit_task_button)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete task", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT,padx=5)
        self.add_delete_hover(self.delete_task_button)

        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_tasks)
        self.save_button.pack(side=tk.LEFT,pady=5)
        self.save_load_hover(self.save_button)

        self.load_button = tk.Button(self.button_frame, text="Load", command=self.load_tasks)
        self.load_button.pack(side=tk.LEFT,pady=5)
        self.save_load_hover(self.load_button)

    # def update_tasks(self):
    # 	pass

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
    
    def edit_task(self):
    	selected_indices = self.task_listbox.curselection()
    	if selected_indices:
    		selected_index = selected_indices[0]
    		selected_task = self.task_listbox.get(selected_index)

    		self.task_input.delete(0, tk.END)
    		self.task_input.insert(0, selected_task)
			# self.task_input.delete(0, tk.END)

			# print(f'Selected task index: {task_index}')
			# new_task = self.task_input.get()
			# print(f'Selected task: {new_task}')
			# if selected_task:
			# 	for idx in selected_indices:
			# 		self.task_listbox.delete(idx)
			# 	self.task_listbox.insert(selected_index, selected_task)
			# 	self.task_input.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
        	with open(file_path, 'w') as file:
        		for task in tasks:
        			file.write(task + "\n")

    def load_tasks(self):
    	file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    	if file_path:
    		with open(file_path, 'r') as file:
    			tasks = [line.strip() for line in file.readlines()]
    		self.task_listbox.delete(0, tk.END)

    		for task in tasks:
    			self.task_listbox.insert(tk.END, task)

    def add_hover_effect(self, button):
    	# bind the hover effect
    	button.bind("<Enter>", lambda event: self.on_enter(event, button))
    	button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, widget):
    	widget.config(bg="#6af111", font=("Helvetica", 12, "bold italic"), fg="#ffffff")

    def on_leave(self, event, widget):
    	widget.config(bg="SystemButtonFace", font=("Arial", 10), fg="black")

    def add_delete_hover(self, button):
    	#bind the delete hover effect
    	button.bind("<Enter>", lambda event: self.on_delete_enter(event, button))
    	button.bind("<Leave>", lambda event: self.on_delete_leave(event, button))

    def on_delete_enter(self, event, widget):
    	widget.config(bg="#D20E0E", font=("Helvetica",12,"bold italic"), fg="#ffffff")

    def on_delete_leave(self, event, widget):
    	widget.config(bg="SystemButtonFace", font=("Arial",10), fg="black")

    def add_task_hover(self, button):
    	#bind the add task effect
    	button.bind("<Enter>", lambda e: self.on_enter_add(e, button))
    	button.bind("<Leave>", lambda e: self.on_leave_add(e, button))

    def on_enter_add(self, event, widget):
    	widget.config(bg="#40ffd7", font=("Helvetica",12,"bold italic"), fg="#ffffff")

    def on_leave_add(self, event, widget):
    	widget.config(bg="SystemButtonFace", font=("Arial",10), fg="black")

    def save_load_hover(self, button):
    	# bind the hover effect on save and load task button
    	button.bind("<Enter>", lambda e: self.save_load_enter(e, button))
    	button.bind("<Leave>", lambda e: self.save_load_leave(e, button))

    def save_load_enter(self, event, widget):
    	widget.config(bg="#40afff", font=("Helvetica", 12, "bold italic"), fg="#ffffff")

    def save_load_leave(self, event, widget):
    	widget.config(bg="SystemButtonFace", font=("Arial",10), fg="black")

    def run(self):
        self.root.mainloop()
# Rough coding
# root = tk.Tk()
# root.title("My To Do List")
# root.geometry("500x500")

# Load icon
# root.iconbitmap(icon_path)

# Set the -alpha value to 0.6
# root.attributes("-alpha", 0.6)

# Run the app's main loop
# root.mainloop()