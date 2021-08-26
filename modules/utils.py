import time, os
import auto_player as player
import random
import imagehash
import mss
import numpy
import cv2
from PIL import Image

def _random_sleep(wmin=5,wmax=15):
    print('final sleep between:(', wmin, ",",wmax,")")
    sleep_time = random.randint(wmin, wmax)
    print("sleep %d s", sleep_time)
    time.sleep(sleep_time)


# 计算哈希值的hamming distance
# def hamming(h1,h2):
#     d = h1^h2
#     res = bin(d).count('1')
#     return res 
def hamming(s1, s2):
    '''
    Calculate the normalized Hamming distance between two strings.
    '''
    assert len(s1) == len(s2)
    return float(sum(c1 != c2 for c1, c2 in zip(s1, s2))) / float(len(s1))
    

def screen_shot():
    with mss.mss() as mss_instance:  # Create a new mss.mss instance
        monitor_1 = mss_instance.monitors[1]  # Identify the display to capture
        screenshot = mss_instance.grab(monitor_1)  # Take the screenshot
        im = numpy.array(screenshot)
        screen = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
    return screen, screenshot



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
    NoneCounterThreshold = 5
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
        print('Current max limit is:', limits)
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
      re, loc, ss = player.find_any_loc(target_list)
      
      matched = False
      
      for n in filtered_pool:
        if re in n['name']:
          print(n)
          tapTimes = n.get('taptimes', 1)
          player.touch(loc)
          player.random_delay()
          if tapTimes > 1:
            screen_hash_delta = 0
            org_hash = imagehash.average_hash(Image.frombytes("RGB", ss.size, ss.bgra, "raw", "BGRX"))
            print(org_hash)
            ss_cnt = 0
            while ss_cnt < 10 and screen_hash_delta < 0.1 :
              ss_cnt = ss_cnt + 1
              nss_arr, nss = screen_shot()
              player.touch(loc)
              player.random_delay()
              new_hash = imagehash.average_hash(Image.frombytes("RGB", nss.size, nss.bgra, "raw", "BGRX"))
              screen_hash_delta = hamming(str(org_hash), str(new_hash))
              print('tap ',re, 'with delta:',str(screen_hash_delta))
          # for xxxxxx in range(tapTimes):
          #   print('tap')
          #   player.touch(loc)
          #   player.random_delay()
          matched = True
          # start processing if there's a click on item
          sleep_time_input = n.get('sleep')
          sleep_factor = n.get('sleep_factor', 1)
          min_sleep_time_main = n.get('minsleep', 1)
          print("extracted sleep factor", sleep_factor)
          print("extracted sleep time", sleep_time_input)
          if sleep_time_input is None:
            sleep_time_input = 2
          # processing actions
          if n.get('action') is None:
            print(n['response'])
          else:
            n['action']()
          # tick counter if needed
          if n.get('tick'):
            print('current tick:' + str(counter['value']))
            counter['value'] += 1
          # sleep base on sleep factor
          min_sleep_time = min_sleep_time_main/sleep_factor
          _random_sleep(wmin=min_sleep_time, wmax=sleep_time_input/sleep_factor)
          filtered_seq = []
          if n.get('next') and len(n.get('next')) > 0:
            next_list = sorted(n.get('next'))
            filtered_seq = [_get_item_from_list_base_on_id(full_seq, x) for x in next_list]
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