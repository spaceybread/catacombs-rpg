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

attkBoost = 1

def cleave():
    return 20

def eschew():
    return 25

def ruleta():
    return 10

def rage():
    return 0

def move():
    move = int(input('What will you do? '))

    if move == 0:
        print('cleave')
        effect = cleave()
        modifier = 1
        type = 0

    if move == 1:
        print('eschew')
        effect = eschew()
        modifier = 0.9
        type = 1

    if move == 2:
        print('ruleta')
        effect = ruleta()
        modifier = 1
        type = 0

    if move == 3:
        print('rage')
        effect = rage()
        modifier = 1.75
        type = 2


    return [effect, modifier, type]

while True:
    outcome = move()

    if outcome[2] == 0:
        calcDamage = outcome[0] * attkBoost
        print('You did {} damage'.format(calcDamage))
        attkBoost = attkBoost * outcome[1]
        print('Attack modifier is {}'.format(attkBoost))

    if outcome[2] == 1:
        print('You healed {} hit points'.format(outcome[0]))
        attkBoost = attkBoost * outcome[1]
        print('Attack modifier is {}'.format(attkBoost))

    if outcome[2] == 2:
        print('You boosted attack')
        attkBoost = attkBoost * outcome[1]
        print('Attack modifier is {}'.format(attkBoost))
