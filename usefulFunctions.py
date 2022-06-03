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
def retreatFlag():
    bFlag = hero.findFlag("black")
    close = hero.findEnemies()
    for c in close:
        dist = hero.distanceTo(c)
        if dist < 5:
            trigger = trigger + 1
    if (trigger > 7) and bFlag:
        trigger = 0
        hero.pickUpFlag(bFlag)
        

# This is for prioritized searching & looting. Based on value, it will fetch the higher of two within n distance of eachother
# then it will break if there is an enemy within z distance from the here (optional, defaults to 5m).
def goldHunt(n, z):
    items = hero.findItems()
    if items:
        for i in items:
            ugly = hero.findNearestEnemy()
            it = hero.findNearestItem()
            distI = hero.distanceTo(it)
            distG = hero.distanceTo(i)
            delta = distG - distI
            if z:
                if ugly and hero.distanceTo(ugly) < z:
                    hero.say(ugly.type)
                    break
                if delta <= n and i.value < it.value:
                    hero.move(i.pos)
                    return
                else:
                    hero.move(it.pos)
                    return
            else:
                if ugly and hero.distanceTo(ugly) < 5:
                    hero.say(ugly.type)
                    break
                if delta <= n and i.value < it.value:
                    hero.move(i.pos)
                    return
                else:
                    hero.move(it.pos)
                    return

# needs the variable included in the main function but outside of any "while" loops that'll update the pos.                
def guardArea(a, b):
    if hero.distanceTo(guard) > 10:
        hero.moveXY(a, b)
    else:
        hero.moveXY(a, b)

guard = hero.pos
