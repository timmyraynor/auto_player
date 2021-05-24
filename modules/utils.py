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
#            { 'name' : name of the image like 'tupo' (list of names [])
#              'action': functions or null or name
#              'id': ID of current action
#              'response': print out message on this action
#              'tick': whether to tick the counter on action
#              'break': whether break the loop on this condition
#              'sleep': sleep interval，
#              'sleep_factor':  actual sleep time = sleep interval / factor
#              'next': [next series of actions using ID to identify]
#             },
#             ....
#           ]
#        limits: how many times we should loop this through
#                default is 3 [optional]
#        nonehandler:  handler when nothing matched [optional]
def perform_touch_loop(seq=[], limits=3, counter={'value': 0}, none_handler=None, full_seq=[]):
    seq = sorted(seq, key= lambda i: i['id'])
    t = [x['name'] for x in seq]
    constructed_touch_seq = [item for sublist in t for item in sublist]
    # control limits, if < 0 then we take it as loop forever
    if limits < 0:
      while True:
        should_break = _act_with_clicks(constructed_touch_seq, seq, counter, none_handler, limits, full_seq)
        if should_break:
          break
    else:
      while counter['value'] < limits:
        should_break = _act_with_clicks(constructed_touch_seq, seq, counter, none_handler, limits, full_seq)
        if should_break:
          break

def _act_with_clicks(constructed_touch_seq, seq, counter, none_handler, limits, full_seq):
      re = player.find_touch_any(constructed_touch_seq)
      matched = False
      for n in seq:
        if re in n['name']:
          matched = True
          # start processing if there's a click on item
          sleep_time_input = n.get('sleep')
          sleep_factor = n.get('sleep_factor', 1)
          if sleep_time_input is None:
            sleep_time_input = 2
          # processing actions
          if n.get('action') is None:
            print(n['response'])
          else:
            n['action']()
          # tick counter if needed
          if n.get('tick'):
            counter['value'] += 1
          # sleep base on sleep factor
          min_sleep_time = 1/sleep_factor
          _random_sleep(wmin=min_sleep_time, wmax=sleep_time_input/sleep_factor)
          if n.get('next') and len(n.get('next')) > 0:
            filtered_seq = [_get_item_from_list_base_on_id(full_seq, x) for x in n.get('next')]
            perform_touch_loop(filtered_seq,limits, counter, none_handler, full_seq)
          if n.get('break'):
            return True
          break
      
      if not matched:
          if none_handler:
            none_handler()
      return False



def _get_item_from_list_base_on_id(chase_list, id):
  for i in chase_list:
    if i.get('id') == id:
      return i