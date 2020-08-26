from words import words
import winsound
import random
def draw(n):
    if(n==1):
        print("+---+")
        print("|   |")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("=========")
    elif(n==2):
        print(" +---+")
        print(" |     |")
        print(" O    |")
        print("       |")
        print("       |")
        print("       |")
        print("=========")
    elif(n==3):
        print(" +---+")
        print(" |     |")
        print(" O    |")
        print(" |     |")
        print("       |")
        print("       |")
        print("=========")
    elif(n==4):
        print(" +---+")
        print(" |     |")
        print(" O    |")
        print("/|     |")
        print("       |")
        print("       |")
        print("=========")
    elif(n==5):
        print(" +---+")
        print(" |     |")
        print(" O    |")
        print("/|\   |")
        print("       |")
        print("       |")
        print("=========")
    elif(n==6):
        print(" +---+")
        print(" |     |")
        print(" O    |")
        print("/|\   |")
        print("/      |")
        print("       |")
        print("=========")
    elif(n==7):
        print("YOU KILLED HANG MAN")
        print(" +---+")
        print(" |     |")
        print(" O    |")
        print("/|\   |")
        print("/ \   |")
        print("       |")
        print("=========")
        print("correct word","".join(word))
        winsound.PlaySound("headshot.wav",winsound.SND_ASYNC)
word=list(random.choice(words))
l=[]
for i in range(len(word)):
    l.append("_")
kill=0
chose=[]
winsound.PlaySound("helpme.wav",winsound.SND_LOOP+winsound.SND_ASYNC)
print(" ".join(l))
while(kill<7):
    print("already choosen =>",chose)
    c=input("try your luck => ")
    if(c in word):
        for i in range(len(l)):
            if(word[i]==c):
                l[i]=c
    else:
        kill+=1
    draw(kill)
    chose.append(c)
    print(" ".join(l))
    
    if(l==word):
        print("u saved hang man")
        winsound.PlaySound("clap.wav",winsound.SND_ASYNC)
        print("correct ans was : ","".join(word))
        break
    print("-----------------------------------------------")
