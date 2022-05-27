# Defeat all of the attacking ogres.
# Use flags to move away from dangerous ogres.

def Kill(enemy):
    if enemy:
        while enemy.health > 0:
            hero.attack(enemy)

def powerUp():
    if hero.isReady("power-up"):
        hero.powerUp()

def throwerLoop():
    thr = hero.findByType("thrower")
    for t in thr:
        dist = hero.distanceTo(t)
        if (t.type == "thrower" or t.type == "shaman") and (dist < 31 ) and hero.canCast("chain-lightning", t):
            hero.cast("chain-lightning", t)


while True:
    near = hero.findNearestEnemy()
    ogres = hero.findByType("ogre")
    bigBih = hero.findNearest(ogres)
    throwers = hero.findByType("thrower")
    throw = hero.findNearest(throwers)
    flag = hero.findFlag()
    if bigBih:
        disti = hero.distanceTo(bigBih)
        if disti < 3:
            powerUp()
            Kill(bigBih)
    if near:
        Kill(near)
    elif throw:
        throwerLoop()
    elif flag:
        hero.pickUpFlag(flag)
