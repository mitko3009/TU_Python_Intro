n = int(input())
dict = {}

for i in range(n):
    key = input()
    value = input()

    dict[key] = value


m = int(input())
l = []

for k in range(m):
    v = input()
    l.append(v)

for i in range(len(l)):
    e = l[i]
    if dict.get(e):
        l[i] = dict.pop(e)

print(dict)
print(l)