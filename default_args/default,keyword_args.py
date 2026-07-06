#default arg

def greet(name = "Soomin"):
    return f"Hello, {name}!"

greet() # Hello, Soomin!
greet("Alex") # Hello, Alex!



#keyword arg

def introduce(name, age):
    print(name, age)

introduce(name = "Soomin", age = 21) # Soomin 21
introduce(age = 21, name = "Soomin")

#Together

def order(item, quantity = 1, size = "Large"):
    print(item, quantity, size)

order("Coffee") # Coffee 1 Large
order("Coffee", quantity = 2) # Coffee 2 Large
order(item = "coffee", size = "Medium", quantity = 3) # Coffee 3 Medium


#INVALID
# def example(x=10,y)
#     pass

#CORRECT
def example(y, x=10):
    pass