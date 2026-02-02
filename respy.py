'''-------------------------------------
This program will accept and print residences.
-------------------------------------'''

# Comment for title
print("This is the residence")

# Accepts user input
Res= input("Please enter neighborhood: ")
# Num= int(input("Please enter a building number from 100-1000: "))

# Building number input validation
while True:
    try:
        Num= int(input("Please enter a building number from 100-1000: "))
        if Num < 100 or Num > 1000:
            print("Please enter a valid building number from 100-1000: ")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# The print statements
print(Res)
print(Num)