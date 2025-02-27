import time, os
import auto_player as player
import random
from modules.friend import _friend_update
from modules.parties import _parties_update
# from modules.enchantment import auto_play_enchantment
from modules.dynamic import auto_play_dynamic


def get_pictures():   
    player.screen_shot()

def auto_play_yuhun(round=50):
    count = 0
    while count < round:       
        ar1 = ['start_yys', 'exp_yys',]
        re = player.find_touch_any(ar1)
        if re == 'start_yys':
            print('开始新一轮...')
            count += 1
            #time.sleep(10)
        elif re == 'exp_yys':
            print('领取奖励...')
        elif re is None:
            ar2 = ['going_yys',]
            re = player.find_touch_any(ar2, False)
            if re == 'ging_yys':
                print('托管中...')
                time.sleep(5)

def auto_play_tower(round=500):
    count = 0
    while count < round:       
        ar1 = ['tmp_start', 'tmp_finish', 'fy_open_box']
        re = player.find_touch_any(ar1)
        if re == 'tmp_start':
            print('开始新一轮...')
            count += 1
            #time.sleep(10)
        elif re == 'fy_open_box':
            print('领取奖励...')
        elif re == 'tmp_finish':
            print('结束本轮...')
        _random_sleep(wmax=100,wmin=1,factor=100)
            


def auto_play_explore(round=10):
    count = 0
    while count < round:       
        ar1 = ['tansuo', 'exp_attack', 'exp_going', 'exp_continue']
        re = player.find_touch_any(ar1)
        if re == 'tansuo':
            print('开始新一轮...')
            count += 1
            #time.sleep(10)
        elif re == 'exp_attack':
            print('开始战斗...')
            ar2 = ['exp_attack',]
            re = player.find_touch_any(ar2, False)
            if re == 'exp_attack':
                print('战斗中...')
                time.sleep(5)
        elif re == 'exp_continue':
            print('点击继续...')
            ar2 = ['exp_continue',]
            re = player.find_touch_any(ar2, False)
            if re == 'exp_continue':
                print('继续...')
                time.sleep(5)
        elif re is None:
            ar2 = ['going_yys',]
            re = player.find_touch_any(ar2, False)
            if re == 'ging_yys':
                print('托管中...')
                time.sleep(5)


def _random_sleep(wmin=5,wmax=15,factor=1):
    sleep_time = random.randint(wmin, wmax)
    print("sleep %d s", sleep_time)
    time.sleep(sleep_time/factor)


def daily_job():
    _friend_update()
    _parties_update()
    entry_jj()
    auto_play_enchantment()
    




def auto_play_fy(round=100):
    count = 0
    is_waiting = False
    while count < round:       
        ar1 = ['fy_matching',  'fy_ready','fy_next', 'fy_open_box', 'fy_queue','fy_start']
        re = player.find_touch_any(ar1)
        if re == 'fy_start':
            print('开始新一轮...')
            count += 1
            _random_sleep(wmin=1,wmax=3)
        elif re == 'fy_matching':
            print('开始匹配...')
            _random_sleep(wmin=4,wmax=7)
        elif re == 'fy_queue':
            print('排队中...')
            ar2 = ['fy_matching',  'fy_ready','fy_next', 'fy_open_box', 'fy_queue']
            while(True):
                re2 = player.find_touch_any(ar2, False)
                if re2 == 'fy_queue':
                    print('继续等待...')
                    _random_sleep(wmin=2,wmax=5)
                elif re2 == 'fy_ready' or re2=='fy_matching' or re2=='fy_next' or re2=='fy_open_box':
                    print('准备战斗...')
                    break
        elif re == 'fy_ready':
            print('开始匹配...')
            ar2 = ['fy_ready',]
            re = player.find_touch_any(ar2, False)
            if re == 'fy_ready':
                print('开始战斗...')
                _random_sleep(wmax=4,wmin=1)
        elif re == 'fy_next':
            print('点击继续...')
            ar2 = ['fy_next',]
            re = player.find_touch_any(ar2, False)
            if re == 'fy_next':
                print('点击继续...')
                _random_sleep(wmax=2,wmin=1)
        elif re == 'fy_open_box':
            print('开箱继续...')
            ar2 = ['fy_open_box',]
            re = player.find_touch_any(ar2, False)
            if re == 'fy_open_box':
                print('开箱继续...')
                _random_sleep(wmax=2,wmin=1)
        elif re is None:
            print('不知所措...')
            _random_sleep(wmax=5,wmin=1)
        print('已经刷了' + str(count) + '次。。。')


def auto_play_enchantment():
    auto_play_dynamic(template='auto-tupo.json')


def auto_play_jx():
    auto_play_dynamic(template='autojx.json')

def auto_play_jx_old():
    auto_play_dynamic(template='autojxbak.json')

def auto_play_28():
    auto_play_dynamic(template='auto-28.json')



def auto_fragement():
    auto_play_dynamic(template="autojx.json", round=3)
    auto_play_dynamic(template="autojxttp.json", round=1)
    auto_play_dynamic(template="auto-tupo.json", round=1)
    auto_play_dynamic(template="auto-tupjx.json", round=1)


def menu(debug=False):

    menu_list = [
    [get_pictures, '获取当前屏幕截图'],
    [auto_play_yuhun, '自动刷图_御魂'],
    [auto_play_explore, '自动刷图_探险'],
    [auto_play_fy, '自动刷碎片'],
    [auto_play_enchantment, '自动结界突破'],
    [daily_job, '自动日常'],
    [auto_play_dynamic, '动态读取配置'],
    [auto_play_jx, '自动觉醒'],
    [auto_play_jx_old, '测试']
    ]

    start_time = time.time()
    print('程序启动，当前时间', time.ctime(), '\n')
    while True:
        i = 0
        for func, des in menu_list:
            msg = str(i) + ": " + des + '\n'
            print(msg)
            i += 1
        player.alarm(1)
        raw = input("选择功能模式：") if not debug else 1
        index = int(raw) if raw else 1
        func, des = menu_list[index]
        print('已选择功能： ' + des)
        func()

if __name__ == '__main__':
    menu()
