#Author:Sheena C Schier
#Created 10May17 for calculating electron scale factors
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?
from array import array
from observables import *
from renormalize import *
from cuts import *


#------------------------------------------------------------------
class antiidhists:
    def __init__(self, tag, topdir, isdata, treetype, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.hists={}
        self.detaillevel=detaillevel
        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        xbins = [0., 10., 20., 30., 40., 50., 60., 70., 80., 90., 100., 150., 200., 300., 400., 600.]
        etabins = [0., 0.7, 1.37, 1.52, 2.01, 2.47]

        self.hists['AntiIDelPt']= ROOT.TH1F("h_"+tag+"_AntiIDelPt",tag+"_AntiIDelPt; AntiID electron p_{T} [GeV]; Events",100, 0, 100)
        self.hists["Met"]=        ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(10 GeV)", 15, array('d',xbins))
        self.hists['Mt']=         ROOT.TH1F("h_"+tag+"_Mt",tag+"_Mt; m_{T} [GeV]; Events/(10 GeV) ",20, 0, 200)
        self.hists['Z0SinTheta']= ROOT.TH1F("h_"+tag+"_Z0sinT",tag+"_Z0sinT; Z_{0}sin(#theta) [mm]; Events/(0.25mm) ",20, 0, 5)
        self.hists['D0Sig']=      ROOT.TH1F("h_"+tag+"_D0sig",tag+"_D0sig; D_{0}sig; Events/(0.2) ",50, 0, 10)
        self.hists['AntiIDelEta']=ROOT.TH1F("h_"+tag+"_AntiIDelEta", tag+"_AntiIDelEta; AntiID electron #eta; Events/0.1",5, array('d', etabins))
        self.hists['NJet']=       ROOT.TH1F("h_"+tag+"_Njet", tag+"_Njet; jet count; Events",8, 0, 8)
        self.hists['Jet1Pt']=     ROOT.TH1F("h_"+tag+"_J1pt", tag+"_J1pt; jet_{1} P_{T} [GeV]; Events/(25 GeV)",35, 25, 900)
        self.hists['JetHt']=      ROOT.TH1F("h_"+tag+"_HT", tag+"_HT; jet H_{T} [GeV]; Events/(50 GeV)",17, 50, 900)
        self.hists['NBJet']=      ROOT.TH1F("h_"+tag+"_Nbjet", tag+"_Nbjet; b-jet count; Events", 8, 0, 8)
        self.hists['AvMu']=       ROOT.TH1F("h_"+tag+"_Mu", tag+"_Mu; av int per crossing; Events/5",7, 5, 40.)
        self.hists['NPV']=        ROOT.TH1F("h_"+tag+"_Npv", tag+"_Npv; primary vertices; Events",29, 1, 30)
        self.hists['dphiJ1met']=  ROOT.TH1F("h_"+tag+"_dphi_j1met",tag+"_dphi_j1met; #Delta#phi_{jet_{1}-met} [rad];Events/(0.5 rad)",7, 0., 3.5 )
        self.hists['dphiL1met']=  ROOT.TH1F("h_"+tag+"_dphi_l1met",tag+"_dphi_l1met;#Delta#phi_{lep_{1}-met} [rad];Events/(0.5 rad)",7, 0., 3.5)

        topdir.cd()
        self.collections={}

    def write(self):
        self.newdir.cd()
        for i,k in self.hists.iteritems():
            k.SetOption("HIST")
            k.Write()
        for i,k in self.collections.iteritems():
            k.write()
        self.topdir.cd()

    def add(self, coll):
        for i,k in self.hists.iteritems():
            if i in coll.hists: k.Add(coll.hists[i])
        for i,k in self.collections.iteritems():
            if i in coll.collections: k.add(coll.collections[i])

    def fill(self, obs, elVec, elZ0, elD0, variation):
        intLumi = 1.0
        met = obs.met
        mt =  obs.getMT(elVec)

        #trigger variables
        triggers = {}
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20

        #electron variables
        AntiIDpt = elVec.Pt()
        AntiIDeta = abs(elVec.Eta())
        AntiIDphi = elVec.Phi()
        n_baseel = obs.n_baseel

        #dphi_variables
        dphiL1met = obs.getDphiL1MET(AntiIDphi)
        dphiJ1met = obs.getDphiJ1MET()

        #jet variables
        n_jet = obs.n_jet
        n_bjet = obs.n_bjet
        j1_pt = obs.jet_pt[0]/1000.
        ht = obs.getHT()

        #pileup variables
        npv = obs.num_pv
        mu =  obs.mu

        #######################################################
        #Create trigger weights instance
        #######################################################
        norm = renorm(obs)

        #######################################################
        #Calculate weights 
        #######################################################
        if self.isdata:
            totalWeight = norm.getTriggerWeights(self.isdata, AntiIDpt, triggers)
        else:
            xs_weight, mc_event_weight, sf_el, sf_jvt, sf_btag, pileup_weight = obs.getWeights()
            if( variation == 'pileup' ):
                totalWeight = float(xs_weight*mc_event_weight*sf_el*sf_jvt*sf_btag*pileup_weight) #for pileup systematic
            else:
                totalWeight = float(xs_weight*mc_event_weight*sf_el*sf_jvt*sf_btag)

        self.hists["AntiIDelPt"].Fill(float(AntiIDpt), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["Met"].Fill(float(met), totalWeight)
        self.hists["Z0SinTheta"].Fill(float(abs(elZ0)), totalWeight)
        self.hists["D0Sig"].Fill(float(abs(elD0)), totalWeight)
        self.hists['AntiIDelEta'].Fill(float(AntiIDeta), totalWeight)
        self.hists["dphiJ1met"].Fill(float(math.fabs(dphiJ1met)), totalWeight)
        self.hists["dphiL1met"].Fill(float(math.fabs(dphiL1met)), totalWeight)
        self.hists["NJet"].Fill(float(n_jet), totalWeight)
        self.hists["NBJet"].Fill(float(n_bjet), totalWeight)
        self.hists["Jet1Pt"].Fill(float(j1_pt), totalWeight)
        self.hists["JetHt"].Fill(float(ht), totalWeight)
        self.hists["AvMu"].Fill(float(mu), totalWeight)
        self.hists["NPV"].Fill(float(npv), totalWeight)


#------------------------------------------------------------------
class idhists:
    def __init__(self, tag, topdir, isdata, treetype, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.hists={}
        self.detaillevel=detaillevel
        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        xbins = [0., 10., 20., 30., 40., 50., 60., 70., 80., 90., 100., 150., 200., 300., 400., 600.]
        etabins = [0., 0.7, 1.37, 1.52, 2.01, 2.47]

        self.hists['IDelPt']=     ROOT.TH1F("h_"+tag+"_IDelPt",tag+"_IDelPt; ID electron p_{T} [GeV]; Events",100, 0, 100)
        self.hists["Met"]=        ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(10 GeV)", 15, array('d',xbins))
        self.hists['Mt']=         ROOT.TH1F("h_"+tag+"_Mt",tag+"_Mt; m_{T} [GeV]; Events/(10 GeV) ",20, 0, 200)
        self.hists['Z0SinTheta']= ROOT.TH1F("h_"+tag+"_Z0sinT",tag+"_Z0sinT; Z_{0}sin(#theta) [mm]; Events/(0.25mm) ",20, 0, 5)
        self.hists['D0Sig']=      ROOT.TH1F("h_"+tag+"_D0sig",tag+"_D0sig; D_{0}sig; Events/(0.2) ",50, 0, 10)
        self.hists['IDelEta']=    ROOT.TH1F("h_"+tag+"_IDelEta", tag+"_IDelEta; ID electron  #eta; Events/0.1",5, array('d', etabins))
        self.hists['NJet']=       ROOT.TH1F("h_"+tag+"_Njet", tag+"_Njet; jet count; Events",8, 0, 8)
        self.hists['Jet1Pt']=     ROOT.TH1F("h_"+tag+"_J1pt", tag+"_J1pt; jet_{1} P_{T} [GeV]; Events/(25 GeV)",35, 25, 900)
        self.hists['JetHt']=      ROOT.TH1F("h_"+tag+"_HT", tag+"_HT; jet H_{T} [GeV]; Events/(50 GeV)",17, 50, 900)
        self.hists['NBJet']=      ROOT.TH1F("h_"+tag+"_Nbjet", tag+"_Nbjet; b-jet count; Events", 8, 0, 8)
        self.hists['AvMu']=       ROOT.TH1F("h_"+tag+"_Mu", tag+"_Mu; av int per crossing; Events/5",7, 5, 40.)
        self.hists['NPV']=        ROOT.TH1F("h_"+tag+"_Npv", tag+"_Npv; primary vertices; Events",29, 1, 30)
        self.hists['dphiJ1met']=  ROOT.TH1F("h_"+tag+"_dphi_j1met",tag+"_dphi_j1met; #Delta#phi_{jet_{1}-met} [rad];Events/(0.5 rad)",7, 0., 3.5 )
        self.hists['dphiL1met']=  ROOT.TH1F("h_"+tag+"_dphi_l1met",tag+"_dphi_l1met;#Delta#phi_{lep_{1}-met} [rad];Events/(0.5 rad)",7, 0., 3.5)

        topdir.cd()
        self.collections={}

    def write(self):
        self.newdir.cd()
        for i,k in self.hists.iteritems():
            k.SetOption("HIST")
            k.Write()
        for i,k in self.collections.iteritems():
            k.write()
        self.topdir.cd()

    def add(self, coll):
        for i,k in self.hists.iteritems():
            if i in coll.hists: k.Add(coll.hists[i])
        for i,k in self.collections.iteritems():
            if i in coll.collections: k.add(coll.collections[i])

    def fill(self, obs, elVec, elZ0, elD0, variation):
        intLumi = 1.0
        met = obs.met
        mt =  obs.getMT(elVec)

        #trigger variables
        triggers = {}
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20

        #electron variables
        IDpt     = elVec.Pt()
        IDeta    = abs(elVec.Eta())
        IDphi    = elVec.Phi()
        n_baseel = obs.n_baseel

        #dphi_variables
        dphiL1met = obs.getDphiL1MET(IDphi)
        dphiJ1met = obs.getDphiJ1MET()

        #jet variables
        n_jet = obs.n_jet
        n_bjet = obs.n_bjet
        j1_pt = obs.jet_pt[0]/1000.
        ht = obs.getHT()

        #pileup variables
        npv = obs.num_pv
        mu =  obs.mu

        #Calculate trigger weight
        norm = renorm(obs)

        #Calculating weight
        if self.isdata:
            totalWeight = norm.getTriggerWeights(self.isdata, IDpt, triggers)
        else:
            xs_weight, mc_event_weight, sf_el, sf_jvt, sf_btag, pileup_weight = obs.getWeights()
            if( variation == 'pileup' ):
                totalWeight = float(xs_weight*mc_event_weight*sf_el*sf_jvt*sf_btag*pileup_weight) #for pileup systematic
            else:
                totalWeight = float(xs_weight*mc_event_weight*sf_el*sf_jvt*sf_btag)

        self.hists["IDelPt"].Fill(float(IDpt), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["Met"].Fill(float(met), totalWeight)
        self.hists["Z0SinTheta"].Fill(float(abs(elZ0)), totalWeight)
        self.hists["D0Sig"].Fill(float(abs(elD0)), totalWeight)
        self.hists['IDelEta'].Fill(float(IDeta), totalWeight)
        self.hists["dphiJ1met"].Fill(float(math.fabs(dphiJ1met)), totalWeight)
        self.hists["dphiL1met"].Fill(float(math.fabs(dphiL1met)), totalWeight)
        self.hists["NJet"].Fill(float(n_jet), totalWeight)
        self.hists["NBJet"].Fill(float(n_bjet), totalWeight)
        self.hists["Jet1Pt"].Fill(float(j1_pt), totalWeight)
        self.hists["JetHt"].Fill(float(ht), totalWeight)
        self.hists["AvMu"].Fill(float(mu), totalWeight)
        self.hists["NPV"].Fill(float(npv), totalWeight)



#------------------------------------------------------------------
class histcollection:
    def __init__(self, tag, topdir, debug, isdata, treetype, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        if debug: 
            print "topdir"
            print topdir.GetName()
        self.isdata = isdata
        self.tree = treetype
        self.detaillevel=detaillevel

        newdir = self.newdir=topdir.mkdir(tag)
        if debug:
            print "newdir"
            print newdir.GetName()
        self.newdir.cd()
        self.collections={}
        self.topdir.cd()

    def write(self):
        self.newdir.cd()
        for i,k in self.collections.iteritems():
            k.write()
        self.topdir.cd()

    def addantiidcollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=antiidhists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.detaillevel)
        self.topdir.cd()

    def addidcollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=idhists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.detaillevel)
        self.topdir.cd()

    def addfakecollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=fakehists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.detaillevel)
        self.topdir.cd()

    def add(self, coll):
        for i,k in self.collections.iteritems():
            if i in coll: k.add(coll[i])

    def fillN(self, event, elVec, nlep, variation):
        for i,k in self.collections.iteritems():
            k.fill(event, elVec, nlep, variation)

    def fillN(self, event, tag, elVec, nlep, variation):
        for i,k in self.collections.iteritems():
            if i==tag:
                k.fill(event, elVec, nlep, variation)
                break

    def fill(self, event, elVec, Z0, D0, variation):
        for i,k in self.collections.iteritems():
            k.fill(event, elVec, Z0, D0, variation)

    def fill(self, event, tag, elVec, Z0, D0, variation):
        for i,k in self.collections.iteritems():
            if i==tag:
                k.fill(event, elVec, Z0, D0, variation)
                break
