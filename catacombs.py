import random

#player stats
#wizard or warrior (defines move set)
#health - speed - attack bonus (out of 7, player can distribute 7 stat points in whatever way they like)
#one health pot, refills after each boss

#basic enemies
#can use only attacking/defense moves - no stat moves
#no attack bonus, health and speed are split randomly with 7 stat points

#boss enemies
#every 5 fight is against a boss
#each boss is unique and has some random gimmick that makes it strong
#while boss order can be random, no boss should be repeated and

#fight scenario
#both sides choose one move between a predetermined set of three
#the party with the higher speed stat goes first, ties cannot happen since player speed always be a whole number while opponent speed will always be some whole number +- 0.5
#fight will continue as long as both sides have health > 0
#if player wins, they move onto the next fight with the exact same health and stats, with a chance to use a health pot to heal themselves
#all stats will be increased by +1 after each boss (undecided)



#fight script

modifier = 1

def cleave(targetHealth):
    damage = 15 + random.randrange(5)

    if random.randrange(1, 20) < 2:
        #Crit
        damage = damage * 1.5

    damage = damage * modifier

    return targetHealth - damage

def eschew(userHealth):
    heal = 20 + random.randrange(10)

    modifier = modifier * 0.95

    return heal

def ruleta(targetHealth):
    damage = 10 + random.randrange(8)

    if random.randrange(1, 20) < 10:
        damage = damage * 1.75

    damage = damage * modifier

    return targetHealth - damage

movePool = ['cleave', 'eschew', 'ruleta']

def playerAttack():
    print('Available moves:')
    print(movePool)

    move = input('What will player do? \n')

    if move == movePool[0]:
        effect = cleave(enemyHealth)

    elif move == movePool[1]:
        effect = eschew(playerHeath)

    elif move = movePool[2]:
        effect = ruleta(enemyHealth)

    else:
        print("You didn't pick a valid move, turn passed")

        effect = 0

    return

playerHeath = 100
enemyHealth = 100
