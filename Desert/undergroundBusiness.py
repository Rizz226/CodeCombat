# This can be improved. wanted to POC the guardArea() function. the 'guard' variable needs defined before starting the level.
# if you need to guard a seperate area, you might be able to magic some math in to the variable but i kept getting errors.
def kill(target):
    if target:
        while target.health > 0:
            if hero.isReady("power-up") and dist > 10:
                hero.powerUp()
            hero.attack(target)

def onSpawn(event):
    pet.moveXY(20, 59)
    pet.moveXY(71, 57)
    pet.moveXY(71, 12)
    pet.moveXY(20, 12)
    pet.moveXY(20, 34)
    pet.moveXY(25, 34)
    pass

def guardArea(a, b):
    if hero.distanceTo(guard) > 10:
        hero.moveXY(a, b)
    else:
        hero.moveXY(a, b)

guard = hero.pos
pet.on("spawn", onSpawn)

while True:
    haz = hero.findNearest(hero.findHazards())
    enemy = hero.findNearestEnemy()
    guardArea(25, 34)
    if enemy:
        dist = hero.distanceTo(enemy)
        if dist < 15:
            kill(enemy)
    elif hero.gold >= 300:
        hero.moveXY(50, 34)
    elif haz:
        hero.say(haz.type)
    pass
