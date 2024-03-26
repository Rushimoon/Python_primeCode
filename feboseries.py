

ramu=True
while ramu :
     sn=int(input("enter the no of febo serie you want : "))
     n1=0
     n2=1
     jhola= f" {n1} {n2} "

     for x in range(0,sn-2):
         n3=n1+n2

         jhola=jhola+ f" {n3} "
         n1=n2
         n2=n3
     print(jhola)
     aa=int(input("1 to continue 2  to exit "))
     if aa==2 :
       ramu=False
       print("thankyu")
       
     