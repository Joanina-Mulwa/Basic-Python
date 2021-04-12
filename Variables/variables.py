# Variables are containers for storing data vales
# in python, variables are created when you assign a value to it
# variables are case sensitive
# you can use single or double quotes while assigning values to variables
x = 5
print(x)

# variable type can be changed after been set
# above, x had been declared ogf type int, now we will declare it of type str

x = "Sally"
print(x)

# casting is specifying data type of a variable
x = int(3)
y = str(3)
z = float(3)
print(x)
print(y)
print(z)

# to get the data type of a variable use the type function
x = 5
y = "John"
print(type(x))
print(type(y))

# assigning many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# assigning one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpacking a collection
fruits = ["Banana", "Orange", "Apple"]
x, y, z = fruits
print(x)
print(y)
print(z)

# creating a global variable inside a function
x = "Awesome"
print("Python is " + x)


def myfunction():
    global x
    x = "Fantastic"


myfunction()

print("Python is " + x)
