if __name__ == '__main__':
    import random

    quantity = int(input("Let's play in r, p, s.How many times do you want to play: "))
    player = 0
    comp_player = 0
    i = 0
    while quantity != i:
        player = input('Choose r, p or s: ')
        if player == 'r' or player == 'p' or player == 's':
            comp_player = random.randint(1, 3)
            if comp_player == 1:
                print(f'Computer r')
            elif comp_player == 2:
                print(f'Computer p')
            else:
                print(f'Computer s')

            if (comp_player == 1 and player == 'r' or comp_player == 2
                    and player == 'p' or comp_player == 3 and player == 's'):
                comp_player = 0
                player = 0
                print(f"it's a draw.Score: {comp_player}:{player}")
            elif (comp_player == 1 and player == 's' or comp_player == 2
                    and player == 'r' or comp_player == 3 and player == 'p'):
                comp_player += 1
                print(f'Computer win.Score: {comp_player}:{player}')
            else:
                player += 1
                print(f'Player win.Score: {comp_player}:{player}')
            i += 1

    if comp_player > player:
        print(f"Computer win this game.Final score: {comp_player}:{player}")
    elif player > comp_player:
        print(f"Computer win this game.Final score: {player}:{comp_player}")
    else:
        print(f"This's draw!Final score: {player}:{comp_player}")
