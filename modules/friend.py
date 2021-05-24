import time, os
import auto_player as player
import random
from modules.utils import perform_touch_loop, _random_sleep


def _friend_update():
    count = 0
    seqs = [
        { 'name': ['friend_receive'],
        'seq': 1,
        'sleep': 1,
        'response': '接受友情点...'
        },
        { 'name': ['friend_receive2'],
        'seq': 2,
        'actions': None,
        'sleep': 1,
        'response': '接受要好友情点...'
        },
        { 'name': ['good_friend_send'],
        'seq': 3,
        'actions': None,
        'sleep': 1,
        'response': '发出好友友情点',
        'tick': True
        },
        { 'name': ['friend_send'],
        'seq': 4,
        'actions': None,
        'sleep': 1,
        'response': '发出友情点',
        'tick': True
        },
        { 'name': ['friend_switch'],
        'seq': 5,
        'actions': None,
        'sleep': 1,
        'response': '切换友情界面'
        },
        { 'name': ['friend_panel'],
        'seq': 6,
        'actions': None,
        'sleep': 1,
        'response': '进入友情窗口'
        }
    ]
    perform_touch_loop(seq=seqs, limits = 10)
    print('友情界面处理完毕，退出....')
    quick_close_cnt = 0
    while quick_close_cnt < 2:
        ar2 = ['close']
        player.find_touch_any(ar2)
        quick_close_cnt += 1
        _random_sleep(wmin=1,wmax=1)