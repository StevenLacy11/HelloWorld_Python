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

fruitList = ["apples", "grapes", "oranges", "bananas"]

print (fruitList[1:3])

fruitList.append("BlueBerries")

print (fruitList)

fruitList[0] = "Cherries"

print (fruitList)

del fruitList[2]
print (fruitList)

print(len(fruitList))

fruitList2 = ["kiwi", "pineapple", "guava"]

print(fruitList + fruitList2)

print(fruitList2 * 2)

listNum = [1, 4, 7, 23, 6]

print(max(listNum))

print(min(listNum))
