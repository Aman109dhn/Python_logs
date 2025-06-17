#map,filter and reduce

# a=[1,2,3,4]
# def val(n):
#     return n**2
# res=list(map(val,a))  #map(function,iterable)
# print(res)


# n=int(input("Enter size of the list: "))
# l=[]
# for i in range(n):
#     l.append(i)
# print(l)

mat=[[1,2,3],
     [4,5,6]]

row=len(mat)
col=len(mat[0])


# for i in range(col):
#     m=[]
#     for j in range(row):
#         m.append(mat[j][i])
#     t.append(m)
# print(t)
 
#using list comprehension

transpose = [[mat[j][i] for j in range(row)] for i in range(col)]
print(transpose)
