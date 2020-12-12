#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      PDF_StatsMonitorThread.py
#       
#       Copyright 2011 earnest gildon <egildon@TheBeast>
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
#       

import random
import time
import threading

from operator import itemgetter, attrgetter
import pickle
import re



#TODO Not working make this work
class StatsPool(object):
    def __init__(self,name):
        #visible stats:
        self.Focus
        self.Pleasure
        self.Pain
        self.Hunger #(red/green/blue ie: red- protien, green- vitamins, blue- water)       
        #Overall stamina/health
        self.stamina_Aerobic
        self.stamina_ArmRight
        self.stamina_ArmLeft
        self.stamina_LegRight
        self.stamina_LegLeft
        self.stamina_torso/hips
        self.stamina_neck
        self.stamina_mind

        #Only visible if trained:
        self.Mana
        self.Qi


class StatsMonitor(object):
    def __init__(self,name):
        self.pain_pool = 0 #TODO New pools to create and monitor with multiprocess thread
        self.pleasur_pool = 0 #TODO use pain gate theory
        self.focus_pool = 0
        self.stamina_pool = 0
        self.mana_pool = 0
        self.mentalbalance_pool = 0
        self.qibalance_pool = 0
        self.physicalbalance_pool = 0

        self.visibleperception #invisible to player
        self.auditoryperceptioin #invisible to player
        self.olfactoryperception #invisible to player
        self.tasteperception #invisible to player
        self.manaperception #invisible to player
        self.qiperception #invisible to player
        #visible stats:




class StatsPool(object):
    def __init__(self,name):
        #visible stats:
        self.Focus
        self.Pleasure
        self.Pain
        self.Hunger #(red/green/blue ie: red- protien, green- vitamins, blue- water)       
        #Overall stamina/health
        self.stamina_Aerobic
        self.stamina_ArmRight
        self.stamina_ArmLeft
        self.stamina_LegRight
        self.stamina_LegLeft
        self.stamina_torso/hips
        self.stamina_neck
        self.stamina_mind
        #Only visible if trained:
        self.Mana
        self.Qi

