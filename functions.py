def add(a,b):
    return a + b


result = add(5, 3)
print(result)   # 8



def greet(name):
    return f"Hello, {name}!"

x = greet("Soomin")
print(x) # None



def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 7, 1, 9])
print(low, high)  # 1 9 
