fruits={"apple","banana","kiwi","mango","mango","apple",0,False}
print(fruits)
print(type(fruits))
vegitables=list(("cauliflower","spinach","ladyfinger","methi","cauliflower","spinach","ladyfinger","methi"))
print(vegitables)

for x in fruits :
    print(x)
 

fruits.add("tomato")
fruits.update(vegitables)
print(fruits)
set1 = {"a","b","c"}
set2 = {1, 2, 3}
set3= set1.union(set2)
print(set3)
x = {"cherry"}
y = {"google", "microsoft","apple", "banana"}
z = x.intersection(y)
print(z)
q=x.symmetric_difference_update(y)
print(q)


fruits={"apple","banana","kiwi","mango","watermelon"}
vegitables=set(("cauliflower","spinach","apple","banana","kiwi"))
# print(fruits.difference(vegitables))
# print(fruits)
# fruits.difference_update(vegitables)
print(fruits)

# print(fruits.intersection(vegitables))
fruits.remove("banana")
print(fruits)
expensive={"kiwi","mango"}
print(expensive.issubset(fruits))
print(fruits.issuperset(expensive))