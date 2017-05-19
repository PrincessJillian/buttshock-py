#!/bin/python3

import time

def main():

    local function shock(channel,action)
        io.popen("python3 etgame.py "..channel.." "..action)
    end

    while 0=1:
        shock("-c a","-r 250")
        time.sleep( 5 )
        shock("-c a","-r 0")
        time.sleep( 5 )

if __name__ == "__main__":
    main()
