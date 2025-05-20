Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
result = []
# in the different list result=[]
for i , x in enumerate(Sample_List):

    if i not in (0,4,5):
        result.append(x)
print(result)

# in the same list
for i in sorted((0,4,5), reverse=True):
    del Sample_List[i]
print(Sample_List)
