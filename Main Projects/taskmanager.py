user= input('1.add: '
             'type task alongside\n:')

if len(user.split())>1:
    user,task = user.split()
if user == '1':
    print('adding a task')
    if task:
        print('nothing')
    print(task)