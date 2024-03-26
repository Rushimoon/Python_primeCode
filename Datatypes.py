import random


# int a;
# a=12
# int b=12;

a=12
b=12.2
c=5j


print(type(a))
print(type(b))
print(type(c))

z=float(a)
print(type(z))

print(random.randrange(1, 1000000))



# Integers:
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("7889888") # z will be 3

print(type(z))
# Floats:
x = float(1) # x will be 1.0
y = float(2.8) # y will be 2.8
z = float("3") # z will be 3.0
w = float("4.2") # w will be 4.2
print(type(w))

q=complex(555)
print(q)


age=21


print(type(str(age)))




str="Strings in python are surrounded by either single quotation"
kqwestr='Strings in python are surrounded by either single quotation'
l="q"


vardan="""   qwewqe
               wqerwqr
               qrweqwewqewqe
               
               qwewqewqewqewqeqw"""

print(str)
print(kqwestr)
print(vardan)
#     012345 
name="aditya"

print(name[0])
print(name[4])
print(len(vardan))


txt ="The best things in life are free!"

print("bestsss" in txt)
print("best" not in txt)