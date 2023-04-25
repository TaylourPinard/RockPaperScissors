import random

playing = True
options = ['rock', 'paper', 'scissors']


def play_again(playing):
    while playing:
        print("Play again? Y or N")
        try:
            if input() == 'N':
                return False
            else:
                return True
        except:
            print("Please only type Y or N")
    return playing


def Winner(winner, player_play, comp_play):
    if winner == "It's a tie!":
        print("Player chooses: " + player_play +
          " Computer chooses: " + comp_play + " " + winner)
    else:
        print("Player chooses: " + player_play +
          " Computer chooses: " + comp_play + " " + winner + " wins!")


while playing:
    comp_choice = random.randint(0, 2)
    comp_play = options[comp_choice]

    try:
        print("Please choose a guess; rock, paper, or scissors all lowercase")
        print("The computer will choose randomly, it will not cheat")
        player_play = input()

        # todo: convert this to a switch statement its cleaner
        if player_play == comp_play:
            winner = "It's a tie!"
            Winner(winner, player_play, comp_play)
            playing = play_again(playing)
        elif player_play == "rock" and comp_play == "paper":
            winner = "computer"
            Winner(winner, player_play, comp_play)
            playing = play_again(playing)
        elif player_play == "rock" and comp_play == "scissors":
            winner = "player"
            Winner(winner, player_play, comp_play)
            playing = play_again(playing)
        elif player_play == "paper" and comp_play == "scissors":
            winner = "computer"
            Winner(winner, player_play, comp_play)
            playing = play_again(playing)
        elif player_play == "paper" and comp_play == "rock":
            winner = "player"
            Winner(winner, player_play, comp_play)
            playing = play_again(playing)
        elif player_play == "scissors" and comp_play == "rock":
            winner = "computer"
            Winner(winner, player_play, comp_play)
            playing = play_again(playing)
        else:
            winner = "player"
            Winner(winner, player_play, comp_play)
            playing = play_again(playing)

    except:
        print("please only type rock, paper, or scissors in all lowercase")
        continue
