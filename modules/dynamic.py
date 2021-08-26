import time, os
import auto_player as player
import random
from modules.utils import perform_touch_loop, _random_sleep
import json



def auto_play_dynamic(round=30, template=None):
    print('run template:', template, ' ', round,'times')
    count = 0
    quit_count = 0
    seqs = None
    if template is None:
        raw = input("选择读取模板：")
        list_open = open('./logics/' + raw, encoding='utf-8')
        sequences = list_open.read()
        seqs = json.loads(sequences)
    else:
        list_open = open('./logics/' + template, encoding='utf-8')
        sequences = list_open.read()
        seqs = json.loads(sequences)

    perform_touch_loop(seq=seqs, limits = round, none_handler=__none_handler,full_seq=seqs)
    print('处理完毕，退出....')
    quick_close_cnt = 0
    while quick_close_cnt < 2:
        ar2 = ['close']
        player.find_touch_any(ar2)
        quick_close_cnt += 1
        _random_sleep(wmin=1,wmax=1)

def __none_handler():
    print('不知所措...')
    _random_sleep(wmax=2,wmin=1)