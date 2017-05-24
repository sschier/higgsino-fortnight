import re, time, copy, math, array
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True)
 #------------------------------------------------------------------
class observable:
    def __init__(self, event, isdata):

        self.varibales={}
        self.met = event.met/1000.
        self.mt = event.mt/1000.
        self.met_phi = event.met_phi
        self.HLT_e5 = event.HLT_e5_lhvloose
        self.HLT_e10 = event.HLT_e10_lhvloose_L1EM7
        self.HLT_e15 = event.HLT_e15_lhvloose_L1EM13VH
        self.HLT_e20 = event.HLT_e20_lhvloose
        self.n_baseel = event.n_baseel
        self.baseel_idTight = event.baseel_idTight
        self.baseel_isoTight = event.baseel_isoTight
        self.baseel_d0sig = event.baseel_d0sig
        self.baseel_z0sinTheta = event.baseel_z0sinTheta
        self.baseel_pt = event.baseel_pt 
        self.baseel_eta = event.baseel_eta 
        self.baseel_phi = event.baseel_phi
        if isdata == '':
            self.xs_weight = event.xs_weight
            self.mc_event_weight = event.mc_event_weight
            self.pileup_weight = event.pileup_weight


    def getMET(self):
        met = self.met
        return met

    #def getMT(self, lep1Vec):
    #    mt = self.mt
    #    return mt
    def getMT(self, lep1Vec):
        met = self.met
        #mt = event.mt/1000.
        #if( self.getDphiL1MET(lep1Vec.Phi()) > -99. ):
        mt = TMath.Sqrt(2*lep1Vec.Pt()*met*(1-TMath.Cos(self.getDphiL1MET(lep1Vec.Phi()))))
        return mt

    def getDphiL1MET(self, l1phi):
        dphi_l1met = -99.
        met_phi = self.met_phi
        if l1phi:
            dphi_l1met = TVector2.Phi_mpi_pi(l1phi - met_phi)
        return dphi_l1met


    def getTriggers(self):
        HLT_e5 = self.HLT_e5
        HLT_e10 = self.HLT_e10
        HLT_e15 = self.HLT_e15
        HLT_e20 = self.HLT_e20
        return HLT_e5, HLT_e10, HLT_e15, HLT_e20

    def getNBaseel(self):
        n_baseel = self.n_baseel
        return n_baseel

    def getIDelectronVec(self):
        IDelectronList = []
        IDelectronVec = ROOT.TVector3() 
        for x in xrange(self.n_baseel):
            if( self.baseel_idTight[x] == 1 and self.baseel_isoTight[x] == 1 and abs(self.baseel_d0sig[x]) < 5. and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
               IDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
               #print "ID GOOD!"
               #print IDelectronVec.Pt(), IDelectronVec.Eta(), IDelectronVec.Phi()
               IDelectronList.append(IDelectronVec)
        #print "ID BAD!"
        #print IDelectronVec.Pt(), IDelectronVec.Eta(), IDelectronVec.Phi()
        return IDelectronVec

    def getAntiIDelectronVec(self):
        AIDelectronList = []
        AIDelectronVec = ROOT.TVector3()
        for x in xrange(self.getNBaseel()):
            if( self.baseel_idTight[x] == 0 or self.baseel_isoTight[x] == 0 or abs(self.baseel_d0sig[x]) >= 5. or abs(self.baseel_z0sinTheta[x]) >= 0.5 ):
                AIDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                #print "ANTI-ID GOOD!"
                #print AIDelectronVec.Pt(), AIDelectronVec.Eta(), AIDelectronVec.Phi()
                AIDelectronList.append(AIDelectronVec)
        #print "ANTI-ID BAD!"
        #print AIDelectronVec.Pt(), AIDelectronVec.Eta(), AIDelectronVec.Phi()
        print AIDelectronList
        return AIDelectronVec


    def getWeights(self):
        xs_weight = self.xs_weight
        mc_event_weight = self.mc_event_weight
        pileup_weight = self.pileup_weight
        return xs_weight, mc_event_weight, pileup_weight






        
