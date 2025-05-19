
# This is a simple program to print a rectangle of stars
# using nested loops and while loops.


for i in range(4):
    for j in range(10):
        print('*', end='')
    print()

print("________________")
print()

for i in range(4):
    print('*' * 10)

print("________________")
print()

i = 0
while i < 4:
    j = 0
    while j < 10:
        print('*', end='')
        j += 1
    print()
    i += 1

print("________________")
print()

i = 0
while i< 4:
    print('*' * 10)
    i += 1
    