#To-Do List

tasks=[]

while True:
    print("To-Do List:\n1.View Tasks\n2.Add Task\n3.Mark Task as Done\n4.Delete Task\n5.Exit")
    ch=input("Enter your choice: ")
    if ch=='1':
        if len(tasks)==0:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                if task['done']:
                    status = "Done"
                else:
                    status = "Not Done"
                print(f"{i}. {task['name']} - {status}")
    elif ch=='2':
        task_name = input("Enter the task name: ")
        tasks.append({'name': task_name, 'done': False})
        print(f"Task '{task_name}' added.")
    elif ch=='3':
        if len(tasks) == 0:
            print("No tasks available to mark as done.")
        else:
            task_num = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]['done'] = True
                print(f"Task '{tasks[task_num]['name']}' marked as done.")
            else:
                print("Invalid task number.")
    elif ch=='4':
        if len(tasks) == 0:
            print("No tasks available to delete.")
        else:
            task_num = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                deleted_task = tasks.pop(task_num)
                print(f"Task '{deleted_task['name']}' deleted.")
            else:
                print("Invalid task number.")
    elif ch=='5':
        print("Exited")
        break
    else:
        print("Invalid choice. Please try again.")
    print() 
    