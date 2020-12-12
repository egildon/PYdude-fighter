#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      FF_Gameclient.py
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

import socket
import json

def Main():
    host = '127.0.0.1'
    port = 3002
    server = ('127.0.0.1', 2000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    
    print ("Client Started")

    
    json.message = input("->")
    
    while message != 'q':
        s.sendto(message,server)
        data, addr = s.recvfrom(1024)
        print ('Recieved from server: ') + str(data)
        message = raw_input("->")
    s.close()
    
if __name__=='__main__':
    Main()