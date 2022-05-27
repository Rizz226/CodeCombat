def Kill(e):
    while e.health > 0:
        hero.attack(e)

def moveUR():
    if enemy and hero.isPathClear(hero.pos, enemy):
        return
    else:
        a=hero.pos.x + 5
        b=hero.pos.y + 5
        hero.moveXY(a, b)


while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        Kill(enemy)
    else:
        moveUR()
    
