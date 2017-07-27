#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Nunchuk Blanc

#VARIABLES IMPORTANTES
addr = 0x52
reg_init = 0x40
accel = [0,0,0]
stick = [0,0]
buttons = [False, False]

import smbus
import time

bus = smbus.SMBus(1)

def get_data(bus):
    # Envoyer un 0x00 pour demander l'acquisition
    bus.write_byte(0x52,0x00)
    # Attendre quelques millisecondes
    time.sleep(0.05)
    stick[0] =  bus.read_byte(0x52)
    stick[1] =  bus.read_byte(0x52)
    accel[0] =  bus.read_byte(0x52)
    accel[1] =  bus.read_byte(0x52)
    accel[2] =  bus.read_byte(0x52)
    miscellaneous  =  bus.read_byte(0x52)
    accel[0] = accel[0] << 2
    accel[1] = accel[1] << 2
    accel[2] = accel[2] << 2
    accel[0] += (miscellaneous & 0x0C) >> 2
    accel[1] += (miscellaneous & 0x30) >> 4
    accel[2] += (miscellaneous & 0xC0) >> 6
    if ((miscellaneous & 0x03) == 0):
        buttons[0] = 0
        buttons[1] = 1
    elif ((miscellaneous & 0x03) == 1):
        buttons[0] = 1
        buttons[1] = 0
    elif ((miscellaneous & 0x03) == 2):
        buttons[0] = 1
        buttons[1] = 1
    else:
        buttons[0] = 0
        buttons[1] = 0
    return [stick, accel, buttons]
