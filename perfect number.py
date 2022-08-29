a = int(input("enter a number: "))
print(f"perfect numbers from 0 to {a}: ")
for i in range(1, a+1):
    sum = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)
