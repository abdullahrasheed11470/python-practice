#write a program to finf the smalest number in a list
def samallest_number(n):
    smallest_num = n[0]
    for i in n:
        if i < smallest_num:
            smallest_num = i
        return smallest_num
        
n = [2, 3, 4, 5, 6, 7, 8, 9]
result = samallest_number(n)
print("the smallest number in the list is ", result)
