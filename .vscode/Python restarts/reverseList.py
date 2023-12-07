lst=[3,54,5,34,4,66,5]

# for i in range(len(lst)):
#     lst.insert(i,lst.pop())

# print(lst)

for i in range(len(lst)):
    lst.insert(i,lst[len(lst)-1])
    lst.remove(lst[len(lst)-1])

print(lst)