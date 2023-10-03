#Task 1.1
# series = [4,8,16,23,42]
# print (f"{series}",sep=" ")


# #Task 1.2
# series = [4,8,16,23,42]
# print (f"{series[0]}\n{series[1]}\n{series[2]}\n{series[3]}\n{series[4]}")


#Task 1.3
# try:
#     number1 = int(input("Enter the first number: "))
    
#     number2 = number1 + 1
#     number3 = number1 + 2

#     result = f"{number1}\n{number2}\n{number3}"
#     print(result)

# except ValueError:
#     print("Invalid input, please input a valid number")


#Task 1.4
# try:
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     num3 = int(input("Enter the third number:"))
#     result = num1+num2+num3
#     print (f"Result equals:{result}")
# except ValueError:
#     print ("Invalid input, please input a valid number")


#Task 1.5
# try:
#     a = int(input("Enter edge length:"))
#     cube_volume = a **3
#     surface_area = 6*a**2
#     print (f"Volume = {cube_volume}\nTotal surface area = {surface_area}")
# except ValueError:
#     print ("Invalid input, please input a valid number")


#Task 2.1
# try:
#     schoolchildrens = int(input())
#     tangerines = int(input())
#     tangerines_per_schoolchildren, tangerines_left = divmod(tangerines,schoolchildrens)
#     print (f"{tangerines_per_schoolchildren}\n{tangerines_left}")
# except ValueError:
#     print ("Invalid input, please input a valid number")
# except ZeroDivisionError:
#     print ("Number of schoolchildren cannot be zero")


#Task 2.2
# try:
#     num1 = int(input())
#     thousand_pos = (num1//1000)
#     hundred_pos = (num1%1000)//100
#     tens_pos = (num1%100)//10
#     units_pos = num1%10
#     print (thousand_pos, hundred_pos, tens_pos, units_pos, sep="\n")
# except ValueError:
#     print ("Invalid input, please input a valid number")


#Task 2.3
# population = int(input())
# destroyed = population/2
# if destroyed%2!=0:
#     destroyed+=0.5
#     print (f"{destroyed}")
# else:
#     print (f"{destroyed}")


#Task 2.4
# try:
#     number = int(input())
#     result = number << 1
#     if(result == 0):
#         print(f"The result = {result}")
#     else:
#         print(f"The result of >> = {result}")
# except ValueError:
#     print ("Invalid input, please input a valid number")


#Task 2.5
# try:
#     first = float(input())
#     second = float(input())
#     operation = str(input())
#     if (first == str):
#         print ("Invalid input, please input a valid number")
#     if (second == str):
#         print ("Invalid input, please input a valid number")
#     else:
#         print ("Everything is fine")
#     if (operation == '+'):
#         print (f"{first} + {second} = {first + second}")
#     elif (operation == '-'):
#         print (f"{first} - {second} = {first - second}")
#     elif (operation == '/'):
#         print (f"{first} / {second} = {first / second}")
#     elif (operation == '*'):
#         print (f"{first} * {second} = {first * second}")
#     else:
#         print ("Invalid input. Please select one of 4 operations: (+; -; /; *)")
# except ValueError:
#     print ("Invalid input, please input a valid number")
# except ZeroDivisionError:
#     print ("Number of schoolchildren cannot be zero")