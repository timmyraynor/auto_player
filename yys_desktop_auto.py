import time, os
import auto_player as player

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

def menu(debug=False):

    menu_list = [
    [get_pictures, '获取当前屏幕截图'],
    [auto_play_yuhun, '自动刷图_御魂'],
    [auto_play_explore, '自动刷图_探险']
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
