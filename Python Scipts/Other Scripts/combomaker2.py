#it4min
userfile = input("Enter The User File ~> ")
userf = open(userfile, "r").read().splitlines()
f = open("combo.txt","a")
for user in userf:
    for passw in range(1365,1383):
        combo = user+":"+str(passw)+str(passw)
        f.write(combo+'\n')
f.close()