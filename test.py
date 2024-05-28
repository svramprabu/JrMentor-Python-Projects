class tester:

    def name_printer(self,name):
        self.name = name
        print(self.name)

name = input('NAme: ')
a = tester()
a.name_printer(name)
# # a.__init__()

# class mine:
#     name='Someone'
#     def my_name(self):
#         print(self.name)
#
# for i in range(3):
#     x = mine()
#     x.name=input('Name: ')
#     x.my_name()
