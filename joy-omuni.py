#!/usr/bin/env python
# encoding:utf-8
import pygame
from pygame.locals import *
import time
import socket
import math

def main():
    pygame.init()
    pygame.joystick.init()
    pygame.joystick.Joystick(0)
    host = "soiya.local"
    port = 9110
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send("0")
    while True:
        eventlist = pygame.event.get()

        if    lambda e:e.type ==pygame.locals.JOYAXISMOTION:
            x, y = j.get_axis(0), j.get_axis(1)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))

            if lambda e: e.type == pygame.locals.JOYAXISMOTION:
                x, y = j.get_axis(0), j.get_axis(1)
                Vx = x * 200
                Vy = y * 200
                V1 = -Vx
                V21 = (float(1) / 2) * Vx
                V22 = (float(math.sqrt(3)) / 2) * Vy
                V2 = V21 - V22
                V31 = (float(1) / 2) * Vx
                V32 = (float(math.sqrt(3)) / 2) * Vy
                V3 = V31 + V32
                if V1 <= 0:
                    sp1 = int(-V1 + 1024) * 100000000
                elif V1 > 0:
                    sp1 = int(V1) * 100000000
                if V2 < 0:
                    sp2 = int(-V2 + 1024) * 10000
                elif V2 >= 0:
                    sp2 = int(V2) * 10000
                if V3 < 0:
                    sp3 = int(-V3 + 1024)
                elif V3 >= 0:
                    sp3 = int(V3)
            senddata = str(sp1 + sp2 + sp3)
            print senddata
            print 'x and y : ' + str(x) + ' , ' + str(y)
            client.send(str(senddata))
        time.sleep(0.3)

if __name__ == '__main__':
    pygame.joystick.init()
    try:
        j = pygame.joystick.Joystick(0)
        j.init()
        main()
    except pygame.error:
        print 'ジョイスティックを差し込め'
