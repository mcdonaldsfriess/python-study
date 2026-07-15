#math module
import math # import whole module, use as math.sqrt(9)
from math import ceil, sqrt # import one name, use as sqrt(9)
from math import sqrt, pi # import several

print(math.sqrt(16)) # 4.0
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045
print(math.factorial(5)) # 120
print(math.log(math.e)) # 1.0 (natural log of e, ln)
print(math.log(100, 10)) # 2.0 (log base 10 of 100)
print(math.sin(math.pi / 2)) # 1.0 (sine of 90 degrees, radians!)
print(math.floor(3.7)), math.ceil(3.2) # 3 4
print(math.radians(180)) # 3.141592653589793 (convert degrees to radians)



#random module
import random

print(random.random()) # float in [0.0, 1.0)
print(random.randint(1, 10)) # int in [1, 10]
print(random.choice(['apple', 'banana', 'cherry'])) # random choice from list

nums = [1, 2, 3, 4, 5]
random.shuffle(nums) # shuffle list in place
print(nums) # shuffled list



#datetime module
from datetime import datetime, date

now = datetime.now()
print(now) # current date and time
print(now.year, now.month, now.day) # current year, month, and day
print(now.hour, now.minute, now.second) # current hour, minute, and second

today = date.today
print(today) # current date

#format it as a string
print(now.strftime("%Y-%m-%d %H:%M:%S")) # formatted date and time ex)"2026-07-15 14:30"

