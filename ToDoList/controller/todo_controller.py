# Controller logic
from model.todo_model import ToDoList, Task

class ToDoController:
    def __init__(self, model: ToDoList):
        self.model = model

    def add_task(self, task: Task):
        self.model.add_task(task)

    def edit_task(self, index, updated_task: Task):
        self.model.edit_task(index, updated_task)

    def delete_task(self, index):
        self.model.delete_task(index)

    def save_tasks(self, filename):
        self.model.save_tasks(filename)

    def load_tasks(self, filename):
        self.model.load_tasks(filename)