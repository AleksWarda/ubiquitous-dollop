print ("This is a basic calulator that will calculatet the answer between two numbers using the four (+,/,*,-) functions.")

#first number and second number: str refers to a string and int refers to an interger. It has to be an interger to calculate using numbers and a string to print.

numberf_str = input(" First number: ")

numberf = int(numberf_str)

numbers_str = input("Second number: ")

numbers = int(numbers_str)

operation = input("Operation [+, -, /, *]: ")

if operation == "+":
    combination = numberf + numbers

elif operation == "-":
    combination = numberf - numbers

elif operation == "/":
    combination = numberf / numbers

elif operation == "*":
    combination = numberf * numbers

combination_str = str(combination)

print("Your answer is: " + combination_str)

print("Thanks for using this calculator!")

print()
input("Press return to continue ...")
