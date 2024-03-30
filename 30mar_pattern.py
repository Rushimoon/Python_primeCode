# * * * * * 
# *       *
# *       *
# *       *
# * * * * * 


   





for z in range(5+1):
    if z==0 or z==5 :
     str=""
     for t in range(5+1):
       str=str+"* "
     print(str) 
    else :
      bag=""
      for x  in range(5+1) :
       if x==0 or x==5:
        bag=bag+"* "
       else:
        bag=bag+"  "
      print(bag)
    




mylist=[["a","b","c"]
       ,["d","e","f"]
       ,["g","h","i"]]

#o/p--> a,b,c,e,g,h,i