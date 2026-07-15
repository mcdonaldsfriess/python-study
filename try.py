try:
    x = int(input("enter a number: "))
    print(10 / x)

except ValueError:
    print("You did not enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")



try:
    risky()

except Exception as e: # 'as e' grabs the error object
    print("An error occurred:", e)
else: 
    print("No errors occurred.")
finally:
    print("This code runs no matter what.")



def withdraw(balance, amout):
    if amout > balance:
        raise ValueError("Insufficient funds.")
    balance -= amout
    return balance
#raise = Java's throw

