  #  0123456789
str="abcdefghijk.ytsjsrthye546"
r="                     abcdefghijk.       ytsjsrthye546             "

print(str[3:6])

print(str[:4])
print(str[5:])

print(str[-6:-1])

print(str.upper())
print(r.upper().strip())

print(str.replace("abcd","wxyz"))


clg="hiiamadityaandistydatghraison"
# clg="hi#i#am#aditya#and#i#styd#at#gh#raison"
print(clg.split("a"))



food=" i ate wada pav  at rs {} and are dosa at rs {}"

c_vp=50
c_dp=100
print(food.format(c_vp,c_dp))
