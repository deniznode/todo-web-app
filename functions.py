FILEPATH = 'todos.txt'


def get_todos(filepath = FILEPATH):
    """Read the todos from storage"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def update_todos(todos, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)
