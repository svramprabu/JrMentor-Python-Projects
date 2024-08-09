#it4min
userfile = input("Enter The User File ~> ")
passwfile = input("Enter The Passw File ~> ")
userlist = []
passwlist = []
userf = open(userfile, "r").read().splitlines()
for us in userf:
    userlist.append(us.replace("\n",""))
passwf = open(passwfile, "r").read().splitlines()
for ps in passwf:
    passwlist.append(ps.replace("\n",""))
f = open("combo.txt","a")
for num in range(999999*99999):
    username = userlist[num]
    password = passwlist[num]
    combo = username+":"+password
    f.write(combo+'\n')
    print (combo)
f.close()