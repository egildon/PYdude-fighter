#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      FF_Gameserver.py
#       
#       Copyright 2016 earnest gildon <egildon@TheBeast>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
import asyncio
import socketserver
import socket
#import twisted
import json


def Main():
    host = '127.0.0.1'
    port = 2000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    print ("Server Started")
    while True:
        data,addr = s.recvfrom(1024)
        print ("message from: ") + str(addr)
        print ("from connected user: ") + str(data)
        data = "sending: " + str(data)
        s.sendto(data,addr)
    s.close()
    
if __name__=='__main__':
    Main()