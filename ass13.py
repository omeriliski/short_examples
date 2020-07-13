j = 0 
i = 0
fibo = []
while i < 55:
    if i < 2: 
        fibo.append(1)
        i += 1
    else:
        fibo.append(fibo[j-2] + fibo[j-1])
        i = fibo[j-2] + fibo[j-1]
    j += 1
print(fibo)