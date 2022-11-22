n = int(input("Enter how many numbers you want to input: "))

l = []

for i in range(n):
    number = int(input("Enter number: "))
    l.append(number)

k = int(input("Enter 0 for even indexes or 1 for odd indexes: "))

if k == 0:
    for i in range(1,len(l)):
        if i % 2 == 0:
            l[i] = l[i] + 5

if k == 1:
    for i in range(1,len(l)):
        if i % 2 == 1:
            l[i] = l[i] + 10

print(l)