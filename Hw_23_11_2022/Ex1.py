number = int(input())

f = 0
k = 1


print(k,end=" ")
for i in range(number + 1):
    j = f + k
    f = k
    k = j
    print(j,end=" ")

