# # regular expression
# string1='this will be printed on the \n new line'
# print(string1)

# string1=r'this will be printed on the \n new line'
# print(string1)

# # using compiler method of re module
# import re
# abc=re.compile(r'm\w\w')
# string1='new day mats matter'
# result=abc.search(string1)
# print(result.group())
 
 
# # create a re to serch the string that have 'a' at any position and having total 3 characters after it using findall().
# import re
# string1='atmiya atm sten strnge'
# result=re.findall(r'\w\w',string1)
# print(result)

# # re.split(r'\w+',string1)
# import re
# string1='hello!,welcome to the class; wish you !good morning'
# result=re.split(r'\w+',string1)
# print(result)

# # split(),splits the given string into pieces according to the regular wxpression and returns the pieces as an element of the list.

# # replacing the sub-string with the other string
# import re
# string1='india is the great country'
# print(string1)
# result=re.sub('india','bharat',string1)
# print(result)

# import re
# string1='sun shine sooner or laster s'
# # result=re.findall(r's[w]*',string1)
# result=re.findall(r's\w+',string1)
# print(result)

# # create re that finds the word starting with a number
# import re
# string1='an extra lecture is arranged on26th and 29th of this month'
# result=re.findall(r'\d[\w]*',string1)
# print(result)

# # create re that retrieve words having 5 character
# import re
# string1='feb marc april septem october'
# result=re.findall(r'\b\w{5}\b',string1)
# print(result)

# # create re that retrieve word having 5 or 6 character
# import re
# string1='feb marc april septem october'
# result=re.findall(r'\b\w{5,6}\b',string1)
# print(result)

# # create re that retrieve word having 4 or more character but not more that 6 characters.
# import re
# string1='feb marc april septem october'
# result=re.findall(r'\b\w{4,6}\b',string1)
# print(result)

# # create re that retrieves only digits having single digit
# import re
# string1='one two 3 13'
# result=re.findall(r'\b\d\b',string1)
# print(result)

# # create re that retrieves the last character of the stringwhich start with's'.
# import re
# string1='fore five seven'
# result=re.findall(r's[\w]*(\w)$',string1)
# print(result)

# # create re that retrieve the enrollment number of the student
# import re
# string1='aaa 123'
# result=re.findall(r'\d+',string1)
# print(result)

# # create re that retrieve the name of the student .
# import re
# string1='aaa 123'
# result=re.findall(r'\D+',string1)
# print(result)

# # create re that retrieve word starting with 'st' .
# import re
# string1='stanger summer sun student semester'
# result=re.findall(r'st[\w]*',string1)
# print(result)


# # create re that retrieve word starting with 'st' or 'su'
# import re
# string1='stanger summer sun student semester'
# result=re.findall(r's[t,u][\w]*',string1)
# print(result)


# functions
# syntax:
# def name_function(para-1,para2):
	# function statements

# # add two value using function
# def sum(a,b):
# 	total=a+b
# 	print('the sum of two values is:',total)
# # call function
# sum(2,5)
# sum(2.5,5.2)

# # returning the result from the function 
# def sum(a,b):
# 	total=a+b
# 	return total
# # call function
# x=sum(2,5)
# print('the sum of two value is:',x)
# y=sum(2.5,5.2)
# print('the sum of two value is:',y)

# # to check wether the number is odd or even using function
# def even_odd(no):
# 	if no%2==0:
# 		print('number is even')
# 	else:
# 		print('number is odd')
# # calling the function
# even_odd(2)
# even_odd(3)

# # to check wether number number is positive nagative or zero using function
# def pos_neg_zer(no):
# 	if no>0:
# 		print('number is positive number')
# 	elif no==0:
# 		print('the number is zero')
# 	else:
# 		print('the number is negative')
# # calling function
# n=int(input('enter the number:'))
# pos_neg_zer(n)

# # returning multiple values from a function
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

# # pass by object
# # immutable object:integer,string,float,tuple
# # mutable object:list
# # to pass an integer to a function and modify it.
# def modify(x):
# 	x=25
# 	print('the value of x inside the function is:',x,id(x))
# # calling function
# x=52
# modify(x)
# print('the value of x outside the function is:',x,id(x))


# # to pass an list to a function and modify it.
# def modify(list):
# 	lst.append(25)
# 	print('the value of x inside the function is:',lst,id(lst))
# # calling function
# lst=[2,5,8,9,7]
# modify(lst)
# print('the value of x outside the function is:',lst,id(lst))

# # formal and actual arguments
# # def sum(a,b):-->formal
# 	# ---
# 	# ---
# # calling function
# # s=2,t=5 -->actual argument

# # there four types of actual argument
# # 1.positional  
# # 2.keyword
# # 3.default
# # 4.variable length

# # 1.positional argument
# # the number of arguments and position in the function defination shoul match exactly
# # with the number and position of the argument in the function call.

# def combine(a,b):
# 	c=a+b
# 	print(c)
# # calling function
# combine('atmiya','university')
# combine('university','atmiya')
# combine('university','atmiya','hello')





# # 2.)keyword argument
# # keyword argument identifies parameters by their names.
# # while calling the function we have to pass their value,
# # one is argumentname and two its value.

# def stud(roll,name):
# 	print('the rollnumber is:',roll)
# 	print('the name is:',name)
# # calling function
# stud(roll=1,name='meera')
# stud(name='disha',roll=2)

# # 3.)default argument
# # it is requiredit if a programer wants to set default value to some parameters.
# # if at the time  of calling function the value is not passed then the default value will be taken.
# # if the value is pass then the value passed wil be taken.

# def stud(roll,name='abc'):
# 	print('the rollnumber is:',roll)
# 	print('the name is:',name)
# # # calling function
# stud(1,'meera')
# stud(2)


# # 4.)variable length argument
# # if in case the program is unaware aboutthe number od parameter to be used,than he canuse variable length arguments.
# # if two parameter are declared and insert value  for there,than error will be genereted.
# # in this case we may use variable length arguments
# # forment:
# 	# def name_def(farg,*arguments)

# def total(farg,*args):
# 	sum=0
# 	for i in args:
# 		sum=sum+i
# 	print('the total of allnumber is :',(farg+sum))
# # callling function
# total(1,2,3)
# total(1,2,3,4,5,6,7)

# # passing a group of element to a function
# def disp(abc):
# 	for i in abc:
# 		print(i)
# # taaking value from the user
# print('enter a value:')
# abc=[a for a in input().split()]
# disp(abc)


# # anonymous finction(lambda)
# # while using normal function we need to define a function and give name to it.
# # def name_of_def(a,b):
# # while using anonymous function there is no need of giving the name to the function.
# # def sqr(no):
# 	# return no*no
# # finding the square of a number using lambda

# sqr=lambda no:no*no
# no=int(input('enter  the number'))
# print('the square of the  entered number is',sqr(no))

# # find out the biggest number from two number
# big=lambda a,b: a if a>b else b
# a,b=3,2
# print('the biggest value is',big(a,b))


# file handling

# formet:
# file handler=open('file name','open')

# f=open('abc.txt','w')
# str=input('enter the data:-')
# f.write(str)
# f.close()
# # read the file
# f=open('abc.txt','r')
# a=f.read()
# print(a)
# f.close()
 
# f=open('abc.txt','w')
# print('enter the text you went to enter:-')
# while str!='%':
# 	str=input()
# 	if str!='%':
# 		f.write(str+ '\n')
# f.close()


# import os,sys
# file_name=input('enter the file name')
# if os.path.isfile(file_name):
# 	f=open(file_name,'r')
# else:
# 	print(file_name+'does not exist')
# 	sys.exit()
# str=f.read()
# print(str)
# f.close()

# counting number of lines,characters and words in the file if the file exist
# import os,sys
# file_name=input('enter the file name')

# 	f=open(file_name,'r')
# else:
# 	print(file_name+'does not exist')
# 	sys.exit()
# lc=wc=cc=0

# appending the file
f=open('abc.txt','a')
str_append=',rajkot'
f.write(str_append)
f.close()

f=open('abc.txt','r')
str=f.read()
print(str)
f.close()


# working with the binary files.
#

program to copy an image file to another file.an

f1=open('au_logo.png','rb')
f2=open('aulogo.png','wb')
a=f1.read()
f2.write(a)
f1.close()
f2.close()

# using with statement
# ->it will take care of closing an opend file
# formet:with open('file name','mode')
# the seek() and tell() methods.and
# tell():it is used to know the position of the file pointer.
# it will return the current position of the file pointer
# formet:n=f.tell()

# seek():it is used to move the file pointer to the position we want to.
# formet:f.seek(offset,fromwhere)
# offset:ie means number of bytes to move.
# fromwhere:it means from where to move.

 # taking the menu item from the user and store it in the file resturant.
record_len=15
with open('restaurant.bin','wb') as f:
	no=int(input('enter the number of food items:'))
	for i in range(no):
		restaurant=input('enter the food item you went to have in the menu:-')
		ln=len(restaurant)
		restaurant=restaurant+(record_len-ln)*' '
		restaurant=restaurant.encode() #it convert to text to binary
		f.write(restaurant)

# take the record number from the user and display the food item at that record number.
record_len=15
with open('restaurant.bin','rb') as f:
	n=int(input('enter record number:-'))
	f.seek(record_len*(n-1))
	str=f.read(record_len)
	print(str.decode())

# ziping the content of file.
# zip_deflated:will compress the data and will be ziped.
# zip_stored:will just save the data in the zip file.

from zipfile import*
f=ZipFile('demo.zip','w',ZIP_DEFLATED)
f.write('restaurant.bin')
f.write('au_logo.png')
f.close()

# unzip file

from zipfile import*
f=ZipFile('demo.zip','r')
f.extractall('c:/m')
f.close()



