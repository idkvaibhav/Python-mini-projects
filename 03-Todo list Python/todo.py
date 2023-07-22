def display_menu():
    """Display the to-do list menu."""
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    """Add a new task to the to-do list."""
    task = input("Enter the task description: ")
    todo_list.append(task)
    print("Task added successfully!")

def view_tasks():
    """View all tasks in the to-do list."""
    print("To-Do List:")
    for index, task in enumerate(todo_list, 1):
        print(f"{index}. {task}")

def delete_task():
    """Delete a task from the to-do list."""
    view_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            del todo_list[index]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def exit_program():
    """Exit the program."""
    print("Exiting program. Goodbye!")
    # You can also save the to-do list to a file here if you want.

todo_list = []

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        exit_program()
        break
    else:
        print("Invalid choice. Please choose a valid option (1-4).")
