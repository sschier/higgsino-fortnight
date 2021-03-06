#!/usr/bin/env python
#Author: Sheena C Schier
#Created 10May2017 Created to calculate electron fake factors
#16May17: changed MET binning, fixed antiID definition, added regions to FFCR and more plots to regions in FFSR


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
from renormalize import *
from functions import *

#======================================================================
def FFIDSR(event, hc, IDCuts, elList, Z0list, D0list, debug):
    nlep = len(elList)
    nlep_fill = 0
    nlepSR_fill = 0
    for CutsDict, el, z0, d0 in zip(IDCuts, elList, Z0list, D0list):
        if(CutsDict["HLT_e5"]):
            hc.fill(event, "HLTe5", el, z0, d0)
        if(CutsDict["HLT_e10"]):
            hc.fill(event, "HLTe10", el, z0, d0)
        if(CutsDict["HLT_e15"]):
            hc.fill(event, "HLTe15", el, z0, d0)
        if(CutsDict["HLT_e20"] ):
            hc.fill(event, "HLTe20", el, z0, d0)
        if( ((CutsDict["HLT_e5"] and CutsDict["idel5"]) or (CutsDict["HLT_e10"] and CutsDict["idel10"]) or (CutsDict["HLT_e15"] and CutsDict["idel15"]) or (CutsDict["HLT_e20"] and CutsDict["idel20"])) ):
            if debug: print "filling ID lep w/ Pt %f" % el.Pt()
            nlep_fill += 1
            hc.fill(event, "FFID", el, z0, d0)
            if( CutsDict["40mtID"] ):
                nlepSR_fill += 1
                hc.fill(event, "FFIDSR", el, z0, d0)
    #if len(elList):
    #    hc.fillN(event, "FFIDN", elList[0], nlep)
    #    hc.fillN(event, "FFIDNfill", elList[0], nlep_fill)
    #    hc.fillN(event, "FFIDSRNfill", elList[0], nlepSR_fill)
    return True
#======================================================================
def FFAIDSR(event, hc, AIDCuts, elList, Z0list, D0list, debug):
    nlep = len(elList)
    nlep_fill = 0
    nlepSR_fill = 0
    for CutsDict, el, z0, d0 in zip(AIDCuts, elList, Z0list, D0list):
        if(CutsDict["HLT_e5"]):
            hc.fill(event, "HLTe5", el, z0, d0)
        if(CutsDict["HLT_e10"]):
            hc.fill(event, "HLTe10", el, z0, d0)
        if(CutsDict["HLT_e15"]):
            hc.fill(event, "HLTe15", el, z0, d0)
        if(CutsDict["HLT_e20"]):
            hc.fill(event, "HLTe20", el, z0, d0)
        if( ((CutsDict["HLT_e5"] and CutsDict["antiidel5"]) or (CutsDict["HLT_e10"] and CutsDict["antiidel10"]) or (CutsDict["HLT_e15"] and CutsDict["antiidel15"]) or (CutsDict["HLT_e20"] and CutsDict["antiidel20"])) ):
            if debug: print "filling Anti ID lep w/ Pt %f" % el.Pt()
            nlep_fill += 1
            hc.fill(event, "FFAID", el, z0, d0)
            if( CutsDict["40mtAID"] ):
                nlepSR_fill += 1
                hc.fill(event, "FFAIDSR", el, z0, d0)
    #if len(elList):
    #    hc.fillN(event, "FFAIDN", elList[0], nlep)
    #    hc.fillN(event, "FFAIDNfill", elList[0], nlep_fill)
    #    hc.fillN(event, "FFAIDSRNfill", elList[0], nlepSR_fill)
    return True
#======================================================================
#
def analyze(infile, tree, data, signal, outfile, debug, region):

    if debug: print "opening input file"

    f=ROOT.TFile(infile, "RO")

    print 'running over file %s' % f.GetName()


    t=f.Get("%s" %tree)
    print 'getting events in %s' % t.GetName()


    #-------------------------
    #create output file
    #-------------------------


    if debug: print "opening output file"

    o=ROOT.TFile(outfile, "RECREATE")

    if debug: print "..making histograms collections"

    IDSR=histcollection("FFIDSR", o, debug, data, tree, 0)
    IDSR.addfakecollection("FFIDN")
    IDSR.addfakecollection("FFIDNfill")
    IDSR.addfakecollection("FFIDSRNfill")
    IDSR.addidcollection("FFID")
    IDSR.addidcollection("FFIDSR")
    IDSR.addidcollection("HLTe5")
    IDSR.addidcollection("HLTe10")
    IDSR.addidcollection("HLTe15")
    IDSR.addidcollection("HLTe20")

    AIDSR=histcollection("FFAIDSR", o, debug, data, tree, 0)
    AIDSR.addfakecollection("FFAIDN")
    AIDSR.addfakecollection("FFAIDNfill")
    AIDSR.addfakecollection("FFAIDSRNfill")
    AIDSR.addantiidcollection("FFAID")
    AIDSR.addantiidcollection("FFAIDSR")
    AIDSR.addantiidcollection("HLTe5")
    AIDSR.addantiidcollection("HLTe10")
    AIDSR.addantiidcollection("HLTe15")
    AIDSR.addantiidcollection("HLTe20")

    eventcount = 0

    #-------------------------
    #loop over events
    #-------------------------

    if debug: print "looping over events"

    for event in t:
        #----------------------
        #bookkeep and monitor
        #______________________

        eventcount +=1
        if debug: print "event %i" % eventcount

        #----------------------------
        #define preliminary variables
        #----------------------------

        #qcd cut variables

        obs = observable(event, data)
        IDelectronlist, IDelectronZ0sinT, IDelectronD0sig = obs.getSigElectrons()
        if debug: print "%i signal electrons" % len(IDelectronlist)
        AIDelectronlist, AIDelectronZ0sinT, AIDelectronD0sig = obs.getAntiIDelectrons(IDelectronlist, debug)
        cutdict = cuts(obs) 
        IDCuts = cutdict.getIDCuts(IDelectronlist)
        AIDCuts = cutdict.getAIDCuts(AIDelectronlist)

        triggers = {}
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20

        if debug: print triggers

        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        if debug:
            if eventcount == 1: 
                if region == 'dilepton':
                    print 'Recalculating generator Weight!!'

        #------------------------------
        #trigger efficiency regions
        #------------------------------
        FFIDSR( obs,  IDSR,  IDCuts, IDelectronlist, IDelectronZ0sinT, IDelectronD0sig, debug)
        FFAIDSR(obs,  AIDSR, AIDCuts, AIDelectronlist, AIDelectronZ0sinT, AIDelectronD0sig, debug)


    print '%i total events' % eventcount
    print "writing histograms for electron fake estimates" 

    IDSR.write()
    AIDSR.write()

    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("--input"      , action='store', default='', help='input root file containing tree to loop over')
    #parser.add_argument("--weight"      , action='store', default='', help='root file containing sum of weights hist')
    parser.add_argument("--tree"        , action='store', default='')
    parser.add_argument("--isData"      , action='store', default='')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("--outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("--region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    analyze(args.input,  args.tree, args.isData, args.isSignal, args.outfile, args.test, args.region)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
