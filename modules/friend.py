import time, os
import auto_player as player
import random

def _random_sleep(wmin=5,wmax=15):
    sleep_time = random.randint(wmin, wmax)
    print("sleep %d s", sleep_time)
    time.sleep(sleep_time)


def _friend_update():
    count = 0
    is_waiting = False
    while count < 10:
        ar1 = ['friend_receive', 'friend_receive2', 'good_friend_send', 'friend_send','friend_switch', 'friend_panel']
        re = player.find_touch_any(ar1)
        if re == 'friend_send':
            print('发出友情点')
            count += 1
            _random_sleep(wmin=1,wmax=1)
        elif re == 'good_friend_send':
            print('发出友情点')
            count += 1
            _random_sleep(wmin=1,wmax=1)
        elif re == 'friend_switch':
            _random_sleep(wmin=1,wmax=1)
        elif re == 'friend_receive':
            print('接受要好友情点...')
            _random_sleep(wmin=1,wmax=1)
        elif re == 'friend_receive2':
            print('接受友情点...')
            _random_sleep(wmin=1,wmax=1)
        elif re == 'friend_panel':
            print('进入友情界面...')
            _random_sleep(wmin=1,wmax=1)
        print('已经进行了' + str(count) + '次操作。。。')
    print('友情界面处理完毕，退出....')
    quick_close_cnt = 0
    while quick_close_cnt < 2:
        ar2 = ['close']
        player.find_touch_any(ar2)
        quick_close_cnt += 1
        _random_sleep(wmin=1,wmax=1)