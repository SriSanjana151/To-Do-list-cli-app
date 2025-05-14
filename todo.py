import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        f.write("\n".join(tasks))

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "3":
            view_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
