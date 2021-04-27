import time, os
import auto_player as player
import random

def _random_sleep(wmin=5,wmax=15):
    sleep_time = random.randint(wmin, wmax)
    print("sleep %d s", sleep_time)
    time.sleep(sleep_time)


def __try_close():
    quick_close_cnt = 0
    while quick_close_cnt < 2:
        ar2 = ['close']
        player.find_touch_any(ar2)
        quick_close_cnt += 1
        _random_sleep(wmin=1,wmax=1)


def _parties_update(wait_rounds=4):
    count = 0
    is_waiting = False
    while True:
        ar1 = ['party','party_jj',]
        re = player.find_touch_any(ar1)
        if re == 'party':
            print('进入阴阳寮')
            _random_sleep(wmin=1,wmax=1)
        elif re == 'party_jj':
            print('进入自己结界')
            _random_sleep(wmin=1,wmax=1)
            break

    ar1 = ['zero_out', 'health_collect','health_click_col',]
    health_count = 0
    while health_count < wait_rounds:
        re = player.find_touch_any(ar1)
        if re == 'health_collect':
            _random_sleep(wmin=1,wmax=1)
        elif re == 'health_click_clo':
            print('收集体力...')
            _random_sleep(wmin=1,wmax=1)
        elif re == 'zero_out':
            print('体力已收集...')
            _random_sleep(wmin=1,wmax=1)
            __try_close()
            break
        else:
          health_count += 1

    ar1 = ['zero_out','ex_collect','ex_click_col' ]
    ex_count = 0
    while ex_count < wait_rounds:
        re = player.find_touch_any(ar1)
        if re == 'ex_collect':
            _random_sleep(wmin=1,wmax=1)
        elif re == 'ex_click_col':
            print('收集经验...')
            _random_sleep(wmin=1,wmax=1)
        elif re == 'zero_out':
            print('经验已收集...')
            _random_sleep(wmin=1,wmax=1)
            __try_close()
            break
        else:
          ex_count += 1
        
    print('结界界面处理完毕，退出....')
    quick_close_cnt = 0
    while quick_close_cnt < 2:
        ar2 = ['back']
        player.find_touch_any(ar2)
        quick_close_cnt += 1
        _random_sleep(wmin=1,wmax=1)
    
    print('阴阳寮界面处理完毕，退出....')
    quick_close_cnt = 0
    while quick_close_cnt < 2:
        ar2 = ['back_from_party']
        player.find_touch_any(ar2)
        quick_close_cnt += 1
        _random_sleep(wmin=1,wmax=1)