str1 = input()
l = len(str1)
if(l<3):
    print (str1)
elif(str1[-3:]=="ing"):
    print(str1+"ly")
else:
    print(str1+"ing")
    