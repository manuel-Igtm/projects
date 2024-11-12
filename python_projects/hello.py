#Hello, World! – 
# Write a Python program that prints “Hello, World!” and asks for the user’s name, 
# then prints a personalized greeting.

print("Hello World!!")
 
name = input("What is your name:")

def greet(name):
    print(f"Nice to meet you, {name}")

greet(name)