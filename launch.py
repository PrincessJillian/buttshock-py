#!/bin/python3

import time
import os


def shock(channel, action):
    os.system("python3 etgame.py " + channel + " " + action + "")

def main():
    while True:
        shock("-c a","-r 250")
        time.sleep( 5 )
        shock("-c a","-r 0")
        time.sleep( 5 )

if __name__ == "__main__":
    main()
