import math
nop=int(input("enter number of players: "))
num_slots = 2 ** math.ceil(math.log2(nop))
data={}
for i in range(1,nop+1):
    ply=input("enter the name of the player: ")
    lvl=int(input("enter number for level/experince of player(beginner(1),intermidiate(2),professional(3)): "))
    data[ply]=lvl
sorted_data=dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
seed=list(sorted_data)
name={i + 1: player for i, player in enumerate(seed)}
slot=[] 
brackets=[]       
for i in range(1,math.ceil(len(name)/2)+1):
    val=(len(name)+1)- i
    brackets.extend((name[i],name[val]))
unique_slots = list(dict.fromkeys(brackets))
for i in range(0, len(unique_slots), 2):
    if i+1<len(unique_slots):
        slot.append((unique_slots[i], unique_slots[i+1]))
    else:
        slot.append((unique_slots[i], None))        
