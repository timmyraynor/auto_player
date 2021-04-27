import time, os
import auto_player as player
import random

def _random_sleep(wmin=5,wmax=15):
    sleep_time = random.randint(wmin, wmax)
    print("sleep %d s", sleep_time)
    time.sleep(sleep_time)


def _daily_misc(rounds=3):
    count = 0
    while count<rounds:
        ar1 = ['yard_serve_food',]
        re = player.find_touch_any(ar1)
        if re == 'yard_serve_food':
            print('搜集食物')
            _random_sleep(wmin=2,wmax=2)
            ar1 = ['yard_serve_confirm',]
            r2 = player.find_touch_any(ar1)
            break
        count += 1