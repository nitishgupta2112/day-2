
def check(num):
    dub = num*2
    n = str(num)
    d = str(dub)
    count=0
    for i in n:
        if i in d:
            count+=1
        else:
            return False
    if(count==len(n)):
        print("True")

num = int(input())
print(check(num))
