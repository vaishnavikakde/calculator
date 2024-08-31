print("~~~~~~~~~~~~~~CALCULATOR~~~~~~~~~~~~~~")

n1= float(input("Enter first number here: "))
n2= float(input("Enter second number here: "))

print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")

choice = int(input("Enter your choice from 1-4:  "))

if choice == 1:
    print("The Addition of given two numbers is:",n1 + n2)
elif choice == 2:
    print("The Subtraction of given two numbers is:",n1 - n2)
elif choice == 3:
    print("The Multiplication of given two numbers is:",n1 * n2)
elif choice == 4:
    print("The Division of given two numbers is:",n1 / n2)
else:
    print("Invalid Input")


