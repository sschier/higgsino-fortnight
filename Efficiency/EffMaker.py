#!/usr/bin/env python
#Author: Sheena C Schier
#Created 01April2017 Created to make trigger efficiency plots
#Intended to run on signal only


import sys, os, subprocess, getopt
import re, time, copy, math, array
import argparse, commands
import ROOT
from ROOT import TString
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?

#local imports
from histograms import *
from observables import *
from cuts import *


#======================================================================
def truth(event, hc, flag, eventNum, evtVec, name):
    if( flag ):
        evtVec += [eventNum]
        hc.fill(event, name)
        return True
    else: return False
#======================================================================
def reco_preselection(event, hc, CutsDict, eventDict, xsec):
    if( CutsDict["met200"] ): eventDict["met200"] += 1##*xsec
    else: return False
    if( CutsDict["Trigger"] ): eventDict["Trigger"] += 1#*xsec  
    else: return False
    if( CutsDict["2Lep"] ): eventDict["2Lep"] += 1#*xsec 
    else: return False
    if( CutsDict["OSSF"] ): eventDict["OSSF"] += 1#*xsec
    else: return False
    if( CutsDict["lep1Pt5"] ): eventDict["lep1Pt5"] += 1#*xsec
    else: return False
    if( CutsDict["bVeto"] ): eventDict["bVeto"] += 1#*xsec
    else: return False
    if( CutsDict["j100"] ): eventDict["j100"] += 1#*xsec
    else: return False
    if( CutsDict["DPhiJ1Met"] ): eventDict["DPhiJ1Met"] += 1#*xsec
    else: return False
    if( CutsDict["minDPhi"] ): eventDict["minDPhi"] += 1#*xsec
    else: return False
    if( CutsDict["MTauTau"] ): eventDict["MTauTau"] += 1#*xsec
    else: return False
    if( CutsDict["mll"] ): eventDict["mll"] += 1#*xsec
    else: return False
    if( CutsDict["rll05"] ): eventDict["rll05"] += 1#*xsec
    else: return False
    hc.fill(event, "recoPresel")
    return True
#======================================================================
def reco_MLL(event, hc, CutsDict, flag, name, truthEvts, eventDict, xsec):
    if( CutsDict["MLLMETOverHTLep"] and CutsDict["mt70"] and CutsDict["rll2"] and flag ):
        hc.fill(event, name)
        eventDict[name] += 1#*xsec
        return True
    else: return False
#======================================================================
def reco_MT2(event, hc, CutsDict, flag, name, truthEvts):
    if( CutsDict["MT2METOverHTLep"] and flag ):
        hc.fill(event, "name")
        return True
    else: return False
#======================================================================
#
def analyze(recofile, truthfile, recotree, DSID, outfile, debug, region):

    if debug: print "opening input file"


    fr=ROOT.TFile(recofile, "RO")
    ft=ROOT.TFile(truthfile, "RO")

    if debug: print fr.GetName()
    if debug: print ft.GetName()

    tr=fr.Get("MGPy8EG_A14N23LO_%s_NoSys" % recotree) #tree either SlepSlep_direct_"l1"p0_"l2"p0_MET50 or SM_Higgsino_"N2"_"N1"_2LMET50_MadSpin
    tt=ft.Get("EwkCompressed2016__ntuple")

    if debug: print "MGPy8EG_A14N23LO_%s_SusySkimHiggsino_v1.9_SUSY16_tree_NoSys" % recotree

    #-------------------------
    #create output file
    #-------------------------

    if debug: print "opening output file"

    o=ROOT.TFile(outfile, "RECREATE")

    #truth SR vectors
    evtNum_SRSF_iMLLa = []
    evtNum_SRSF_iMLLb = []
    evtNum_SRSF_iMLLc = []
    evtNum_SRSF_iMLLd = []
    evtNum_SRSF_iMLLe = []
    evtNum_SRSF_iMLLf = []
    evtNum_SRSF_iMLLg = []

    evtNum_SRSF_eMLLa = []
    evtNum_SRSF_eMLLb = []
    evtNum_SRSF_eMLLc = []
    evtNum_SRSF_eMLLd = []
    evtNum_SRSF_eMLLe = []
    evtNum_SRSF_eMLLf = []
    evtNum_SRSF_eMLLg = []

    evtNum_SRSF_iMT2a = []
    evtNum_SRSF_iMT2b = []
    evtNum_SRSF_iMT2c = []
    evtNum_SRSF_iMT2d = []
    evtNum_SRSF_iMT2e = []
    evtNum_SRSF_iMT2f = []

    if debug: print "..making histograms collections"
    print o

    truthHists=histcollection("truthCollection", o, debug, 0)
    truthHists.addtruthcollection("Event_SRSF_iMLLa")
    truthHists.addtruthcollection("Event_SRSF_iMLLb")
    truthHists.addtruthcollection("Event_SRSF_iMLLc")
    truthHists.addtruthcollection("Event_SRSF_iMLLd")
    truthHists.addtruthcollection("Event_SRSF_iMLLe")
    truthHists.addtruthcollection("Event_SRSF_iMLLf")
    truthHists.addtruthcollection("Event_SRSF_iMLLg")

    recoPreselHists=histcollection("recoPreselCollection", o, debug, 0)
    recoPreselHists.addrecocollection("recoPresel")

    recoMLLHists=histcollection("recoMLLCollection", o, debug, 0)
    recoMLLHists.addrecocollection("Event_SRSF_iMLLa")
    recoMLLHists.addrecocollection("Event_SRSF_iMLLb")
    recoMLLHists.addrecocollection("Event_SRSF_iMLLc")
    recoMLLHists.addrecocollection("Event_SRSF_iMLLd")
    recoMLLHists.addrecocollection("Event_SRSF_iMLLe")
    recoMLLHists.addrecocollection("Event_SRSF_iMLLf")
    recoMLLHists.addrecocollection("Event_SRSF_iMLLg")
    eventcount = 0

    #-------------------------
    #loop over truthevents
    #-------------------------

    if debug: print "looping over truth events"

    for event in tt:
        #----------------------
        #bookkeep and monitor
        #______________________

        eventcount +=1

        obs = truthobservable(event)
        cutdict = truthcuts(obs)
        truthCuts = cutdict.getCuts()

        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount

        truth(obs, truthHists, truthCuts["Event_SRSF_iMLLa"], obs.EventNumber, evtNum_SRSF_iMLLa, "Event_SRSF_iMLLa")
        truth(obs, truthHists, truthCuts["Event_SRSF_iMLLb"], obs.EventNumber, evtNum_SRSF_iMLLb, "Event_SRSF_iMLLb")
        truth(obs, truthHists, truthCuts["Event_SRSF_iMLLc"], obs.EventNumber, evtNum_SRSF_iMLLc, "Event_SRSF_iMLLc")
        truth(obs, truthHists, truthCuts["Event_SRSF_iMLLd"], obs.EventNumber, evtNum_SRSF_iMLLd, "Event_SRSF_iMLLd")
        truth(obs, truthHists, truthCuts["Event_SRSF_iMLLe"], obs.EventNumber, evtNum_SRSF_iMLLe, "Event_SRSF_iMLLe")
        truth(obs, truthHists, truthCuts["Event_SRSF_iMLLf"], obs.EventNumber, evtNum_SRSF_iMLLf, "Event_SRSF_iMLLf")
        truth(obs, truthHists, truthCuts["Event_SRSF_iMLLg"], obs.EventNumber, evtNum_SRSF_iMLLg, "Event_SRSF_iMLLg")

        #print evtNum_SRSF_iMLLg

    if debug: print "...done with truth"

    eventcount = 0

    #-------------------------
    #loop over recoevents
    #-------------------------

    if debug: print "looping reco events"

    eventDict = {}
    eventDict['Trigger'] = 0
    eventDict['2Lep'] = 0
    eventDict['OSSF'] = 0
    eventDict['bVeto'] = 0
    eventDict['met200'] = 0
    eventDict['j100'] = 0
    eventDict['DPhiJ1Met'] = 0
    eventDict['minDPhi'] = 0
    eventDict['lep1Pt5'] = 0
    eventDict['MTauTau'] = 0
    eventDict['mll'] = 0
    eventDict['rll05'] = 0
    eventDict ['Event_SRSF_iMLLa'] = 0
    eventDict ['Event_SRSF_iMLLb'] = 0
    eventDict ['Event_SRSF_iMLLc'] = 0
    eventDict ['Event_SRSF_iMLLd'] = 0
    eventDict ['Event_SRSF_iMLLe'] = 0
    eventDict ['Event_SRSF_iMLLf'] = 0
    eventDict ['Event_SRSF_iMLLg'] = 0

    for event in tr:
        #----------------------
        #bookkeep and monitor
        #______________________

        eventcount +=1
        obs = recoobservable(event)
        cutdict = recocuts(obs)
        recoCuts = cutdict.getCuts()

        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        if( reco_preselection(obs, recoPreselHists, recoCuts, eventDict, obs.xsec) ):
            reco_MLL(obs, recoMLLHists, recoCuts, recoCuts["Event_SRSF_iMLLa"], "Event_SRSF_iMLLa", evtNum_SRSF_iMLLa, eventDict, obs.xsec)        
            reco_MLL(obs, recoMLLHists, recoCuts, recoCuts["Event_SRSF_iMLLb"], "Event_SRSF_iMLLb", evtNum_SRSF_iMLLb, eventDict, obs.xsec)        
            reco_MLL(obs, recoMLLHists, recoCuts, recoCuts["Event_SRSF_iMLLc"], "Event_SRSF_iMLLc", evtNum_SRSF_iMLLc, eventDict, obs.xsec)        
            reco_MLL(obs, recoMLLHists, recoCuts, recoCuts["Event_SRSF_iMLLd"], "Event_SRSF_iMLLd", evtNum_SRSF_iMLLd, eventDict, obs.xsec)        
            reco_MLL(obs, recoMLLHists, recoCuts, recoCuts["Event_SRSF_iMLLe"], "Event_SRSF_iMLLe", evtNum_SRSF_iMLLe, eventDict, obs.xsec)        
            reco_MLL(obs, recoMLLHists, recoCuts, recoCuts["Event_SRSF_iMLLf"], "Event_SRSF_iMLLf", evtNum_SRSF_iMLLf, eventDict, obs.xsec)        
            reco_MLL(obs, recoMLLHists, recoCuts, recoCuts["Event_SRSF_iMLLg"], "Event_SRSF_iMLLg", evtNum_SRSF_iMLLg, eventDict, obs.xsec)        


    if debug: print eventcount
    print "writing histograms for %s efficiency" % region
    print eventDict

    truthHists.write()
    recoPreselHists.write()
    recoMLLHists.write()


    if debug: print "...done with reco"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("-reco_input"      , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("-truth_input"      , action='store', default='', help='root file containing sum of weights hist')
    parser.add_argument("-reco_tree"        , action='store', default='')
    parser.add_argument("-DSID"        , action='store', default='')
    parser.add_argument("-outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("-region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    if args.test:
        print args.DSID

    analyze(args.reco_input, args.truth_input, args.reco_tree, args.DSID, args.outfile, args.test, args.region)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
