number = int(input())
position = int(input())

binary = bin(number).replace("0b","")

if len(binary) < position or position < 1:
    raise Exception("Invalid element. There is no element on this position!")

numAtPosition = int(binary[position - 1])

if numAtPosition == 1:
    print("Yes")
else:
    print("No")
