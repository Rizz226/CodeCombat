metalDetector.py

def coinDistance():
    # Write the function.
    # item = hero.findNearestItem()
    item = hero.findNearestItem()
    if item:
        return hero.distanceTo(item)
    else:
        return 0
    pass


while True:
    distance = coinDistance()
    if distance > 0:
        hero.say(distance)

        pass