#it4min
file = open("numbers.txt", 'a')
code = input("enter the code: ")
nums = '0123456789'
strs = '''
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:@it4min
'''
for q1 in nums:
     for q2 in nums:
         for q3 in nums:
             for q4 in nums:
                 for q5 in nums:
                     for q6 in nums:
                         for q7 in nums:
                             number = "TEL;TYPE=VOICE,CELL;VALUE=text:"+code+q1+q2+q3+q4+q5+q6+q7
                             file.write(number+strs)
                             print (number)
file.close()
