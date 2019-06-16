import random

num = random.randint(1,52)
sN= num/13
fN= num%13
# print (str(num)+" "+str(sN)+" "+str(fN))
'''
# print (sN)
if sN < 1:
    suit = "Spades"
elif sN < 2:
    suit = "Hearts"
elif sN < 3:
    suit = "Spades"
elif sN <= 4:
    suit = "Diamonds"
# print(suit)

# print (fN)
if fN==0:
    rank="Ace"
elif fN==1:
    rank="Two"
elif fN==2:
    rank="Three"
elif fN==3:
    rank="Four"
elif fN==4:
    rank="Five"
elif fN==5:
    rank="Six"
elif fN==6:
    rank="Seven"
elif fN==7:
    rank="Eight"
elif fN==8:
    rank="Nine"
elif fN==9:
    rank="Ten"
elif fN==10:
    rank="Jack"
elif fN==11:
    rank="Queen"
elif fN==12:
    rank="King"
# print(rank)
print("The card is a "+rank+" of "+suit)
'''

Suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
Ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
i=0
for i in range (i,len(Suits)):      # "len(List)"= length.Array
    if sN < i+1:
        suit= Suits[(i)]
        break
    elif sN==4:
        suit= Suits[3]
# print(suit)

i=0
for i in range (i,len(Ranks)):
    if fN==i:
        rank = Ranks[i-1]
        break
# print(rank)

print("The card is a "+rank+" of "+suit)
