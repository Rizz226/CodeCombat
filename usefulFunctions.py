# this is a library of functions that I use often.

# this checks if there are more than 6 enemies within 10m, and if cleave is ready then it'll cleave. 
def cleaveCrowd:
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
        
# this is essentially the same as the last one, but if you dont have cleave then drop a 
# black flag outside of the fighting and your hero will rally to it when surrounded.
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
        
