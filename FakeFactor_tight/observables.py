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
        self.n_el = event.n_el
        self.baseel_idTight = event.baseel_idTight
        self.baseel_isoTight = event.baseel_isoTight
        self.baseel_isoGradientLoose = event.baseel_isoGradientLoose
        self.baseel_d0sig = event.baseel_d0sig
        self.baseel_z0sinTheta = event.baseel_z0sinTheta
        self.baseel_pt = event.baseel_pt 
        self.baseel_eta = event.baseel_eta 
        self.baseel_phi = event.baseel_phi
        self.el_pt  = event.el_pt
        self.el_phi = event.el_phi
        self.el_eta = event.el_eta
        self.el_z0sinTheta = event.el_z0sinTheta
        self.el_d0sig = event.el_d0sig
        if isdata == '':
            self.xs_weight = event.xs_weight
            self.mc_event_weight = event.mc_event_weight
            self.pileup_weight = event.pileup_weight
            self.sf_total = event.sf_total


    def getMET(self):
        met = self.met
        return met

    #def getMT(self, lep1Vec):
    #    mt = self.mt
    #    return mt
    def getMT(self, lep1Vec):
        met = self.met
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

    def getSigElectrons(self):
        elVectors = []
        elZ0sinT = []
        elD0sig = []
        for x in xrange(self.n_el):
            elVec = ROOT.TVector3()
            elVec.SetPtEtaPhi(self.el_pt[x]/1000., self.el_eta[x], self.el_phi[x])
            elVectors.append(elVec)
            elZ0sinT.append(self.el_z0sinTheta[x])
            elD0sig.append(self.el_d0sig[x])
        return elVectors, elZ0sinT, elD0sig


    def getElVectors(self):
        elVectors = []
        for x in xrange(self.n_el):
            elVec = ROOT.TVector3()
            elVec.SetPtEtaPhi(self.el_pt[x]/1000., self.el_eta[x], self.el_phi[x])
            elVectors.append(elVec)
        return elVectors

    def getIDelectrons(self, sigElList, debug):
        if debug: print "####################################"
        if debug: print "**Getting ID electrons"
        IDelectronVectors = []
        IDelectronZ0sinT = []
        IDelectronD0sig = []
        for x in xrange(self.n_baseel):
            if debug: print "base electron %i" % x
            isID = False
            IDelectronVec = ROOT.TVector3() 
            IDelectronTemp = ROOT.TVector3() 
            IDelectronTemp.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
            for el in sigElList:
                if debug:
                    print self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x]
                    print el.Pt(), el.Eta(), el.Phi()
                    print "delta R %f" % IDelectronTemp.DeltaR(el)
                    print "before %s" % isID
                if( IDelectronTemp.DeltaR(el) < 0.00001 ):
                    isID = True
                    break
                if debug: print "after %s" % isID
            if isID:
                IDelectronVec = IDelectronTemp
                IDelectronVectors.append(IDelectronVec)
                IDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                IDelectronD0sig.append(self.baseel_d0sig[x])
                #print "ID Z0:"
                #print IDelectronZ0sinT
                #print "ID pt:"
                #for vec in IDelectronVectors:
                #    print vec.Pt()
        if debug: print "Done getting ID electrons"
        return IDelectronVectors, IDelectronZ0sinT, IDelectronD0sig

    def getAntiIDelectrons(self, sigElList, debug):
        AIDelectronVectors = []
        AIDelectronZ0sinT = []
        AIDelectronD0sig = []
        for x in xrange(self.n_baseel):
            isID = False
            AIDelectronVec = ROOT.TVector3()
            AIDelectronTemp = ROOT.TVector3() 
            AIDelectronTemp.SetPtEtaPhi(self.baseel_pt[x]/1000., self.baseel_eta[x], self.baseel_phi[x])
            if (len(sigElList) == 0 ):
                isID = False
                #if( abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                #    isAID = True
            elif( len(sigElList) == self.n_baseel):
                isID = True
            else:
                if debug: print "LOOK HERE"
                for el in sigElList:
                    if( AIDelectronTemp.DeltaR(el) < 0.00001 ): # and abs(self.baseel_z0sinTheta[x]) < 0.5 ):
                        isID = True
                        break
            if( isID == False ):
                AIDelectronVec = AIDelectronTemp
                AIDelectronVectors.append(AIDelectronVec)
                AIDelectronZ0sinT.append(self.baseel_z0sinTheta[x])
                AIDelectronD0sig.append(self.baseel_d0sig[x])
                #print "Anti ID Z0:"
                #print AIDelectronZ0sinT
                #print "Anti ID pt:"
                #for vec in AIDelectronVectors:
                #    print vec.Pt()
        return AIDelectronVectors, AIDelectronZ0sinT, AIDelectronD0sig


    def getWeights(self):
        xs_weight = self.xs_weight
        mc_event_weight = self.mc_event_weight
        pileup_weight = self.pileup_weight
        sf_total = self.sf_total
        return xs_weight, mc_event_weight, pileup_weight, sf_total






        
