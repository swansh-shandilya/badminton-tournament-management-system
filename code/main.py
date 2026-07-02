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
for i in range(nop + 1, num_slots + 1):
    name[i] = None
seed_order = [1]
while len(seed_order) < num_slots:
    m = len(seed_order) * 2
    seed_order = [x for s in seed_order for x in (s, m + 1 - s)]
pairs = []
for i in range(0, num_slots, 2):
    pairs.append((name[seed_order[i]], name[seed_order[i+1]]))
bye=[]
match=[]
for i in pairs:
    if None in i:
        bye.append(i[0])
    else:
        match.append(i)    
winners=[]
for i in match:
    while True:
        inp=input("enter the winner of the match betweeen {} and {}: ".format(i[0],i[1]))
        if inp==i[0] or inp==i[1]:
            winners.append(inp)
            break
        else:
            print("Invalid input.")    
alive_players=bye+winners 
seed_order.clear()
seed_order = [1]
while len(seed_order) < len(alive_players):
    m = len(seed_order) * 2
    seed_order = [x for s in seed_order for x in (s, m + 1 - s)]
alive_players = [alive_players[seed_order[i] - 1] for i in range(len(seed_order))]
match=[]
winners=[]
while len(alive_players)>1:
    for i in range(0,len(alive_players),2):
        if i+1<len(alive_players):
            match.append((alive_players[i],alive_players[i+1]))
    for i in match:
        while True:
            inp=input("enter the winner of the match betweeen {} and {}: ".format(i[0],i[1]))
            if inp==i[0] or inp==i[1]:
                winners.append(inp)
                break
            else:
                print("Invalid input.")                      
    alive_players.clear()
    alive_players.extend(winners)
    match.clear()
    winners.clear()
if len(alive_players)==1:
    print("The winner of the tournament is: {}".format(alive_players[0]))  