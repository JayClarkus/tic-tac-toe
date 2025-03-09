import random

grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

options = ["TL", "TM", "TR", "ML", "MM", "MR", "LL", "LM", "LR"]

def divider():
    print("__________")

def draw_map():
    for row in grid:
        for tile in row:
            print (tile, end= " ")
        print()

def player_win_condition():
    if grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        divider()
        draw_map()
        divider()
        print("Player Wins!")
        exit()
    elif grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X":
        divider()
        draw_map()
        divider()
        print("Player Wins!")
        exit()
    elif grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X":
        divider()
        draw_map()
        divider()
        print("Player Wins!")
        exit()

    elif grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X":
        divider()
        draw_map()
        divider()
        print("Player Wins!")
        exit()
    elif grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        divider()
        draw_map()
        divider()
        print("Player Wins!")
        exit()
    elif grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        divider()
        draw_map()
        divider()
        print("Player Wins!")
        exit()

    elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        divider()
        draw_map()
        divider()
        print("Player Wins!")
        exit()
    elif grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        divider()
        draw_map()
        divider()
        print("Player Wins!")
        exit()
    else:
        pass


def computer_win_condition():
    if grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O":
        divider()
        draw_map()
        divider()
        print("Computer Wins!")
        exit()
    elif grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O":
        divider()
        draw_map()
        divider()
        print("Computer Wins!")
        exit()
    elif grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O":
        divider()
        draw_map()
        divider()
        print("Computer Wins!")
        exit()

    elif grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O":
        divider()
        draw_map()
        divider()
        print("Computer Wins!")
        exit()
    elif grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O":
        divider()
        draw_map()
        divider()
        print("Computer Wins!")
        exit()
    elif grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O":
        divider()
        draw_map()
        divider()
        print("Computer Wins!")
        exit()

    elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        divider()
        draw_map()
        divider()
        print("Computer Wins!")
        exit()
    elif grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
        divider()
        draw_map()
        divider()
        print("Computer Wins!")
        exit()
    else:
        pass

def tie_game_condition():
    if options == []:
        divider()
        draw_map()
        divider()
        print("Tie Game!")
        exit()
    else:
        pass

def computer_move():
    computer_choice = random.choice(options)
    print(f"Computer's Turn: {computer_choice}")
    if computer_choice == "TL":
        grid[0][0] = "O"
        options.remove("TL")
    elif computer_choice == "TM":
        grid[0][1] = "O"
        options.remove("TM")
    elif computer_choice == "TR":
        grid[0][2] = "O"
        options.remove("TR")
    elif computer_choice == "ML":
        grid[1][0] = "O"
        options.remove("ML")
    elif computer_choice == "MM":
        grid[1][1] = "O"
        options.remove("MM")
    elif computer_choice == "MR":
        grid[1][2] = "O"
        options.remove("MR")
    elif computer_choice == "LL":
        grid[2][0] = "O"
        options.remove("LL")
    elif computer_choice == "LM":
        grid[2][1] = "O"
        options.remove("LM")
    elif computer_choice == "LR":
        grid[2][2] = "O"
        options.remove("LR")

while True:
    divider()
    draw_map()
    divider()
    print(f"Enter one of the following remaining options: {', '.join(options)}")
    choice = input("Player's Turn: ").upper()
    if choice not in options:
        print("Invalid Input... Try again")
        continue
    elif choice == "TL":
        grid[0][0] = "X"
        options.remove("TL")
    elif choice == "TM":
        grid[0][1] = "X"
        options.remove("TM")
    elif choice == "TR":
        grid[0][2] = "X"
        options.remove("TR")
    elif choice == "ML":
        grid[1][0] = "X"
        options.remove("ML")
    elif choice == "MM":
        grid[1][1] = "X"
        options.remove("MM")
    elif choice == "MR":
        grid[1][2] = "X"
        options.remove("MR")
    elif choice == "LL":
        grid[2][0] = "X"
        options.remove("LL")
    elif choice == "LM":
        grid[2][1] = "X"
        options.remove("LM")
    elif choice == "LR":
        grid[2][2] = "X"
        options.remove("LR")
    else:
        break
    player_win_condition()
    tie_game_condition()
    computer_move()
    computer_win_condition()
