# remove dublicates from a list by using set
def remoove_dublicates(l):
    return list(set(l))

l = [1,1,1,2,2,3,4,5,6,6,7,8,]
result = remoove_dublicates(l)
print(result)


#remove dublicates from a list by using dict and maintaining the order of elements
def remove_dublicates(l):
    return list(dict.fromkeys(l))

l = [1,1,1,2,2,3,4,5,6,6,7,8,]
result = remove_dublicates(l)
print(result)

#remove dublicates from a list by using set while maintaining the order of elements

def remove_dubs(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result

l = [1,1,1,2,2,3,4,5,6,6,7,8,]
result = remove_dubs(l)
print(result)