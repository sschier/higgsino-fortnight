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

    def getIDCuts(self, electronList):
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
                Cuts["40mtID"] = True
            else:
                Cuts["40mtID"] = False

            if( mtID > 100. and mtID < 200. ):
                Cuts["100mtID200"] = True
            else: 
                Cuts["100mtID200"] = False

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

            if( IDpt > 0. and IDpt < 10 ):
                Cuts["idel5"] = True
            else: Cuts["idel5"] = False

            if( IDpt >= 10. and IDpt < 15 ):
                Cuts["idel10"] = True
            else: Cuts["idel10"] = False

            if( IDpt >= 15. and IDpt < 20 ):
                Cuts["idel15"] = True
            else: Cuts["idel15"] = False

            if( IDpt >= 20. ):
                Cuts["idel20"] = True
            else: Cuts["idel20"] = False

            if( IDpt > 0. ):
                Cuts["idel"] = True
            else: Cuts["idel"] = False

            Dics.append(Cuts)

        return Dics


    def getAIDCuts(self, electronList):
        obs = self.obs
        #trigger variables
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        #electron variables
        AntiIDlist = electronList
        #AntiIDlist = obs.getAntiIDelectronList()
        #n_baseel = obs.getNBaseel()

        #Make list of dictionaresy of cuts
        Dics = []
        for el in AntiIDlist:
            AntiIDpt = el.Pt()
            mtAID =  obs.getMT(el)
            #Make dictionary of cuts
            Cuts = {}
            
            #if( n_baseel >= 1 ):
            #    Cuts["1el"] = True
            #else: Cuts["1el"] = False

            if( mtAID < 40. ):
                Cuts["40mtAID"] = True
            else:
                Cuts["40mtAID"] = False

            if( mtAID > 100. and mtAID < 200. ):
                Cuts["100mtAID200"] = True
            else: 
                Cuts["100mtAID200"] = False

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

            if( AntiIDpt > 0. and AntiIDpt < 10 ):
                Cuts["antiidel5"] = True
            else: Cuts["antiidel5"] = False

            if( AntiIDpt >= 10. and AntiIDpt < 15 ):
                Cuts["antiidel10"] = True
            else: Cuts["antiidel10"] = False

            if( AntiIDpt >= 15. and AntiIDpt < 20 ):
                Cuts["antiidel15"] = True
            else: Cuts["antiidel15"] = False

            if( AntiIDpt >= 20. ):
                Cuts["antiidel20"] = True
            else: Cuts["antiidel20"] = False

            if( AntiIDpt > 0. ):
                Cuts["antiidel"] = True
            else: Cuts["antiidel"] = False

            Dics.append(Cuts)

        return Dics
