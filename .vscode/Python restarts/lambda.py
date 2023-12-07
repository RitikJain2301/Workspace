# a=[[1,14],[4,2],[43,42]]
# a.sort(key=lambda x:x[1])
# print(a)

# a="1.2.ddz.ef"
# li=a.split(".")
# print(li)
# n=len(li)-1
# while(n>0):
#     print(li[n]+'.',end='')
#     n-=1
# print(li[0])

li=[3,52,53,37]
# print(type(li))
li2=li[::-1]
# print(type(li2))
print('.'.join(li))