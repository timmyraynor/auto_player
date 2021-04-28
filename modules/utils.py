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


# This will be a general performance loop so that we could focus on 
# clicking logics, example of the input should be like below:
#       seq: a list of actions (with sequence inside for the clicks)
#          [
#            { name : name of the image like 'tupo'
#              action: functions or null or name
#              response: print out message on this action
#              tick: whether to tick the counter on action
#              break: whether break the loop on this condition
#              sleep: sleep interval
#             },
#             ....
#           ]
#        limits: how many times we should loop this through
def perform_touch_loop(seq=[], limits=2):
    sorted_seq = sorted(seq, key= lambda i: i.seq)
    constructed_touch_seq = [x.name for x in sorted_seq]

    # control limits, if < 0 then we take it as loop forever
    if limits < 0:
      while True:
        should_break = _act_with_clicks(constructed_touch_seq, sorted_seq, counter)
        if should_break:
          break
    else:
      counter = {value: 0}
      while counter.value < limits:
        should_break = _act_with_clicks(constructed_touch_seq, sorted_seq, counter)
        if should_break:
          break

def _act_with_clicks(constructed_touch_seq, sorted_seq, counter):
      re = player.find_touch_any(constructed_touch_seq)
      for n in sorted_seq:
        if re == n.name:
          # start processing if there's a click on item
          sleep_factor = n.sleep
          if n.sleep is None:
            sleep_factor = 2
          # processing actions
          if n.action is None:
            print(n.response)
          else:
            action()
          # tick counter if needed
          if n.tick:
            counter.value += 1
          # sleep base on sleep factor
          _random_sleep(wmin=1, wmax=sleep_factor)
          if n['break'] is not None and n['break']:
            return True
      return False
