# Model classes
class Task:
    def _init_(self, description, status="To Do"):
        self.description = description
        self.status = status

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, index, updated_task):
        self.tasks[index] = updated_task

    def delete_task(self, index):
        del self.tasks[index]

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(task.description + "\n")

    def load_tasks(self, filename):
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]

        self.tasks = [Task(description) for description in tasks]