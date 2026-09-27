# Function - a group of lines that can be called on-demand
# User-Defined Functions
#def - DEFINED
def intro():
    print("Good day everyone!")

# Call the Function
intro()
intro()
intro()

# Name is an argument - data that I can pass to the function
def greeting(name, age, city):
    print(f"Good evening, I am {name} and I am {age} years old.")
    print(f"I live in {city}")

name = "David Etuh"
age = 21
city = input("Where do you live? ")

greeting(name, age, city)