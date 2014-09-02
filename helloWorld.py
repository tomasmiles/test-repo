#Hello World!
print("Hello World!")
#Declare the variables, python assumes they are ints.
a = 3
b = 2
#Add the strings together (adding the ints together first in the last string).
print(str(a) + " + " + str(b) + " = " + str(a + b))
#To the power of = **
print("2 to the power of 10 = " + str(2 ** 10))
#Conditionals need indents to define the code to execute.
a = 2;
a **= a;
if a >= 16:
	print("a is greater than or equal to 16")
	print(a)
elif a >= 8:
	print("a is greater than or equal to 8 and less that 16")
	print(a)
else:
	print("a is less than 8")
	print(a)
	#def keyword defines functions
	def helloFunction():
		print("Hello. This is the helloFunction.")
	helloFunction()
	#For loop
	for x in range(0, 10):
		print(x)
	#While loop
	x = 0;
	while x < 100:
		if x%10 == 0:
			print(x)
		x+=1;
	#type() returns the type of the argument
	someType = "123490  "
	someType.strip()
	print("Variable someType = " + someType)
	print("someType type is " + str(type(someType)))
	print("Occurences of 1 in someType" + str(someType.count('1')))
	print(str(someType).find('1'))
	print(str(someType).lower())
	print(str(someType).upper())
	print(str(someType).replace('1', '2'))
	#Indices and strings
	print(someType[3:5])
	print(someType[:-4])