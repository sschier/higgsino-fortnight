import re, time, copy, math
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True)
#from observables import *
 #------------------------------------------------------------------
class recocuts:
    def __init__(self, obs):

        self.obs = obs

    def getCuts(self):
        obs = self.obs
        metTrig = obs.metTrig
        #Remember triggers!
        nBJet20 = obs.nBJet20
        j1pt = obs.jetPt[0]
        met = obs.met_Et
        DPhiJ1Met = obs.DPhiJ1Met
        minDPhiAllJetsMet = obs.minDPhiAllJetsMet
        nLep_signal = obs.nLep_signal
        nLep_base = obs.nLep_base
        isOSSF = obs.isOSSF()
        lep1Pt = obs.lep1Pt
        MTauTau = obs.MTauTau
        mll = obs.mll
        Rll = obs.Rll
        METOverHTLep = obs.METOverHTLep
        mt2 = obs.mt2leplsp_100
        mt_lep1 = obs.mt_lep1



        #Make list of dictionaresy of cuts
        #Dics = []
        #Make dictionary of cuts
        Cuts = {}
        
        if( metTrig ):
            Cuts["Trigger"] = True
        else: Cuts["Trigger"] = False

        if( nBJet20 == 0 ):
            Cuts["bVeto"] = True
        else: Cuts["bVeto"] = False

        if( met > 200. ):
            Cuts["met200"] = True
        else: Cuts["met200"] = False

        if( j1pt > 100. ):
            Cuts["j100"] = True
        else: Cuts["j100"] = False

        if( DPhiJ1Met > 2.0 ):
            Cuts["DPhiJ1Met"] = True
        else: Cuts["DPhiJ1Met"] = False

        if( minDPhiAllJetsMet > 0.4 ):
            Cuts["minDPhi"] = True
        else: Cuts["minDPhi"] = False

        if( nLep_base == 2 and nLep_signal == 2 ):
            Cuts["2Lep"] = True
        else: Cuts["2Lep"] = False

        if( isOSSF ):
            Cuts["OSSF"] = True
        else: Cuts["OSSF"] = False

        if( lep1Pt > 5. ):
            Cuts["lep1Pt5"] = True
        else: Cuts["lep1Pt5"] = False

        if( MTauTau < 0. or MTauTau > 160. ):
            Cuts["MTauTau"] = True
        else: Cuts["MTauTau"] = False

        if( (mll > 1. and mll < 3.) or (mll > 3.2 and mll < 60.) ):
            Cuts["mll"] = True
        else: Cuts["mll"] = False

        if( Rll > 0.05 ):
            Cuts["rll05"] = True
        else: Cuts["rll05"] = False

        if( Rll < 2.0 ):
            Cuts["rll2"] = True
        else: Cuts["rll2"] = False

        if( METOverHTLep > max(5., (15.-2.*mll))):
            Cuts["MLLMETOverHTLep"] = True
        else: Cuts["MLLMETOverHTLep"] = False
    
        if( METOverHTLep > max(3., (15.-2.*(mt2-100.)))):
            Cuts["MT2METOverHTLep"] = True
        else: Cuts["MT2METOverHTLep"] = False

        if( mt_lep1 < 70. ):
            Cuts["mt70"] = True
        else: Cuts["mt70"] = False

        if( mll < 3. ):
            Cuts["Event_SRSF_iMLLa"] = True
        else: Cuts["Event_SRSF_iMLLa"] = False

        if( mll < 5. ):
            Cuts["Event_SRSF_iMLLb"] = True
        else: Cuts["Event_SRSF_iMLLb"] = False

        if( mll < 10. ):
            Cuts["Event_SRSF_iMLLc"] = True
        else: Cuts["Event_SRSF_iMLLc"] = False

        if( mll < 20. ):
            Cuts["Event_SRSF_iMLLd"] = True
        else: Cuts["Event_SRSF_iMLLd"] = False

        if( mll < 30. ):
            Cuts["Event_SRSF_iMLLe"] = True
        else: Cuts["Event_SRSF_iMLLe"] = False

        if( mll < 40. ):
            Cuts["Event_SRSF_iMLLf"] = True
        else: Cuts["Event_SRSF_iMLLf"] = False

        if( mll < 60. ):
            Cuts["Event_SRSF_iMLLg"] = True
        else: Cuts["Event_SRSF_iMLLg"] = False

        return Cuts


class truthcuts:
    def __init__(self, obs):

        self.obs = obs

    def getCuts(self):
        obs = self.obs
        EventNumber = obs.EventNumber
        Event_SRSF_iMLLa = obs.Event_SRSF_iMLLa
        Event_SRSF_iMLLb = obs.Event_SRSF_iMLLb
        Event_SRSF_iMLLc = obs.Event_SRSF_iMLLc
        Event_SRSF_iMLLd = obs.Event_SRSF_iMLLd
        Event_SRSF_iMLLe = obs.Event_SRSF_iMLLe
        Event_SRSF_iMLLf = obs.Event_SRSF_iMLLf
        Event_SRSF_iMLLg = obs.Event_SRSF_iMLLg
        DSID = obs.DSID



        #Make list of dictionaries of cuts
        #Dics = []
        #Make dictionary of cuts
        Cuts = {}
        
        if( Event_SRSF_iMLLa ):
            Cuts["Event_SRSF_iMLLa"] = True
        else: Cuts["Event_SRSF_iMLLa"] = False

        if( Event_SRSF_iMLLb ):
            Cuts["Event_SRSF_iMLLb"] = True
        else: Cuts["Event_SRSF_iMLLb"] = False

        if( Event_SRSF_iMLLc ):
            Cuts["Event_SRSF_iMLLc"] = True
        else: Cuts["Event_SRSF_iMLLc"] = False

        if( Event_SRSF_iMLLd ):
            Cuts["Event_SRSF_iMLLd"] = True
        else: Cuts["Event_SRSF_iMLLd"] = False

        if( Event_SRSF_iMLLe ):
            Cuts["Event_SRSF_iMLLe"] = True
        else: Cuts["Event_SRSF_iMLLe"] = False

        if( Event_SRSF_iMLLf ):
            Cuts["Event_SRSF_iMLLf"] = True
        else: Cuts["Event_SRSF_iMLLf"] = False

        if( Event_SRSF_iMLLg ):
            Cuts["Event_SRSF_iMLLg"] = True
        else: Cuts["Event_SRSF_iMLLg"] = False


        return Cuts
