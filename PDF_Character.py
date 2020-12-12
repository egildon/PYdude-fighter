#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
#
#       CFCharacter.py
#


class CFCharactor:
    '''This is the base class for all cahracters in Capoeira Fighter'''
    def __init__(self, userid, name):

        self.userid = userid
        self.name = name
        is_in_roda = True
        is_conscious = True
        is_alive = True





        self.char_stats = {'char_name': name, 'exp_total':0, 'exp_current':0, 'sex':None, 'size':0, 'mestre':None,
                    'capoeira_school':None, 'corda':0, 'predction_ponts':0,
                    'malicia':0, 'spirit':0, 'swag':0,
                    'intelegence':0, 'strength':0, 'agility':0,
                    'perception':0, 'health':10, 'reflexes': 0, 'accuracy':0,
                      'mestre_levels':0, 'prediction_points':0}

        self.equipment = {'shirt':0, 'pants':0, 'shoes':0, 'cord':None,
                    'necklace':0, 'bracelet':0, 'anklet':0,
                    'hand_weapon':0, 'foot_weapon':0}

        self.techniques_level = {'ginga':1, 'meialua_de_frente':1, 'esquiva_na_ginga':1, 'deceda_basica':1}



def pool_balanca(char_stats):
    pool_balanca = (char_stats['agility'] *  char_stats['perception'] +  char_stats['reflexes'])
    return pool_balanca

def pool_health(char_stats):
    pool_health = (char_stats['health'] *  char_stats['spirit'] +  char_stats['strength'])
    return pool_health

def pool_stamina(char_stats):
    pool_stamina = (char_stats['agility'] *  char_stats['spirit'] +  pool_health)
    return pool_stamina

def pool_axe(char_stats):
    pool_axe = (char_stats['spirit'] * char_stats['malicia'] + char_stats['swag'])
    print('axe:', pool_axe)
    return pool_axe

def combat_strike(char_stats, pools,techniques_level):
    #TODO Make Esquiva a function in combat
    accuracy = (char_stats['intelegence'] + pools.pool_balanca - pools.pool_stamina)
    return accuracy


def combat_esquiva(char_stats, pools,techniques_level):
    #TODO Make Esquiva a function in combat
    esquiva = (char_stats['intelgence'] *  char_stats['malicia'] +  char_stats['agility'] +  char_stats['perception'] - pools.pool_stamina)
    return esquiva


#p1 = CFCharactor('Bambam@googs.net', 'Sebathius')


##print(p1.name)
#print('character Name: ', p1.char_stats['char_name'])
#print('Technique: ',p1.techniques_level['ginga'])
#print('Balance Pool: ',pool_balanca(p1.char_stats))
