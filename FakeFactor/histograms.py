#Author:Sheena C Schier
#Created 10May17 for calculating electron scale factors
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?
from array import array
from observables import *
from renormalize import *


#------------------------------------------------------------------
class fakehists:
    def __init__(self, tag, topdir, isdata, treetype, DSID, sumWHist, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.sumWHist = sumWHist
        self.hists={}
        self.detaillevel=detaillevel
        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        xbins = [0., 5., 10., 15., 20., 100.]

        #self.hists['elPt']=ROOT.TH1F("h_"+tag+"_elPt",tag+"_elPt; electron p_{T} [GeV]; Events",5, array('d',xbins))
        self.hists['IDelPt']=ROOT.TH1F("h_"+tag+"_IDelPt",tag+"_IDelPt; ID electron p_{T} [GeV]; Events",20, 0, 100)
        self.hists['AntiIDelPt']=ROOT.TH1F("h_"+tag+"_AntiIDelPt",tag+"_AntiIDelPt; AntiID electron p_{T} [GeV]; Events",20, 0, 100)
        self.hists["Met"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(25 GeV)",22,50,600)
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

    def fill(self, event):
        weight=float(1.0)
        totalWeight=float(1.0)
        intLumi = 1.0

        IDel_pt = -99.
        AntiIDel_pt = -99.
        baseel_pt = event.baseel_pt[0]/1000.
        met = event.met/1000.
        mt = event.mt/1000.
        #electron variables
        baseel_d0sig = event.baseel_d0sig
        baseel_z0sinTheta = event.baseel_z0sinTheta
        baseel_eta = event.baseel_eta
        baseel_isoTight = event.baseel_isoTight
        baseel_idTight = event.baseel_idTight

        if( baseel_idTight[0] == 0 or baseel_isoTight[0] == 0 ):
            AntiIDel_pt = baseel_pt
        if len(event.el_pt) > 0:
            IDel_pt = event.el_pt[0]/1000.

        #Recalculate generator weight
        #newNorm = renorm(self.sumWHist, event)
        #if self.isdata:
        #    genWeight = 1.0
        #else:
        #    genWeight = newNorm.getGenWeight(intLumi)
        #genWeight = event.genWeight

        #Calculating weight
        if self.isdata:
            totalWeight = 1.0
        else:
            #totalWeight = float(event.SherpaVjetsNjetsWeight*event.ttbarNNLOWeight*event.pileupWeight*event.eventWeight*event.leptonWeight*event.jvtWeight*event.bTagWeight*genWeight) #TODO: NO TRIGGER WEIGHT!!
            totalWeight = 1.0

        self.hists["IDelPt"].Fill(float(IDel_pt), totalWeight)
        self.hists["AntiIDelPt"].Fill(float(AntiIDel_pt), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["Met"].Fill(float(met), totalWeight)


#------------------------------------------------------------------
class histcollection:
    def __init__(self, tag, topdir, debug, isdata, treetype, DSID, sumWHist, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        if debug: 
            print "topdir"
            print topdir.GetName()
        self.isdata = isdata
        self.tree = treetype
        self.DSID = DSID
        self.sumWHist = sumWHist
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

    def addfakecollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=fakehists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.DSID, self.sumWHist, self.detaillevel)
        self.topdir.cd()

    def add(self, coll):
        for i,k in self.collections.iteritems():
            if i in coll: k.add(coll[i])

    def fill(self, event):
        for i,k in self.collections.iteritems():
            k.fill(event)

    def fill(self, event, tag):
        for i,k in self.collections.iteritems():
            if i==tag:
                k.fill(event)
                break
