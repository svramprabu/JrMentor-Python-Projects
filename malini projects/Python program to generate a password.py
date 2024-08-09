import random
password_length = int(input("enter the length of password:"))
words="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password= "".join(random.sample(words,password_length))
print("The password is:",password)











