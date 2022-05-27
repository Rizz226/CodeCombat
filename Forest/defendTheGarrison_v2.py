# Defeat all of the attacking ogres.
# Use flags to move away from dangerous ogres.

def Kill(enemy):
    if enemy:
        while enemy.health > 0:
            hero.attack(enemy)

def powerAtk(a):
    if hero.isReady("power-up"):
        hero.powerUp()
        hero.attack(a)

def spellCheck(target):
    if hero.canCast("chain-lightning", target):
        return True


def dist(target):
    if target:
        distance = hero.distanceTo(target)
    return distance


while True:
    flag = hero.findFlag()
    near = hero.findNearestEnemy()
    ogres = hero.findByType("ogre")
    bigBih = hero.findNearest(ogres)
    throwers = hero.findByType("thrower")
    throw = hero.findNearest(throwers)
    shaman = hero.findByType("shaman")
    sha = hero.findNearest(shaman)
    testArray = throwers + shaman
    nRanged = hero.findNearest(testArray)
    if flag:
        hero.pickUpFlag(flag)
    elif (throw or sha) and spellCheck(nRanged):
        if (dist(nRanged) < 31) and (dist(nRanged) > 5):
            hero.cast("chain-lightning", nRanged)
        else:
            if near:
                Kill(near)
    elif bigBih:
        if dist(bigBih) < 5:
            powerAtk(bigBih)
            Kill(bigBih)
        else:
            if near:
                Kill(near)
    else:
        if near:
            Kill(near)

