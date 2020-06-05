import subprocess

def run(*args):
    return subprocess.check_call(['git'] + list(args))

def commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")