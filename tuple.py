# tuple = ("apple","banana","cherry","apple","cherry")
# length_of_my_tuple=len(tuple)
# print(length_of_my_tuple)

li=["cricket"]
print(type(li))
thistuple = ("apple",)
print(type(thistuple))


nn=tuple(("data"))
print(type(nn))
thistuple = tuple(("apple","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry","banana","cherry"))
print(thistuple[1:-5])


if "kiwi" not in thistuple :
    print("apple is present")

   
players=("ronaldo","messi","dhoni","ashisi","virat","gautam")
hp=("dhayanchand","rohit","manoj","shubhman")
print(players)
plist=list(players)
# del plist
plist[3]="ashish"
players=tuple(plist)
players+=hp
# del players
print(players)


fruits = ("apple","banana","cherry","mango","cherry","mango","cherry","mango","watermelon","kiwi")
(red, yellow,*darkred,green,gsd) = fruits
print(red)
print(yellow)
print(darkred)
print(green)
print(gsd)



fruits = ("apple","banana","cherry")
mytuple = fruits * 8
print(mytuple)