n = int(input())

l = []

for i in range(n):
    m = int(input())
    l.append(m)

m = int(input())

if m == 0:
    for i in range(1,len(l)):
        if i % 2 == 0:
            l[i] = l[i] + 5

if m == 1:
    for i in range(1,len(l)):
        if i % 2 == 1:
            l[i] = l[i] + 10

print(l)