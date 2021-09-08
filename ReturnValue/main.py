print("Welcome to Python")
# Return value
a = 11
print("a is ", a)
print("a is ", a, "is b", end="\n")

# using sep and end argument
print("a is ", a, sep="XYZ", end="\n")
print("a is ", a, sep="XYZ", end="$$$\n\n\n")

# Taking string input from the user
name = input("Enter your name ")
print("The student name is", name, end="\n\n")

# Taking other data types from the user
Cat1 = int(input("Enter the students Cat1 marks "))
print(name, "cat 1 marks is", Cat1, end="\n\n")
Cat2 = int(input("Enter the students Cat2 marks "))
print(name, "cat 2 marks is", Cat2, end="\n\n")

# Python + operator
Cat = Cat1 + Cat2
print(name, "Total Cat marks is", Cat, end="\n\n")


