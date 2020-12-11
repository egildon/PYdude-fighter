import YM_Character

class StatsMonitor():

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