def functions(str1):
    l=len(str1)
    if(l>=2):
        return (str1[:2]+str1[-2:])
    else:
        return ("-1")
        
str1 = input()
print(functions(str1))
    