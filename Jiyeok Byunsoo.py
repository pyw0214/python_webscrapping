gun = 10


def checkpoint(soldiers):  # watching job
    global gun  # using 'gun' in the front area
    gun = gun - soldiers
    print("(Within the function) guns in hand: {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("(Within the function) guns in hand: {0}".format(gun))
    return gun


print("Guns in total: {0}".format(gun))
checkpoint(2)  # 2 soldiers on duty
gun = checkpoint_ret(gun, 2)
print("Guns in rest: {0}".format(gun))
