def task():
    tasks = [] #empty list
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    
    total_task = int(input("Enter how many task you want to add = "))
    for i in range (1,total_task+1):
        task_name = input(f"Enter task {i} = ")#enter
        tasks.append(task_name)
    
    print(f"Today's tasks are\n{tasks}")
    while True:
        operation = int(input("ENTER\n 1-ADD\n 2-UPDATE\n 3-DELETE\n 4-VIEW\n 5-EXIT/STOP"))
        if operation == 1:
            ADD = input("Enter a additionaly task u want to add = ")
            tasks.append(ADD)
            print(f"Task {ADD} has been successfully added...")

        elif operation == 2:
            update_val = input("Enter the task name you want to update = ")
            if update_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"update task {up}")

        elif operation == 3:
            delete_val = input("Which task you want to delete = ")
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f" Task {delete_val} has been deleted...")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print(" Closing the program...")
            break
        else:
            print("INVALID INPUT")
            
task()
