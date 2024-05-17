# class tester:
#
#     def __init__(self,name):
#         print(name)
#
# name = input('NAme: ')
# a = tester(name)
# # a.__init__()

class mine:
    name='Someone'
    def my_name(self):
        print(self.name)

for i in range(3):
    x = mine()
    x.name=input('Name: ')
    x.my_name()
