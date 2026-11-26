
tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(i + 1, ".", task["task"], "-", status)

def complete_task():
    view_tasks()

    if not tasks:
        return

    num = int(input("Enter task number to complete: "))

    if 1 <= num <= len(tasks):
        tasks[num - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()

    if not tasks:
        return

    num = int(input("Enter task number to delete: "))

    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice. Please try again.")
