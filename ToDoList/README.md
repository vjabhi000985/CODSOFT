We# ToDOList Application

## Introduction
Welcome to the ToDoList application, a project developed during an internship at CODSOFT.

## Project Description
This project is a simple To-Do List application built using Python and Tkinter. The application follows the MVC (Model-View-Controller) architecture to organize the codebase efficiently.

## Tkinter and Its Components
Tkinter is a Python library for creating graphical user interfaces. In this project, Tkinter is utilized to build the application's user interface. The key components include:
- *Entry:* Widget for user input (e.g., task entry).
- *Button:* Interactive elements to trigger actions (e.g., add, edit, delete tasks).
- *Listbox:* Displaying the list of tasks.
- *Label:* Displaying the title and other labels.
- *Frame:* A container to organize and group widgets.

## MVC Architecture
The application follows the MVC architecture for better code organization:
- *Model (model/):* Defines the data structure, e.g., tasks in todo_model.py.
- *View (view/):* Manages the user interface, e.g., Tkinter-based view in todo_view.py.
- *Controller (controller/):* Handles user input and interacts with the model, e.g., todo_controller.py.

## Screenshots
![Screenshot (28)](https://github.com/vjabhi000985/CODSOFT/assets/46738718/daa20efe-48fd-41a1-a4c6-7ddd2511e402) ![Screenshot (29)](https://github.com/vjabhi000985/CODSOFT/assets/46738718/7e3fb22b-da28-4f86-8013-a5a3c3c37200)

## ToDoList(Demo) 
![90b46717-102f-422c-b218-e904ae291daf](https://github.com/vjabhi000985/CODSOFT/assets/46738718/f266f90c-a45f-46c3-8c7e-bc478b92972c)

## File Structure
The project follows a structured layout to organize its components and files. Below is an overview of the main directories and files:

- *`ToDoList/`*
  - *`controller/`*
    - *`__pycache__`* 
    - `__init__.py` 
    - `todo_controller.py` (Contains controller logic for handling data and user input)
  - *`model/`* 
    - *`__pycache__`*
    - `__init__.py`
    - `todo_model.py` (Contains model classes, representing the data structure)
  - *`tests/`*: (Directory for test code)
    - `test.py/` (Test code for testing various functionalities)
  - *`view/`*
    - *`__pycache__`*
    - *`icons/`*
      - `icon.ico` (Icon file used for the application)
    - `__init__.py`
    - `todo_view.py` (Contains Tkinter-based view for the user interface)
  - `main.py` (Entry point of your application)

## Bug in "Edit Task" Functionality
### Issue Description
There is a bug in the "Edit Task" functionality. When attempting to edit a task, we have to first delete the selected task and we can edit the field.
### Code Sample
```python
 def edit_task(self):
    	selected_indices = self.task_listbox.curselection()
    	if selected_indices:
    		selected_index = selected_indices[0]
    		selected_task = self.task_listbox.get(selected_index)

    		self.task_input.delete(0, tk.END)
    		self.task_input.insert(0, selected_task)
        # The above lines do not properly set the input field with the selected task text
        # Additional code is needed to handle this issue.
```
Feel free to contribute or provide insights on the mentioned issue!

## Technology Used
The ToDoList application is developed using the following technologies:

- *Sublime Text 4:* The text editor used for coding and project management.
- *Python:* The programming language chosen for the application's backend logic.
- *Tkinter:* The Python library utilized for creating the graphical user interface.

## Credits
Developed by *Pandey Abhishek Nath Roy [me]*
