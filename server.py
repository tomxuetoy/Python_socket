#!/usr/bin/env python
# UDP Echo Server -  udpechoserver.py
import socket, traceback

host = ''
port = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM - UDP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while 1:
    try:
        message, address = s.recvfrom(8192) # 8192: buffer size
        print "Got data from", address
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise # will show either KeyBoardInterrupt or SystemExit exception
    except:
        traceback.print_exc()
