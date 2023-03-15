l1 = list(map(int,input().strip().split()))
n = int(input())
count = 0
for i in range(0,len(l1)):
    for  j in range(i+1,len(l1)):
        if l1[i]+l1[j]==n:
            count+=1
            print(l1[i],l1[j])
        else:
            continue
print(count)
