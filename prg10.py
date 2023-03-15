def translate(dictr,s):
    l=s.split()
    for i in l:
        print(dictr[i],end=" ")
s=input()
dictr ={"merry":"god","chirstmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
translate(dictr,s)