""" name = input("what's your name?")
print("hello, " + name)

age = input("how old are you?")
# print(int(age) + 5) This will cause an error because age is a string

print("you are " + age + " years old.")

age = int(input("how old are you?")) # Now we can perform arithmetic operations on age
print(age + 5)
"""


print("what's your favorite number?")
number = int(input())
print(f"your favorite number is {number + 10}")
# or print("your favorite number is " + str(number + 10))