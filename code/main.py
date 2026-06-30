import math
nop=int(input("enter number of players: "))
num_slots = 2 ** math.ceil(math.log2(nop))
data={}
for i in range(1,nop+1):
    ply=input("enter the name of the player: ")
    lvl=int(input("enter number for level/experince of player(beginner(1),intermidiate(2),professional(3)): "))
    data[ply]=lvl
sorted_data=dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
name=list(sorted_data)
def seed_positions(num_slots):
    positions = [1]
    while len(positions) < num_slots:
        positions = [x for pair in positions for x in (pair, num_slots + 1 - pair)]    
    return positions
seeded_slots = seed_positions(num_slots)
slots=[]        
for seed in seeded_slots:       
    if seed <= len(name):
        slots.append(name[seed])
    else:
        slots.append(None)
print(slots)
