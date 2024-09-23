import random
ezr =["apple","mango","vegitables","orange"]
chooseword=random.choice(ezr)
player1=list(chooseword)
player21=[]
for i in chooseword:
    player21 +="_"
picture=["picture1","picture2","picture3","picture4","picture5"]
life=len(picture)
lo=0
l1=0
ezra=int(len(player1))
ezra1=int(len(player21))
x=0
while life!=1 and x!=ezra1:
    player2 =input("guess the word you belive player1 put : ")
    for len in range(ezra1):
        if player2==player1[len]:
            player21[len]=player1[len]
            print(player21)
            print(picture[l1])
            x=x+1
            break
    else:
       lo=lo + 1
       pictur=picture[lo]
       picture[l1]=pictur
       print(pictur)
       life = life - 1
       print(f"you are left with {life} life please play care fully ")











