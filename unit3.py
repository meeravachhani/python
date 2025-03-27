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

# # sqr=lambda no:no*no
# # no=int(input('enter  the number'))
# # print('the square of the  entered number is',sqr(no))

# # find out the biggest number from two number
# big=lambda a,b: a if a>b else b
# a,b=3,2
# print('the biggest value is',big(a,b))








