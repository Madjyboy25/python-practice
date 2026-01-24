# This is a simple competition player management system using while loop and if-else in Python.
players=[]
while True:
    print("1-Adding a new player")
    print("2-Removing a player")
    print("3-Displaying all players")
    print("4-Exit")
    choice = input("Enter your choice (1-4):")
    if choice == '1':
        name = input("Enter the name of the new player: ").capitalize()
        if name not in players:
            players.append(name)
            print("Player added successfully!")
        else:
            print("Player already exists!")
    elif choice == '2':
        name = input("Enter the name of the player to remove: ").capitalize()
        if name in players:
            players.remove(name)
            print("Player removed successfully!")
        else:
            print("Player not found!")
    elif choice == '3':
        if players:
            print("List of all players:")
            for player in players:
                print(player)
            if len(players) > 1:
                print(f"We have {len(players)} we can play with!")
        else:
            print("No players in the list!")
