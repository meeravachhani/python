# # 1)
# main_string=list(input('enter the string:-').split(','))
# serch=input('enter the serch string:-')
# if serch  in main_string:
#     print('the serch string is found in the string.')
# else:
#     print('the serch string is not found in the string.')

# # 2)
# string=input('enter word or string')
# print(string)
# pal=(string[::-1])
# if string==pal:
# 	print('palimdrom')
# else:
# 	print('not palimdrom')

# # 3)
# string=input('enter string:-')
# print(string)
# rev=(string[::-1])
# print(rev)

# # # or
# i=1
# le=len(string)
# while i<=le:
# 	print(string[::-1],end='')

# # 4)
# str=input('enter string:-')
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.swapcase())

# # 5)
# str=(input('enter string:-').split())
# print(str)
# str.sort()
# print(str)
# # 6)
# tup=('hii','helo','ga','gm')
# print(type(tup))
# print(tup)

# tup[2]=25
# print(tup)

# # 7)
# lib={'Bookid':'1', 'Title':'python', 'Author':'shrey', 'Price':'200', 'Publisher':'xyz'}
# print(type(lib))
# print(lib)
# print(lib['Author'])
# print(lib['Bookid'])
# print(len(lib))
# lib['Price']=300
# print(lib)
# lib['year']=2004
# print(lib)


# 8)
# from numpy import *
# num=array([1,3,4,23,56,67,42])
# print(num)
# print(num+2)
# print(num-3)
# print(num*3)
# print(num/2)


# # 9)
# from array import *

# num=array('i',[1,3,4,23,56,67,42])
# print(num)
# num.append(99)
# print(num)
# num.pop()
# print(num)

# num.insert(2,0)
# print(num)

# num.reverse()
# print(num)

# lst=list(num)
# print(type(lst))
# print(lst)

# # 10) baki 6e serching
# from numpy import *
# import array
# a=input('enter number:-').split(',')
# b1=array(a)
# print(type(b1))
# print(b1)
# serch=input('enter serch element:-')
# if serch in b1:
# 	print("position",b1.index(serch))
# else:
# 	print('not found')

# # 11) baki 6e
# from array import *
# # from numpy import *
# arr1=('i',[1,6,3,8,23])
# arr2=('i',[4,2,12,7,11])
# arr3=where(arr2>arr1,arr2,arr1)
# print(arr3)
# print(arr1)
# print(arr2)

# 12)


# # 13.
# def intrest(p,r,n):
# 	print('simple intrest:-',p*r*n/100)
# x=int(input('enter principale'))
# y=int(input('enter rant'))
# z=int(input('enter year'))
# intrest(x,y,z)


# 14)
# def arith(a,b):
# 	add=a+b
# 	sub=a-b
# 	mul=a*b
# 	div=a/b
# 	return add,sub,mul,div
# # caling function
# x,y,z,p=arith(20,5)
# print('the addition of two numbers is:',x)
# print('the subtraction of two numbers is:',y)
# print('the multiplication of two numbers is:',z)
# print('the division of two numbers is:',p)




# # 15.
# def list1(str):
# 	print(str)

# a=[input('enter string').split()]
# list1(a)

# 16)
# big=lambda a,b,c: max(a,b,c)
# a,b,c=3,12,9
# print('the biggest value is',big(a,b,c))

# 17)






