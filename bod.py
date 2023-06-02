import os
import time
import random

attacks=['block','attack','heal']

start_time = time.time()

bot2_attack=0
bot1_attack=0
def clear():
  'system(command: AnyPath) -> int'
  os.system('clear')

bot1_health=100
bot2_health=100

def check():
  'check(AnyPath) -> int'
  if bot1_health<=0:
    print('bot1 loses\nand bot2 wins')
    print(f'it took bot2 {time.time()-start_time} seconds to beat bot1')
    time.sleep(1273123)
  else:
    if bot2_health<=0:
      print('bot2 loses\nand bot1 wins')
      print(f'it took bot1 {time.time()-start_time} seconds to beat bot2')
      time.sleep(12381273)
    else:
      pass




while True:
  print(f'bot1s health:{bot1_health} bot2s health:{bot2_health}\n1. attack\n2. block\n3. heal')
  time.sleep(2.5)
  bot_1_response=random.choice(attacks)
  if bot_1_response=='attack':
    clear()
    bot1_attack=random.randint(5,30)
    print(f'bot 1 chose {bot_1_response}\nand took {bot1_attack} health from bot2')
    time.sleep(random.randint(2,3))
    bot2_health=bot2_health-bot1_attack
    check()
    clear()
    bot1_attack=0
    print('bot2s turn')
    time.sleep(2.5)
    print(f'bot1s health:{bot1_health} bot2s health:{bot2_health}\n1. attack\n2. block\n3. heal')
    bot2_response=random.choice(attacks)
    if bot2_response=='attack':
      time.sleep(2.5)
      clear()
      bot2_attack=random.randint(5,30)
      print(f'bot2 chose {bot2_response} and took {bot2_attack} health away from bot1')
      time.sleep(2)
      bot1_health=bot1_health-bot2_attack
      bot2_attack=0
      check()
      clear()
    elif bot2_response=='block':
      clear()
      print(f'bot2 {bot2_response}ed so he gets whatever was attacked back from him')
      time.sleep(3)
      bot2_health=bot2_health+bot1_attack
      check()
      clear()
    elif bot2_response=='heal':
      bot2_heal=random.randint(1,15)
      print(f'bot {bot2_response}ed {bot2_heal} health')
      bot2_health=bot2_health+bot2_heal
      time.sleep(2.5)
      check()
      clear()
  elif bot_1_response=='block':
    clear()
    print('bot1 blocked so he gets whatever was attacked last back')
    bot1_health=bot1_health+bot2_attack
    check()
    time.sleep(2)
    clear()
    bot2_response=random.choice(attacks)
    if bot2_response=='attack':
      time.sleep(2.5)
      clear()
      bot2_attack=random.randint(5,30)
      print(f'bot2 chose {bot2_response} and took {bot2_attack} health away from bot1')
      time.sleep(2)
      bot1_health=bot1_health-bot2_attack
      bot2_attack=0
      check()
      clear()
    elif bot2_response=='block':
      clear()
      print(f'bot2 {bot2_response}ed so he gets whatever was attacked back from him')
      time.sleep(3)
      bot2_health=bot2_health+bot1_attack
      check()
      clear()
    elif bot2_response=='heal':
      bot2_heal=random.randint(1,15)
      print(f'bot2 {bot2_response}ed {bot2_heal} health')
      bot2_health=bot2_health+bot2_heal
      time.sleep(2.5)
      check()
      clear()
  elif bot_1_response=='heal':
    bot1_heal=random.randint(1,15)
    print(f'bot1 healed {bot1_heal} health')
    time.sleep(2.5)
    check()
    clear()
    bot2_response=random.choice(attacks)
    if bot2_response=='attack':
      time.sleep(2.5)
      clear()
      bot2_attack=random.randint(5,30)
      print(f'bot2 chose {bot2_response} and took {bot2_attack} health away from bot1')
      time.sleep(2)
      bot1_health=bot1_health-bot2_attack
      bot2_attack=0
      check()
      clear()
    elif bot2_response=='block':
      clear()
      print(f'bot2 {bot2_response}ed so he gets whatever was attacked back from him')
      time.sleep(3)
      bot2_health=bot2_health+bot1_attack
      check()
      clear()
    elif bot2_response=='heal':
      bot2_heal=random.randint(1,15)
      print(f'bot {bot2_response}ed {bot2_heal} health')
      bot2_health=bot2_health+bot2_heal
      time.sleep(2.5)
      check()
      clear()
