# refactor file 
import math
def input_players():
    total_players = int(input("Enter the total number of players: "))
    data={}
    for i in range(total_players):
        player_name = input(f"Enter the name of player {i + 1}: ")
        player_experience = int(input(f"Enter the experience level of {player_name} (1-3): "))
        data[player_name] = player_experience
    num_slots = 2 ** math.ceil(math.log2(total_players))
    sorted_data=dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    seed=list(sorted_data)
    return seed, num_slots,total_players
def generate_seed_order(num_slots, total_players, seed):

    player_name = {i + 1: player for i, player in enumerate(seed)}

    for i in range(total_players + 1, num_slots + 1):
        player_name[i] = None

    seed_order = [1]

    while len(seed_order) < num_slots:
        m = len(seed_order) * 2
        seed_order = [x for s in seed_order for x in (s, m + 1 - s)]

    return seed_order, player_name
def create_first_round(seed_order,num_slots,player_name):
    pairs=[]
    for i in range(0, num_slots, 2):
        pairs.append((player_name[seed_order[i]], player_name[seed_order[i+1]]))
    bye=[]
    match=[]
    for i in pairs:
        if None in i:
            bye.append(i[0])
        else:
            match.append(i)
    return bye,match
def get_match_winners(match):
    winners=[]
    for i in match:
        while True:
            inp=input("enter the winner of the match betweeen {} and {}: ".format(i[0],i[1]))
            if inp==i[0] or inp==i[1]:
                winners.append(inp)
                break
            else:
                print("Invalid input.")
    return winners
def arrange_next_round(alive_players,bye,winners):
    alive_players=bye+winners 
    seed_order = [1]
    while len(seed_order) < len(alive_players):
        m = len(seed_order) * 2
        seed_order = [x for s in seed_order for x in (s, m + 1 - s)]
    alive_players = [alive_players[seed_order[i] - 1] for i in range(len(seed_order))]
    return alive_players
def play_remaining_rounds(alive_players):
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
def main():
    seed, num_slots, total_players = input_players()
    seed_order, player_name = generate_seed_order(
        num_slots,
        total_players,
        seed
    )
    bye, match = create_first_round(
        seed_order,
        num_slots,
        player_name
    )
    winners = get_match_winners(match)
    alive_players = arrange_next_round(
        [],
        bye,
        winners
    )
    play_remaining_rounds(alive_players)
main()