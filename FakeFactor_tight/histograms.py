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

        self.hists['AntiIDelPt']=ROOT.TH1F("h_"+tag+"_AntiIDelPt",tag+"_AntiIDelPt; AntiID electron p_{T} [GeV]; Events",20, 0, 100)
        self.hists["Met"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(10 GeV)",60,0,600)
        self.hists['Mt']=ROOT.TH1F("h_"+tag+"_Mt",tag+"_Mt; m_{T} [GeV]; Events/(10 GeV) ",20, 0, 200)

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

    def fill(self, obs, elVec):
        intLumi = 1.0
        met = obs.getMET()
        mt =  obs.getMT(elVec)
        #mt =  obs.getMT(obs.getAntiIDelectronVec())
        triggers = {}
        #trigger variables
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20
        #electron variables
        AntiIDpt = ROOT.TLorentzVector()
        AntiIDpt = elVec.Pt()
        #AntiIDpt = obs.getAntiIDelectronVec().Pt()
        n_baseel = obs.getNBaseel()


        #Calculate trigger weight
        norm = renorm(obs)
        ptRegion = norm.getRegion(AntiIDpt, triggers)

        #Calculating weight
        if self.isdata:
            #print "getting trigger prescales"
            totalWeight = norm.getTriggerWeights(self.isdata, AntiIDpt, triggers)
        else:
            xs_weight, mc_event_weight, pileup_weight = obs.getWeights()
            #totalWeight = float(xs_weight*mc_event_weight*pileup_weight) #TODO: NO TRIGGER WEIGHT!!
            totalWeight = float(xs_weight*mc_event_weight) #TODO: NO TRIGGER WEIGHT!!

        self.hists["AntiIDelPt"].Fill(float(AntiIDpt), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["Met"].Fill(float(met), totalWeight)


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

        self.hists['IDelPt']=ROOT.TH1F("h_"+tag+"_IDelPt",tag+"_IDelPt; ID electron p_{T} [GeV]; Events",20, 0, 100)
        self.hists["Met"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(10 GeV)",60,0,600)
        self.hists['Mt']=ROOT.TH1F("h_"+tag+"_Mt",tag+"_Mt; m_{T} [GeV]; Events/(10 GeV) ",20, 0, 200)

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

    def fill(self, obs, elVec):
        intLumi = 1.0
        met = obs.getMET()
        mt =  obs.getMT(elVec)
        #mt =  obs.getMT(obs.getIDelectronVec())
        triggers = {}
        #trigger variables
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20
        #electron variables
        IDpt     = elVec.Pt()
        #IDpt     = obs.getIDelectronVec().Pt()
        n_baseel = obs.getNBaseel()


        #Calculate trigger weight
        norm = renorm(obs)

        #Calculating weight
        if self.isdata:
            #print "getting trigger prescales"
            totalWeight = norm.getTriggerWeights(self.isdata, IDpt, triggers)
        else:
            xs_weight, mc_event_weight, pileup_weight = obs.getWeights()
            totalWeight = float(xs_weight*mc_event_weight*pileup_weight) #TODO: NO TRIGGER WEIGHT!!

        self.hists["IDelPt"].Fill(float(IDpt), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["Met"].Fill(float(met), totalWeight)


#------------------------------------------------------------------
class fakehists:
    def __init__(self, tag, topdir, isdata, treetype, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.hists={}
        self.detaillevel=detaillevel
        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        xbins = [0., 5., 10., 15., 20., 100.]

        #self.hists['elPt']=ROOT.TH1F("h_"+tag+"_elPt",tag+"_elPt; electron p_{T} [GeV]; Events",5, array('d',xbins))
        self.hists['IDelPt']=ROOT.TH1F("h_"+tag+"_IDelPt",tag+"_IDelPt; ID electron p_{T} [GeV]; Events",20, 0, 100)
        self.hists['AntiIDelPt']=ROOT.TH1F("h_"+tag+"_AntiIDelPt",tag+"_AntiIDelPt; AntiID electron p_{T} [GeV]; Events",20, 0, 100)
        self.hists["Met"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(10 GeV)",60,0,600)
        self.hists['Mt']=ROOT.TH1F("h_"+tag+"_Mt",tag+"_Mt; m_{T} [GeV]; Events/(10 GeV) ",20, 0, 200)

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

    def fill(self, obs, elVec):
        intLumi = 1.0
        met = obs.getMET()
        mt =  obs.getMT()
        triggers = {}
        #trigger variables
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20
        #electron variables
        IDpt = obs.getIDelectronPt()
        AntiIDpt = obs.getAntiIDelectronPt()
        n_baseel = obs.getNBaseel()
        IDel_pt = -99.
        AntiIDel_pt = -99.
        if len(IDpt) > 0:
            IDel_pt = IDpt[0]
        if len(AntiIDpt) > 0:
            AntiIDel_pt = AntiIDpt[0]


        #Recalculate generator weight
        #newNorm = renorm(self.sumWHist, event)

        #Calculating weight
        if self.isdata:
            totalWeight = 1.0
        else:
            xs_weight, mc_event_weight, pileup_weight = obs.getWeights()
            totalWeight = float(xs_weight*mc_event_weight*pileup_weight) #TODO: NO TRIGGER WEIGHT!!
            #totalWeight = 1.0

        self.hists["IDelPt"].Fill(float(IDel_pt), totalWeight)
        self.hists["AntiIDelPt"].Fill(float(AntiIDel_pt), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["Met"].Fill(float(met), totalWeight)


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

    def fill(self, event, elVec):
        for i,k in self.collections.iteritems():
            k.fill(event, elVec)

    def fill(self, event, tag, elVec):
        for i,k in self.collections.iteritems():
            if i==tag:
                k.fill(event, elVec)
                break
