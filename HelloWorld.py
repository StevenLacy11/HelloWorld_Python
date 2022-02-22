# # this is my first python code
#
# print("Hello world!")
#
# ################################### variables#############################################
#
# # age = 20
# # sentence = "My name is Steven"
# #
# # print sentence
# #
# # # mike = 23
# # # sarah = 21
# # # bob = 32
# #
# # mike, sarah, bob = 23, 21, 32
# #
# # print mike
# #
# # name, age = "Steven", 26
# #
# # print name
# # print age
#
# ################################ Arithmetic operators ################################################
#
# age1 = 12
# age2 = 18
#
# print (age1 + age2)
#
# print (age1 - age2)
#
# print(age1 * age2)
#
# print (age1/age2)
#
# print (age1 % age2)
#
# sent1 = "Today is a beautiful day"
#
# firstName = "Steven"
# lastName = "Lacy"
#
# print (firstName + " " + lastName)
#
# # print("Hi " * 10)
#
# sentence = "Steven was playing basketball"
#
# print(sentence[0])
#
# print(sentence[4])
#
# #Splicing
# # print(sentence[0:6])
# print(sentence[:6])

###################### PlaceHolders ###########################

# name = "Jake"
#
# # print(name + " is 20 years old")
#
# sent = "%s is 20 years old"
#
# # print(name + sent)
#
# print(sent % name)
#
# print(sent % "bob")
#
# sent = "%s %s is the President of the US"
# print(sent % ("Joe", "Biden"))
#
# sent = "%s is %d years old"
#
# print(sent % ("Joe", 79))


# ############### Lists ##################

# fruitList = ["apples", "grapes", "oranges", "bananas"]
#
# print (fruitList[1:3])
#
# fruitList.append("BlueBerries")
#
# print (fruitList)
#
# fruitList[0] = "Cherries"
#
# print (fruitList)
#
# del fruitList[2]
# print (fruitList)
#
# print(len(fruitList))
#
# fruitList2 = ["kiwi", "pineapple", "guava"]
#
# print(fruitList + fruitList2)
#
# print(fruitList2 * 2)
#
# listNum = [1, 4, 7, 23, 6]
#
# print(max(listNum))
#
# print(min(listNum))

######################Dictonary #####################

# students = ["bob", 21, "Rachel", 31, "emily", 51]
#
# students = {"bob": 21, "Rachel": 31, "emily": 51}
#
# print(students)
#
# print(students["bob"])
#
# students["Rachel"] = 23
#
# print students["Rachel"]
#
# del students["emily"]
# print students
# print len(students)


################# Tuples #########################
######### Can not change a tuple (CONST)#############
# tup = ('oranges', 'apples', 'bananas')

####################Conditionals############################

# if(5 >3):
# 	print ("Hello")

# if (3 < 2):
# 	print("Hello")
# else:
# 	print("The condition is false")

# age = 26
# if (age < 13):
# 	print("You are young")
# ##### elif = else if from java####
# elif(age >= 13 & age < 18):
# 	print ("You are a teenager")
# else:
# 	print("You are an adult")
#
# if (5 > 3 and 2 > 1):
# 	print ("Hi")
#
# if (5 > 3 or 2 <1):
# 	print ("Hello")


########### For loops ######################
#
# list1 = ["apples", "grapes", "oranges", "bananas"]
# tupl = (13, 12, 15)

# for item in list1:
# 	print (item)

# for item in tupl:
# 	print(item)

# for i in range(0,11) :
# 	print(i)

# for i in range(0,11,2):
# 	print(i)

# for i in range(0, 51, 5):
# 	print (i)

# for i in range(0, 5):
# 	for j in range(0, 3):
# 		print(i * j)


# ############### While loops #################
#
# c = 0


# while c < 5:
# 	print(c)
# 	c = c + 1

# while c < 5:
# 	print (c)
#
# 	if c == 3:
# 		break
# 	c = c + 1

# while c < 5:
# 	c = c + 1
# 	if c == 3:
# 		continue
# 	print(c)

# while c < 5:
# 	c = c + 1
# 	if c == 3:
# 		pass    ### filler statment to hold an empty line
# 	print(c)


############## Try and Except##################

# try:
# 	if name > 3:
# 		print("Hello")
# except:
# 	print("There is something wrong with your code - please check again")

# def HelloWorld():
# 	print("Hello World")
#
#
# HelloWorld()
#
#
# def Greeting(name):
# 	print("Hi " + name + "!")
#
#
# Greeting("Steven")
#
#
# def Add(x, y):
# 	print (x + y)
#
# Add(10, 15)
#
# def returnAdd(x,y):
# 	return (x +y)
#
# sum = returnAdd(12,34)
#
# print(sum)

###################### Built-in Function#################

# print(abs(34))
# print(abs(-12))  #### Absolut value!########
#
# bool(1)
# bool(100)
# bool(None)

# print(dir("Hello"))

# sent = "Hello"
# print(help(sent.upper))
#
# print(help(sent.splitlines))

# sent = 'print("Hi")'
# eval(sent)
#
# exec(sent)
#
# a = 1
# print(str(a))
# print (float(a))
# print(int(a))


################# OOP######################
# #
# class Person:
# 	pass
#
#
# p = Person()
#
#
# #
# #
# # class Person:
# # 	def getName(self):
# # 		print("Steven")
# #
# # 	def getAge(self):
# # 		print("26")
# #
# #
# # p = Person()
# # print(p.getName())
# # print(p.getAge())
#
#
# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def getName(self):
# 		print("Your name is " + self.name)
#
# 	def getAge(self):
# 		print("Your age is " + self.age)
#
#
# p1 = Person("Bob", "22")
# print(p1.getName())
# print(p1.getAge())

############## Inheritance ##############################

class Parent:

	def __init__(self):
		print("This is the Parent class")

	def parentFunc(self):
		print("This is the parent function")

p = Parent()

p.parentFunc()

class Child(Parent):

	def __init__(self):

		print("This is the child class")

	def childFunc(self):
		print("This is the child function")

c = Child()

c.childFunc()

c.parentFunc()

class Parent:
	def __init__(self):
		pass

	def test(self):
		print("parent")
p = Parent()
p.test()

class Child(Parent):
	def __init__(self):
		pass
	def test(self):
		print("child")

c = Child()
c.test()





