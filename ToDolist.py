class TodoItem:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(TodoItem(task))
        print(f"Task '{task}' added to the list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task.completed else "Pending"
                print(f"{i}. {task.task} ({status})")

    def mark_as_completed(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].completed = True
            print(f"Task '{self.tasks[index - 1].task}' marked as completed.")
        else:
            print("Invalid index.")

    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task '{removed_task.task}' removed.")
        else:
            print("Invalid index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_as_completed(index)
        elif choice == '4':
            index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(index)
        elif choice == '5':
            print("Exiting the To-Do List app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()