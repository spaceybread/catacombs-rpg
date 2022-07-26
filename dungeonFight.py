import random

def cleave():
    damage = 10 + random.randrange(8)

    return damage

def ruleta():
    damage = 5 + random.randrange(7)
    
    modifier = random.choice([0.5, 1, 1, 1, 1, 1, 1.25, 1.25, 2])

    damage = damage * modifier

    return damage

moveList = [cleave(), ruleta()]

playerHealth = 100
enemyHealth = 100

playerSpeed = random.randrange(5)
enemySpeed = random.randrange(5) - 0.5

print(playerSpeed)
print(enemySpeed)

print('Entering combat...')

while True:
    input()
    print('Your health: {}'.format(playerHealth))
    print('Enemy health: {}'.format(enemyHealth))

    print('')

    print('0 for Cleave \n1 for Ruleta \n')

    playerMove = int(input('What will you do? ')

    enemyMove = random.choice([0, 1])

    if playerSpeed > enemySpeed:
        enemyHealth = enemyHealth - moveList[playerMove]

        print('You used cleave')
        print('Enemy health: {}\n'.format(enemyHealth))


        if enemyHealth <= 0:
            print('You win!')
            exit()

        else:
            playerHealth = playerHealth - moveList[enemyMove]

            print('Enemy used cleave')
            print('Your health: {}\n'.format(playerHealth))

            if playerHealth <= 0:
                print('Enemy wins T-T')
                exit()
    else:
        playerHealth = playerHealth - moveList[enemyMove]

        print('Enemy used cleave')
        print('Your health: {}\n'.format(playerHealth))

        if playerHealth <= 0:
            print('You win!')
            exit()

        else:
            enemyHealth = enemyHealth - moveList[playerMove]
            print('You used cleave')
            print('Enemy health: {}\n'.format(enemyHealth))

            if enemyHealth <= 0:
                print('Enemy wins T-T')
                exit()
