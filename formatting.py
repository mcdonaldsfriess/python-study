name = "Soomin"
age = 20
print(f"Hello, {name}! You are {age} years old.")

#yesterday
print("Name: " + name + ", Age: " + str(age))

#f-string
print(f"Name: {name}, Age: {age}")


# expression inside braces
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} / {b} = {a / b}")
print(f"is even: {a % 2 == 0}")

# number formatting
pi = 3.141592653589793
print(f"pi to 2 decimals: {pi:.2f}")
print(f"pi to 4 decimals: {pi:.4f}")

price = 1234567
print(f"price: ${price:,}")

# multi-line f-string also works
language = "Python"
year = 1991
print(f"{language} was created in {year}, "
      f"making it {2026 - year} years old.")

##
