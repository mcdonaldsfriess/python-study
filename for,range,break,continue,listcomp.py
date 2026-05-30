for i in range(5):
    print(i)


range(5) #0, 1, 2, 3, 4
range(2,6) #2, 3, 4, 5
range(0,10,2) #0, 2, 4, 6, 8


#count 1 to 10

for i in range(1,11):
    print(i)



i = 0
while i < 5:
    print(i)
    i += 1

#print input until user types 'exit'

i = 0
while True:
    userInput = input("Type something (or 'exit' to quit): ")
    if userInput.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        print(f"You typed: {userInput}")



    #make list 1 to 10 using list comprehension only even numbers

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)