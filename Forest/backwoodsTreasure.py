def Kill(e):
    if e:
        while e.health > 0:
            hero.attack(e)

def skillChk(skill, target):
    if hero.isReady(skill):
        return True
    elif hero.canCast(skill, target):
        return True
    else:
        return False

while True:
    nItem = hero.findNearestItem()
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    ogres = hero.findByType("ogre")
    og = hero.findNearest(ogres)
    throwers = hero.findByType("thrower")
    thr = hero.findNearest(throwers)
    shaman = hero.findByType("shaman")
    sha = hero.findNearest(shaman)
    Ranged = throwers + shaman
    nRanged = hero.findNearest(Ranged)
    if flag:
        hero.pickUpFlag(flag)
        nItem = hero.findNearestItem()
    if enemy and enemy.type:
        if og and (hero.distanceTo(og) < 10) and skillChk("power-up"):
            hero.powerUp()
            hero.attack(og)
            pass
        if nRanged and hero.distanceTo(nRanged) < 31:
            if skillChk("chain-lightning", nRanged):
                hero.cast("chain-lightning", nRanged)
        else:
            hero.attack(enemy)
    elif nItem:
        hero.moveXY(nItem.pos.x, nItem.pos.y)
    else:
        if enemy:
            Kill(enemy)