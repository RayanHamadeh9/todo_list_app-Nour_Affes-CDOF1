class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return

        print("\nYour to-do list:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} [{status}]")

    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task deleted: {removed_task['task']}")
        else:
            print("Invalid task number.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                todo_list.mark_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()