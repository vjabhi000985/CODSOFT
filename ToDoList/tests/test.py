import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os

class ToDoList:
	def __init__(self):
		self.root = tk.Tk()

		# Set-up the window title
		self.root.title("My To-Do List")

		# Set window geometry
		self.root.geometry("400x400")

		# Set window icon
		# try:
		# 	icon_path = os.path.join(os.path.dirname(__file__),"icons","icon.ico")
		# 	self.root.iconbitmap(icon_path)
		# except tk.TclError:
		# 	print("Icon file not found")

		self.create_widgets() 

	def create_widgets(self):
		self.task_input = tk.Entry(self.root, width=30)
		self.task_input.pack(pady=10)

		self.add_task_button = tk.Button(self.root, text="Add task", command=self.add_task)
		self.add_task_button.pack(pady=5)

		self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
		self.task_listbox.pack(pady=5)

		self.button_frame = tk.Frame(self.root)
		self.button_frame.pack(pady=5)

		self.edit_task_button = tk.Button(self.button_frame, text="Edit task", command=self.edit_task)
		self.edit_task_button.pack(padx=5)

		self.delete_task_button = tk.Button(self.button_frame, text="Delete task", command=self.delete_task)
		self.delete_task_button.pack(padx=5)

		self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_tasks)
		self.save_button.pack(pady=5)

		self.load_button = tk.Button(self.button_frame, text="Load", command=self.load_tasks)
		self.load_button.pack(pady=5)

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
		task_index = self.task_listbox.curselection()
		if task_index:
			self.task_listbox.delete(task_index)

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
	def run(self):
		self.root.mainloop()

# self.controller = controller

obj = ToDoList()
obj.run()