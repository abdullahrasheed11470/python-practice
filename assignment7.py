

def clone_lst(original_list):
    # cloned_list = original_list[:]
    cloned_list = original_list.copy()
    return cloned_list

original_list = [1, 2, 3, 4, 5]
cloned_list = clone_lst(original_list)
print("Original list:", original_list)
print("Cloned list:", cloned_list)

print(id(original_list))
print(id(cloned_list))