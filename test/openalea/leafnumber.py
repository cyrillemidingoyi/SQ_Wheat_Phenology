import numpy as np 
from copy import copy
from math import *

def leafnumber(deltaTT=23.5895677277,
               phyllochron=0.0,
               hasFlagLeafLiguleAppeared=0,
               switchMaize=0,
               atip=10.0,
               leaf_tip_emerg=10.0,
               k_bl=1.412,
               nlim=6.617,
               leafNumber=0.0,
               cumulTTPhenoMaizeAtEmergence=300.0,
               cumulTT=402.042720581,
               phase=1.0):
    """


    CalculateLeafNumber Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA Montpellier
    Abstract: calculate leaf number. LeafNumber increase is caped at one more leaf per day

    """
    leafNumber1 =leafNumber
    ntip=0   
    if (phase == 1 and cumulTTPhenoMaizeAtEmergence == 0):
        cumulTTPhenoMaizeAtEmergence = cumulTT        
    if (phase >= 1 and phase< 4):       
        if (hasFlagLeafLiguleAppeared==0): 
            if (switchMaize==0):            
                if (phyllochron == 0.0):
                    phyllochron = 0.0000001
                leafNumber = leafNumber1 + min(deltaTT / phyllochron, 0.999)
                ntip=0
            else:
                if (leafNumber1 < leaf_tip_emerg):
                    leafNumber = leaf_tip_emerg        
                else:
                    nextstartExpTT = 0
                    nexttipTT = ((leafNumber1 + 1) - leaf_tip_emerg) / atip + cumulTTPhenoMaizeAtEmergence
                    abl = k_bl * atip
                    tt_lim_lip = ((nlim - leaf_tip_emerg) / atip) + cumulTTPhenoMaizeAtEmergence
                    bbl = nlim - (abl * tt_lim_lip)
                    tt_bl = ((leafNumber1 + 1) - bbl) / abl
                    if (tt_bl > nexttipTT):
                        nextstartExpTT = nexttipTT
                    else:     
                        nextstartExpTT = tt_bl    
                    if (cumulTT >= nextstartExpTT):  
                        leafNumber = leafNumber1 + 1    
                    else:   
                        leafNumber = leafNumber1
                ntip = atip * (cumulTT - cumulTTPhenoMaizeAtEmergence) + leaf_tip_emerg
    return  leafNumber, ntip
