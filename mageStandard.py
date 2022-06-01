# Credit to Vadim Kuznetsov (vadim-job-hg) for the findTarget() function & its associated code.
#
# Define enemies and team:
enemy_types = {}
ogres types
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
            if enemy and enemy.type != 'yak' and enemy.team != team and hero.distanceTo(enemy) < enemy_types[
                type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    # if enemy_return is None:
    #    enemy_return =  hero.findNearestEnemy()
    if enemy_return and enemy_return.type != 'yak':
        return enemy_return
    else:
        return None

def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)

def sumSkel():
    if corpses:
        if (len(corpses) > 4 and hero.canCast("raise-dead"))

def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'skeleton':
            cmdSkel(friend)
#        elif friend.type == 'soldier' or friend.type == 'archer':
#            CommandSoldier(friend)

def cmdSkel(friend):
    target = hero.findNearestEnemy()
    if target:
        hero.command(friend, "attack", target)

def fight(target):
    if target:
        cast(target)
        if hero.isReady("attack"):
            hero.attack(en)
        else:
            hero.shield()

def cast(target):
    if target:
        if hero.health < (hero.maxHealth / 3) and hero.canCast("drain-life", en):
            hero.cast("drain-life", en)
        elif hero.canCast("chain-lightning", en) and (yak_alert == False):
            hero.cast("chain-lightning", en)
        elif hero.canCast("poison-cloud", en):
            hero.cast("poison-cloud", en)
        elif hero.canCast("fear", en) and en.type == ("thrower" or "shaman" or "witch"):
            hero.cast("fear", en)
        else hero.canCast("drain-life", en):
            hero.cast("drain-life", en)

def itemHunt():
    while True:
        item = hero.findNearestItem()
        if item and (item.type == "coin" or item.type == "potion"):
            hero.move(item.pos)
        elif hero.distanceTo(enemy) < 15:
            break


# Main Loop
while True:
    yak_alert = False
    yak = hero.findNearest(hero.findByType('sand-yak'))
    if yak and hero.distanceTo(yak) > 40:
        yak_alert = True
    paste = findTarget()
    if paste:
        fight(paste)
    sumSkel()
    
















#
#   
#   depreciated stuff that I like to reference back to
#
#
"""  ///Depreciated///
def fight(target):
    while True:
        enemies1 = hero.findEnemies()
        enemy = hero.findNearest(enemies1)
        if enemy:
            while enemy.health > 0:
                castCycle()
                hero.attack(enemy)
        if hero.time > untilTime:
            break
    hero.moveXY(59, 33)

def castCycle():
    while True:
        enemies = hero.findEnemies()
        corpses = hero.findCorpses()
        if enemies:
            en = hero.findNearest(enemies)
            if corpses and len(corpses) > 4:
                hero.cast("raise-dead")
            elif hero.health < (hero.maxHealth / 3) and hero.canCast("drain-life", en):
                hero.cast("drain-life", en)
            elif hero.canCast("poison-cloud", en):
                hero.cast("poison-cloud", en)
            elif hero.canCast("chain-lightning", en):
                hero.cast("chain-lightning", en)
            elif hero.canCast("fear", en) and en.type == ("thrower" or "shaman"):
                hero.cast("fear", en)
            elif hero.canCast("drain-life", en):
                hero.cast("drain-life", en)
            else:
                hero.attack(en)
            return
"""
