#sum of fist 'n' natural numbers

n = int(input("Input your value: "))
sum=0
for num in range(0, n+1, 1):
    sum+= num

print("sum of first ",n, "number is: ", sum)