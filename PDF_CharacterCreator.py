#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       PDF_CharacterCreator.py
#
#       Copyright 2010 earnest gildon <egildon@gmail.com>
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

import os
import time
from operator import itemgetter, attrgetter
import pickle
from . import PDF_Character
from time import sleep
import sqlite3
import sqlalchemy





import json

print ("The PDF_CharacterCreator Module")
#TODO: Add Load and save methods for character creation process
#TODO: Create method to allow user to utilize experience points and buildpoints
#TODO: Use json/sqlite database for starage instead of pickle. 

timex = 0
def seriallize_player_info(player1, player2):
    timex = 0

    player2 = PDF_Character.Charactor("None")
    player1 = PDF_Character.Charactor("None")
    # attack_order = player1,player2

    # Pickle the TG files #make  2 files one combat one Character
    pickle_file1 = open("PDF_Char1.tg","wb",2)#This only works with python 2
    pickle.dump(player1,pickle_file1,)
    pickle_file1.close()
    print("\n")
    print("CHARACTERS FILES 1 SAVED")
    # Pickle the Opponent TG files
    pickle_file2 = open("PDF_Char2.tg","wb",2)
    pickle.dump(player2,pickle_file2,)
    pickle_file2.close()
    print("\n")
    print("CHARACTERS FILES 2 SAVED")

    
def load_player_files(player1, player2):
    """load the attack_order TG files"""
    #player1 = pickle.load("PDF_Char1.tg")
    #player2 = pickle.load("PDF_Char2.tg")
    player1 = open("PDF_Char1.tg",'rb')
    player2 = open("PDF_Char2.tg",'rb')
    print("\n")
    print ("CHARACTER FILES LOADED")





    print("\n")
    print("player Characters Initilized")

    print("\n")

    time.sleep(timex)


def get_players(player1, player2):
    pname = input("What is your characters name?")
    if pname == "":
        print ('Name cannot be blank!')
        print ("Assging name")
        pname = ("The Stranger")
    player1.set_name(pname)# is this broken?
    print ("Your Characters name is: ")
    print((player1.get_name()))

    time.sleep(timex)

    userid = input("What is your e-mail address? (userId)")
    player1.set_userid(userid)
    print ("Your UserID/Email is: ")
    print((player1.get_userid()))

    time.sleep(timex)


    chi = input("What is your chi score?")
    player1.set_chi(chi)
    print((player1.get_chi()))
    print ("Your chi score is now: ")
    print((player1.get_chi()))
    time.sleep(timex)

    print ("What styles will you study?")
    print((player1.get_stylesknown()))
    time.sleep(timex)

    print ("What is your intelegence score?")
    print((player1.get_intelegence()))
    time.sleep(timex)

    print ("What is your strength score?")
    print((player1.get_strength()))
    time.sleep(timex)

    print ("What is your Dexterity score?")
    print((player1.get_dexterity()))
    time.sleep(timex)

    print ("What is your perception score?")
    print((player1.get_perception()))
    time.sleep(timex)

    print("\n")
    print ("player CHARACTER CREATED")
    time.sleep(timex)
    print("\n")

    #start Opponent Initilizaion
    print("player Opponent Initilized")

    time.sleep(timex)


    p2name = input("What is your character's opponents name?")
    if p2name == "":
        print ('Name cannot be blank!')
        print ("Assging name...")
        p2name = ("Joe Schmoe")
    player2.set_name(p2name)
    print((player2.get_name()))
    time.sleep(timex)

    print ("What is your e-mail address? (userId)")
    print((player2.get_userid()))

    print ("What is your chi score?")
    print((player2.get_chi()))

    print ("What styles will you study?")
    print((player2.get_stylesknown()))

    print ("What is your intelegence score?")
    print((player2.get_intelegence()))

    print ("What is your strength score?")
    print((player2.get_strength()))

    print ("What is your Dexterity score?")
    print((player2.get_dexterity()))

    print ("What is your perception score?")
    print((player2.get_perception()))

    print("\n")
    print ("player: OPPONENT CREATED")


    # Pickle the SW files
    pickle_file1 = file("PDF_Char1.tg", "w", 2)
    pickle.dump(player1,pickle_file1,)
    pickle_file1.close()
    print("\n")
    print("PLAYER CUSTOM CHARACTER SAVED!")

    pickle_file2 = file("PDF_Char2.tg", "w", 2)
    pickle.dump(player2,pickle_file2,)
    pickle_file2.close()

    print("\n")
    print("PLAYER CUSTOM OPPONENT SAVED!")

    print("\n")

    attack_order = player1,player2
    print(("playercount:",len(attack_order)))



    counted = 0
    sizex = len(attack_order)
    print (sizex)




    print("END OF CHARACTER CREATION")

    return (player1,player2)




        #return 0

if __name__ == '__main__':
    # main()
    load_player_files(get_players(1))
    # get_players(2)
