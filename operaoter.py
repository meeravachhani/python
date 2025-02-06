# number convert in decimal number

a=0b1010101010
b=0o2222
c=0xE222
d=int(a)
print("binary number convert in to decimal number",d)
print("octal number convert in to decimal number",b)
print("hexa number convert in to decimal number",c)

# other way
a='0b1010101010'
b='0o2222'
c='0xE222'
d=int(a,2)
e=int(b,8)
f=int(c,16)
print("binary to decimal with other way",d)

# decimal to binary,octal,hexa
a=0o222
binary=bin(a)
octal=oct(a)
hexadecimal=hex(a)

print(binary)
print(octal)
print(hexadecimal)

# converting datatype
a=23.2
b=int(a)
print(b)

a=23
b=float(a)
print(b)

# string releted 
a="python is a very instresting subject. \ paython is easy subject."
print (a)

a="python is a very instresting subject. \n paython is easy subject."
print (a)

a="python is a very instresting subject. \\ paython is easy subject."
print (a)

a="python is a very instresting subject. \' paython is easy subject."
print (a)

a="python is a very instresting subject. \" paython is easy subject."
print (a)

a="python is a very instresting subject.\b  b paython is easy subject."
print (a)

a="python is a very instresting subject. \r r paython is easy subject."
print (a)

a="python is a very instresting subject. \t t paython is easy subject."
print (a)

a="python is a very instresting subject. \v v paython is easy subject."
print (a)

# variable datatype find
a="hi,good morning"
print(type(a))

b=234
print(type(b))


# example for h.w 
a=10
b=5

 # arithmetic
print("addition to value",a+b)
print("subtrastion ",a-b)
print("multiplication",a*b)
print("divistion",a/b)
print("modual",a%b)
print("power",a**b)
print("sumthing",a//b)

# assiment

a=2
print(a)

a+=5
print(a)

a-=1
print(a)

a*=2
print("multi",a)

a/=2
print(a)

a*=2
print("multiplication",a)

a%=2
print(a)

a=10
print(a)

a//=2
print(a)

a**=2
print(a)

# compsrision
a=10
b=5
print("equeal", a==b)
print("not equeal",a!=b)
print("lesthen",a<b)
print("graterthen",a>b)
print("leassorqueal",a<=b)
print("grateror qqeueal",a>=b)

# logical
a=2
b=0
print(a and b)

a=0
b=2
print(a and b)

a=2
b=3
print(a or b)

a=0
b=3
print(a or b)

a=2
b=3
print(not a)

a=0
b=3
print(not b)

# boolean operater
a=True
b=False
print(a and b)

a=True
b=True
print(a and b)

a=False
b=False
print(a and b)

a=True
b=True
print(a or b)

a=True
b=False
print(a and b)

a=False
b=False
print(a or b)

a=True
print( not a)

# member operator
furniture=['chair','table','cupbord']
print(furniture)

print('table' in furniture)
print('Table' in furniture)
print('dianing' in furniture)
print('Table' not in furniture)
print('dining' not in furniture)

a=2>7
print(a)

a=7>2
print(a)

# 3) sequences data type 
    # 1) str datatype 
a='''python is one of the very intersting 
programing language,which requires very less code...'''
print(a)
c="""python is one of the very intersting 
programing language,which requires very less code..."""
print(c)

b='welcome to atmiya university'
print(b)
print(b[0])
print(b[11:21])
print(b[11:17])
print(b[11:])
print(b[:11])
print(b[21:])
print(b[:])
print(b[-13:-9])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

    # 2)byte datatype 
a=[2,4,6,8,32,7,5,87,100,255]                                                                              
print(type(a))
print(a)
b=bytes(a)
print(type(b))
print(b[0])
print(b[8])
print(b[0:8])
b[1]=5

# 3)bytearray datatype 
a=[2,4,6,8,32,7,5,87,100,255]                                                                              
print(type(a))
print(a)
b=bytearray(a)
print(type(b))
print(b[0])
print(b[8])
print(b[0:8])
b[1]=40
print(b[1])

# 4)list datatype 
a=[2,5,6,8,-56,'a','A','abc']
print(a)
print(a[5])
print(a[5:8])
a[1]=10
print(a)
print(a*2)

# 5)tuple datatype 
a=(2,5,6,8,-56,'a','A','abc')
print(type(a))
print(a)
print(a[5])
print(a[5:8])
a[1]=10
# print(a)

    # 6) range datatype 
a=range(7)
print(a)
for i in a:
    print(i)
a=list(range(8))
print(a)


# # identity operater
a=7
print(id(a))
b=7
print(id(b))

a=[2,5,4,67,87]
print(id(a))

# b=[2,5,4,67,87]
print(id(b))

b=a
print(id(b))



# bitwise operater
a=28
b=19
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(~b)

# print statment
print()
print('the string is printed \n on the new line')
print('we have used \t tab key')
print('welcome to ' + 'rajkot')

a=7 
b=8
print(a)
print(b)
a,b=7,8
print(a,b)
print(a,b,sep="/")

print('atmiya',end='\t')
print('rajkot')
print('gujrat')

# print with operater object
a=[1,2,3,45]
print(a)

a=7
print(a,'the variable value isprinted')
print('the variable' ,a,'value isprinted')

# string formeted string
a=7
print(a,'the variable value is %i'%a)
a=23.2
print('the value is%f'%a)
print('the value is%8.2f'%a)

a,b=7,8
print('a=%i,b=%i' %(a,b))

a='welcome to atmiya university'
print('%s'%a)

uni='atmiya'
print('hi %s'%uni)
print('hi %20s'%uni)
uni='atmiya uni'
print('hi %-20s'%uni)
print('hi %-30s'%uni,'hello')
print('hi %-1s'%uni,'hello')
print('the first character is %c'%uni[0])
print('the first character is %c the second character is %c'%(uni[0],uni[4]))


















