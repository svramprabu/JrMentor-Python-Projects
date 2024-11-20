list_of_tasks = [] #database
print('Welcome to my task manager application')
while True:
    option = input('1.Add a task'
                   '\n2.Remove a task'
                   '\n3.Search a task'
                   '\n4.Number of tasks'
                   '\n5.Print all tasks'
                   '\n6.Exit'
                   '\nChoice: ')
    if (option == '1'):
        task = input('Enter the task: ')
        if task in list_of_tasks:
            print('Task already in list')
        else:
            list_of_tasks.append(task)
            print('Added successfully')
    elif (option == '2'):
        task = input('Enter the task: ')
        if task not in list_of_tasks:
            print('Task not found in list')
        else:
            list_of_tasks.remove(task)
            print('Removed successfully')  
    elif (option == '3'):
        task = input('Enter the task: ')
        if task in list_of_tasks:
            print('Task found in list')
        else:
            print('Task not found in list')
    elif (option == '4'):
        print(f"Number of tasks are {len(list_of_tasks)}")
    elif (option == '5'):
        for each_task in list_of_tasks:
            print('->',each_task)
    elif (option == '6'):
        print('Thank you')
        break
    else:
        print('Invalid option')