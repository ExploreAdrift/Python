def countdown(num):
    output = []
    for i in range(num, -1, -1):
        output.append(i)
    return output


print(countdown(5))


def print_return(list):
    print(list[0])
    return list[1]


print(print_return([4, 6]))


def list_return(list):
    return list[0] + len(list)


print(list_return([1, 2, 3, 4, 5]))


def greater(list):
    if len(list) <= 2:
        return False
    output = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(greater([5, 2, 3, 2, 1, 4]))
print(greater([3]))


def lav(list, length):
    output = []
    for i in range(0, list):
        output.append(length)
    return output


print(lav(4, 7))
print(lav(6, 2))
