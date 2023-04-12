def get_todos(filepath='todos.txt'):
    """
    The function reads the todos from given file name
    and return as list of todos
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filename='todos.txt'):
    """
    The function writes the todos list into file in given location
    :param todos_local:
    :param filename:
    :return:
    """
    with open(filename, 'w') as file_local:
        file_local.writelines(todos_local)

if __name__ == "__main__":
    print("Ashish in main")