# load all my mvc architectural contents into main.py
from controller.todo_controller import ToDoController
from model.todo_model import ToDoList
from view.todo_view import ToDoView

def main():
    model = ToDoList()
    view = ToDoView(controller=ToDoController(model))
    controller = view.controller

    view.run()

if __name__ == "__main__":
	main()