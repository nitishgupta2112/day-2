
# x= [int(x) for x in input().split()]
# print(x)

n1 =int(input())
n2=int(input())
l1=[i for i in range(n1,n2+1)]
# for i in range(n1,n2+1):
#     l1.append(i)
b = [l1[i:j+1] for i in range(0,len(l1)) for j in range(i,len(l1))]
# for i in range(0,len(l1)):
#     for j in range(i,len(l1)):
#         b.append(l1[i:j+1])
#newlist = [x for x in fruits if "a" in x]

count = 0
for i in range(0,len(b)): 
    if sum(b[i])%2!=0:
        count+=1
print(l1)
print(b)
print(count)
#b = [l[i:j+1] for i in range(0,len(l1)) for j in range(i,len(l1))]
