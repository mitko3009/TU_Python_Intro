number = int(input())
n = number
sum = 0

for i in range(n):

    print(str(number),end="")

    if n - i == 1:
        print(end=" = ")
    else:
        print(end=" + ")
    sum +=number
    number = n + number * 10

print(sum,end="")