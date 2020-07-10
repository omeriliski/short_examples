number = int(input("Enter a number: "))
prime = True
for i in range(2,number):
    if number%i == 0:
        prime = False
        break
if number == 1: prime = False
print(prime*f"{number} is a Prime number")
print((not prime)*f"{number} is not a Prime number")