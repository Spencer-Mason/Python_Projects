#Create a general enemy class. Values will be determined when instance is created
class enemy:
    name = ''
    HP = 1
    attackDamage = 0

#Creates an elite version of enemies as a child of enemy class.
#Not all elites have a weakness, determined when instance is created
class elite(enemy):
    weakness = 'None'
    powerAttack = ' '

#Creates a boss as a child of enemy. Not all bosses have resistances,
#will be determined along with loot drop when instance is created
class boss(enemy):
    resistances = 'None'
    lootDrop = ' '
