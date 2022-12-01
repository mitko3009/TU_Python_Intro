def list_avg(lst,multiplier = 1):
    if type(multiplier) != int:
        print("Error")
        return

    number = []
    sum = 0

    for e in lst:
        if type(e) == int or type(e) == float:
            number.append(e * multiplier)
            sum += e * multiplier
        elif str(e).isdigit():
            number.append(float(e) * multiplier)
            sum += float(e) * multiplier

    if len(number) == 0:
        print("Error division by zero")
        return

    print(sum / len(number))

print(list_avg(['4', 1.5, "@7$", 3.5, (1, "hi")]))

