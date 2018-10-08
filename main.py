# -*- coding: utf-8 -*-

#__/\\\\____________/\\\\_____/\\\\\\\\\\\____/\\\_________________________/\\\\\\_____/\\\\\\____        
# _\/\\\\\\________/\\\\\\___/\\\/////////\\\_\/\\\________________________\////\\\____\////\\\____       
#  _\/\\\//\\\____/\\\//\\\__\//\\\______\///__\/\\\___________________________\/\\\_______\/\\\____      
#   _\/\\\\///\\\/\\\/_\/\\\___\////\\\_________\/\\\_____________/\\\\\\\\_____\/\\\_______\/\\\____     
#    _\/\\\__\///\\\/___\/\\\______\////\\\______\/\\\\\\\\\\____/\\\/////\\\____\/\\\_______\/\\\____    
#     _\/\\\____\///_____\/\\\_________\////\\\___\/\\\/////\\\__/\\\\\\\\\\\_____\/\\\_______\/\\\____   
#      _\/\\\_____________\/\\\__/\\\______\//\\\__\/\\\___\/\\\_\//\\///////______\/\\\_______\/\\\____  
#       _\/\\\_____________\/\\\_\///\\\\\\\\\\\/___\/\\\___\/\\\__\//\\\\\\\\\\__/\\\\\\\\\__/\\\\\\\\\_ 
#        _\///______________\///____\///////////_____\///____\///____\//////////__\/////////__\/////////__
#
# MShell written by Michael Rojas.
# Simple shell written in python adapted from: https://brennan.io/2015/01/16/write-a-shell-in-c/ 

import sys
import os
import time

commands = ['cd', 'exit']
CURRENTDIRECTORY = ""


# Read => Parse => Execute

def shell_loop():
    status = True
    while True and status:
        line = input('🔥 ' + CURRENTDIRECTORY)
        args = tokenize(line)
        # Case 1: We are executing a built in command ie: cd
        # Case 2: We are starting a program so call fork()
        if args[0] in commands:
            status = built_in_commands(args)
        else:
            fork(args)

def tokenize(line):
    return line.split(' ')

def fork(args):
    child_pid = os.fork()
    if child_pid == 0:
        os.execvp(args[0], args)
    elif child_pid < 0:
        print("Fork error.")
    else:
        print("Im a parent.")
        pid, status = os.waitpid(child_pid, 0)
        print("Waiting done ", pid, " ", status)

def built_in_commands(args):
    args = list(filter(lambda x: x != '', args))
    if args[0] == 'cd':
        change_directories(args)
    if args[0] == 'exit':
        return False
    return True
    
def change_directories(args):
    if len(args) != 2:
        print("To change directories enter `cd <path>`")
        return
    path = str(args[1])
    os.chdir(path)
    global CURRENTDIRECTORY 
    CURRENTDIRECTORY = os.getcwd() + " "



# Main
shell_loop()


#/Users/michael/Code/TEST