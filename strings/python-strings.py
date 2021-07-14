print('hello')
print("hello")

a = "Hello"
print(a)

# Multiline Strings

a = """
Hi, this is Thilrash
I'm a Software Developer
SLIIT
"""

print(a)

a = '''
Hi, this is Thilrash
I'm a Software Developer
SLIIT
'''

print(a)

# Strings are array

a = "Hello World"
print(a[0])
print(a[1])
print(a[2])

# Looping through the strings

for x in "banana":
    print(x)

# String length

a = "I'm Thilrash"
print(len(a))

# Check String (returns boolean value)
txt = "Welcome to my world"
print("my" in txt)

if "my" in txt:
    print("Welcome to my world!")

# Check if NOT (returns boolean value)
print("Hello" not in txt)

if "Hello" not in txt:
    print("No, 'Hello' is NOT in the text")