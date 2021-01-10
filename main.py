import os
import subprocess
import random
from datetime import datetime
import config


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def setup():
    run("config", "user.email", config.user['email'])
    run("config", "user.name", config.user['name'])


def add():
    run("add", ".")


def commit(msg):
    run("commit", "-am", msg)


def push():
    run("push", "-u", "origin", "master")


setup()

# filename
today = datetime.today().strftime('%Y-%m-%d')

# must be at least two contributions, add and delete file
contributions = random.randrange(2, 10)

for i in range(contributions):
    if i == 0:
        # create file, add, and commit it
        f = open(today + '.txt', 'w')
        f.write(today + '\n')
        f.close()
        add()
        commit("added today's file")
    elif i == contributions - 1:
        # delete file, commit, and push all changes
        os.remove(today + '.txt')
        commit("removed today's file")
        push()
    else:
        # contribute to file and commit changes
        f = open(today + '.txt', 'a')
        f.write(today + '\n')
        f.close()
        commit(f"appended today's file {i} times")
