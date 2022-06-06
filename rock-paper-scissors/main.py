import random


while (True):
    player_choice = input(" Enter R for rock, P for paper, S for scissors: ")
    any_choice = ['R', 'P', 'S']
    cpu_choice = random.choice('any_choice')
    
    if player_choice == cpu_choice:
        print("it's a tie")
        
    elif player_choice == 'R':
        if cpu_choice == 'P':
            print ("player(rock) : cpu(paper)")
            print("paper covers rock, you loose! game over")
            break
        else:
            print("player(rock) : cpu(scissors)")
            print ("rock smash scissors, you win!! congrats!!")
            break

    elif player_choice == 'P':
        if cpu_choice == 'R':
            print ("player(paper) : cpu(rock)")
            print("paper covers rock,  you win!! congrats!!")
            break
        else:
            print("player(paper) : cpu(scissors)")
            print ("scissors cuts paper, you loose! game over")
            break

    
    elif player_choice == 'S':
        if cpu_choice == 'R':
            print ("player(scissors) : cpu(rock)")
            print("rock smashes scissors, you loose! game over")
            break
        else:
            print("player(scissors) : cpu(paper)")
            print ("scissors cuts paper, you win!! congrats!!")
            break




