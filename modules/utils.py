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
    action_pool = []
    t = [x['name'] for x in seq]
    constructed_touch_seq = [item for sublist in t for item in sublist]
    # control limits, if < 0 then we take it as loop forever
    NoneCounter = 0
    NoneCounterThreshold = 10
    if limits < 0:
      while True:
        should_break, next_ops = _act_with_clicks(constructed_touch_seq, seq, counter, none_handler, limits, full_seq, action_pool)
        if should_break:
          break
        else:
          result = _process_no_action_matched(action_pool,NoneCounter,NoneCounterThreshold,next_ops)
          action_pool = result[0]
          NoneCounter = result[1]
    else:
      while counter['value'] < limits:
        should_break, next_ops = _act_with_clicks(constructed_touch_seq, seq, counter, none_handler, limits, full_seq, action_pool)
        if should_break:
          break
        else:
          result = _process_no_action_matched(action_pool,NoneCounter,NoneCounterThreshold,next_ops)
          action_pool = result[0]
          NoneCounter = result[1]


def _process_no_action_matched(action_pool, none_counter, limit, next_ops):
    if next_ops is None:
      # reset action pool when no action count over max counts
      none_counter += 1
      if none_counter > limit:
        none_counter = 0
        return [], none_counter
      else:
        return action_pool, none_counter
    else:
      return next_ops, none_counter

def _act_with_clicks(constructed_touch_seq, seq, counter, none_handler, limits, full_seq, action_pool):
      if len(action_pool) == 0:
        target_list = constructed_touch_seq
        filtered_pool = full_seq
      else:
        t = [x['name'] for x in action_pool]
        target_list = [item for sublist in t for item in sublist]
        filtered_pool = action_pool
      re = player.find_touch_any(target_list)
      matched = False
      
      for n in filtered_pool:
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
          filtered_seq = []
          if n.get('next') and len(n.get('next')) > 0:
            filtered_seq = [_get_item_from_list_base_on_id(full_seq, x) for x in n.get('next')]
          if n.get('break'):
            return True,filtered_seq
          return False, filtered_seq
      
      if not matched:
          if none_handler:
            none_handler()
          return False, None



def _get_item_from_list_base_on_id(chase_list, id):
  for i in chase_list:
    if i.get('id') == id:
      return i