from operator import add, sub, mul,truediv
a={'+':add,'-':sub,'*':mul,'/':truediv}
number_1=int(input("enter number:"))
number_2=int(input("enter number:"))
oprtr=input("type the operator(+,-,*,/):")
print(a[oprtr](number_1,number_2))   