from capitols import states
import random


def play_states(states):
    correct = 0
    false = 0
    random.shuffle(states)

    want_to_play = input("Welcome to State Capitals, do you want to play?\n")

    if(want_to_play == "yes"):
        for i in range(0, len(states)):
            answer = input(f'what is the capital of {states[i]["name"]}\n')
            if(answer == states[i]["capital"]):
                correct += 1
            else:
                false += 1

            print(f"You have {correct} correct and {false} wrong")

        play_again = input('do you want to play again?\n')
        if(play_again == 'yes'):
            play_states(states)
    else:
        print('goodbye')



play_states(states)