# Walk to a few points around the ogre camps, defeating any enemies along the way.
# Visit the statue to begin the event.
# Stand your ground and defeat the attacking ogres.

# Hint: fight close to the statue for it's assistance during the battle.
enemy_types = {}
# ogres types
enemy_types['shaman'] = {'danger': 10, 'focus': 10}
enemy_types['warlock'] = {'danger': 10, 'focus': 10}
enemy_types['burl'] = {'danger':10, 'focus':5}
enemy_types['witch'] = {'danger': 8, 'focus': 10}
enemy_types['brawler'] = {'danger':7, 'focus':5}
enemy_types['ogre'] = {'danger':5, 'focus':5}
enemy_types['chieftain'] = {'danger':6, 'focus':10}
enemy_types['fangrider'] = {'danger': 4, 'focus': 20}
enemy_types['skeleton'] = {'danger':5, 'focus':10}
enemy_types['scout'] = {'danger':4, 'focus':10}
enemy_types['thrower'] = {'danger':3, 'focus':15}
enemy_types['munchkin'] = {'danger':2, 'focus':5}
enemy_types['yak'] = {'danger': -1, 'focus': 0}
enemy_types['ice-yak'] = {'danger': -1, 'focus': 0}

if hero.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'

def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and enemy.type != 'yak' and enemy.team != team and hero.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    # if enemy_return is None:
    #    enemy_return =  hero.findNearestEnemy()
    if enemy_return and enemy_return.type != 'yak':
        return enemy_return
    else:
        return None

def fight(tar):
    while tar.health > 0:
        dis = hero.distanceTo(tar)
        if dis > 15 and hero.canCast("chain-lightning", tar):
            hero.cast("chain-lightning", tar)
        if dis > 10 and hero.isReady("jump"):
            hero.jumpTo(tar)
        if hero.isReady("power-up") and dis < 10:
            hero.powerUp()
            hero.attack(tar)
        if hero.isReady("bash") and dis < 10:
            hero.bash(tar)
        elif hero.isReady("attack"):
            hero.attack(tar)
        else:
            hero.shield()
            


# Dont use me yet. Gotta do more work.
def guard(gPos):
    while True:
        enemy = findTarget()
        gDist = hero.distanceTo(gPos)
        if gDist < 30:
            if enemy:
                fight(enemy)
            else:
                hero.move(gPos)
                continue
        if gDist > 50:
            if enemy and hero.cast("chain-lightning", enemy):
                hero.cast("chain-lightning", enemy)
                fight(enemy)
            else:
                hero.move(gPos)
                continue
        hero.move(gPos)
        if hero.pos == gPos:
            hero.wait(3)
            if hero.pos == gPos:
                return

def disBetween(pointA, pointB):
    if (pointA.pos and pointB.pos) != None:
        xDis = pointA.pos.x - PointB.pos.x
        yDis = pointA.pos.x - PointB.pos.x
    elif pointA.pos != None and pointB == None:
        xDis = pointA.pos.x - PointB.x
        yDis = pointA.pos.y - PointB.y
    elif pointA.pos == None and pointB != None:
        xDis = pointA.x - PointB.pos.x
        yDis = pointA.y - PointB.pos.y
    elif (pointA and pointB) == None:
        xDis = pointA.x - PointB.x
        yDis = pointA.y - PointB.y
    distance = (((xDis**2) + (yDis**2)) ** (1/2))
    return distance


statPos = ({'x':61, 'y':72})
guardPos = ({'x':61, 'y':61})
stops = [[31, 30], [28, 73], [90, 72], [77, 30], [37, 32]]
stopsIndex = 0
while stopsIndex < len(stops):
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if (enemy and hero.distanceTo(enemy) < 50):
        if (hero.isReady('jump') and hero.distanceTo(enemy) > 10):
            hero.jumpTo(enemy.pos)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
            enemy = hero.findNearestEnemy()
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(enemy)
            enemy = hero.findNearestEnemy()
        elif hero.isReady("attack"):
            hero.attack(enemy)
        else:
            hero.shield()
    else:
        if (hero.isReady('jump')):
            hero.jumpTo({'x': stops[stopsIndex][0], 'y': stops[stopsIndex][1]})
        else:
            hero.moveXY(stops[stopsIndex][0], stops[stopsIndex][1])
        stopsIndex += 1
while True:
    guard(guardPos)


