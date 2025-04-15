

# unit:-2 array


# #array
# # 1st way
# import array
# a=array.array('i',[7,9,5,4,6,3])
# print(a)

# # 2nd way
# import array as ar
# a=ar.array('i',[7,9,5,4,6,3])
# print(a)

# # 3rd way
# from array  import * 
# a=array('i',[7,9,5,4,6,3])
# print(a)

# # indexing and slicing on arrays
# # indexing
# # using for loop
# from array  import * 
# a=array('i',[7,9,5,4,6,3])
# print(a)
# no=len(a)
# # print(no)
# for i in range(no):
#     print(a[i]) 


# # using while loop
# from array  import * 
# a=array('i',[7,9,5,4,6,3])
# print(a)
# no=len(a)
# i=0
# while i<no:
#     print(a[i])
#     i=i+1


# # indexing of character aray
# from array import *
# charactre=array('u',['a','b','c','d'])
# print(charactre)
# print(type(charactre))
# for c in charactre:
#     #print(c)
#     print(c,end=',') 


# # slicing
# # the forment of slicing: array_name[start:stop:string]

# from array import *
# a=array('u',['r','a','j','k','o','t','g','u','j','r','a','t'])
# print(a)
# b=a[0:13]
# print(b)

# b=a[0:]
# print(b)

# b=a[:13]
# print(b)

# b=a[-16:]
# print(b)

# b=a[0:6]
# print(b)

# b=a[0:13:2]
# print(b)

# b=a[0::2]
# print(b)

# b=a[::2]
# print(b)


# # slicing using for loop
# from array import *
# a=array('u',['r','a','j','k','o','t','g','u','j','r','a','t'])
# print(a)
# for i in a[0:16]:
#     print(i,end=' ')


# # procecing the arrays/array method
# from array import *
# a=array('i',[7,9,5,4,6,3])
# print(a)

# appending the value
# a.append(2)
# print(a)

# # inserting value
# a.insert(0,7)
# print(a)

# removing value
# a.remove(7)
# print(a)

# # removing the last element
# b=a.pop()
# print(b)

# # finding the position of an element
# b=a.index(5)
# print(b)
# print(a)

# converting an array to the list
# lst=a.tolist()
# print(type(a))
# print(a)
# print(type(lst))
# print(lst)


# # accept amount of goods purchased,give the total amout of purchase and the average  cost of the product purchased.
# from array import *
# str=input('enter the amout: ').split(',')
# amount=[int(number)for number in str]
# tot_amt=0
# for i in amount:
#     print(i) 
#     tot_amt=tot_amt+i 
# print('the total amount is: ',tot_amt)
# l=len(amount)
# average=tot_amt+l
# print('the average of all goods is: ',average)


# types of array
    # 1)single dimentional array
    # 2)multi dimentional array
# # 1st way to create numpy
# import numpy
# a=numpy.array([2,4,9,7,9])
# print(a)

# # 2nd way
# import numpy as nu
# a=nu.array([2,4,9,7,9])
# print(a)

# # 3rd way
# from numpy import *
# a=array([2,4,9,7,9])
# print(a)

# # 2)multi dimentional array
# from numpy import *
# a=array([[1,2,3],[2,3,4],[5,6,7]])
# print(a)
# print(ndim(a))

# from numpy import *
# a=array(['apple','bnana','orange','mango'])
# print(a)
# print(ndim(a))


# # creating array using linspace()
# from numpy import *
# a=linspace(1,9,2)
# print(a)

# from numpy import *
# a=linspace(1,10,5)
# print(a)


# # creting array using arrange
# from numpy import *
# a=arange(1,15,5)
# print(a)

# # operation on array
# from numpy import *
# a=array([10,20,30,40,50,60])
# print(a)
# print('addition:',a+10)
# print('subtraction:',a-5)
# print('multiplication:',a*2)
# print('divition:',a/2)
# print('minimumvalue:',min(a))
# print('maximumvalue:',max(a))
# print('sum of value:',sum(a))
# print('avrage:',mean(a))

# # comparing array
# from numpy import *
# a=array([10,20,30,40,80,60])
# b=array([20,20,70,40,50,60])
# print('result',a==b)
# print('result',a>b)
# print('result',a<=b)



# # using where()
# from numpy import *
# a=array([2,8,13,17,9,16])
# b=array([1,9,12,6,15,10])

# c=where(b>a,b,a)
# print(a)
# print(b)
# print(c)

# # uing nonzero()
# # it used to element is zero that mean particular this element index not display
# from numpy import *
# a=array([2,8,13,17,9,16])
# c=nonzero(a)
# print(type(c))
# print(a)
# print(c)

# from numpy import *
# a=array([2,0,13,17,9,16])
# c=nonzero(a)
# print(type(c))
# print(a)
# print(c)

# # view()
# from numpy import *
# a=array([2,8,0,17,9,16])
# b=a.view()
# print(a)
# print(b)
# a[3]=28
# print(a)
# print(b)
# b[4]=82
# print(a)
# print(b)

# # copy()
# from numpy import *
# a=array([2,8,0,17,9,16])
# b=a.copy()
# print(a)
# print(b)
# a[3]=28
# print(a)
# print(b)
# b[4]=82
# print(a)
# print(b)

# # slicing and indexing numpyarrays
# # slicing
# from numpy import *
# a=array([2,8,0,17,9,16])
# print(a)
# print(a[:])
# print(a[::])
# print(a[2:])
# print(a[2::2])

# # indexing
# from numpy import *
# a=array([2,8,0,17,9,16])
# print(a)
# i=0
# while(i<len(a-1)):
#     print(a[i])
#     i=i+1

# # attributes
# # 1)ndim attribute
# from numpy import *
# a=array([2,8,0,17,9,16])
# print(a)
# print(a.ndim)
# a=array([[2,8,0],[17,9,16]])
# print(a)
# print(a.ndim)

# # 2)shape attribute
# from numpy import *
# a=array([2,8,0,17,9,16])
# print(a)
# print(a.shape)
# a=array([[2,8,0],[17,9,16]])
# print(a)
# print(a.shape)

# # 3)size zttribute
# from numpy import *
# a=array([2,8,0,17,9,16])
# b=array([[2,8,0],[17,9,16]])
# print(a)
# print(a.size)
# print(b)
# print(b.size)

# # dtype attributr
# from numpy import *
# a=array([[2,8,0],[17,9,16]])
# print(a)
# print(a.dtype)
# a=array([2,8,0,17,9,16])
# print(a)
# print(a.dtype)


# # method()

# # reshape()
# from numpy import *
# a=array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# b=a.reshape(2,2,3)
# print(b)
# b=a.reshape(4,3)
# print(b)

# # flatten()
# from numpy import *
# a=array([[1,2,3,4],[5,6,7,8]])
# print(a)
# b=a.flatten()
# print(b)
# print(b.shape)


# from numpy import *
# a=array([[1,2,3],[4,5,6],[7,8,9]])
# # print(a)
# for i in range(len(a)):
#     print(a[i])
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j],end=' ')

# from numpy import *
# a=array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(a[0:1])
# print(a[2:])
# print(a[:,0])
# print(a[0:1,0:1])
# print(a[2,1])


# # string:-
# a='welcome to the class an entry to the world'
# print(a)
# b='welcome to the class an "entry" to the world'
# print(b)
# c='welcome to \t the class an antry to \n the world'
# print(c)
# d=r'welcome to the \t class an antry to \n the world'
# print(d)

# e='atmiya'
# f='university'
# g=e+f
# print(g)
# print(e*2)

# # display the string in the reverse
# # now stright

# a='rajkot gujrat'
# i=0
# l=len(a)
# while i<l:
#     print(a[i],end=' ')
#     i=i+1

# # reverse
# a='rajkot gujrat'
# i=1
# l=len(a)
# while i<=l:
#     print(a[-i],end=' ')
#     i=i+1

# a='rajkot gujarat'
# for i in a[::-1]:
#     print(i,end=' ')

# # finding the substring from the string
# main_string=input('enter the string:-')
# serch=input('enter the serch string:-')
# if serch  in main_string:
#     print('the serch string is found in the string.')
# else:
#     print('the serch string is not found in the string.')


# # to check whether the string is palimdrom or not

# m=input('enter the string:-')
# print(m)
# n=(m[::-1])
# if m==n:
#     print('the enter string is palindrom.')
# else:
#     print('the enter string is not  palindrom.')
 

# # count the sub string in the string(limited)
# main_string=input('enter the string:-')
# sub_string=input('enter the substring of the serch:-')
# a=main_string.count(sub_string,0,5)
# print('the sub string was found ',a,'time(s)')

# # unlimited(full string)
# main_string=input('enter the string:-')
# sub_string=input('enter the substring of the serch:-')
# a=main_string.count(sub_string)
# print('the sub string was found ',a,'time(s)')


# # changing the case of the string
# main_string=input('enter the string')
# print(main_string.upper())
# print(main_string.lower())
# print(main_string.swapcase())
# print(main_string.title())







# working with character

# string1='india'
# print(string1)
# print(type(string1))
# character=string1[0]
# print(character)
# print(type(character))
# character=string1[4]
# print(character)
# character=string1[0:3]
# print(character)


# # check the type of a character
# string1=input('enter a character:-')
# character=string1[0]
# if character.isalpha():
#     print('user has entered an alphabet.')
#     if character.isupper():
#         print('user has entered an upper case.')
#     else:
#         print('the characteris an lower case')
# else:
#     print('user has entered either a number or a special char.')


# # working with list
# # creting list using rage
# # format:range(start,stop,stepsize)

#crate a list having number from 0-9
# list1=range(10)
# for i in list1:
#     print(i,end=" ")
# print(type(list1))

# # start to any number
# list1=range(11,16)
# for i in list1:
#     print(i,end=' ')

# # store even number between 1-10
# list1=range(2,11,2)
# for i in list1:
#     print(i,end=' ')


# # update the value in the list
# # append
# list1=[1,2,3,4,8,7,6,9,60]
# print(list1)
# list1.append(11)
# print(list1)
# list1.append(12)
# print(list1)

# # update at the specific location
# list1[6]=60
# print(list1)

# # deliting the element by value
# list1.remove(60)
# print(list1)

# # finding the length of a string
# a=len(list1)
# print(a)

# # deleting/clearing all the element from the list at a time
# list1.clear()
# print(list1)

# # create a list display all the element in the reverse order.
# list1=['kalawad road','rajkot','gujarat','india']
# list1.reverse()
# print(list1)

# # concating two lists.
# list1=['kalawad road','rajkot','gujarat','india']
# list2=['gamdhinagar','mumbai','bhopal']
# print(list1+list2)


# # printing the same list as many times you want
# list1=['kalawad road','rajkot','gujarat','india']
# print(list1*2)

# # membership
# # making the use of 'in' and 'not in'
# list1=[10,20,30,40,50]
# n1=1
# n2=30
# print(n1 in list1)
# print(n1 not in list1)
# print(n2 in list1)
# print(n2 not in list1)

# # we can alias the list
# list1=[10,20,30,40,50]
# print(list1)
# list2=list1
# print(list2)
# list2[3]=300
# print(list2)
# print(list1)

# # cloan the list
# list1=[10,20,30,40,50]
# print(list1)
# list2=list1[:]
# print(list2)
# list2[3]=300

# print(list2)
# print(list1)

# # find how many times an element is available in the list
# list1=[]
# num=int(input('enter many elements you want to enter?:-'))
# for i in range(num):
#     print('enter the element: ',end=' ')
#     list1.append(int(input()))
# print(list1)
# to_find=int(input('which element you want to find?:-'))
# count=0
# for i in list1:
#     if(to_find==i):
#         count=count+1
# print('{}is found {}time(s).'.format(to_find,count))

# # finding the colum elements
# # converting the list to set
# list1=[10 ,20 ,30, 40 ,50]
# print(list1)
# list2=[10,12,30,41,50]
# print(list2)
# set1=set(list1)
# set2=set(list2)
# print(set1)
# print(set2)
# set3=set1.intersection(set2)
# print(set3)
# print(type(set3))
# list3=list(set3)
# print(list3)


# list1=[10,20,30,40,[1,2,3,4]]
# print(list1)
# for i in list1[0:4]:
#     print(i)
# for i in list1[4]:
#     print(i)

# # working with tuple
# tuple1=(10,)
# print(tuple1)
# print(type(tuple1))

# tuple1=1,2,3,10,20,30
# print(tuple1)
# print(type(tuple1))

# list1=[1,2,3,10,20,30]
# tuple1=tuple(list1)
# print(type(tuple1))
# print(tuple1)

# tuple1=(1,2,3,10,20,30)
# a=tuple1[1:3]
# print(a)


# tuple1=('abc',1)
# name,roll=tuple1[0:2]
# print(name)
# print(roll)


# tuple1=(10,20,30,1,10,3,2)
# print(len(tuple1))
# print(min(tuple1))
# print(max(tuple1))
# print(sorted(tuple1))
# print(sorted(tuple1,reverse=True))
# print(tuple1.count(2))
# print(tuple1.index(10))

# # nested tuple
# tuple1=(10,2,30,1,(20,3,2))
# print(tuple1)
# print(tuple1[3])

# take values like roll,name,marks of student,sort it.
# tuple1=((2,'cde',27),(3,'efg',29),(1,'abc',29),(4,'jkl',19))
# print(tuple1)
# print(tuple1[2])
# print(sorted(tuple1))


## modifi the value
# names=('a','b','c','d','e')
# print(names)
# nm=input('wnter the new name that you want to enter:')
# posi=int(input('enter the position at which you want to enter": '))
# new_name=tuple(nm)
# temp=names[0:posi-1]
# print(temp)
# temp=temp+new_name
# print(temp)
# names=temp+names[posi:posi]
# print(names)

# # deleting from the specific position
# names=('a','b','c','d','e')
# print(names)
# posi=int(input('enter the position at which want to eanter: '))
# name1=names[0:posi-1]
# print(name1)
# names=name1+names[posi:]
# print(names)



# # working with dictionary
# # stud={1:"abc",2:"cde",3:"efg",4:"ghi",5:"ijk"}
# # print(stud)
# stud={'roll':1,'name':"abc",'mark':29}
# print(stud)
# print('marks are',stud['mark'])
# print('roll.no ',stud['roll'])
# print('name is',stud['name'])

# length=len(stud)
# print(length)

# stud['mark']=30
# print('marks are:',stud['mark'])
# print('city' in(stud))
# print('name' not in(stud))

# methods
# # copy
# stud={'roll':1,'name':"abc",'marks':29}
# stud1=stud.copy()
# print(stud1)
# a1=stud.keys()
# print(a1)

# #get
# a1=stud.get('marks')
# print(a1)

# #update
# stud.update({'marks':30})
# print(stud)

# #items
# a1=stud.items()
# print(a1)
# print(type(a1))

# a1=stud.pop('marks')
# print(a1)
# print(stud)

# popitems
# a1=stud.popitem()
# print(a1)
# print(stud)

# # formskeys()
# d=('a1','a2','a3')
# dict1=dict.formkeys(d)
# print(dict1)
# d=('a1','a2','a3')
# a1=10
# dict1=dict.formkeys(d,d1)
# print(dict1)

# stud.clear()
# print(stud)

# # accept number of students,and subkects you want to enter
# marks={}
# no=int(input('how many subject you want to enter?:'))
# for i in range(no):
#     print('enter subject name:')
#     key=input()
#     print('enter mark of subject:')
#     value=int(input())
#     marks.update({key:value})
# print('the subject or marks are:' ,marks)
# total=sum(marks.values())
# print('the total of all entered subject is: ',total)

# # ask student the name of a student,dispaly marks of that subject
# name_subject=input('enter the name of subject: ')
# sub_marks=marks.get(name_subject,-1)
# if(sub_marks==-1):
#     print('subject no founfd')
# else:
#     print('the marks in {} are {} '.format(name_subject,sub_marks))


# # conerting list into dictionary
# capital_city=['bengalur','bhopal','jaipur','mumbai','gandhinagar']
# state=['karnatak','mp','rajasthan','maharastra','gujrat']
# a=zip(capital_city,state)

# print(a)
# state_capital=dict(a)
# print(state_capital)
# print(type(state_capital))

# # converting string into dictionary
# string1='1=abc,2=cde,3=ehg,4=hij'
# print(string1)
# lst=[]
# for i in string1.split(','):
#     a=i.split('=')
#     lst.append(a)
# print(lst)

# dictionary1=dict(lst)
# print(dictionary1)

# dictionary2={}
# for key,value in dictionary1.items():
#     dictionary2[int(key)]=value
# print(dictionary2)

# # order dict
# dict1=orderedDict()
# dict1[1]='a'
# dict1[2]='b'
# dict1[3]='c'
# dict1[4]='d'
# print(dict1)
# for i,j in dict1.items():
#     print(i,j)







