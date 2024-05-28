class Todo:
    def __init__(self, task, status="Incomplete"):
        self.task = task
        self.status = status
class TodoList:
    def __init__(self):
        self.todo=[]
    def add_task(self, task):
        self.todo.append("Task added ")
    def update_task_status(self, task_index, status):
        if 0 <= task_index < len(self.todo):
            print("Task is updated")
        else:
            print("Invalid task number")
    def display_task(self):
        if self.todo:
            for index, todo in enumerate(self.todo):
                print(f"{index + 1}.[{todo.status}] {todo.task}")

   
def main():
    todo_list = TodoList()
    while True:
        print("\nTo_Do List Applications")
        print("1. Add Task")
        print("2. Update Task Status")
        print("3. DisplayTask")
        print("4. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            task=input("Enter the task:")
            todo_list.add_task(task)
            print("Task is added")
        elif choice == "2":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index: ")) -1
            status = input("Enter the new status")
            todo_list.update_task_status(task_index, status)
        elif choice =="3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting.....")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()