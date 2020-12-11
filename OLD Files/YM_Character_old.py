#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       YM_Character.py
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

import random
import time
import threading

print ("The YM_Character Module")


class Charactor(object):
    def __init__(self,name):#,intelegence,strength,dexterity,perception):
        #the player charactor
        self.name = name
        self.experiencepointstotal = 0 #collect this and use these and buildpoints to buy skills and stats
        self.experiencepointscurrent = ()
        self.buildpointsapplied = {"intelegence":None,"chi":None,"strength":None,"dexterity":None,"perception":None,"luck":None,"health":None,"agility":None,"reflexes":None,"evasion":None,"accuracy":None,"style":None} #this is a list of dictionaries it will list every skill you can advance and your current points in the skill(earned from use of that skill). You apply experience points to purchase advancement points from this list at 100exp per advancementpoint.
        self.buildpointstotal = ()
        self.buildpointscurrent = () 
        self.userid ="egildon@gmail.com"        
        self.equipment = {"Slot1":None,"Slot2":None,"Slot3":None,"Slot4":None,"Slot5":None}
        self.equipped = {"HEAD":None,"TORSO":None,"ARMS":None,"LEGS":None,"FEET":None,"HANDS":None,"Face":None}
        self.currentweapon = {"NorthFist":{"TrainingLevel":1,"Attributes":{"speed":1,"accuracy":1,"power":1,"evasion":1,"parry":1,"repost":1,"throw":1,"pressurepointattack":1}}}
        self.notsleeping = True
        self.isvisible = True
        self.isloggedin = True  
        self.currentweapontraininglvl = 1
        self.weaponquality = 1
        #self.chi = 2 #(random.randint(1,10))
        self.armorDR = 2        
        self.stylesknown = []   
        self.chi = 2 #(random.randint(1,10))        
        self.intelegence = 2 # (random.randint(1,10))
        self.strength =  2 #(random.randint(1,10))
        self.dexterity =  (random.randint(1,10))
        self.perception = (random.randint(1,10))
        self.tao = 3
        self.stamina = (self.strength + self.chi)
        self.luck = (random.randint(1,3))
        self.health = ((self.strength + self.chi + self.tao ) / 3)
        """Methods to develop?"""    
        #testing to see if these work:
        
        self.healthpoints =  ( self.health )* 10
        self.agility = (( self.dexterity + self.health )/2)+self.luck       
        self.reflexes = (((self.agility + self.intelegence + self.perception)))/3# do this in Combat : " * self.tao)* self.perception)"
        self.evasion =  1#((2 * self.reflexes) + self.dexterity)#In Combat: * self.tao + self.luck
        self.weaponskill = 1 + ((self.dexterity + self.reflexes + self.health) / 2) * self.currentweapontraininglvl #accuracy and defense multiplier
        self.weapondamage = 1 + (self.chi + self.weaponskill + self.weaponquality) / 2 # Damage multiplier
        self.accuracy = (self.reflexes + self.dexterity + self.perception + self.intelegence) / 3 * self.weaponskill + 1
        self.activedefense = ((((self.agility + self.weapondamage + self.intelegence) / 3) * self.weaponskill))# in combat: " * self.tao)"
        self.balance = (self.tao + self.chi)/2
        self.attack = (((( self.strength + self.chi + self.health + self.weaponskill) /3 ))  * self.weapondamage)        
        self.defense = (self.activedefense +  self.armorDR)
        """Pools are created for adjustment in combat"""   
        self.characterinfo = {"Name":self.name}
        

        self.reflexespool = 0#self.defensepool = self.defens0
        self.basemodifiedattackpool  = 0 #modified/combined attack value
        self.modifiedattackpool = 0
        self.damagerecieved = 0 #damage that actually reaches target
        self.basedefensepool = 0#modified/combined defense value
        self.defensepool  = 0#defense that actually defends vs modifiedattackpool
        self.hitpointspool = 0#modified hp placeholder as base value
        self.hppool = 0#fluctuating value with plus/minus damage
        self.accuracypool = 0 
        self.evasionpool =  0
        self.staminapool =  0
        self.taopool = 3
        self.agilitypool = 0
        self.attackaction = None
        self.defenseaction = None
        self.attackcombos = {}
        self.defensecombos = {}
        self.isattacker = None
        self.balancepool = 0
        #Todo make new pools work
        self.bloodpool = 0
        self.shockpool = 0
        self.painpool = 0
        
        #Todo New pools
        self.visiblepainpool = 0
        self.visiblefocuspool = 0
        self.visiblestaminapool = 0
        self.visiblemanapool = 0
        self.visibleqipool = 0
                
        
        self.currenthealthpoints = 0
        self.basehealthpoints = self.healthpoints
        self.healthpointsdifference = self.currenthealthpoints - self.basehealthpoints        
       
        self.modifiedattackpool = 0 #damage that actually reaches target
        self.attackdamageinflicted = self.modifiedattackpool - self.defensepool

        #self.modifieddefensescore = self.defense
        self.currentdefense = 0
        #self.defensepool = self.defense + self.armorDR   
        
        self.damagerecieved = 0    
            
        self.IntelegenceQuotient = 0 #player facing section affects groups with kinetic focus
        self.KineticQuotient = 0 #player facing section affects groups in intelegence focus
        self.EmotionalQuotient = 0 #player facing section affects groups in emotional focus
        self.ChakaraQuotient = 0 #player facing section affects groups in chakara focus
        self.Humanity = 0 #player facing section visible, effected by social penalties, visible only as aura.
		
        
        self.stats ={"Name":self.name,"Exp":self.experiencepointscurrent,\
        "BuildPoints":self.buildpointscurrent,"UserId":self.userid,\
        "Chi":self.chi,"Intelegence":self.intelegence,"Strength":self.strength,\
        "Dexterity":self.dexterity,"Perception":self.perception,"Tao":self.tao,\
        "Stamina":self.stamina,"Luck":self.luck}
      
        self.completestats = {"Name":self.name,"Exp":self.experiencepointstotal,\
        "ExpC":self.experiencepointscurrent,"BP":self.buildpointsapplied,\
        "BPT":self.buildpointstotal,"BPC":self.buildpointscurrent,"UID":self.userid,\
        "Eq":self.equipment,"Equipped":self.equipped,"CW":self.currentweapon,"NS":self.notsleeping,\
        "Inv":self.isvisible,"Ilogged":self.isloggedin,"CWTrainingLvl":self.currentweapontraininglvl,\
        "WQ":self.weaponquality,"Chi":self.chi,"ADR":self.armorDR,"Styles":self.stylesknown,"Int":self.intelegence,\
        "Strength":self.strength,"Dexterity":self.dexterity,\
        "Perception":self.perception,"Tao":self.tao,"Stamina":self.stamina,\
        "Luck":self.luck,"Health":self.health,"HP":self.healthpoints,"Agi":self.agility,"Reflexes":self.reflexes,\
        "Evasion":self.evasion,"WeaponSkill":self.weaponskill,"WeaponDamage":self.weapondamage,"Accuracy":self.accuracy,\
        "ActiveDefense":self.activedefense,"Balance":self.balance,\
        "Attack":self.attack,"Defense":self.defense,"CharacterInfo":self.characterinfo}
        
        self.combatstats = {"BMAP":self.basemodifiedattackpool,"MAP":self.modifiedattackpool,\
        "BDP":self.basedefensepool,"DP":self.defensepool,"HP":self.hitpointspool,"HPP":self.hppool,\
        "AP":self.accuracypool,"EP":self.evasionpool,"SP":self.staminapool,"TP":self.taopool,"AP":self.agilitypool,\
        "AA":self.attackaction,"DA":self.defenseaction,"AC":self.attackcombos,\
        "DC":self.defensecombos,"IA":self.isattacker,"BP":self.balancepool,\
        "CHP":self.currenthealthpoints,"BHP":self.basehealthpoints,\
        "HPD":self.healthpointsdifference,"MHP":self.modifiedattackpool,\
        #"ADI":self.attackdamageinflicted,"MDS":self.modifieddefensescore,\
        "CD":self.currentdefense,"DR":self.damagerecieved}
        
        self.combatstatspool = {"RefPool":self.reflexespool,\
        "AccuracyPool":self.accuracypool,"EvasionPool":self.evasionpool,\
        "Taopool":self.taopool,"BaseMAttackPool":self.basemodifiedattackpool,\
        "ModAttackpool":self.modifiedattackpool,"BaseDefPool":self.basedefensepool,\
        "DefensePool":self.defensepool,"AgilityPool":self.agilitypool,\
        "HitPointsPool":self.hitpointspool,"HPPool":self.hppool,"StaminaPool":self.staminapool}
        
        #SWThread1().start() #Attributes thread starter.
    def __repr__(self):
        return repr(self.name)      
        
         
    def  __str__(self):
        #this allows the call to crit1 (base) to print the self.name value
        rep ="Charactor object\n"
        rep += "Name: " + self.name +"\n"
        return rep 
        
    def __printOutStr__(self):
        #Print put entire character sheet
        rep ="Charactor object\n"
        rep += "Name: " + self.name +"\n"
        return rep 
        
    def get_name(self,):
        get_name = self.name
        if get_name == "":
            print('A Character name is required.')
        else:
            return get_name  
                      
    def set_name(self,new_name):
        if new_name == "":
            print('A Character name is required!')
        else:
            self.name = new_name
            print('Name change Complete.')
            print (self.name)
            

            
    def get_userid(self,):
        get_userid = self.userid
        if get_userid == "":
            print('A unique User ID is required.')
        else:
            return get_userid

    def set_userid(self,new_userid):
        if new_userid == "":
            print('A unique User ID is  is required!')
        else:
            self.userid = new_userid
            print('User Id change Complete.')
            print (self.userid)
            
    def get_equipment(self,get_equipment):
        get_equipment = self.equipment
        if get_equipment == "":
            print('A piece of equipment is required.')
                    
        else:
            for item in self.equipment:
                print(item)
            return self.equipment 
                      
    def set_equipment(self,new_equipment):
        if new_equipment == "":
            print('A piece of equipment is required!')
        else:
            self.equipment += new_equipment
            print('Equipment added Complete.')
            print (self.equipment)
            
    def drop_equipment(self,drop_equipment):
        if drop_equipment == "":
            print ('there is nothing here to drop')
        else:
            self.equipment -= drop_equipment
            print ('Equipment Drop Complete')
            print (drop_equipment)
            
            
    def get_equipped(self,get_equipped_item):
        get_equippen = self.equipped
        if get_equipment == "":
            print('A piece of equipment is required.')
        else:
            return self.equipment 
                      
    def set_equipment(self,new_equipped_item):
        if new_equipped_item == "":
            print('A piece of equipment is required!')
        else:
            self.equipment -= new_equipped_item
            self.equipped_item += new_equipped_item
            
            print('Item Equipped: Complete.')
            print (self.equipped_item)
            
    def drop_equipped_item(self,drop_equipment):
        if drop_equipment == "":
            print ('there is nothing here to unequip')
        else:
            self.equipment += drop_equipment           
            self.equipped_item -= drop_equipment

            print ('Equipment unequip Complete')
            print (drop_equipment)

    def get_weapon(self,):
        get_weapon = self.weapon
        if get_weapon == "":
            print('A weapon is required.')
        else:
            return get_weapon

    def set_weapon(self,new_weapon):
        if new_weapon == "":
            print('A weapon is required!')
        else:
            self.weapon = new_weapon
            print('User weapon change Complete.')
            print (self.weapon)
            
    def get_weapontraining(self,):
        get_weapontraining = self.weapontraining
        if get_weapontraining == "":
            print('A martial style is required.')
        else:
            return self.weapontraining

    def set_weapontraining(self,new_weapontraining):
        if new_weapontraining == "":
            print('A martial style is  is required!')
        else:
            self.weapontraining = new_weapontraining
            print('User martial training Complete.')
            print (self.weapontraining) 
                       
    def get_chi(self,):
        get_chi = self.chi
        if self.chi == "":
            print('A number value for chi is required.')
        else:
            return get_chi

    def set_chi(self,new_chi):
        if new_chi == "":
            print('A number value for chi is required!')
        else:
            self.chi = new_chi
            print('User chi change Complete.')
            print (self.chi)

    def get_armorDR(self,):
        get_armorDR = self.armorDR
        if get_armorDR == "":
            print('A number value for armorDR is required.')
        else:
            return self.armorDR

    def set_armorDR(selfS,new_armorDR):
        if new_armorDR == "":
            print('A number value for armorDR is required!')
        else:
            self.armorDR = new_armorDR
            print('User armorDR change Complete.')
            print (self.armorDR)

    def get_notsleeping(self,):
        get_notsleeping = self.notsleeping
        if get_notsleeping == "":
            print('A Boolian value for notsleeping is required.')
        else:
            return self.notsleeping

    def set_notsleeping(self,new_notsleeping):
        if new_notsleeping == "":
            print('A Boolian value for notsleeping is required!')
        else:
            self.notsleeping = new_notsleeping
            print('User notsleeping change Complete.')
            print (self.notsleeping)
    def get_isvisible(self,):
        get_isinvisible = self.isinvisible
        if get_isvisible == "":
            print('A Boolian value for isvisible is required.')
        else:
            return self.isvisible

    def set_isvisible(self,new_isvisible):
        if new_isvisible == "":
            print('A Boolian value for isvisible is required!')
        else:
            self.isvisible = new_isvisible
            print('User isvisible change Complete.')
            print (self.isvisible)
            
    def get_isloggedin(self,):
        get_isloggedin = self.isloggedin
        if get_isloggedin == "":
            print('A Boolian value for isloggedin is required.')
        else:
            return self.isloggedin

    def set_isloggedin(self,new_isloggedin):
        if new_isloggedin == "":
            print('A Boolian value for isloggedin is required!')
        else:
            self.isloggedin = new_isloggedin
            print('User isloggedin change Complete.')
            print (self.isloggedin)

    def get_stylesknown(self,):
        get_stylesknown = self.stylesknown
        if self.stylesknown == "":
            print('A number value for stylesknown is required.')
        else:
            return self.stylesknown

    def set_stylesknown(self,new_stylesknown):
        if new_stylesknown == "":
            print('A number value for stylesknown is required!')
        else:
            self.stylesknown = new_stylesknown
            print('User stylesknown change Complete.')
            print (self.stylesknown)

    def get_intelegence(self,):
        get_intelegence = self.intelegence
        if self.intelegence == "":
            print('A number value for intelegence is required.')
        else:
            return self.intelegence

    def set_intelegence(self,new_intelegence):
        if new_intelegence == "":
            print('A number value for intelegence is required!')
        else:
            self.intelegence = new_intelegence
            print('User intelegence change Complete.')
            print (self.intelegence)

    def get_strength(self,):
        get_strength = self.strength
        if self.strength == "":
            print('A number value for strength is required.')
        else:
            return self.strength

    def set_strength(self,new_strength):
        if new_strength == "":
            print('A number value for strength is required!')
        else:
            self.strength = new_strength
            print('User strength change Complete.')
            print (self.strength)

    def get_dexterity(self,):
        get_dexterity = self.dexterity
        if get_dexterity == "":
            print('A number value for dexterity is required.')
        else:
            return self.dexterity

    def set_dexterity(self,new_dexterity):
        if new_dexterity == "":
            print('A number value for dexterity is required!')
        else:
            self.dexterity = new_dexterity
            print('User dexterity change Complete.')
            print (self.dexterity)

    def get_perception(self,):
        get_perception = self.perception
        if get_perception == "":
            print('A number value for perception is required.')
        else:
            return self.perception

    def set_perception(self,new_perception):
        if new_perception == "":
            print('A number value for perception is required!')
        else:
            self.perception = new_perception
            print('User perception change Complete.')
            print (self.perception)

    def get_tao(self,):
        get_tao = self.tao
        if get_tao == "":
            print('A number value for tao is required.')
        else:
            return self.tao

    def set_tao(self,new_tao):
        if new_tao == "":
            print('A number value for tao is required!')
        else:
            self.tao = new_tao
            print('User tao change Complete.')
            print (self.tao)


    def SWSaves():       
        # Pickle the SW files
        pickle_file1 = file("SW_Char1.sw","w",2)
        pickle.dump(player1,pickle_file1,)
        pickle_file1.close()    
        print("\n")
        print("CHARACTERS FILES 1 SAVED")   
        # Pickle the SW files
        pickle_file2 = file("SW_Char2.sw","w",2)
        pickle.dump(player2,pickle_file2,)
        pickle_file2.close()
        print("\n")
        print("CHARACTERS FILES 2 SAVED")
        
        pickle.dump(player1,file("SW_Char1.sw","w"))
        pickle.dump(player2,file("SW_Char2.sw.sw","w"))
        pickle_file2.close()
        print ("Character FILES SAVED") 
         
    def SWloads(self):
        player1 = pickle.load(file("SW_Char1.sw"))
        player2 = pickle.load(file("SW_Char2.sw"))
        attack_order = player1,player2  
        print ("PLAYER FILES LOADED") 
        print (attack_order,":from load file")
        return (attack_order)
#TODO: Add get and set or possibly constructors for Equipment classes.
#TODO: Add get and set or possibly constructors for Martial Style classes.
