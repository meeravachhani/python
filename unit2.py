# working with character
string1='india'
print(string1)
print(type(string1))
character=string1[0]
print(character)
print(type(character))
character=string1[4]
print(character)
character=string1[0:3]
print(character)


# check the type of a character
string1=input('enter a character:-')
character=string1[0]
if character.isalpha():
	print('user has entered an alphabet.')
	if character.isupper():
		print('user has entered an upper case.')
	else:
		print('the characteris an lower case')
else:
	print('user has entered either a number or a special char.')

# working with list
# creting list using rage
# format:range(start,stop,stepsize)

# crate a list having number from 0-9
list1=range(10)
for i in list1:
	print(i,end=" ")

# start to any number
list1=range(11,16)
for i in list1:
	print(i,end=' ')



















