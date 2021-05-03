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
        { 'name': 'jj_attack',
        'seq': 1,
        'actions': None,
        'sleep': 1,
        'response': '进攻选择....'
        },
        { 'name': 'fy_ready',
        'seq': 2,
        'actions': None,
        'sleep': 1,
        'response': '准备战斗...'
        },
        { 'name': 'jj_fail_continue',
        'seq': 3,
        'actions': None,
        'sleep': 1,
        'response': '(失败)结束清算...'
        },
        { 'name': 'jj_success_continue',
        'seq': 4,
        'actions': None,
        'sleep': 1,
        'tick': True,
        'response': '(成功)结束清算...'
        },
        { 'name': 'jj_tupo',
        'seq': 5,
        'actions': None,
        'sleep': 1,
        'response': '突破中...'
        },
        { 'name': 'jj_tupo_refresh',
        'seq': 7,
        'actions': None,
        'sleep': 1,
        'response': '刷完界面更新...'
        },
        { 'name': 'jj_tupo_confirm_refresh',
        'seq': 6,
        'actions': None,
        'sleep': 1,
        'response': '刷新确认...'
        }
    ]

    perform_touch_loop(seq=seqs, limits = 30, none_handler=__none_handler)
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