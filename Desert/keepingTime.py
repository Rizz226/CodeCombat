while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if hero.time < 10:
        if enemy and enemy.type != "palisade":
            hero.attack(enemy)
        pass
    elif hero.time < 35:
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
            hero.moveXY(x, y)
            
        pass
    else:
        if enemy and enemy.type != "palisade":
            hero.attack(enemy)
        pass
