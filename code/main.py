import math
Round=1
def heading(title):

    print("╔" + "═"*56 + "╗")
    print("║" + title.center(56) + "║")
    print("╚" + "═"*56 + "╝")
    print()
def register_player():
    heading("PLAYER REGISTRATION")
    total_players = int(input("Enter the total number of players: "))
    data={}
    for i in range(total_players):
        print()
        print(f"Player {i+1}")
        print("-" * 20)

        player_name = input("Name            : ")
        player_experience = int(input("Experience(1-3) : "))
        data[player_name] = player_experience
    num_slots = 2 ** math.ceil(math.log2(total_players))
    sorted_data=dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    seed=list(sorted_data)
    return seed, num_slots,total_players
def generate_fixtures(num_slots, total_players, seed, winners, bye,alive_players):
    heading("GENERATE FIXTURES")
    pairs=[]
    match=[]
    if Round>1: 
        if Round==2:
            bye.clear()
            pass
        else:
            alive_players=winners    
        print("Remaining Players: ",len(alive_players))
        input("\nPress Enter to generate fixtures for round {}...".format(Round))
        seed_order = [1]
        while len(seed_order) < len(alive_players):
            m = len(seed_order) * 2
            seed_order = [x for s in seed_order for x in (s, m + 1 - s)]
        alive_players = [alive_players[seed_order[i] - 1] for i in range(len(seed_order))]
        match=[]
        winners=[]
        for i in range(0,len(alive_players),2):
            if i+1<len(alive_players):
                match.append((alive_players[i],alive_players[i+1]))
        print("\nFixtures generated successfully!")
        input("\nPress Enter to return to the Main Menu...")            
    else:
        print("Registered Players: ",len(seed))
        print("Bracket size      : ",num_slots)
        print("Byes required     : ",num_slots - total_players)
        input("\nPress Enter to generate fixtures for round {}...".format(Round))
        player_name = {i + 1: player for i, player in enumerate(seed)}

        for i in range(total_players + 1, num_slots + 1):
            player_name[i] = None

        seed_order = [1]
        bye=[]
        while len(seed_order) < num_slots:
            m = len(seed_order) * 2
            seed_order = [x for s in seed_order for x in (s, m + 1 - s)]
        for i in range(0, num_slots, 2):
            pairs.append((player_name[seed_order[i]], player_name[seed_order[i+1]]))
        for i in pairs:
            if None in i:
                bye.append(i[0])
            else:
                match.append(i)
        print("\nFixtures generated successfully!")
        input("\nPress Enter to return to the Main Menu...")        
    
    return bye,match
def match_result(match,winners,alive_players,bye):
    heading("ENTER MATCH RESULTS")
    
    if len(winners)>0:
        winners.clear()
        alive_players.clear()
    else:
        winners=[]    
    for i in range(len(match)):
        while True:
            print("MATCH ",i+1)
            print("{} VS {} ".format(match[i][0],match[i][1]))
            print("Winner")
            print(1,match[i][0])
            print(2,match[i][1])
            inp=int(input("Enter choice: "))
            if inp==1 or inp==2:
                winners.append(match[i][inp-1])
                print("SAVED!")
                print("-"*56)
                break
            else:
                print("Invalid input.")
    match.clear()
    
    alive_players=bye+winners
    
    print("All match results have been entered successfully!")
    if len(winners) > 1:
        print("You can now generate fixtures for the next round.")
    input("\nPress Enter to return to the Main Menu...")            
    return winners,alive_players
def view_players(seed,alive_players):
    heading("REGISTERED PLAYERS")
    print()
    if Round>1:
        print("Total number of players: {}".format(len(alive_players)))
        print()
        print("┌─────────┬──────────────────────┐")
        print("│ ID/Seed │ Name                 │")
        print("├─────────┼──────────────────────┤")
        for i in range(len(alive_players)):
            print(f"│ {i+1:<7} │ {alive_players[i]:<20} │")
            print("└─────────┴──────────────────────┘")
        input("\nPress Enter to return to the Main Menu...")
    else:
        print("Total number of players: {}".format(len(seed)))
        print()
        print("┌─────────┬──────────────────────┐")
        print("│ ID/Seed │ Name                 │")
        print("├─────────┼──────────────────────┤")
        for i in range(len(seed)):
            print(f"│ {i+1:<7} │ {seed[i]:<20} │")
            print("└─────────┴──────────────────────┘")
        input("\nPress Enter to return to the Main Menu...")
def view_fixtures(match):
    global Round
    heading("TOURNAMENT FIXTURES")
    print("Round: ",Round)
    print()
    print("FIXTURES")
    print()
    print("-" * 56)
    for i in range(len(match)):
        print("Match ",(i+1))
        print(match[i][0])
        print("          VS")
        print(match[i][1])
        print("-" * 56)
       
def menu():
    global Round
    heading("TOURNAMENT SYSTEM")
    print()
    print("1. Register Player")
    print("2. View Players")
    print("3. Generate Fixtures for Round {}".format(Round))
    print("4. View Fixtures for Round {}".format(Round))
    print("5. Enter Match Result")
    print("6. Next Round")
    print("0. Exit")

    print()

    choice = input("Enter your choice: ")

    return choice                    
def main():

    global Round

    seed = []
    match = []
    bye = []
    winners = []
    alive_players = []

    num_slots = 0
    total_players = 0

    while True:

        choice = menu()

        if choice == "1":

            seed, num_slots, total_players = register_player()


        elif choice == "2":

            if len(seed) == 0:
                print("\nNo players have been registered yet.")
                input("\nPress Enter to return to the Main Menu...")
            else:
                view_players(seed, alive_players)


        elif choice == "3":

            if len(seed) == 0:
                print("\nPlease register players first.")
                input("\nPress Enter to return to the Main Menu...")
            else:
                bye, match = generate_fixtures(
                    num_slots,
                    total_players,
                    seed,
                    winners,
                    bye,
                    alive_players
                )


        elif choice == "4":

            if len(match) == 0:
                print("\nNo fixtures available.")
                input("\nPress Enter to return to the Main Menu...")
            else:
                view_fixtures(match)


        elif choice == "5":

            if len(match) == 0:
                print("\nGenerate fixtures first.")
                input("\nPress Enter to return to the Main Menu...")
            else:
                winners, alive_players = match_result(
                    match,
                    winners,
                    alive_players,
                    bye
                )
            Round += 1
            if len(alive_players) == 1:
                print("\nTournament Champion:", alive_players[0])
                seed.clear()
                num_slots =0
                total_players =0
                bye.clear()
                match.clear()
                winners.clear()
                alive_players.clear()
                Round = 1
                input("\nPress Enter to continue...")    


        elif choice == "6":

            if len(winners) == 0:
                print("\nPlease enter all match results first.")
                input("\nPress Enter to return to the Main Menu...")
            elif len(alive_players) == 1:
                print("\nTournament has already finished.")
                input("\nPress Enter to return to the Main Menu...")
            else:
                print("\nGenerating fixtures for the next round...")

                bye, match = generate_fixtures(
                    num_slots,
                    total_players,
                    seed,
                    winners,
                    bye,
                    alive_players
                )


        elif choice == "0":

            print("\nThank you for using the Tournament Manager!")
            break


        else:

            print("\nInvalid Choice!")
            input("\nPress Enter to continue...")
if __name__ == "__main__":
    main()            