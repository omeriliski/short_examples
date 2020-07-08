# assigment 11 Armstrong Number
sum = 0
a = True
while a == True:
    number = input("Please enter a number: ")
    if  not number.isnumeric():
        a = True
    elif int(number) < 0:
        a = True 
    else:
        a = False
    print(a * "it is an invalid entry. Don't use non-numeric, float, or negative values!")    
for i in number:
    sum += (int(i)**len(number))
if sum == int(number):
    print(f"{number} is an Armstrong Number")
else:
    print(f"{number} is not an Armstrong Number")