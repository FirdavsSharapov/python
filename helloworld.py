# Importing math library


# from math import *
# print(sqrt(81))
###########
# color = input("Enter a color: ")
# plural_noun = input("Enter a Plular noun: ")
# celebraty =input("Enter Celebraty name: ")
# print("Roses are" + color)
# print(plurlar_noun + "are blue")
# print("I love " + celebraty)

###########   LIST ##################
# lucky_numbers=[4,8,9,10,15,19]
# friends = ["Kevin", "Martin", "Jim", "Oscar"]
# friends[2] = "Simon"
# print(friends[1:3])
# friends.extend(lucky_numbers)
# friends.insert(1, lucky_numbers[2])
# print(friends)
# print(friends.index("Oscar"))
# lucky_numbers.reverse()
# print(lucky_numbers)

############ tuple
# ordinates = (4, 5)
# int(coordinates[0])
##### Functions ######
# def say_hi(name: object, age: object) -> object:
#     print("hello" + name + str(age))
#     print("Bye")
#
#
# say_hi("test", 22)

################ IF .... ELIF...... ELSE (statements)  ##########
# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("You are male or tall")
# elif is_male and not(is_tall):
#     print("You are male but not tall")
# elif is_tall and not(is_male):
#     print("You are tall but not male")
# else:
#     print("you are either not male and not tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(4, 5, 3))





