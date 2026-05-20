# Arithmetic Operator
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333... ← float!
print(a // b)   # 3         ← quotient
print(a % b)    # 1         ← remainder
print(a ** b)   # 1000      ← 10 to the power of 3


# type conversion
num_str = "42"
num = int(num_str)
print(num + 1)              # 43

pi = float("3.14")
print(pi * 2)               # 6.28

# Trap: int() cuts off everything after the decimal part
print(int(3.7))             # 3 (not 4)
print(int(-2.9))            # -2

# conversion is required to combine with a string
age = 25
print("age is " + str(age)) # "age is 25"