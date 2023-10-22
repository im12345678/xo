                                                 xo
one="a"
two="b"
three="c"
four="d"
five="e"
six="f"
seven="g"
eight="h"
nine="i"
a = 0
while a<9 :
    if a <1 :
      z=[one,four,seven]
      x=[two,five,eight]
      v=[three,six,nine]
      for j,k,l in zip(z,x,v) :
         print(j,k,l)  
    a+=1 
    place=input("select a,b,c,d,e,f,g,h,i ? ").strip()
    if place=="a" or place=="b" or place=="c" or place=="d" or place=="e" or place=="f" or place=="g" or place=="h" or place=="i" :
       slove=input("x or o").strip()
       if slove == "x" or slove=="o":
           if place=="a":
             one = slove
           elif place=="b":
             two=slove
           elif place=="c":
             three = slove
           elif place=="d":
              four = slove
           elif place=="e":
              five = slove
           elif place=="f":
             six = slove
           elif place=="g":
             seven = slove
           elif place=="h":
             eight = slove
           elif place=="i":
             nine = slove       
           else :
             raise Exception("you can enter x or o only")
    else :
       raise Exception ("you should select from a to i ")       
    z=[one,four,seven]
    x=[two,five,eight]
    v=[three,six,nine]
    for j,k,l in zip(z,x,v) :
      print(j,k,l)
    if one==two==three or one==four==seven or nine==six==three or seven==eight==nine or six==five==four or five==two==eight:
        print("great you win")
        break
else :
   print("draw")   