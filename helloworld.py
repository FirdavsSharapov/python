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

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print(max_num(4, 5, 3))


############ WHILE LOOP ###########
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("done with loop")
#


########### Guessing game #########
# secret_word = "test"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not (out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#         print("Not right, try it again!")
#         print("You have " + str(guess_limit - guess_count) + " more try")
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses, You LOSE")
# else:
#     print("You win!")

#### FOR LOOP #############
# friends = ["Jim", "Karen", "Kevin"]
# len(friends)
# for index in range(len(friends)):
#     print(friends[index])
#     friends["Tim"]
#
# print(friends)

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
#
# print(raise_to_power(3, 2))

###########2D dimenssional list and nested list#############

# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# for row in number_grid:
#     for col in row:
#         print(col)

#
# try:
#     number = int(input("Enter a number:"))
#     print(number)
# except ValueError as err:
#     print(err)

# employees_file = open('c:\test\employees.txt', "r+")
# print (employees_file.readline())
# employees_file.close()

import useful_tools

print(useful_tools.random_dice(9))
