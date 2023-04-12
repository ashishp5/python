import functions
while True:
    user_action = input("Enter use action add , show, edit, complete or exit: ").strip()
    if user_action.startswith('add'):
        todo = user_action[4:] +'\n'
        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    if user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            new_item = item.strip("\n")
            print(f"{index + 1}.{new_item}")
    if user_action.startswith('edit'):
        try:
            todos = functions.get_todos()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}.{item}")
            number = int(user_action[5:])
            index = number - 1
            new_todo = input("Enter the new todo:")
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)

        except ValueError:
            print("edit command is not valid")
            continue
        except IndexError:
            print(f"Index: {number}  provided in edit command does not exist")
            continue

    if user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            number = int(user_action[9:])
            index = number - 1
            complete_item = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            print(f"To do {complete_item} , marked as completed")
        except ValueError:
            print("complete command is not valid")
            continue
        except IndexError:
            print(f"Index: {number}  provided in complete command does not exist")
            continue

    if user_action.startswith('exit'):
        break
print("Bye!!!!")