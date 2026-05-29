print(5 > 3) # True
print(5 < 3) # False
print(5 >= 3) # True
print (5 == 5) # True
print(5 != 3) # True


age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")



score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:   
    print("Grade: F") 





age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the concert.")
if age < 18 or not has_ticket:
    print("You cannot enter the concert.")




score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: F")
    