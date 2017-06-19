import re, time, copy, math, array
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
            IDpt = el.Pt()
            mtID = obs.getMT(el)
            #Make dictionary of cuts
            Cuts = {}
            
            #if( n_baseel >= 1 ):
            #    Cuts["1el"] = True
            #else: Cuts["1el"] = False

            if( mtID < 40. ):
                Cuts["40mt"] = True
            else:
                Cuts["40mt"] = False

            if( mtID > 100. and mtID < 200. ):
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

            if( IDpt > 0. and IDpt <= 11 ):
                Cuts["el5"] = True
            else: Cuts["el5"] = False

            if( IDpt > 11. and IDpt <= 18 ):
                Cuts["el10"] = True
            else: Cuts["el10"] = False

            if( IDpt > 18. and IDpt <= 23 ):
                Cuts["el15"] = True
            else: Cuts["el15"] = False

            if( IDpt > 23. ):
                Cuts["el20"] = True
            else: Cuts["el20"] = False

            if( IDpt > 0. ):
                Cuts["el"] = True
            else: Cuts["el"] = False

            Dics.append(Cuts)

        return Dics


