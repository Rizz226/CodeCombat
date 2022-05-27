

def throwerLoop():
    thrower = hero.findByType("thrower")
    for t in thrower:
        dist = hero.distanceTo(t)
        if (t.type == "thrower" or t.type == "shaman") and (dist < 31 ) and hero.canCast("chain-lightning", t):
            hero.cast("chain-lightning", t)

def crowdCheck():
    tik = 0
    close = hero.findEnemies()
    for c in close:
        dist = hero.distanceTo(c)
        if dist < 5:
            trigger = trigger + 1
    if (trigger > 7) and bFlag:
        trigger = 0
        hero.pickUpFlag(bFlag)

def cleaveCrowd():
    trigger = 0
    close = hero.findEnemies()
    for c in close:
        dist = hero.distanceTo(c)
        if (dist < 11):
            trigger = trigger + 1
    if trigger > 6 and hero.isReady("cleave"):
        hero.cleave(enemy)
        hero.say("GIT SOME!")
        trigger = 0
    else:
        hero.attack(enemy)

while True:
    gFlag = hero.findFlag("green")
    bFlag = hero.findFlag("black")
    enemy = hero.findNearestEnemy()
    throwers = hero.findByType("thrower")
    if gFlag:
        hero.pickUpFlag(gFlag)
        pass
    if throwers:
        throwerLoop()
        pass
    if enemy:
        hero.attack(enemy)
        crowdCheck()
        pass
    else:
        hero.shield()
