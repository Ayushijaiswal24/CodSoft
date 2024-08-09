class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Pending"})
        print(f"Task '{task}' added to the list.")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task
            print(f"Task {task_index + 1} updated to '{new_task}'.")
        else:
            print(f"Task {task_index + 1} not found in the list.")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["status"] = "Completed"
            print(f"Task {task_index + 1} marked as completed.")
        else:
            print(f"Task {task_index + 1} not found in the list.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' removed from the list.")
        else:
            print(f"Task {task_index + 1} not found in the list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task['task']} - {task['status']}")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. View Tasks")
    print("6. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '5':
            todo_list.view_tasks()
        elif choice == '6':
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
