def action():
    friend = hero.findNearestFriend()
    if friend:
        if friend.type == 'soldier':
            hero.cast('heal', friend)
        elif friend.type == 'goliath':
            hero.cast('grow', friend)
        else:
            hero.cast('regen', friend)
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type == 'ogre':
            hero.cast('force-bolt', enemy)
        elif enemy.type == 'brawler':
            hero.cast('shrink', enemy)
        else:
            hero.cast('poison-cloud', enemy)
    item = hero.findNearestItem()
    if item:
        if item.type == "potion":
            hero.moveXY(item.pos.x, item.pos.y)
        if item.type == "poison":
            hero.cast("grow", self)
            hero.moveXY(item.pos.x, item.pos.y)


hero.moveXY(18, 24)
action()
hero.moveXY(18, 40)
action()
hero.moveXY(34, 24)
action()
hero.moveXY(34, 40)
action()
hero.moveXY(50, 40)
action()
hero.moveXY(50, 24)
action()
hero.moveXY(66, 40)
action()
hero.moveXY(66, 24)
action()
hero.moveXY(66, 24)
