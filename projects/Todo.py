import os

FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from file into a list."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    """Save the list of tasks back to file."""
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    """Print all tasks with numbers."""
    if not tasks:
        print("\nNo tasks yet!")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()