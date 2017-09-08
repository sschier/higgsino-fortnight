import re, time, copy, math
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True)
#from observables import *
 #------------------------------------------------------------------
class cuts:
    def __init__(self, obs):

        self.obs = obs
        #self.IDlist = obs.getIDmuonList()

    def getCuts(self, muonList):
        obs = self.obs
        #trigger variables
        HLT_mu4, HLT_mu10, HLT_mu14, HLT_mu18 = obs.getTriggers()
        #muon variables
        IDlist = muonList
        #IDlist = obs.getIDmuonList()
        #n_basemu = obs.getNBasemu()
        n_bjet = obs.n_bjet
        j1pt = obs.jet_pt[0]/1000.

        #Make list of dictionaresy of cuts
        Dics = []
        for mu in IDlist:
            pt = mu.Pt()
            eta = abs(mu.Eta())
            mt = obs.getMT(mu)
            #Make dictionary of cuts
            Cuts = {}
            
            if( j1pt > 75. ):
                Cuts["j75"] = True
            else: Cuts["j75"] = False
            if( j1pt > 100. ):
                Cuts["j100"] = True
            else: Cuts["j100"] = False

            if( n_bjet == 0 ):
                Cuts["bveto"] = True
            else: Cuts["bveto"] = False

            #if( n_basemu >= 1 ):
            #    Cuts["1mu"] = True
            #else: Cuts["1mu"] = False

            if( mt < 30. ):
                Cuts["30mt"] = True
            else:
                Cuts["30mt"] = False

            if( mt < 50. ):
                Cuts["50mt"] = True
            else:
                Cuts["50mt"] = False

            if( mt < 40. ):
                Cuts["40mt"] = True
            else:
                Cuts["40mt"] = False

            if( mt > 100. and mt < 200. ):
                Cuts["100mt200"] = True
            else: 
                Cuts["100mt200"] = False

            if( HLT_mu4 ):
                Cuts["HLT_mu4"] = True
            else: Cuts["HLT_mu4"] = False

            if( HLT_mu10 ):
                Cuts["HLT_mu10"] = True
            else: Cuts["HLT_mu10"] = False

            if( HLT_mu14 ):
                Cuts["HLT_mu14"] = True
            else: Cuts["HLT_mu14"] = False

            if( HLT_mu18 ):
                Cuts["HLT_mu18"] = True
            else: Cuts["HLT_mu18"] = False

            if( pt > 0. and pt <= 11 ):
                Cuts["mu5"] = True
            else: Cuts["mu5"] = False

            if( pt > 11. and pt <= 15 ):
                Cuts["mu10"] = True
            else: Cuts["mu10"] = False

            if( pt > 15. and pt <= 20 ):
                Cuts["mu15"] = True
            else: Cuts["mu15"] = False

            if( pt > 20. ):
                Cuts["mu20"] = True
            else: Cuts["mu20"] = False

            if( pt > 0. ):
                Cuts["mu"] = True
            else: Cuts["mu"] = False

            if( eta >= 0.0 and eta < 0.7 ):
                Cuts["muEta07"] = True
            else: Cuts["muEta07"] = False

            if( eta >= 0.7 and eta < 1.37 ):
                Cuts["muEta137"] = True
            else: Cuts["muEta137"] = False

            if( eta >= 1.37 and eta < 1.52 ):
                Cuts["muEta152"] = True
            else: Cuts["muEta152"] = False

            if( eta >= 1.52 and eta < 2.01 ):
                Cuts["muEta201"] = True
            else: Cuts["muEta201"] = False

            if( eta >= 2.01 and eta < 2.47 ):
                Cuts["muEta247"] = True
            else: Cuts["muEta247"] = False

            Dics.append(Cuts)

        return Dics


    def getAIDCuts(self, muonList):
        obs = self.obs
        #trigger variables
        HLT_mu4, HLT_mu10, HLT_mu14, HLT_mu18 = obs.getTriggers()
        #muon variables
        AntiIDlist = muonList
        #AntiIDlist = obs.getAntiIDmuonList()
        #n_baseel = obs.getNBasemu()

        #Make list of dictionaresy of cuts
        Dics = []
        for mu in AntiIDlist:
            AntiIDpt = mu.Pt()
            mtAID =  obs.getMT(mu)
            #Make dictionary of cuts
            Cuts = {}
            
            #if( n_basemu >= 1 ):
            #    Cuts["1mu"] = True
            #else: Cuts["1mu"] = False

            if( mtAID < 40. ):
                Cuts["40mtAID"] = True
            else:
                Cuts["40mtAID"] = False

            if( mtAID > 100. and mtAID < 200. ):
                Cuts["100mtAID200"] = True
            else: 
                Cuts["100mtAID200"] = False

            if( HLT_mu4 ):
                Cuts["HLT_mu4"] = True
            else: Cuts["HLT_mu4"] = False

            if( HLT_mu10 ):
                Cuts["HLT_mu10"] = True
            else: Cuts["HLT_mu10"] = False

            if( HLT_mu14 ):
                Cuts["HLT_mu14"] = True
            else: Cuts["HLT_mu14"] = False

            if( HLT_mu18 ):
                Cuts["HLT_mu18"] = True
            else: Cuts["HLT_mu18"] = False

            if( AntiIDpt > 0. and AntiIDpt < 10 ):
                Cuts["antiidmu5"] = True
            else: Cuts["antiidmu5"] = False

            if( AntiIDpt >= 10. and AntiIDpt < 15 ):
                Cuts["antiidmu10"] = True
            else: Cuts["antiidmu10"] = False

            if( AntiIDpt >= 15. and AntiIDpt < 20 ):
                Cuts["antiidmu15"] = True
            else: Cuts["antiidmu15"] = False

            if( AntiIDpt >= 20. ):
                Cuts["antiidmu20"] = True
            else: Cuts["antiidmu20"] = False

            if( AntiIDpt > 0. ):
                Cuts["antiidmu"] = True
            else: Cuts["antiidmu"] = False

            Dics.append(Cuts)

        return Dics
