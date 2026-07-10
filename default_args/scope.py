#scope

count = 0

def bump():
    print(count) # you'd think this reads the global...
    count = count + 1 # ...but this assignment makes `count` local everywhere



PI = 3.14159
def area(radius):
    return PI * radius * radius # reads global PI, fine
    



x = 10
def f():
    x = 99 # brand new local, unrelated to outer x

f()
print(x) # still 10

score = 0
def add_points():
    global score # now we can modify the outer score
    score += 1


def counter():
    n = 0
    def step():
        nonlocal n # now we can modify the outer n
        n += 1
        return n
    return step
