import time, os
import auto_player as player
import random

def _random_sleep(wmin=5,wmax=15):
    sleep_time = random.randint(wmin, wmax)
    print("sleep %d s", sleep_time)
    time.sleep(sleep_time)

# This will be a general performance loop so that we could focus on 
# clicking logics, example of the input should be like below:
#       seq: a list of actions (with sequence inside for the clicks)
#          [
#            { 'name' : name of the image like 'tupo'
#              'action': functions or null or name
#              'response': print out message on this action
#              'tick': whether to tick the counter on action
#              'break': whether break the loop on this condition
#              'sleep': sleep interval
#             },
#             ....
#           ]
#        limits: how many times we should loop this through
#                default is 3 [optional]
#        nonehandler:  handler when nothing matched [optional]
def perform_touch_loop(seq=[], limits=3, none_handler=None):
    sorted_seq = sorted(seq, key= lambda i: i['seq'])
    constructed_touch_seq = [x['name'] for x in sorted_seq]
    # control limits, if < 0 then we take it as loop forever
    if limits < 0:
      while True:
        should_break = _act_with_clicks(constructed_touch_seq, sorted_seq, counter, none_handler)
        if should_break:
          break
    else:
      counter = {'value': 0}
      while counter['value'] < limits:
        should_break = _act_with_clicks(constructed_touch_seq, sorted_seq, counter, none_handler)
        if should_break:
          break

def _act_with_clicks(constructed_touch_seq, sorted_seq, counter, none_handler):
      re = player.find_touch_any(constructed_touch_seq)
      matched = False
      for n in sorted_seq:
        if re == n['name']:
          matched = True
          # start processing if there's a click on item
          sleep_factor = n.get('sleep')
          if sleep_factor is None:
            sleep_factor = 2
          # processing actions
          if n.get('action') is None:
            print(n['response'])
          else:
            n['action']()
          # tick counter if needed
          if n.get('tick'):
            counter['value'] += 1
          # sleep base on sleep factor
          _random_sleep(wmin=1, wmax=sleep_factor)
          if n.get('break'):
            return True
      
      if not matched:
          if none_handler:
            none_handler()
      return False
