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
    tik = 0
    close = hero.findEnemies()
    for c in close:
        dist = hero.distanceTo(c)
        if dist < 5:
            trigger = trigger + 1
    if (trigger > 7) and bFlag:
        trigger = 0
        hero.pickUpFlag(bFlag)
        

# This is for prioritized  searching & looting. it grabs the nearest item but scans
# for anything with a value greater than two.
def search()
    if item:
        it = hero.findItems()
        x = item.pos.x
        y = item.pos.y
        for i in it:
            dis = hero.distanceTo(i)
            a = i.pos.x
            b = i.pos.y
            if i.value > 2 and dis < 5:
                hero.moveXY(a, b)
