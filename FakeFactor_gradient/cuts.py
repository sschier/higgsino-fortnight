import re, time, copy, math
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True)
#from observables import *
 #------------------------------------------------------------------
class cuts:
    def __init__(self, obs):

        self.obs = obs
        #self.IDlist = obs.getIDelectronList()

    def getCuts(self, electronList):
        obs = self.obs
        #trigger variables
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        #electron variables
        IDlist = electronList
        #IDlist = obs.getIDelectronList()
        #n_baseel = obs.getNBaseel()

        #Make list of dictionaresy of cuts
        Dics = []
        for el in IDlist:
            elPt = el.Pt()
            elEta = abs(el.Eta())
            mt = obs.getMT(el)
            #Make dictionary of cuts
            Cuts = {}
            
            #if( n_baseel >= 1 ):
            #    Cuts["1el"] = True
            #else: Cuts["1el"] = False

            if( mt < 40. ):
                Cuts["40mt"] = True
            else:
                Cuts["40mt"] = False

            if( mt > 100. and mt < 200. ):
                Cuts["100mt200"] = True
            else: 
                Cuts["100mt200"] = False

            if( HLT_e5 ):
                Cuts["HLT_e5"] = True
            else: Cuts["HLT_e5"] = False

            if( HLT_e10 ):
                Cuts["HLT_e10"] = True
            else: Cuts["HLT_e10"] = False

            if( HLT_e15 ):
                Cuts["HLT_e15"] = True
            else: Cuts["HLT_e15"] = False

            if( HLT_e20 ):
                Cuts["HLT_e20"] = True
            else: Cuts["HLT_e20"] = False

            if( elPt > 0. and elPt <= 11 ):
                Cuts["el5"] = True
            else: Cuts["el5"] = False

            if( elPt > 11. and elPt <= 18 ):
                Cuts["el10"] = True
            else: Cuts["el10"] = False

            if( elPt > 18. and elPt <= 23 ):
                Cuts["el15"] = True
            else: Cuts["el15"] = False

            if( elPt > 23. ):
                Cuts["el20"] = True
            else: Cuts["el20"] = False

            if( elPt > 0. ):
                Cuts["el"] = True
            else: Cuts["el"] = False

            if( elEta >= 0.0 and elEta < 0.7 ):
                Cuts["elEta07"] = True
            else: Cuts["elEta07"] = False

            if( elEta >= 0.7 and elEta < 1.37 ):
                Cuts["elEta137"] = True
            else: Cuts["elEta137"] = False

            if( elEta >= 1.37 and elEta < 1.52 ):
                Cuts["elEta152"] = True
            else: Cuts["elEta152"] = False

            if( elEta >= 1.52 and elEta < 2.01 ):
                Cuts["elEta201"] = True
            else: Cuts["elEta201"] = False

            if( elEta >= 2.01 and elEta < 2.47 ):
                Cuts["elEta247"] = True
            else: Cuts["elEta247"] = False

            Dics.append(Cuts)

        return Dics


