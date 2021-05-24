import time, os
import auto_player as player
import random
from modules.utils import perform_touch_loop, _random_sleep



def entry_enchantment():
    while True:
        ar1 = ['explore_entry', 'tupo_entry', 'jj_tupo', 'jj_tupo_refresh']
        re = player.find_touch_any(ar1)
        _random_sleep(wmin=1,wmax=1)
        if re == 'jj_tupo':
            break
        elif re == 'jj_tupo_refresh':
            break


def auto_play_enchantment(round=30):
    count = 0
    quit_count = 0
    seqs = [
        { 'name': ['jj_attack', 'tupo_attack2'],
        'id': 1,
        'actions': None,
        'sleep': 1,
        'response': '进攻选择....',
        'next': [2]
        },
        { 'name': ['fy_ready', 'jj_ready'],
        'id': 2,
        'actions': None,
        'sleep': 1,
        'response': '准备战斗...',
        'next' : [3,4]
        },
        { 'name': ['jj_fail_continue'],
        'id': 3,
        'actions': None,
        'sleep': 1,
        'response': '(失败)结束清算...',
        'next': [5, 6]
        },
        { 'name': ['jj_success_continue', 'jj_success_continue2'],
        'id': 4,
        'actions': None,
        'sleep': 1,
        'tick': True,
        'response': '(成功)结束清算...',
        'next': [5, 6]
        },
        { 'name': ['jj_tupo'],
        'id': 5,
        'actions': None,
        'sleep': 1,
        'response': '突破中...',
        'next': [1]
        },
        { 'name': ['jj_tupo_refresh', 'jj_tupo_refresh2'],
        'id': 6,
        'actions': None,
        'sleep': 1,
        'response': '刷完界面更新...',
        'next': [7]
        },
        { 'name': ['jj_tupo_confirm_refresh'],
        'id': 7,
        'actions': None,
        'sleep': 1,
        'response': '刷新确认...',
        'next': [5]
        }
    ]

    perform_touch_loop(seq=seqs, limits = 30, none_handler=__none_handler,full_seq=seqs)
    print('友情界面处理完毕，退出....')
    quick_close_cnt = 0
    while quick_close_cnt < 2:
        ar2 = ['close']
        player.find_touch_any(ar2)
        quick_close_cnt += 1
        _random_sleep(wmin=1,wmax=1)

def __none_handler():
    print('不知所措...')
    _random_sleep(wmax=2,wmin=1)