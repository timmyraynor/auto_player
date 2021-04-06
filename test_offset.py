import time, os
import auto_player as player

def get_pictures():   
    player.screen_shot()


def auto_play_explore(round=10):
    count = 0
    while count < round:       
        ar1 = ['apple']
        re = player.find_move_any(ar1)
        if re == 'apple':
            print('开始新一轮...')
            count += 1
            time.sleep(3)

def menu(debug=False):
    menu_list = [
    [get_pictures, '获取当前屏幕截图'],
    [auto_play_explore, '自动刷图_探险']
    ]

    start_time = time.time()
    print('程序启动，当前时间', time.ctime(), '\n')
    while True:
        auto_play_explore()

if __name__ == '__main__':
    menu()
