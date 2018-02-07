import re, time, copy, math
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True)
 #------------------------------------------------------------------
class recoobservable:
    def __init__(self, event):

        self.varibales={}
        #trigger
        self.metTrig =                      event.trigMatch_metTrig
        #bjets
        self.nBJet20 =                      event.nBJet20_MV2c10_FixedCutBEff_85
        #MET variables
        self.met_Et =                       event.met_Et
        self.met_Phi =                      event.met_Phi
        #Jet variables
        self.nJet30 =                       event.nJet30
        self.jetEta =                       event.jetEta
        self.jetPhi =                       event.jetPhi
        self.jetPt =                        event.jetPt
        self.DPhiJ1Met =                    event.DPhiJ1Met
        self.minDPhiAllJetsMet =            event.minDPhiAllJetsMet
        #lepton varaibles
        self.nLep_signal =                  event.nLep_signal
        self.nLep_base =                    event.nLep_base
        self.lep1Flavor =                   event.lep1Flavor
        self.lep1Charge =                   event.lep1Charge
        self.lep1Author =                   event.lep1Author
        self.lep1Pt =                       event.lep1Pt
        self.lep1Eta =                      event.lep1Eta
        self.lep1Phi =                      event.lep1Phi
        self.lep1Signal =                   event.lep1Signal
        self.lep1TruthMatched =             event.lep1TruthMatched
        self.lep2Flavor =                   event.lep2Flavor
        self.lep2Charge =                   event.lep2Charge
        self.lep2Author =                   event.lep2Author
        self.lep2Pt =                       event.lep2Pt
        self.lep2Eta =                      event.lep2Eta
        self.lep2Phi =                      event.lep2Phi
        self.lep2Signal =                   event.lep2Signal
        self.lep2TruthMatched =             event.lep2TruthMatched
        self.lep3Flavor =                   event.lep3Flavor
        self.lep3Charge =                   event.lep3Charge
        self.lep3Author =                   event.lep3Author
        self.lep3Pt =                       event.lep3Pt
        self.lep3Eta =                      event.lep3Eta
        self.lep3Phi =                      event.lep3Phi
        self.lep3Signal =                   event.lep3Signal
        self.lep3TruthMatched =             event.lep3TruthMatched
        #dilepton variables
        self.mll =                          event.mll
        self.MTauTau =                      event.MTauTau
        self.Rll =                          event.Rll
        self.mt2leplsp_100 =                event.mt2leplsp_100
        self.METOverHTLep =                 event.METOverHTLep
        self.mt_lep1 =                      event.mt_lep1
        #Event Weights
        self.pileupWeight =                 event.pileupWeight
        self.leptonWeight =                 event.leptonWeight
        self.eventWeight =                  event.eventWeight
        self.genWeight =                    event.genWeight
        self.bTagWeight =                   event.bTagWeight
        self.jvtWeight =                    event.jvtWeight
        #Event variables
        self.xsec =                         event.xsec
        self.FS =                           event.FS
        self.DatasetNumber =                event.DatasetNumber
        self.EventNumber =                  event.EventNumber


    def getWeight(self):
        pileupWeight = self.pileupWeight
        leptonWeight = self.leptonWeight
        eventWeight = self.eventWeight
        genWeight = self.genWeight
        bTagWeight = self.bTagWeight
        jvtWeight = self.jvtWeight
        #return pileupWeight*leptonWeight*eventWeight*genWeight*bTagWeight*jvtWeight
        return pileupWeight*leptonWeight*eventWeight*bTagWeight*jvtWeight

    def isOSSF(self):
        flag = False
        #if( self.nLep_base != 2 or self.nLep_signal != 2 ):
        #    return flag
        if( self.lep1TruthMatched == False or (self.lep1Flavor == 1 and self.lep1Author == 16) or self.lep2TruthMatched == False or (self.lep2Flavor == 1 and self.lep2Author == 16) ):
            return flag
        if( self.lep1Charge*self.lep2Charge == -1 and self.lep1Flavor == self.lep2Flavor ):
            flag = True
        return flag

class truthobservable:
    def __init__(self, event):

        self.varibales={}
        self.eventWeight = event.eventWeight
        self.EventNumber = event.Event
        self.Event_SRSF_iMLLa = event.Event_SRSF_iMLLa
        self.Event_SRSF_iMLLb = event.Event_SRSF_iMLLb
        self.Event_SRSF_iMLLc = event.Event_SRSF_iMLLc
        self.Event_SRSF_iMLLd = event.Event_SRSF_iMLLd
        self.Event_SRSF_iMLLe = event.Event_SRSF_iMLLe
        self.Event_SRSF_iMLLf = event.Event_SRSF_iMLLf
        self.Event_SRSF_iMLLg = event.Event_SRSF_iMLLg
        self.DSID = event.DSID
        #Add more here




        
