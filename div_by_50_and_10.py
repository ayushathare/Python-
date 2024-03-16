
number = int(input("Enter a number: "))

# Check if the number is divisible by both 10 and 50
if number % 10 == 0 and number % 50 == 0:
    print(number, "is divisible by both 10 and 50.")
else:
    print(number, "is not divisible by both 10 and 50.")
