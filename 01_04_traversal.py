# mylist=[[["a","b","c"]
#        ,["d","e","f"]
#        ,["g","h","i"]],
#        [["j","k","l"] 
#        ,["m","n","o"]
#        ,["o","q","r"]]]

# print(mylist[1][1][0])


mylist=[["a","b","c"]
       ,["d","e","f"]
       ,["g","h","i"]]

print(mylist[0][0])
print(mylist[0][1])  
print(mylist[0][2])

r=0
c=0
# 1
# 2
bag=""
while(c<=2):
  bag=bag+mylist[r][c]+" "
  c+=1


r=0
c=2

while(r<=2) :
  bag=bag+mylist[r][c]+" "
  r+=1
  c-=1

r=2
c=0
while(c<=2) :
  bag=bag+mylist[r][c]+" "
  c+=1
  

print(bag)


newlist=[["a","b","c","d"],
         ["e","f","g","h"],
         ["i","j","k","l"],
         ["m","n","o","p"]]


