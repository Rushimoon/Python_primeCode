str=input("enter the string - \n")

# print(str)

# str="aabbara"
p1=0
p2=len(str)-1
ispal=True
while(p1<p2):
     if(str[p1]!=str[p2]):
          ispal=False
     p1+=1
     p2-=1     


if(ispal):
     print("it is palendrome")
else:
     print("it is not palendrome")