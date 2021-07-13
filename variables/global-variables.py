# Global Variables

x = "awesome"

def myFunc():
    print("Python is " + x)

myFunc()

x = "awesome"

def loacalFunction():
    x = "fantastic"
    print("Python is " + x)

loacalFunction()

y = "best programming"

def myLocalFunc():
    global y
    y = "programming language"

myLocalFunc()

print("Python is " + y)