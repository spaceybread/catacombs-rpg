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

import random

def cleave():
    return 20

def eschew():
    return 25 + random.randrange(3)

def ruleta():
    return 15 + random.randrange(10)

def rage():
    return 0

def move(isEnemy):

    if isEnemy == True:
        move = random.choice([0, 1, 2, 3])
        user = 'Enemy'
    else:
        move = int(input('What will you do? '))
        user = 'You'

    if move == 0:
        print('{} used cleave!'.format(user))
        effect = cleave()
        modifier = 0
        type = 0

    if move == 1:
        print('{} used eschew!'.format(user))
        effect = eschew()
        modifier = -0.6
        type = 1

    if move == 2:
        print('{} used ruleta!'.format(user))
        effect = ruleta()
        modifier = 0
        type = 0

    if move == 3:
        print('{} used rage'.format(user))
        effect = rage()
        modifier = 1.5
        type = 2


    return [effect, modifier, type]

#while True:
#    outcome = move(False)

#    if outcome[2] == 0:
#        calcDamage = outcome[0] * attkBoost
#        print('You did {} damage'.format(calcDamage))
#        attkBoost = attkBoost * outcome[1]
#        print('Attack modifier is {}'.format(attkBoost))

#    if outcome[2] == 1:
#        print('You healed {} hit points'.format(outcome[0]))
#        attkBoost = attkBoost * outcome[1]
#        print('Attack modifier is {}'.format(attkBoost))

#    if outcome[2] == 2:
#        print('You boosted attack')
#        attkBoost = attkBoost * outcome[1]
#        print('Attack modifier is {}'.format(attkBoost))


playerHealth = 500
enemiesDefeated = 0

while True:

    print('Enemies defeated: {}'.format(enemiesDefeated))

    attkBoost = 1
    eAttkBoost = 1

    enemyHealth = 100 + (20 * enemiesDefeated)

    playerSpeed = random.randrange(5)
    enemySpeed = random.randrange(5) - 0.5

    print('Your speed stat: {}'.format(playerSpeed))
    print('Enemy speed stat: {}'.format(enemySpeed))
    input()

    print('Entering combat...')

    while True:
        print('Your health: {}'.format(playerHealth))
        print('Enemy health: {}'.format(enemyHealth))

        print('')

        playerMove = move(False)

        enemyMove = move(True)

        if playerSpeed > enemySpeed:

            if playerMove[2] == 0:
                calcDamage = playerMove[0] * attkBoost
                enemyHealth = enemyHealth - calcDamage
                print('You did {} damage'.format(calcDamage))
                attkBoost = attkBoost + playerMove[1]
                print('Attack modifier is {}'.format(attkBoost))

            if playerMove[2] == 1:
                playerHealth = playerHealth + playerMove[0]
                print('You healed {} hit points'.format(playerMove[0]))
                attkBoost = attkBoost + playerMove[1]
                print('Attack modifier is {}'.format(attkBoost))

            if playerMove[2] == 2:
                print('You boosted attack')
                attkBoost = attkBoost + playerMove[1]
                print('Attack modifier is {}'.format(attkBoost))

            if enemyHealth < 1:
                print('You win!')
                print('Onto the next enemy!')

            else:
                if enemyMove[2] == 0:
                    calcDamage = enemyMove[0] * eAttkBoost
                    playerHealth = playerHealth - calcDamage
                    print('Enemy did {} damage'.format(calcDamage))
                    eAttkBoost = eAttkBoost + enemyMove[1]
                    print('Attack modifier is {}'.format(eAttkBoost))

                if enemyMove[2] == 1:
                    enemyHealth = enemyHealth + enemyMove[0]
                    print('Enemy healed {} hit points'.format(enemyMove[0]))
                    eAttkBoost = eAttkBoost + enemyMove[1]
                    print('Attack modifier is {}'.format(eAttkBoost))

                if enemyMove[2] == 2:
                    print('Enemy boosted attack')
                    eAttkBoost = eAttkBoost + enemyMove[1]
                    print('Attack modifier is {}'.format(eAttkBoost))

                if playerHealth < 1:
                    print('Enemy Wins T-T')
                    exit()
        else:
            if enemyMove[2] == 0:
                calcDamage = enemyMove[0] * eAttkBoost
                playerHealth = playerHealth - calcDamage
                print('Enemy did {} damage'.format(calcDamage))
                eAttkBoost = eAttkBoost + enemyMove[1]
                print('Attack modifier is {}'.format(eAttkBoost))

            if enemyMove[2] == 1:
                enemyHealth = enemyHealth + enemyMove[0]
                print('Enemy healed {} hit points'.format(enemyMove[0]))
                eAttkBoost = eAttkBoost + enemyMove[1]
                print('Attack modifier is {}'.format(eAttkBoost))

            if enemyMove[2] == 2:
                print('Enemy boosted attack')
                eAttkBoost = eAttkBoost + enemyMove[1]
                print('Attack modifier is {}'.format(eAttkBoost))

            if playerHealth < 1:
                print('Enemy Wins T-T')
                exit()

            else:
                if playerMove[2] == 0:
                    calcDamage = playerMove[0] * attkBoost
                    enemyHealth = enemyHealth - calcDamage
                    print('You did {} damage'.format(calcDamage))
                    attkBoost = attkBoost + playerMove[1]
                    print('Attack modifier is {}'.format(attkBoost))

                if playerMove[2] == 1:
                    playerHealth = playerHealth + playerMove[0]
                    print('You healed {} hit points'.format(playerMove[0]))
                    attkBoost = attkBoost + playerMove[1]
                    print('Attack modifier is {}'.format(attkBoost))

                if playerMove[2] == 2:
                    print('You boosted attack')
                    attkBoost = attkBoost + playerMove[1]
                    print('Attack modifier is {}'.format(attkBoost))

                if enemyHealth < 1:
                    print('You win!')
                    print('Onto the next enemy!')
                    #exit()

    enemiesDefeated = enemiesDefeated + 1
