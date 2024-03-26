x=153
ans=0
while x>9 :
    z=x%10 
    ans+=z**3
    x=x//10
    print(z)
   
ans+=x**3
print(ans)