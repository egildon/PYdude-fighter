#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       PDF_Body.py
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



class Head(object):
    def __init__(self,name):
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0


        self.EyeR ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}


        self.EyeL ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.Neck ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Face ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Throat ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.EarR ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.EarL ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
                        
        self.Mouth ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
class Torso(object):
    def __init__(self,name):
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0

        self.ShoulderR ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.ShoulderL ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.ChestF ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.ChestB ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.AbdomenF ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.AbdomenB ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

class Pelvis(object):
    def __init__(self,name):
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0


        self.Genetals ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.HipR ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.HipL ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.Tail ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        


class ArmR(object):
    def __init__(self,name):
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0


        self.UpperArm ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.LowerArm ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.Hand ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Fingers ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.Elbow ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Wrist ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    


class ArmL(object):
    def __init__(self,name):
        nerveystem = 0
        circulatorysystem = 0
        muscularsystem = 0
        skeletalattachment = 0


        self.UpperArm ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.LowerArm ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.Hand ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Fingers ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.Elbow ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Wrist ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    


class LegR(object):
    def __init__(self,name):
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0

        self.UpperLeg ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.LowerLeg ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.Foot ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Toes ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.Knee ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Ankle ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    


class LegL(object):
    def __init__(self,name):
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0

        self.UpperLeg ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.LowerLeg ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.Foot ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Toes ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.Knee ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Ankle ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    


class Skeleton(object):
    def __init__(self,name):
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0


        self.Skull ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Neck ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.CervicalSpine ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.ThoracicSpine ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Lubmbarspine ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.RibCage ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.LumbarPelvis ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.UpperLeg ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.LowerLeg ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.Foot ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Toes ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.Knee ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.Ankle ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    

        self.Tail ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}  

    
class Skin(object):
    def __init__(self,name):
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0


        self.Head ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}


        self.Neck ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.TorsoF ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.TorsoR ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.AbdomenF ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}
        
        self.AbdomenR ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.ArmsR ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}     
        
        self.ArmsL ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}   
        
        self.LegsR ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}  
        
        self.LegsL ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    
                                                
        self.Tail ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment} 
        
class InternalSystems(object):
    def __init__(self,name):
        
        self.nerveystem = 0
        self.circulatorysystem = 0
        self.muscularsystem = 0
        self.skeletalattachment = 0
        
        self.NervousSystem ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}

        self.CirculatorySystem ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}     
        
        self.LymphaticSystem ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}   
        
        self.RespertorySystem ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}  
        
        self.GISystem ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment}    
                                                
        self.MannaSystem ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment} 
                
        self.QiSystem ={"Name":self.name,"nervousSystem":self.nervesystem,\
        "muscularsystem":self.muscularsystem,"circulatorysystm":self.circulatorysystem,\
        "skeletalattachment":self.skeletalattachment} 
