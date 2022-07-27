# catacombs-rpg
rogue-like, turn-based RPG

The game follows turn-based combat that uses a speed stat to decide which side goes first; currently this is randomly assigned however, in later builds, I intend to add a stat-point system to allow for more customisation

Speed ties cannot exist, enemy's speed stat is never a whole number while the player's is, thus ensuring a greater/lower than test can take place correctly

Currently the game has 4 moves: Cleave (0), Eschew (1), Ruleta (2), Rage (3)
The number in the bracket corresponds to the number you must type if you want to use the move

Moves can be divided into three types: Outgoing, Incoming, and Stat Modification

Outgoing type moves alter enemy health - Cleave, Ruleta

Incoming type moves alter user health - Eschew

Stat Modification moves alter damage scalars - Rage

Outgoing type moves:

Cleave does flat 20 damage

Ruleta does between 15 and 25 damage

Incoming type moves: 

Eschew results in healing between 25 and 28

Stat Modification moves:

Rage increases attack boost by 1.5 (linearly)

The game assigns the player with 400 health each run and the moment the health equals or goes below, the run is over

With each enemey defeated, opponent health increases by 20

Stat changes are not carried between fights

Try to beat as many enemies as possible! 
GLHF!
