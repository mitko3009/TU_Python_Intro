def input_nums(n):
    l = []
    if type(n) == int:
        for i in range(int(n)):
            e = input("Enter a list element: ")
            if str(e).isnumeric():
                l.append(int(e))
    else:
        return []

    return l


def sum_list(lst):
    sum = 0

    for e in lst:
        if type(e) == int or type(e) == float:
            sum += e
        elif str(e).isdigit():
            sum += float(e)


    return sum

def max_of_two(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if a > b or a == b:
            return print(a)
        else:
            return print(b)

    if (type(a) == int or type(a) == float) and (type(b) != int or type(b) != float):
        return print(a)

    if (type(a) != int or type(a) != float) and (type(b) == int or type(b) == float):
        return print(b)

    if (type(a) != int or type(a) != float) and (type(b) != int or type(b) != float):
        return



max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2")

