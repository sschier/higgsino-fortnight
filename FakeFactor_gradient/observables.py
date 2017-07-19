import re, time, copy, math
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True)
 #------------------------------------------------------------------
class observable:
    def __init__(self, event, isdata):

        self.varibales={}
        self.met = event.met/1000.
        #self.mt = event.mt/1000.
        self.met_phi = event.met_phi
        self.HLT_e5 = event.HLT_e5_lhvloose
        self.HLT_e10 = event.HLT_e10_lhvloose_L1EM7
        self.HLT_e15 = event.HLT_e15_lhvloose_L1EM13VH
        self.HLT_e20 = event.HLT_e20_lhvloose
        self.n_baseel = event.n_baseel
        self.baseel_idTight = event.baseel_idTight
        self.baseel_isoTight = event.baseel_isoTight
        self.baseel_isoGradientLoose = event.baseel_isoGradientLoose
        self.baseel_d0sig = event.baseel_d0sig
        self.baseel_z0sinTheta = event.baseel_z0sinTheta
        self.baseel_pt = event.baseel_pt 
        self.baseel_eta = event.baseel_eta 
        self.baseel_phi = event.baseel_phi
        #self.lep_truthMatched = event.lep_truthMatched
        #self.lep_pt = event.lep_pt
        #self.lep_phi = event.lep_phi
        #self.lep_eta = event.lep_eta
        #self.n_lep = event.n_lep
        if isdata == '':
            self.xs_weight = event.xs_weight
            self.mc_event_weight = event.mc_event_weight
            self.pileup_weight = event.pileup_weight
            self.sf_total = event.sf_total
            self.sf_el = event.sf_el
            self.sf_jvt = event.sf_jvt
            self.sf_btag = event.sf_btag


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

    def getLeptonVectors(self):
        lepVectors = []
        for x in xrange(self.n_lep):
            lepVec = ROOT.TVector3()
            lepVec.SetPtEtaPhi(self.lep_pt[x]/1000., self.lep_eta[x], self.lep_phi[x])
            lepVectors.append(lepVec)
        return lepVectors

    def getIDelectrons(self):
        IDelectronVectors = []
        IDelectronZ0sinT = []
        IDelectronD0sig = []
        for x in xrange(self.n_baseel):
            IDelectronVec = ROOT.TVector3() 
            if( self.baseel_idTight[x] == 1 and self.baseel_isoGradientLoose[x] == 1 and abs(self.baseel_d0sig[x]) < 5. and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                IDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                IDelectronVectors.append(IDelectronVec)
                IDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                IDelectronD0sig.append(self.baseel_d0sig[x])
                #print "ID Z0:"
                #print IDelectronZ0sinT
                #print "ID pt:"
                #for vec in IDelectronVectors:
                #    print vec.Pt()
        return IDelectronVectors, IDelectronZ0sinT, IDelectronD0sig

    def getAntiIDelectrons(self):
        AIDelectronVectors = []
        AIDelectronZ0sinT = []
        AIDelectronD0sig = []
        for x in xrange(self.getNBaseel()):
            AIDelectronVec = ROOT.TVector3()
            if( (self.baseel_idTight[x] == 0 or self.baseel_isoGradientLoose[x] == 0 or abs(self.baseel_d0sig[x]) >= 5.) and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                AIDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                AIDelectronVectors.append(AIDelectronVec)
                AIDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                AIDelectronD0sig.append(self.baseel_d0sig[x])
        return AIDelectronVectors, AIDelectronZ0sinT, AIDelectronD0sig

    def getAntiIDelectrons1(self):
        AIDelectronVectors = []
        AIDelectronZ0sinT = []
        AIDelectronD0sig = []
        for x in xrange(self.getNBaseel()):
            AIDelectronVec = ROOT.TVector3()
            if( (self.baseel_idTight[x] == 0 and self.baseel_isoGradientLoose[x] == 1 and abs(self.baseel_d0sig[x]) < 5.) and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                AIDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                AIDelectronVectors.append(AIDelectronVec)
                AIDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                AIDelectronD0sig.append(self.baseel_d0sig[x])
        return AIDelectronVectors, AIDelectronZ0sinT, AIDelectronD0sig
    def getAntiIDelectrons2(self):
        AIDelectronVectors = []
        AIDelectronZ0sinT = []
        AIDelectronD0sig = []
        for x in xrange(self.getNBaseel()):
            AIDelectronVec = ROOT.TVector3()
            if( (self.baseel_idTight[x] == 1 and self.baseel_isoGradientLoose[x] == 0 and abs(self.baseel_d0sig[x]) < 5.) and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                AIDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                AIDelectronVectors.append(AIDelectronVec)
                AIDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                AIDelectronD0sig.append(self.baseel_d0sig[x])
        return AIDelectronVectors, AIDelectronZ0sinT, AIDelectronD0sig
    def getAntiIDelectrons3(self):
        AIDelectronVectors = []
        AIDelectronZ0sinT = []
        AIDelectronD0sig = []
        for x in xrange(self.getNBaseel()):
            AIDelectronVec = ROOT.TVector3()
            if( (self.baseel_idTight[x] == 1 and self.baseel_isoGradientLoose[x] == 1 and abs(self.baseel_d0sig[x]) >= 5.) and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                AIDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                AIDelectronVectors.append(AIDelectronVec)
                AIDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                AIDelectronD0sig.append(self.baseel_d0sig[x])
        return AIDelectronVectors, AIDelectronZ0sinT, AIDelectronD0sig

    def getAntiIDelectrons12(self):
        AIDelectronVectors = []
        AIDelectronZ0sinT = []
        AIDelectronD0sig = []
        for x in xrange(self.getNBaseel()):
            AIDelectronVec = ROOT.TVector3()
            if( (self.baseel_idTight[x] == 0 and self.baseel_isoGradientLoose[x] == 0 and abs(self.baseel_d0sig[x]) < 5.) and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                AIDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                AIDelectronVectors.append(AIDelectronVec)
                AIDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                AIDelectronD0sig.append(self.baseel_d0sig[x])
        return AIDelectronVectors, AIDelectronZ0sinT, AIDelectronD0sig

    def getAntiIDelectrons13(self):
        AIDelectronVectors = []
        AIDelectronZ0sinT = []
        AIDelectronD0sig = []
        for x in xrange(self.getNBaseel()):
            AIDelectronVec = ROOT.TVector3()
            if( (self.baseel_idTight[x] == 0 and self.baseel_isoGradientLoose[x] == 1 and abs(self.baseel_d0sig[x]) >= 5.) and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                AIDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                AIDelectronVectors.append(AIDelectronVec)
                AIDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                AIDelectronD0sig.append(self.baseel_d0sig[x])
        return AIDelectronVectors, AIDelectronZ0sinT, AIDelectronD0sig

    def getAntiIDelectrons23(self):
        AIDelectronVectors = []
        AIDelectronZ0sinT = []
        AIDelectronD0sig = []
        for x in xrange(self.getNBaseel()):
            AIDelectronVec = ROOT.TVector3()
            if( (self.baseel_idTight[x] == 1 and self.baseel_isoGradientLoose[x] == 0 and abs(self.baseel_d0sig[x]) >= 5.) and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                AIDelectronVec.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
                AIDelectronVectors.append(AIDelectronVec)
                AIDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                AIDelectronD0sig.append(self.baseel_d0sig[x])
        return AIDelectronVectors, AIDelectronZ0sinT, AIDelectronD0sig

    def getWeights(self):
        xs_weight = self.xs_weight
        mc_event_weight = self.mc_event_weight
        sf_el = self.sf_el
        sf_jvt = self.sf_jvt
        sf_btag = self.sf_btag
        pileup_weight = self.pileup_weight
        sf_total = self.sf_total
        return xs_weight, mc_event_weight, sf_el, sf_jvt, sf_btag, pileup_weight






        
