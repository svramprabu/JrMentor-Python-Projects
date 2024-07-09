# Declare a variable
# variable_name = Data

# hacker_kid = 12345

# print(hacker_kid)

# Datatypes
# int - nos w/o decimal points positive,negative,0
# float - all nos with decimal points

# a = 123145
# print(a)
# print(type(a))
# b = 123.456
# print(b)
# print(type(b))

# String
# array of bytes of data containting unicode characters
# _ _ _ _ _
# unicode character - all keyboard inputs

# 'abcdABCE0123!@#!#'
# "abcdABCE0123!@#!#"
# """abcdABCE0123!@#!#"""
#
# c = "trisha gupta"
# print(c)
# print(type(c))

# import pandas as pd
# from scipy import sparse
# import scipy
# import numpy as np
# df = pd.read_csv("Customers 100.csv")
# # df = pd.DataFrame()
# arr = np.array([0,0,0,1])
# # scipy.csr
# print(sparse.csr_matrix(arr))

# import numpy as np
# import pandas as pd
# data=(np.random.rand(2,4))
# df = pd.DataFrame(data)
# print(df[0:])
# print()

import pandas as pd
data = pd.read_csv("Customers 100.csv")
# print(data)
# print(data[0:2])
# print(data[0:10])
# print(data[5:10])
# print(data.head())
# print(data.loc[:,['Index','Customer Id','Subscription Date']])

# df = pd.read_json("test.json")
# print(df.head())
datas=pd.read_excel("File Example 10.xlsx")
print(datas.head())