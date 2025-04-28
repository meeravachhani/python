# # 1)Accept two integer values from the user; display the number which is smaller and the number 
# # which is bigger. 
# no1=int(input('enter the first number:-'))
# no2=int(input('enter the second number:-'))
# print('min value',min(no1,no2))
# print('max value',max(no1,no2))

# # 2)Accept one integer value from the user; check whether entered number is divisible by 5 or not. 
# def dividibel(no):
# 	if no%5==0:
# 		print('value is divisible by 5')
# 	else:
# 		print('value is no divisible')
# a=int(input('enter the any value:-'))
# dividibel(a)

# # 3)Accept one integer value from the user; check whether entered number is between 0-100 or 
# # not. 
# def check_num(no):
# 	if no>=0 and no<=100:
# 		print('number is 0 to 100 ')
# 	else:
# 		print('not between to 0 to 100')
# a=int(input('enter number you want to chech 0 to 100 between:-'))
# check_num(a)

# # 4)Accept one integer value from the user; display the length of the entered number, also display 
# # that the entered number is of four digits or not. 
# num = input("Enter an integer: ")
# def check_4digit(a):
#     length =len(num)
#     if length==4:
#         print("The length of the entered number is:",length)
#     else:
#         print("you are not enter 4 digit")
# check_4digit(num)

# 5) Accept one integer value from the user; display appropriate day of the week.
# def check_days(day):
#     if day==1:
#         print('sunday')
#     elif day==2:
#         print('monday')
#     elif day==3:
#         print('tuesday')
#     elif day==4:
#         print('wednesday')
#     elif day==5:
#         print('thresday')
#     elif day==6:
#         print('friday')
#     elif day==7:
#         print('saturday')
#     else:
#         print('enter 1 to 7 number')
# num= int(input("Enter an number: "))
# check_days(num)

# 6) Take choice from the user, and perform the arithmetic operation as per the choice. 
# Choices: 1) Addition, 2) Subtraction, 3) Multiplication 4) Division 

# def add_sub_mul_divi(num1,num2):
#     if ch==1:
#         print('addition of two value:',num1+num2)
#     elif ch==2:
#         print('Subtraction of two value:',num1-num2)
#     elif ch==3:
#         print('Multiplication of two value:',num1*num2)
#     elif ch==4:
#         print('Division of two value:',num1/num2)
#     else:
#         print('not proper.....')

# print('enter 1 for addition:2 for subtraction: 3 for multiplication: 4 for division')
# ch=int(input('enter proper arithmetic operaction you want to used:'))
# a=int(input('enter 1 value:'))
# b=int(input('enter 2 value:'))
# add_sub_mul_divi(a,b)

#  # 7) Accept the string from the user; display the count of vowels and consonants. 
# def count_vowels_consonants(str):
#     vovels='a,e,i,o,u,A,E,I,O,U'

#     vov_count=0
#     con_count=0
#     for i in str:
#         if i.isalpha():
#             if i in vovels:
#                 vov_count += 1
#             else:
#                 con_count += 1
#     print(vov_count,'vovels',con_count,'consonants')

# stri=input('enter the string:')
# count_vowels_consonants(stri)

# # 8) Accept one integer value from the user; display the table of it. 
# # def table(num):
#     i=1
#     while i<=10:
#         print(num,'*',i,'=',num*i)
#         i +=1
# a=int(input('number enter'))
# table(a)


# # 9) Display square and cube of numbers 1-10. 
# # def squ_cub(num):
# for i in range(1,10):
#     print('square',i*i)
#     print('cube',i*i*i)


# # 10)
# string=input('enter string:-')
# print(string)
# print(string.upper())


# 11) Display the following output using loop: 
# i. 1 to 10 
# ii. 10 to 1 
# iii.1 3 5 7 9 
# iv. 2 4 6 8 10 

# for i in range(1,11):
#     print(i)

# for i in range(10,1,-1):
#     print(i)

# for i in range(2,11,2):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# # 12) Print 1 2 4 8 16 32 64 128 256 512 1024 
# for i in range(11):
#     print(2**i)



# 13)
# sem as a 8


# 14) Accept numbers from the user; display the sum of the entered numbers. 
# b=0
# no=int(input('enter number'))
# for i in range(no):
#     a=int(input('enter:'))
#     b+=a
# print(b)

# # 15) Accept numbers from the user; display the count of the entered numbers.
# def coun(l):
# 	print('count',len(str(l)))
# str1=int(input('enter number:-'))
# coun(str1)

# # 16) Accept numbers from the user; find and display number of zeros available in the number. 
# def zero(a):
# 	print('count zero',str(a).count('0'))
# mm=int(input('enter number:-'))
# zero(mm)

# # 17 ) Accept an integer from the user; tell user that whether entered number is even or odd. 
# def odd_even(a):
# 	if a%2==0:
# 		print('number is even')
# 	else:
# 		print('numer is odd')
# while True:
# 	x=int(input('enter a number for check odd even:'))
# 	odd_even(x)

# 	again=input('do you want to check another number? y/n:-')
# 	if again!='y':
# 		break


