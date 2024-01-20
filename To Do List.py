class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks[task_index - 1]
            print(f"Task '{completed_task}' marked as completed.")
            self.tasks.pop(task_index - 1)
        else:
            print("Invalid task index.")



def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Display Tasks\n2. Add Task\n3. Delete Task\n4. Mark Task as Completed\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == "4":
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == "5":
            print("Exiting ToDo List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
