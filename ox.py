user1="A"
user2="B"
user3="C"
user4="D"
user5="E"
user6="F"
user7="G"
user8="H"
user9="I"
k=0
while k<9:
    if k<1 :
     a =[user1,user4,user7]
     b=[user2,user5,user8]
     c = [user3,user6,user9]
     for d,e,f in zip(a,b,c):
        print(d,e,f)
    place = input(" Which place do you prefer A,B,C,D,E,F,G,H,I? ").strip()
    if place == "A"  : 
        user1=input("X OR O").strip()
    elif place == "B":
        user2=input("X OR O").strip()
    elif place == "C":
         user3=input("X OR O").strip()
    elif place == "D":
        user4=input("X OR O").strip()
    elif place == "E":
        user5=input("X OR O").strip()
    elif place == "F":
        user6=input("X OR O").strip()
    elif place == "G":
        user7=input("X OR O").strip()                   
    elif place == "H":
        user8=input("X OR O").strip()
    elif place == "I":
        user9=input("X OR O").strip()
    a =[user1,user4,user7]
    b=[user2,user5,user8]
    c = [user3,user6,user9]
    for d,e,f in zip(a,b,c):
        print(d,e,f)    



    if user1==user2==user3 or user1==user4==user7 or user9==user6==user3 or user7==user8==user9 or user6==user5==user4 or user5==user2==user8:
        print("great you win")
        break        
   
    k+=1    
else:
    print("draw try again")




