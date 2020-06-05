import os
import subprocess
import random
from datetime import datetime

def run(*args):
    return subprocess.check_call(['git'] + list(args))

def add():
   run("add", ".")

def commit(msg):
    run("commit", "-am", msg)

def push():
    run("push", "-u", "origin", "master")

# if day > 20, there will be contributions today
# day = random.randrange(0, 100)
# if day < 21:
#    exit()

today = datetime.today().strftime('%Y-%m-%d')
contributions = random.randrange(2,10)

for i in range(contributions):
   if i == 0:
      f = open(today + '.txt', 'w')
      f.write(today + '\n')
      f.close()
      add()
      commit("added today's file")
   elif i == contributions - 1:
      os.remove(today + '.txt')
      commit("removed today's file")
      push()
   else:
      f = open(today + '.txt', 'a')
      f.write(today + '\n')
      f.close()
      commit(f"appended today's file {i-1} times")