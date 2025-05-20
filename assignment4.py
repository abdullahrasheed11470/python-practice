


def list_multiplication(lst):
    if len(lst) == 0:
        return 1
    return lst[0] * list_multiplication(lst[1:])

l = [1,3,5,7,11]
print(list_multiplication(l))