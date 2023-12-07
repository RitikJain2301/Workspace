li=[5,2,7,4,6,5,2,71,7,3,53,0,4243,5,455,3,5]

### method 1 ###
# def rev(li):
#     for i in range(len(li)-1):
#         j=i+1
#         if li[i]<li[j]:
#             li[i],li[j] = li[j], li[i]
#             # i=0
#             rev(li)
#     return li

# print(rev(li))

### method 2 ###
# i=0
# while i<len(li)-1:
#         j=i+1
#         if li[i]>li[j]:
#             li[i],li[j] = li[j], li[i]
#             i=0
#         else:
#             i+=1

# print(li)
