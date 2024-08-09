numbers=[12,45,78,98,100,53,2368,0,56]
even_list=[]
odd_list=[]
for i in numbers:
    if i %2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even numbers:",even_list)
print("Odd numbers:",odd_list)