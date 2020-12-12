#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       YM_Combat.py
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
#v01
#06.09.2010
#07.09.2010 13:04:59

import random
import time
import threading
from . import YM_Character
from operator import itemgetter, attrgetter
import pickle
import re
from . import YM_StatsMonitor#make this work with print functions


print ("The YM_Combat Module")
#TODO: Make the Experience points save
#TODO: Experience Points calculator based on build points used
#TODO: Make buildpoints save and increment

'''Naughty Global constants are here!!!'''
_RandCrit2 = (random.randint(1, 2))#random crit to reduce Balance -  tao by
_RandCrit1 = (random.randint(1, 2))

pie = "It has been broughten!"





class Combat():
    time1 = 1#1
    time2 = 1#2
    time3 = 1#3
    _Fighter1Location = []
    _Fighter2Location = []
    
    _Fighter1agipool = 0
    _Fighter2agipool = 0
    _Fighter1basemodifiedattackpoolX = 0
    _Fighter2basemodifiedattackpoolX = 0
    _AttackerActions = []
    _DefenderAction = []

    def __init__(self,):
        """The combat function for fighting"""  
        self.round = 0
        self.case = None
        self.CombatOver = False

        """This statement begins/runs combat and loads the attack_order .TG files"""
        Combat.Round(self,Combat._StatsPopulate(self,Combat._TGloads(self)))



    @staticmethod
    def Round(self,attack_order):

        Combat.PrintStatsComplete(self,attack_order)
        Combat.StatsTest(self,attack_order)
        self.round    
        if self.round <= 1:
            print ("\n")
            time.sleep(Combat.time1)
            Combat.PrintHeadings(self,attack_order)
            print ("\n")

            time.sleep(Combat.time2)   
            print ("Case:%s")%(self.case)
            time.sleep(Combat.time2)
            print ("Round:", self.round, "\n")

        if self.round < 25:
            time.sleep(Combat.time2)
            print ("!!!!!FIGHT!!!!!!")
            time.sleep(Combat.time2)       
            print ("\n")            

        else:
            #self.round > 25:
            print("too many puppies...")
            return(Combat.PrintEndOfFight(self))


        return (Combat.Inititive(self,attack_order))

    @staticmethod    
    def Inititive(self,attack_order,):# TODO: In inititive() decrease player1.inititivepool by 70% and increase player2 by same amount. to allow turn changes. depend on logic of statements and remove true=false.



        if self.round <= 1:
            if attack_order[0].agility > attack_order[1].agility:
                attack_order = attack_order[0],attack_order[1]
                attack_order[0].isattacker = True
                attack_order[1].isattacker = False                       
                self.case = 101


            elif attack_order[0].agility < attack_order[0].agility:
                attack_order = attack_order[1],attack_order[0]
                attack_order[1].isattacker = True
                attack_order[0].isattacker = False  
                self.case = 102 
                
            else :
                print ("Simultaneous attack!")###Make this work properly
                attack_order[0].agility == attack_order[0].agility
                attack_order = attack_order[1],attack_order[0]
                attack_order[1].isattacker = True
                attack_order[0].isattacker = True
                self.case = 103                

        else:
            if attack_order[0].agility > attack_order[1].agility:
                attack_order = attack_order[0],attack_order[1]
                attack_order[0].isattacker = True
                attack_order[1].isattacker = False                       
                self.case = 201


            elif attack_order[0].agility < attack_order[0].agility:
                attack_order = attack_order[1],attack_order[0]
                attack_order[1].isattacker = True
                attack_order[0].isattacker = False  
                self.case = 202 
                
            else :
                print ("Simultaneous attack!")###Make this work properly
                attack_order[0].agility == attack_order[0].agility
                attack_order = attack_order[1],attack_order[0]
                attack_order[1].isattacker = True
                attack_order[0].isattacker = True
                self.case = 203 
                
        print ('end of inititive method')
        print ("\n")
        time.sleep(Combat.time2)   

        Combat.PrintShortHpNRound(self,attack_order)   
        print ("Case:%s")%(self.case)

        time.sleep(Combat.time2)
        print ("\n")
        Combat.RoundCheck(self,round,attack_order)
        return (Combat.FightersAttack(self,attack_order))

    def RoundCheck(self,round,attack_order):
        if self.round < 1:
            print("The Round is about to begin.")
            print("\n")
            time.sleep(Combat.time2)
            if self.round >= 1:
                time.sleep(Combat.time2)
                print ("!!!!!FIGHT!!!!!!")
                time.sleep(Combat.time2)       
            print ("\n")            

            if self.round > 25:
                print("too many puppies...")
                return(Combat.PrintEndOfFight(self,attack_order))



    def FightersAttack(self,attack_order):
        self.round = self.round +  1        

        """This section is the Beginning of the Combat section. \
        It checks the HP of all characters and then passes to the attack/damage function"""

        Combat.PrintShortHpNRound(self,attack_order)        
        Combat.AttackNdefense(self,attack_order)  




    def AttackNdefense(self,attack_order):
        _combatover = False
        _fighter1dampool = None
        _fighter2hppool  = None
        #_fighter1dampool =  attack_order[0].damagepool
        #_fighter2hppool =   self.attack_order[1].hppool
        #_fighter2defpool =  self.attack_order[1].defpool    
        _fighter1damagedealt = 0

        #Combat._TaoModStart(self,attack_order)# is this necessary?   
        for player in attack_order:     
            Combat._PlayerOptionAction(self,player)  
        Combat.PrintStatsComplete(self,attack_order)
        print ("Initial Attack Round")

        print(" (%s) Attacks...")%(attack_order[0].name)          

        '''evasion''' 
        if True: #attack_order[0].evasionpool <= attack_order[1].accuracypool:
            _fighter1damagedealt = (attack_order[0].basemodifiedattackpool - attack_order[1].defensepool)#deal some damage

            if _fighter1damagedealt < 1 :#keep damage from being negative
                _fighter1damagedealt = 0
                print("A glancing blow! 1")
            if _fighter1damagedealt < 2:
                print("A glancing blow! 2")

                print("%s's attack did little damage.(%s)"%(attack_order[0].name,_fighter1damagedealt))

            '''Here is the F1-F2 Damage function'''
            #FIXME The F1 F2 damage is broken! rework

            attack_order[1].hppool = (attack_order[1].hppool - _fighter1damagedealt)

            attack_order[1].damagerecieved  = _fighter1damagedealt    

            Combat.PrintFAD(self,attack_order)
            if  _fighter1damagedealt > ((attack_order[1].hppool * .62)):    #this checks for large demoralizing hit and removes _RandCrit2 from your balance modifyer.
                attack_order[1].taopool = (attack_order[1].taopool - _RandCrit2) #This changes player's psychological balance
                print("\n") 
                print("%s struck his opponent a MIGHTY BLOW!!! %s looks shaken!")%(attack_order[0].name,attack_order[1].name)# prints good hit if fighter no longer in balance
                print("\n") 

            if attack_order[1].taopool != 3:
                print("\n") 
                print(" %s is off balance!!!")%(attack_order[1].name)# prints good hit if fighter no longer in balance
                print("\n")         
        else:
            print("\n") 
            Combat.PrintFAD(self,attack_order)
            time.sleep(Combat.time1)
            print("\n")         
            print ("%s Has....!Dodged!....the attack")%(attack_order[1].name)            

#FIXME: Make Simultaneous attack structure work!    
    #else:
    # Combat.SimultaneousAttack(self,attack_order)
        Combat.PrintFHD(self,attack_order)
        Combat.PrintAttackBreakdown(self,attack_order) 
    # for player in attack_order:
        print ("hitting hp check")
        Combat._HpCheck(self,attack_order)
        if self.CombatOver is False:            
            attack_order = Combat._attack_order_swap(self,attack_order)# reverses the player1,player2 order in attack_order 
            print("hit the _TaoModReset and attack_order_swap")
            Combat._TaoModReset(self,attack_order)
            Combat.Inititive(self,attack_order)
        else:
            Combat.PrintEndOfFight(self,attack_order)
        return (0)  

    def SimultaneousAttack(self,attack_order):
        #Broken
        _fighter1damagedealt = 0
        _fighter2damagedealt = 0

            #if attack_order[0].evasionpool <= _attack_order[1].accuracypool:
            #_fighter1damagedealt = (attack_order[0].basemodifiedattackpool - attack_order[1].defensepool)#deal some damage

                #if attack_order[0].basemodifiedattackpool < 1 :#keep damage from being negative
                    #attack_order[0].basemodifiedattackpool = 0
                    #print("A glancing blow! 1")
                #elif attack_order[0].modifiedattackpool < 0:
                    #attack_order[0].modifiedattackpool = 0                
                    #print("A glancing blow! 2")

        #attack_order[0].hppool = (attack_order[0].hppool - _fighter1damagedealt)
        #attack_order[1].hppool = (attack_order[1].hppool - _fighter2damagedealt)

        #print ("Both attackers attack simultaneously!!!")

        #print(" (%s) Attacks...")%(attack_order[0].name)          

        #'''evasion''' 
        #if _fighter2evasion <= _fighter1accuracy:
            ##new and improved F1 attack and defense#new and improved F1 attack and defense

            ##deal some damage
            #_fighter1damagedealt = (_basemodifiedattackpool - _fighter2defpool)

            #if attack_order[0].basemodifiedattackpool < 1 :#keep damage from being negative
                #attack_order[0].basemodifiedattackpool = 0

            #if attack_order[0].basemodifiedattackpool > 0:

                #'''Here is the F1-F2 Damage function'''

                #attack_order[1].hppool = (attack_order[1].hppool - _fighter1damagedealt)
                #_fighter2hppool = attack_order[1].hppool

            #else:
                #print("%s's attack did little damage.(%s)"%(attack_order[0].name,_fighter1damagedealt))
            #Combat.PrintFAD(self,attack_order)
            #if  _fighter1damagedealt > ((attack_order[1].hppool * .62)):    #this checks for large demoralizing hit and removes _RandCrit2 from your balance modifyer.
                #attack_order[1].taopool = (attack_order[1].taopool - _RandCrit2) #This changes player's psychological balance
                #print("\n") 
                #print("%s struck his opponent a MIGHTY BLOW!!! %s looks shaken!")%(attack_order[0].name,attack_order[1].name)# prints good hit if fighter no longer in balance
                #print("\n") 

            #if attack_order[1].taopool != 3:
                #print("\n") 
                #print(" %s looks shaken!")%(attack_order[1].name)# prints good hit if fighter no longer in balance
                #print("\n")         
        #else:
            #print("\n") 
            #Combat.PrintFAD(self,attack_order)
            #time.sleep(Combat.time1)
            #print("\n")         
            #print ("%s Has....!Dodged!....The attack"%attack_order[0].Fighter2name)            
        #Combat.PrintFHD(self,attack_order)
        #Combat.PrintAttackBreakdown(self,attack_order) 
        #return (attack_order[0].basemodifiedattackpool,attack_order[1].basemodifiedattackpool,attack_order)

#TODO: Make Riposte method work for instant attack retalliation
    def Riposte():
        _basemodifiedattackpool = None
        _fighter2hppool  = None
        _basemodifiedattackpool =  self.Fighter1basemodifiedattackpool
        _fighter2hppool = self.Fighter2hppool
        _fighter2defpool = self.Fighter2defpool         

    def _attack_order_swap(self,attack_order):
        (a,b) = attack_order
        (b,a) = (a,b)
        attack_order = (a,b)
        return (attack_order)

    def _TGloads(self):
        player1 = pickle.load(file("YM_Char1.tg"))
        player2 = pickle.load(file("YM_Char2.tg"))
        attack_order = player1,player2 
        print ("PLAYER FILES LOADED") 
        print (attack_order,":from load file")
        return (attack_order)

    def _StatsPopulate(self,attack_order):
        """populates the stat pools"""
        for player in attack_order:
            Combat.reflexespool(self,player)
            Combat.accuracypool(self,player) 
            Combat.evasionpool(self,player) 
            Combat.taopool(self,player) 
            Combat.basemodifiedattackpool(self,player) 
            Combat.modifiedattackpool(self,player) 
            Combat.basedefensepool(self,player) 
            Combat.defensepool(self,player) 
            Combat.agilitypool(self,player) 
            Combat.hitpointspool(self,player) 
            Combat.hppool(self,player) 
            Combat.staminapool(self,player)  

            #reflexespool(self,player)
            #Combat.accuracypool(self,player) 
            #Combat.evasionpool(self,player) 
            #Combat.taopool(self,player) 
            #Combat.basemodifiedattackpool(self,player) 
            #Combat.modifiedattackpool(self,player) 
            #Combat.basedefensepool(self,player) 
            #Combat.defensepool(self,player) 
            #Combat.agilitypool(self,player) 
            #Combat.hitpointspool(self,player) 
            #Combat.hppool(self,player) 
            #Combat.staminapool(self,player)     
        print (attack_order,"attack_order in StatsPopulate2")
        return (attack_order)

    #def _StatsPopulate2(self,attack_order):

            #Combat.reflexespool(self,attack_order[0])
            #Combat.accuracypool(self,attack_order[0]) 
            #Combat.evasionpool(self,attack_order[0]) 
            #Combat.taopool(self,attack_order[0]) 
            #Combat.basemodifiedattackpool(self,attack_order[0]) 
            #Combat.modifiedattackpool(self,attack_order[0]) 
            #Combat.basedefensepool(self,attack_order[0]) 
            #Combat.defensepool(self,attack_order[0]) 
            #Combat.agilitypool(self,attack_order[0]) 
            #Combat.hitpointspool(self,attack_order[0]) 
            #Combat.hppool(self,attack_order[0]) 
            #Combat.staminapool(self,attack_order[0])  

            #Combat.reflexespool(self,attack_order[1])
            #Combat.accuracypool(self,attack_order[1]) 
            #Combat.evasionpool(self,attack_order[1]) 
            #Combat.taopool(self,attack_order[1]) 
            #Combat.basemodifiedattackpool(self,attack_order[1]) 
            #Combat.modifiedattackpool(self,attack_order[1]) 
            #Combat.basedefensepool(self,attack_order[1]) 
            #Combat.defensepool(self,attack_order[1]) 
            #Combat.agilitypool(self,attack_order[1]) 
            #Combat.hitpointspool(self,attack_order[1]) 
            #Combat.hppool(self,attack_order[1]) 
            #Combat.staminapool(self,attack_order[1])  
            #return (attack_order)

    def _TaoModStart(self,attack_order):
        '''Tao attack/defense multiplier'''
        print ("_TaoModStarts hit.")
        if attack_order[1].taopool <= 3: 
            attack_order[1].defensepool = (((attack_order[1].defensepool) * attack_order[1].taopool) + attack_order[1].intelegence)

        if attack_order[0].taopool <= 3: 
            attack_order[0].modifiedattackpool = ((attack_order[0].modifiedattackpool * attack_order[0].taopool) + attack_order[0].intelegence )

    def _TaoModStartX(self,attack_order):
        '''Tao attack/defense multiplier'''
        print ("_TaoModStarts hit.")
        if player.taopool <= 3: 
            player.defensepool = (((attack_order.defensepool) * attack_order.taopool) + attack_order.intelegence)

        if attack_order.taopool <= 3: 
            attack_order.modifiedattackpool = ((attack_order.modifiedattackpool * attack_order.taopool) + attack_order.intelegence )       

    def _TaoModReset(self,attack_order):
        '''Tao attack/defense multiplier/pools reset'''        
        print ("_TaoModReset hit.")
        for player in attack_order:
            Combat._CombatPoolsToZero(self,player)
            print ("Name:%s---Defense:(%i)---Offense:(%i)")%(player.name,player.defensepool,player.modifiedattackpool)

    def _CombatPoolsToZero(self,player):
        player.defensepool = 0
        player.modifiedattackpool =  0


    def _HpCheck(self,attack_order):
        print ("inside hp check")
        for player in attack_order:
            if player.hppool <= 0:
                print ("%s HP: (%s)")%(player.name,player.hppool)
                print("\n") 
                print("%s Has Collapsed!")%player.name
                self.CombatOver = True
        return(0)

    def _AttackActionsEffectsListA(self,player):
        player.attackaction  = player.attackaction  
        player.defenseaction  = player.defenseaction       

        if player.attackaction  == 6:#Rest
            player.evasionpool = ((player.evasionpool * .21) * ((player.intelegence) / 6))           
            player.taopool = player.taopool + 1
            player.staminapool = player.staminapool + player.staminapool * .41
            player.modifiedattackpool = 0

        elif player.attackaction  == 5:#Combo/Parry
            player.evasionpool = ((player.evasionpool +  player.taopool)*(player.intelegence))
            player.modifiedattackpool = player.modifiedattackpool
            print ("This is broken/incomplete right now")
            player.staminapool = player.staminapool - 70

        elif player.attackaction  == 4:#All out Evasion
            player.evasionpool = ((player.evasionpool +  player.taopool)*(player.intelegence))
            player.modifiedattackpool = 0
            player.staminapool = player.staminapool - 25

        elif player.attackaction  == 3:#all out Attack/Defense
            player.modifiedattackpool = ((player.modifiedattackpool +  player.taopool)*(player.intelegence * player.staminapool))
            player.taopool = player.taopool - 1
            player.defensepool = 0 
            player.staminapool = player.staminapool - 55

        elif player.attackaction  == 2:#Focused Attack(accuracy)
            player.accuracypool = ((player.accuracypool +  player.taopool)*(player.intelegence * player.staminapool))
            player.staminapool = player.staminapool - 30

        elif player.attackaction  == 1:#normal attack/defense
            player.staminapool = player.staminapool - 5
            # not needed: player.stamina = player.staminapool
            print("%s does a Normal attack"%(player.name))           
            print("%s Chose the fallback option."%(player.name))
            player.staminapool = player.staminapool - 5

        return(0)


    def _AttackActionsEffectsListD(self,player):
        player.attackaction  = player.attackaction  
        player.defenseaction  = player.defenseaction       


        if player.attackaction  == 6:#Rest
            player.evasionpool = ((player.evasionpool * .21) * ((player.intelegence) / 6))
            player.defensepool = player.basedefensepool()
            player.taopool = player.taopool + 1
            player.staminapool = (player.staminapool + (player.staminapool * .41))
            player.modifiedattackpool = 0

            #TODO: '''intelegence+reflexes vs intelegence+reflexes player challenge decides if the parry/combo goes off'''

        elif player.attackaction  == 5:#Combo/Parry
            player.evasionpool = ((player.evasionpool +  player.taopool)*(player.intelegence))
            player.modifiedattackpool = player.modifiedattackpool
            print ("This is broken/incomplete right now")
            player.staminapool = player.staminapool - 70

        elif player.attackaction  == 4:#All out Evasion
            player.evasionpool = ((player.evasionpool +  player.taopool)*(player.intelegence))
            player.modifiedattackpool = 0
            player.staminapool = player.staminapool - 25

        elif player.attackaction  == 3:#all out Attack/Defense
            player.defensepool = ((player.modifiedattackpool +  player.taopool)*(player.intelegence * player.staminapool))
            player.taopool = player.taopool - 1
            player.modifiedattackpool = 0 
            player.staminapool = player.staminapool - 55

        elif player.attackaction  == 2:#Focused Attack(accuracy)
            player.accuracypool = ((player.accuracypool +  player.taopool)*(player.intelegence * player.staminapool))
            player.staminapool = player.staminapool - 30

        elif player.attackaction  == 1:#normal attack/defense
            player.staminapool = player.staminapool - 5
            # not needed: player.stamina = player.staminapool
            print("%s does a Normal attack")%(player.name)          
            print("%s Chose the fallback option.")%(player[1].name)
            player.staminapool = player.staminapool - 5          


        return (0)
#FIXME: Make attack and defense dialogs more personalized
    def _PlayerOptionAction(self,player):
        print(player.name,"player... in _PlayerOptionAction")
        print ("\n")  
        #print (" %s Attacks and %s Defends")%(attack_order[0].name,attack_order[1].name)
        print ("Press 1 for Normal Attack/Defense.")#%(attack_order[0].name)
        print ("Press 2 for Focused Attack/Defense")#%(attack_order[0].name)
        print ("Press 3 for All Out Power Attack/Defense.")#%(attack_order[0].name)
        print ("Press 4 for all Out Evasion")#%(attack_order[0].name) 
        print ("Press 5 to  Combo/Parry")#%(attack_order[0].name)         
        print ("Press 6 to  Rest")#%(attack_order[0].name)    
        Combat._PlayerOptionActionQuery(self,player)

    def _PlayerOptionActionDef(self,player):
        print(player.name,"player... in _PlayerOptionAction")
        print ("\n")  
        #print (" %s Defends and %s Attacks")%(attack_order[1].name,attack_order[0].name)
        print ("Press 1 for Normal Attack/Defense.")#%(attack_order[1].name)
        print ("Press 2 for Focused Attack/Defense")#%(attack_order[1].name)
        print ("Press 3 for All Out Power Attack/Defense.")#%(attack_order[1].name)
        print ("Press 4 for all Out Evasion")#%(attack_order[1].name) 
        print ("Press 5 to  Combo/Parry")#%(attack_order[1].name)         
        print ("Press 6 to  Rest")#%(attack_order[1].name)    
        Combat._PlayerOptionActionQuery(self,player)        

    def _PlayerOptionActionQuery(self,player):
        _player_action = None  

        print(player,"player... in Combat phase # Combat._PlayerOptionActionQuery")
        print ("\n") 
        _player_action = raw_input("%s : What action would you like to Take?"%(player.name))
        print ("\n")
        if player.isattacker is True:
            player.attackaction = _player_action
        else:
            player.defenseaction = _player_action
        print ("\n")                        
        if  player.isattacker is True:
            return Combat._AttackActionsEffectsListA(self,player) 
        else:
            return Combat._AttackActionsEffectsListD(self,player)
        return (0)



    def PrintEndOfFight(self,attack_order):
        self.CombatOver = True
        time.sleep(Combat.time1)
        print("\n") 
        print(".")
        time.sleep(Combat.time1)
        print(".")
        time.sleep(Combat.time1)
        print("..")
        time.sleep(Combat.time2)
        print("...")
        time.sleep(Combat.time1)
        print("\n") 
        print("This fight is over!!!")
        print("\n") 
        time.sleep(Combat.time2)
        Combat.PrintWinner(self,attack_order)
        time.sleep(Combat.time1)
        print("\n")
        time.sleep(Combat.time1)
        Combat.PrintStats(self,attack_order)
        time.sleep(Combat.time2)        
        print("\n") 
        return (0)

    def PrintFAD(self,attack_order):
        #print("\n")
        time.sleep(Combat.time2)   
        print("%s attacks for:(%i) damage!"%(attack_order[0].name, attack_order[0].basemodifiedattackpool))
    @staticmethod
    def PrintFHD(self,attack_order,):        
        time.sleep(Combat.time2)
        print("\n")
        print("%s      HP:(%i)     Def:(%i)" %(attack_order[1].name,attack_order[1].hppool,attack_order[1].defensepool + attack_order[1].defensepool),)     #print("\n")

    def PrintStats(self,attack_order):
        fighter = attack_order
        print ("%s - Tao(%i) Agi(%i) HP:(%i)  :|-vs-|: %s - Tao(%i) Agi(%i) HP:(%i)" )%(fighter[0].name,fighter[0].taopool,fighter[0].agilitypool, fighter[0].hppool,fighter[1].name,fighter[1].taopool,fighter[1].agilitypool, fighter[1].hppool)

    def PrintShortHpNRound(self,attack_order):
        print ("F1: %s     HP:(%i) |:Round: %i :| F2: %s      HP:(%i)")%(attack_order[0].name,attack_order[0].hppool,self.round,attack_order[1].name,attack_order[1].hppool)

    def PrintWinner(self,attack_order):
        fighter = attack_order
        if fighter[0].hppool <= 0:
            print ("%s LOST!!! In Round: %i ")%(fighter[0].name,self.round)
        elif fighter[1].hppool <= 0: 
            print ("%s LOST!!! In Round: %i ")%(fighter[1].name,self.round)
        else: print (" This Battle is a DRAW!!! In Round: %i ")%(self.round)    

    def PrintFighterNames(self,attack_order):
        attack_order
        print ("               |%s|:VS:|%s|")%(attack_order[0].name,attack_order[1].name) 


    def PrintRound(self):
        print ("Round: %i")%(self.round)

    @staticmethod
    def PrintAttackBreakdown(self,attack_order):# TODO: Make this iterate over the list of stats
        print("From PrintAttackBreakdown",attack_order)
        print ("Attacker: %s - Defender: %s")%(attack_order[0].name,attack_order[1].name)
        print("\n")
        time.sleep(Combat.time2)
        print ("Atacker/Defender Health points:             (%5i) / (%5i)")%(attack_order[0].hppool,attack_order[1].hppool)
        time.sleep(Combat.time2)       
        print ("Atacker/Defender Inititive:                 (%5i) / (%5i)")%(attack_order[0].agilitypool,attack_order[1].agilitypool)
        time.sleep(Combat.time2)
        print ("Atacker/Defender Accuracy/Evasion:          (%5i) / (%5i)")%(attack_order[0].accuracypool,attack_order[1].evasionpool)
        time.sleep(Combat.time2)
        print ("Atacker/Defender Attack Power/ Defenses:    (%5i) / (%5i)")%(attack_order[0].modifiedattackpool,attack_order[1].defensepool)
        time.sleep(Combat.time2)
        print ("Attacker/Defender Tao points:               (%5i) / (%5i)")%(attack_order[0].taopool,attack_order[1].taopool)
        time.sleep(Combat.time2)
        print ("Attacker/Defender Stamina:                  (%5i) / (%5i)")%(attack_order[0].staminapool,attack_order[1].staminapool)
        time.sleep(Combat.time2)
        print ("Attacker Attack Action:(%s)")%(attack_order[0].attackaction)
        print ("Defender Defense Action:(%s)")%(attack_order[1].defenseaction)

        time.sleep(Combat.time2)    
        print ("Base Damage potential done by attacker:         (%5i)") %(attack_order[0].basemodifiedattackpool)  
        print ("                           ---               ")
        print("\n") 


    @staticmethod        
    def PrintHeadings(self,attack_order):
        time.sleep(Combat.time2)
        print ("\n")
        print("THE COMBAT IS ABOUT TO BEGIN!")
        print ("\n")
        Combat.PrintFighterNames(self,attack_order)
        print("\n")
        if self.round == 1:
            time.sleep(Combat.time2)

        return   

#TODO: Make print statements use regex and loop over stats              
    def PrintStatsComplete(self,attack_order):
        print ("\n")        
        print ("Name:             (%5s)           (%5s) ")%(attack_order[0].name,attack_order[1].name)       
        print ("Experience points:(%5s)           (%5s) ")%(attack_order[0].experiencepointscurrent,attack_order[1].experiencepointscurrent) 
        #print ("Adv Points:       (%5s)           (%5s) ")%(attack_order[0].buildpoints,attack_order[1].buildpoints)
        print ("Userid:           (%5s)           (%5s) ")%(attack_order[0].userid,attack_order[1].userid) 
        print ("equipment")
        print ("equipped")
        print ("current weapon")
        print ("chi:              (%5s)           (%5s) ")%(attack_order[0].chi,attack_order[1].chi) 
        print ("ArmorDR:          (%5s)           (%5s) ")%(attack_order[0].armorDR,attack_order[1].armorDR) 
        #print ("Notsleeping:%s")%(attack_order.notsleeping)                   
        #print ("isinvisible:%s")%(attack_order.isvisible)                     
        #print ("isloggedin:%s")%(attack_order.isloggedin)                    
        print ("intelegence       (%5s)           (%5s) ")%(attack_order[0].intelegence,attack_order[1].intelegence)
        print ("strength:         (%5s)           (%5s) ")%(attack_order[0].strength,attack_order[1].strength)
        print ("dex:              (%5s)           (%5s) ")%(attack_order[0].dexterity,attack_order[1].dexterity)
        print ("perception        (%5s)           (%5s) ")%(attack_order[0].perception,attack_order[1].perception)
        print ("tao:              (%5s)           (%5s) ")%(attack_order[0].tao,attack_order[1].tao)
        print ("stamina:          (%5s)           (%5s) ")%(attack_order[0].stamina,attack_order[1].stamina)
        print ("luck:             (%5s)           (%5s) ")%(attack_order[0].luck,attack_order[1].luck)
        print ("health:           (%5s)           (%5s) ")%(attack_order[0].health,attack_order[1].health)
        print ("*healthpoints:    (%5s)           (%5s) ")%(attack_order[0].healthpoints,attack_order[1].healthpoints)
        print ("*agility:         (%5s)           (%5s) ")%(attack_order[0].agility,attack_order[1].agility)
        print ("*reflexes:        (%5s)           (%5s) ")%(attack_order[0].reflexes,attack_order[1].reflexes)
        print ("*evasion:         (%5s)           (%5s) ")%(attack_order[0].evasion,attack_order[1].evasion)
        print ("*weaponskill:     (%5s)           (%5s) ")%(attack_order[0].weaponskill,attack_order[1].weaponskill)
        print ("*weapondamage:    (%5s)           (%5s) ")%(attack_order[0].weapondamage,attack_order[1].weapondamage)
        print ("*accuracy:        (%5s)           (%5s) ")%(attack_order[0].accuracy,attack_order[1].accuracy)
        print ("*activedefense:   (%5s)           (%5s) ")%(attack_order[0].activedefense,attack_order[1].activedefense)
        print ("*balance          (%5s)           (%5s) ")%(attack_order[0].balance,attack_order[1].balance)    
        print ("*attack:          (%5s)           (%5s) ")%(attack_order[0].attack,attack_order[1].attack)
        print ("*defense          (%5s)           (%5s) ")%(attack_order[0].defense,attack_order[1].defense)
        print ("**reflexespool:   (%5s)           (%5s) ")%(attack_order[0].reflexespool,attack_order[1].reflexespool)
        print ("**basemodifiedattackpool:(%5s)           (%5s) ")%(attack_order[0].basemodifiedattackpool,attack_order[1].basemodifiedattackpool)
        print ("**modifiedattackpool(%5s)           (%5s) ")%(attack_order[0].modifiedattackpool,attack_order[1].modifiedattackpool)
        print ("**basedefensepool  (%5s)           (%5s) ")%(attack_order[0].basedefensepool,attack_order[1].basedefensepool)
        print ("**defensepool:     (%5s)           (%5s) ")%(attack_order[0].defensepool,attack_order[1].defensepool)
        print ("**hitpointspool:   (%5s)           (%5s) ")%(attack_order[0].hitpointspool,attack_order[1].hitpointspool)
        print ("**hppool:          (%5s)           (%5s) ")%(attack_order[0].hppool,attack_order[1].hppool)
        print ("**accuracypool:    (%5s)           (%5s) ")%(attack_order[0].accuracypool,attack_order[1].accuracypool)
        print ("**evasionpool:     (%5s)           (%5s) ")%(attack_order[0].evasionpool,attack_order[1].evasionpool)
        print ("**staminapool:     (%5s)           (%5s) ")%(attack_order[0].staminapool,attack_order[1].staminapool)
        print ("**taopool:         (%5s)           (%5s) ")%(attack_order[0].taopool,attack_order[1].taopool)
        print ("**agilitypool:     (%5s)           (%5s) ")%(attack_order[0].agilitypool,attack_order[1].agilitypool)
        print ("**attackaction:    (%5s)           (%5s) ")%(attack_order[0].attackaction,attack_order[1].attackaction)
        print ("**defenseaction:   (%5s)           (%5s) ")%(attack_order[0].defenseaction,attack_order[1].defenseaction)
        #print ("isattacker:%b")%(attack_order.isattacker)               acker)                                       
    # print ("reflexes:         (%5s)           (%5s) ")%(attack_order[0].reflexespool,attack_order[1].reflexespool)
    # print ("accuracypool:     (%5s)           (%5s) ")%(attack_order[0].accuracypool,attack_order[1].accuracypool)  
        #print ("evasionpool:      (%5s)           (%5s) ")%(attack_order[0].evasionpool,attack_order[1].evasionpool) 
    # print ("reflexespool:     (%5s)           (%5s) ")%(attack_order[0].taopool,attack_order[1].taopool) 
        print ("***currenthelathpoints:    (%5s)           (%5s) ")%(attack_order[0].currenthealthpoints,attack_order[1].currenthealthpoints)  
        print ("***basehealthpoints:       (%5s)           (%5s) ")%(attack_order[0].basehealthpoints,attack_order[1].basehealthpoints) 
        print ("***healthpointsdiofference:(%5s)           (%5s) ")%(attack_order[0].healthpointsdifference,attack_order[1].healthpointsdifference) 

        print ("*attack:                   (%5s)           (%5s) ")%(attack_order[0].attack,attack_order[1].attack) 
        print ("*modifiedattackpool:       (%5s)           (%5s) ")%(attack_order[0].modifiedattackpool,attack_order[1].modifiedattackpool) 
        print ("*attackdamageinflicted:    (%5s)           (%5s) ")%(attack_order[0].attackdamageinflicted,attack_order[1].attackdamageinflicted) 

        print ("***modifieddefensescore:   (%5s)           (%5s) ")%(attack_order[0].defense,attack_order[1].defense) 
        print ("***currentdefense:         (%5s)           (%5s) ")%(attack_order[0].currentdefense,attack_order[1].currentdefense) 
        print ("***defensepool:            (%5s)           (%5s) ")%(attack_order[0].defensepool,attack_order[1].defensepool) 
        print ("***damagerecieved:         (%5s)           (%5s) ")%(attack_order[0].damagerecieved,attack_order[1].damagerecieved) 

        print ("\n")
        print ("\n") 


    def reflexespool(self,player):
        #this is the Reflexes estimator
        player.reflexespool = ((player.reflexes * player.taopool)* player.perception)
        return (self.reflexespool)

        #~ self.accuracypool = 0       
    def accuracypool(self,player):
        '''accuracy pool creator'''
        player.accuracypool = (player.reflexes + player.dexterity + player.perception + player.intelegence) / 3 * player.weaponskill + 1
        return (player.accuracypool) 

        #~ self.evasionpool =  0        
    def evasionpool(self,player):
        '''evasion pool creator'''
        player.evasionpool = ((player.reflexes * 2) + player.dexterity)* player.taopool + player.luck
        return (player.evasionpool) 

        #~ self.taopool = 0  do we really need this?      
    def taopool(self,player):
        '''tao pool creator'''
        player.taopool = player.taopool
        return (player.taopool) 

        #~ self.basemodifiedattackpool  = 0         
    def basemodifiedattackpool(self,player):
        '''damage pool creator'''
        player.basemodifiedattackpool = player.attack
        return (player.basemodifiedattackpool) 

        #~ self.modifiedattackpool = 0         
    def modifiedattackpool(self,player):
        '''damage pool creator'''
        player.modifiedattackpool = ((( player.strength + player.chi + player.health + player.weaponskill) /3 ))
        return (player.modifiedattackpool) 

        #~ self.basedefensepool = 0     
    def basedefensepool(self,player):
        '''defense creator depreciated'''
        player.basedefensepool = player.armorDR
        return (player.basedefensepool)  



        #~ self.defensepool  = 0 
    def defensepool(self,player):
        '''defense pool creator '''
        player.defensepool = (player.activedefense * player.tao + player.luck) + player.armorDR
        return (player.defensepool)  

        #~ self.agilitypool = 0       
    def agilitypool(self,player):
        '''agility pool creator'''
        player.agilitypool = (player.agility * player.taopool)
        return (player.agilitypool) 


        #~ self.hitpointspool = 0    Redundant???
    def hitpointspool(self,player):
        '''passive defense pool creator'''
        player.hitpointspool = ((player.strength + player.chi) * player.health ) * 10
        return (player.hitpointspool)  

        #~ self.hppool = 0  
    def hppool(self,player):
        '''hp pool creator'''
        player.hppool = ((player.strength + player.chi) * player.health ) 
        return (player.hppool)  

        #~ self.staminapool =  0    
    def staminapool(self,player):
        '''stamina pool creator'''
        player.staminapool = (player.strength + player.chi)
        return (player.staminapool)

    def Statspools(self,player):#TODO: Make these dicts work
        self.combatstats = {"BMAP":self.basemodifiedattackpool,"MAP":self.modifiedattackpool,\
                            "BDP":self.basedefensepool,"DP":self.defensepool,"HP":self.hitpointspool,"HPP":hppool,\
                            "AP":self.accuracypool,"EP":self.evasionpool,"SP":self.staminapool,"TP":self.taopool,"AP":self.agilitypool,\
                            "AA":self.attackaction,"DA":self.defenseaction,"AC":self.attackcombos,\
                            "DC":self.defensecombos,"IA":self.isattacker,"BP":self.balancepool,\
                            "CHP":self.currenthealthpoints,"BHP":self.basehealthpoints,\
                            "HPD":self.healthpointsdifference,"MHP":self.modifiedattackpool,\
                            "ADI":self.attackdamageinflicted,"MDS":self.modifieddefensescore,\
                            "CD":self.currentdefense,"DR":self.damagerecieved}

    def StatsTest(self,attack_order):
        for player in attack_order:
            for item in player.stats:
                print("%14s: %14s")%(item,player.stats.get(item,[0]))
            print("----\n")


def _TGSaves():

    pickle.dump(player1,file("YM_Char1.tg","w"))
    pickle.dump(player2,file("YM_Char2.tg","w"))
    print ("Character FILES SAVED") 

def _TGloads():
    player1 = pickle.load(file("YM_Char1.tg"))
    player2 = pickle.load(file("YM_Char2.tg"))
    attack_order = player1,player2  

    print ("PLAYER FILES LOADED") 
    print ("CHARACTER FILES LOADED For Realzzz")

    return (attack_order)

def _Message(self,message):
    print(message)

#class Messages

def DictUpdater(self,player):
    player.stats.update(player.stats)



