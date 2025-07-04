to_do_list = []

def add_task(task):
    to_do_list.append(task)
    print("Task added:", task)

def view_list():
    if len(to_do_list) == 0:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

def remove_task(task_number):
    if 1 <= task_number <= len(to_do_list):
        removed_task = to_do_list.pop(task_number - 1)
        print("Task removed:", removed_task)
    else:
        print("Invalid task number. Please enter a valid task number.")

while True:
    print("\nOptions:")
    print("Enter 'add' to add a task")
    print("Enter 'view' to view your to-do list")
    print("Enter 'remove' to remove a task")
    print("Enter 'quit' to quit the program")
    
    choice = input("What would you like to do? ").lower()
    
    if choice == 'add':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == 'view':
        view_list()
    elif choice == 'remove':
        view_list()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == 'quit':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
