import re, time, copy, math
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True)
 #------------------------------------------------------------------
class observable:
    def __init__(self, event, isdata):

        self.varibales={}
        #pileup
        self.num_pv =                           event.num_pv
        self.mu =                               event.av_int_per_xing
        #MET variables
        self.met =                              event.met/1000.
        self.met_phi =                          event.met_phi
        #Trigger variables
        self.HLT_mu4 =                          event.HLT_mu4
        self.HLT_mu10 =                         event.HLT_mu10
        self.HLT_mu14 =                         event.HLT_mu14
        self.HLT_mu18 =                         event.HLT_mu18
        #Jet variables
        self.n_jet =                            event.n_jet
        self.n_bjet =                           event.n_bjet
        self.jet_eta =                          event.jet_eta
        self.jet_phi =                          event.jet_phi
        self.jet_pt =                           event.jet_pt
        #Muon variables
        self.n_basemu =                         event.n_basemu
        self.basemu_idMedium =                  event.basemu_idMedium
        self.basemu_isoFixedCutTightTrackOnly = event.basemu_isoFixedCutTightTrackOnly
        self.basemu_d0sig =                     event.basemu_d0sig
        self.basemu_z0sinTheta =                event.basemu_z0sinTheta
        self.basemu_pt =                        event.basemu_pt 
        self.basemu_eta =                       event.basemu_eta 
        self.basemu_phi =                       event.basemu_phi
        self.n_mu =                             event.n_mu
        self.mu_pt =                            event.mu_pt
        self.mu_phi =                           event.mu_phi
        self.mu_eta =                           event.mu_eta
        self.mu_z0sinTheta =                    event.mu_z0sinTheta
        self.mu_d0sig =                         event.mu_d0sig
        self.mu_idMedium =                      event.mu_idMedium
        self.mu_isoFixedCutTightTrackOnly =     event.mu_isoFixedCutTightTrackOnly
        if isdata == '':
            self.xs_weight =                    event.xs_weight
            self.mc_event_weight =              event.mc_event_weight
            self.pileup_weight =                event.pileup_weight
            self.sf_total =                     event.sf_total
            self.sf_mu =                        event.sf_mu
            self.sf_jvt =                       event.sf_jvt
            self.sf_btag =                      event.sf_btag


    def getHT(self):
        ht =0.0 
        for x in xrange(self.n_jet):
            ht += self.jet_pt[x]/1000.
        return ht

    def getMET(self):
        met = self.met
        return met

    def getMT(self, lep1Vec):
        met = self.met
        mt = TMath.Sqrt(2*lep1Vec.Pt()*met*(1-TMath.Cos(self.getDphiL1MET(lep1Vec.Phi()))))
        return mt

    def getDphiJ1MET(self):
        dphi_j1met = -99.
        met_phi = self.met_phi
        if self.n_jet > 0:
            j1phi = self.jet_phi[0]
            dphi_j1met = TVector2.Phi_mpi_pi(j1phi - met_phi)
        return dphi_j1met

    def getDphiL1MET(self, l1phi):
        dphi_l1met = -99.
        met_phi = self.met_phi
        if l1phi:
            dphi_l1met = TVector2.Phi_mpi_pi(l1phi - met_phi)
        return dphi_l1met


    def getTriggers(self):
        HLT_mu4 = self.HLT_mu4
        HLT_mu10 = self.HLT_mu10
        HLT_mu14 = self.HLT_mu14
        HLT_mu18 = self.HLT_mu18
        return HLT_mu4, HLT_mu10, HLT_mu14, HLT_mu18

    def getNBasemu(self):
        n_basemu = self.n_basemu
        return n_basemu

    def getSigMuons(self):
        muVectors = []
        muZ0sinT = []
        muD0sig = []
        for x in xrange(self.n_mu):
            muVec = ROOT.TVector3()
            muVec.SetPtEtaPhi(self.mu_pt[x]/1000., self.mu_eta[x], self.mu_phi[x])
            muVectors.append(muVec)
            muZ0sinT.append(self.mu_z0sinTheta[x])
            muD0sig.append(self.mu_d0sig[x])
            #print 'all sig mu'
            #print 'lepton %i' % x
            #print self.mu_eta[x]
            #print abs(self.mu_z0sinTheta[x]) < 0.5
            #print self.mu_idMedium[x]
            #print self.mu_isoFixedCutTightTrackOnly[x]
            #print abs(self.mu_d0sig[x]) >= 3.
        return muVectors, muZ0sinT, muD0sig

    def getMuVectors(self):
        muVectors = []
        for x in xrange(self.n_mu):
            muVec = ROOT.TVector3()
            muVec.SetPtEtaPhi(self.mu_pt[x]/1000., self.mu_eta[x], self.mu_phi[x])
            muVectors.append(muVec)
        return muVectors

    def getIDmuons(self, sigMuList, debug):
        IDmuonVectors = []
        IDmuonZ0sinT = []
        IDmuonD0sig = []
        for x in xrange(self.n_basemu):
            condition = False
            IDmuonVec = ROOT.TVector3() 
            if( self.basemu_isoFixedCutTightTrackOnly[x] == 1 and abs(self.basemu_d0sig[x]) < 3. and abs(self.basemu_z0sinTheta[x]) < 0.5 and abs(self.basemu_eta[x]) < 2.5 ):
                condition = True
                IDmuonVec.SetPtEtaPhi(self.basemu_pt[x]/1000., self.basemu_eta[x], self.basemu_phi[x])
                IDmuonVectors.append(IDmuonVec)
                IDmuonZ0sinT.append(self.basemu_z0sinTheta[x])
                IDmuonD0sig.append(self.basemu_d0sig[x])
        return IDmuonVectors, IDmuonZ0sinT, IDmuonD0sig

    #def getAntiIDmuons(self, sigMuList, variation, debug):
    #    AIDmuonVectors = []
    #    AIDmuonZ0sinT = []
    #    AIDmuonD0sig = []
    #    print 'getting AID muons'
    #    for x in xrange(self.n_basemu):
    #        condition = False
    #        #print 'all base mu'
    #        #print 'lepton %i' % x
    #        #print self.basemu_eta[x]
    #        #print abs(self.basemu_z0sinTheta[x]) < 0.5
    #        #print self.basemu_idMedium[x]
    #        #print self.basemu_isoFixedCutTightTrackOnly[x]
    #        #print abs(self.basemu_d0sig[x]) >= 3.
    #        isID = False
    #        AIDmuonVec = ROOT.TVector3()
    #        AIDmuonVecTemp = ROOT.TVector3()
    #        AIDmuonVecTemp.SetPtEtaPhi(self.basemu_pt[x]/1000., self.basemu_eta[x], self.basemu_phi[x])
    #        if( len(sigMuList) == 0 ):
    #            isID = False
    #        elif( len(sigMuList) == self.n_basemu ):
    #            isID = True
    #        else:
    #            for mu in sigMuList:
    #                if( AIDmuonVecTemp.DeltaR(mu) < 0.00001 ):
    #                    isID = True
    #                    break
    #        if( variation == 'z0' or variation == 'Z0' ):
    #            if debug: print "Z0 cut not applied"
    #            if( isID == False ): condition = True
    #        else: #else nominal Anti-ID definition
    #            if( isID == False and abs(self.basemu_z0sinTheta[x]) < 0.5 and abs(self.basemu_eta[x]) < 2.5): 
    #                condition = True
    #                print 'all aid mu'
    #                print 'lepton %i' % x
    #                print self.basemu_eta[x]
    #                print abs(self.basemu_z0sinTheta[x]) < 0.5
    #                print self.basemu_idMedium[x]
    #                print self.basemu_isoFixedCutTightTrackOnly[x]
    #                print abs(self.basemu_d0sig[x]) >= 3.
    #        if( condition ):
    #            AIDmuonVec = AIDmuonVecTemp
    #            AIDmuonVectors.append(AIDmuonVec)
    #            AIDmuonZ0sinT.append(self.basemu_z0sinTheta[x])
    #            AIDmuonD0sig.append(self.basemu_d0sig[x])
    #    return AIDmuonVectors, AIDmuonZ0sinT, AIDmuonD0sig


    def getAntiIDmuons(self, variation, debug):
        AIDmuonVectors = []
        AIDmuonZ0sinT = []
        AIDmuonD0sig = []
        for x in xrange(self.n_basemu):
            condition = False
            AIDmuonVec = ROOT.TVector3()
            if( abs(self.basemu_z0sinTheta[x]) < 0.5 and abs(self.basemu_eta[x]) < 2.5 and (self.basemu_isoFixedCutTightTrackOnly[x] == 0 or abs(self.basemu_d0sig[x]) >= 3.) ):
                condition = True
            if condition == True:
                AIDmuonVec.SetPtEtaPhi(self.basemu_pt[x]/1000., self.basemu_eta[x], self.basemu_phi[x])  
                AIDmuonVectors.append(AIDmuonVec)
                AIDmuonZ0sinT.append(self.basemu_z0sinTheta[x])
                AIDmuonD0sig.append(self.basemu_d0sig[x])
        return AIDmuonVectors, AIDmuonZ0sinT, AIDmuonD0sig


        #fail isolation only
    def getAntiIDMuons1(self, variation, debug):
        AIDmuonVectors = []
        AIDmuonZ0sinT = []
        AIDmuonD0sig = []
        for x in xrange(self.n_basemu):
            condition = False
            AIDmuonVec = ROOT.TVector3()
            if( abs(self.basemu_z0sinTheta[x]) < 0.5 and self.basemu_isoFixedCutTightTrackOnly[x] == 0 and abs(self.basemu_d0sig[x]) < 3. and abs(self.basemu_eta[x]) < 2.5):
                condition = True
                if debug:
                    print 'all aid1'
                    print 'lepton %i' % x
                    print self.basemu_eta[x]
                    print abs(self.basemu_z0sinTheta[x]) < 0.5
                    print self.basemu_idMedium[x]
                    print self.basemu_isoFixedCutTightTrackOnly[x]
                    print abs(self.basemu_d0sig[x]) >= 3.
            if condition == True:
                AIDmuonVec.SetPtEtaPhi(self.basemu_pt[x]/1000., self.basemu_eta[x], self.basemu_phi[x])  
                AIDmuonVectors.append(AIDmuonVec)
                AIDmuonZ0sinT.append(self.basemu_z0sinTheta[x])
                AIDmuonD0sig.append(self.basemu_d0sig[x])
        return AIDmuonVectors, AIDmuonZ0sinT, AIDmuonD0sig

        #fail d0 only
    def getAntiIDMuons2(self, variation, debug):
        AIDmuonVectors = []
        AIDmuonZ0sinT = []
        AIDmuonD0sig = []
        for x in xrange(self.n_basemu):
            condition = False
            AIDmuonVec = ROOT.TVector3()
            if( abs(self.basemu_z0sinTheta[x]) < 0.5 and self.basemu_isoFixedCutTightTrackOnly[x] == 1 and abs(self.basemu_d0sig[x]) >= 3. and abs(self.basemu_eta[x]) < 2.5):
                condition = True
                if debug:
                    print 'all aid2'
                    print 'lepton %i' % x
                    print self.basemu_eta[x]
                    print abs(self.basemu_z0sinTheta[x]) < 0.5
                    print self.basemu_idMedium[x]
                    print self.basemu_isoFixedCutTightTrackOnly[x]
                    print abs(self.basemu_d0sig[x]) >= 3.
            if condition == True:
                AIDmuonVec.SetPtEtaPhi(self.basemu_pt[x]/1000., self.basemu_eta[x], self.basemu_phi[x])  
                AIDmuonVectors.append(AIDmuonVec)
                AIDmuonZ0sinT.append(self.basemu_z0sinTheta[x])
                AIDmuonD0sig.append(self.basemu_d0sig[x])
        return AIDmuonVectors, AIDmuonZ0sinT, AIDmuonD0sig


        #fail all
    def getAntiIDMuons12(self, variation, debug):
        AIDmuonVectors = []
        AIDmuonZ0sinT = []
        AIDmuonD0sig = []
        for x in xrange(self.n_basemu):
            condition = False
            AIDmuonVec = ROOT.TVector3()
            if( abs(self.basemu_z0sinTheta[x]) < 0.5 and self.basemu_isoFixedCutTightTrackOnly[x] == 0 and abs(self.basemu_d0sig[x]) >= 3. and abs(self.basemu_eta[x]) < 2.5):
                condition = True
                if debug:
                    print 'all aid12'
                    print 'lepton %i' % x
                    print self.basemu_eta[x]
                    print abs(self.basemu_z0sinTheta[x]) < 0.5
                    print self.basemu_idMedium[x]
                    print self.basemu_isoFixedCutTightTrackOnly[x]
                    print abs(self.basemu_d0sig[x]) >= 3.
            if condition == True:
                AIDmuonVec.SetPtEtaPhi(self.basemu_pt[x]/1000., self.basemu_eta[x], self.basemu_phi[x])  
                AIDmuonVectors.append(AIDmuonVec)
                AIDmuonZ0sinT.append(self.basemu_z0sinTheta[x])
                AIDmuonD0sig.append(self.basemu_d0sig[x])
        return AIDmuonVectors, AIDmuonZ0sinT, AIDmuonD0sig




    def getWeights(self):
        xs_weight = self.xs_weight
        mc_event_weight = self.mc_event_weight
        pileup_weight = self.pileup_weight
        sf_total = self.sf_total
        sf_mu = self.sf_mu
        sf_jvt = self.sf_jvt
        sf_btag = self.sf_btag
        return xs_weight, mc_event_weight, sf_mu, sf_jvt, sf_btag, pileup_weight






        
