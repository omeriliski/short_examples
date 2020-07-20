year = ""
while len(str(year)) != 4:
    year = int(input("Dört haneli bir sayı giriniz: "))
if (year%4 == 0) & (year%400 == 0):
    print(f"{year} is a leap year")
else: print(f"{year} is not a leap year")