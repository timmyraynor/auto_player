import time, os
import auto_player as player
import random
from modules.utils import perform_touch_loop, _random_sleep
import json



def auto_play_dynamic(round=30):
    count = 0
    quit_count = 0
    raw = input("选择读取模板：")
    startpoint = input("选择启动模块：")
    list_open = open('./logics/' + raw)
    sequences = list_open.read()
    master_seqs = json.loads(sequences)
    master_seqs_ref = {}

    # convert list to dictionary for quick reference
    for master_seq in master_seqs:
        master_seqs_ref[master_seq.get('name')] = master_seq


    next_to_go = []

    for master_seq in master_seqs:
       if master_seq.get('name') == startpoint:
           next_to_go.append(master_seq)

    while len(next_to_go) > 0:
        master_seq = next_to_go.pop()
        seqs = master_seq.get('sequence')
        counts = master_seq.get('counter', 0)
        exit_seq = master_seq.get('exit')
        perform_touch_loop(seq=seqs, limits = counts, none_handler=__none_handler, full_seq=seqs)
        next_to_go.append(master_seqs_ref.get('next'))



def __none_handler():
    print('不知所措...')
    _random_sleep(wmax=2,wmin=1)