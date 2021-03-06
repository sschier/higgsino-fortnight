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

        self.hists['AntiIDelPt']=ROOT.TH1F("h_"+tag+"_AntiIDelPt",tag+"_AntiIDelPt; AntiID electron p_{T} [GeV]; Events",100, 0, 100)
        self.hists["Met"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(10 GeV)",60,0,600)
        self.hists['Mt']=ROOT.TH1F("h_"+tag+"_Mt",tag+"_Mt; m_{T} [GeV]; Events/(10 GeV) ",20, 0, 200)
        self.hists['Z0SinTheta']=ROOT.TH1F("h_"+tag+"_Z0sinT",tag+"_Z0sinT; Z_{0}sin(#theta) [mm]; Events/(0.25mm) ",20, 0, 5)
        self.hists['D0Sig']=ROOT.TH1F("h_"+tag+"_D0sig",tag+"_D0sig; D_{0}sig; Events/(0.2) ",50, 0, 10)

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

    def fill(self, obs, elVec, elZ0, elD0):
        intLumi = 1.0
        met = obs.getMET()
        mt =  obs.getMT(elVec)
        #mt =  obs.getMT(obs.getAntiIDelectronVec())
        #trigger variables
        triggers = {}
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20
        #electron variables
        #AntiIDpt = ROOT.TLorentzVector()
        AntiIDpt = elVec.Pt()
        AntiIDphi = elVec.Phi()
        AntiIDeta = elVec.Eta()
        #leptons
        n_baseel = obs.getNBaseel()

        #Calculate trigger weight
        norm = renorm(obs)
        #ptRegion = norm.getRegion(AntiIDpt, triggers)

        #Calculating weight
        if self.isdata:
            #print "getting trigger prescales"
            totalWeight = norm.getTriggerWeights(self.isdata, AntiIDpt, triggers)
            print 'Anti ID total weight = %f' % totalWeight
        else:
            xs_weight, mc_event_weight, pileup_weight, sf_total = obs.getWeights()
            totalWeight = float(xs_weight*mc_event_weight*sf_total) #TODO: NO TRIGGER WEIGHT!!
            #totalWeight = float(xs_weight*mc_event_weight) #TODO: NO TRIGGER WEIGHT!!

        self.hists["AntiIDelPt"].Fill(float(AntiIDpt), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["Met"].Fill(float(met), totalWeight)
        self.hists["Z0SinTheta"].Fill(float(abs(elZ0)), totalWeight)
        self.hists["D0Sig"].Fill(float(abs(elD0)), totalWeight)


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

        self.hists['IDelPt']=ROOT.TH1F("h_"+tag+"_IDelPt",tag+"_IDelPt; ID electron p_{T} [GeV]; Events",100, 0, 100)
        self.hists["Met"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(10 GeV)",60,0,600)
        self.hists['Mt']=ROOT.TH1F("h_"+tag+"_Mt",tag+"_Mt; m_{T} [GeV]; Events/(10 GeV) ",20, 0, 200)
        self.hists['Z0SinTheta']=ROOT.TH1F("h_"+tag+"_Z0sinT",tag+"_Z0sinT; Z_{0}sin(#theta) [mm]; Events/(0.25mm) ",20, 0, 5)
        self.hists['D0Sig']=ROOT.TH1F("h_"+tag+"_D0sig",tag+"_D0sig; D_{0}sig; Events/(0.2) ",50, 0, 10)

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

    def fill(self, obs, elVec, elZ0, elD0):
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
        n_baseel = obs.getNBaseel()


        #Calculate trigger weight
        norm = renorm(obs)

        #Calculating weight
        if self.isdata:
            print "getting trigger prescales"
            totalWeight = norm.getTriggerWeights(self.isdata, IDpt, triggers)
            print 'ID total weight = %f' % totalWeight
        else:
            xs_weight, mc_event_weight, pileup_weight, sf_total = obs.getWeights()
            totalWeight = float(xs_weight*mc_event_weight*sf_total) #TODO: NO TRIGGER WEIGHT!!

        self.hists["IDelPt"].Fill(float(IDpt), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["Met"].Fill(float(met), totalWeight)
        self.hists["Z0SinTheta"].Fill(float(abs(elZ0)), totalWeight)
        self.hists["D0Sig"].Fill(float(abs(elD0)), totalWeight)


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

        self.hists['n_el']=ROOT.TH1F("h_"+tag+"_n_el",tag+"_n_el; n el; Events ", 4, 0, 4)
        self.hists["Met"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(10 GeV)",60,0,600)

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

    def fill(self, obs, elVec, nLep):
        intLumi = 1.0
        met = obs.getMET()
        triggers = {}
        #trigger variables
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20
        #electron variables
        IDpt     = elVec.Pt()
        n_IDel = nLep

        #Calculate trigger weight
        norm = renorm(obs)

        #Calculating weight
        if self.isdata:
            #print "getting trigger prescales"
            totalWeight = norm.getTriggerWeights(self.isdata, IDpt, triggers)
        else:
            xs_weight, mc_event_weight, pileup_weight = obs.getWeights()
            totalWeight = float(xs_weight*mc_event_weight*sf_total) #TODO: NO TRIGGER WEIGHT!!

        self.hists["n_el"].Fill(float(n_IDel), totalWeight)
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

    def fillN(self, event, elVec, nlep):
        for i,k in self.collections.iteritems():
            k.fill(event, elVec, nlep)

    def fillN(self, event, tag, elVec, nlep):
        for i,k in self.collections.iteritems():
            if i==tag:
                k.fill(event, elVec, nlep)
                break

    def fill(self, event, elVec, Z0, D0):
        for i,k in self.collections.iteritems():
            k.fill(event, elVec, Z0, D0)

    def fill(self, event, tag, elVec, Z0, D0):
        for i,k in self.collections.iteritems():
            if i==tag:
                k.fill(event, elVec, Z0, D0)
                break
