#!/usr/bin/env python
#Author: Sheena C Schier
#Created 10May2017 Created to calculate electron fake factors
#16May17: changed MET binning, fixed antiID definition, added regions to FFCR and more plots to regions in FFSR


import sys, os, subprocess, getopt
import re, time, copy, math
import argparse, commands
import ROOT
from ROOT import TString
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?

#local imports
from histograms import *
from observables import *
from cuts import *
from renormalize import *


#======================================================================
def FFIDSR(event, hc, IDCuts, elList, Z0list, D0list, variation):
    nlep = len(elList)
    nlep_fill = 0
    nlepSR_fill = 0
    for CutsDict, el, z0, d0 in zip(IDCuts, elList, Z0list, D0list):
        if(CutsDict["HLT_e5"]):
            hc.fill(event, "HLTe5", el, z0, d0, variation)
        if(CutsDict["HLT_e10"]):
            hc.fill(event, "HLTe10", el, z0, d0, variation)
        if(CutsDict["HLT_e15"]):
            hc.fill(event, "HLTe15", el, z0, d0, variation)
        if(CutsDict["HLT_e20"] ):
            hc.fill(event, "HLTe20", el, z0, d0, variation)
        if( ((CutsDict["HLT_e5"] and CutsDict["el5"]) or (CutsDict["HLT_e10"] and CutsDict["el10"]) or (CutsDict["HLT_e15"] and CutsDict["el15"]) or (CutsDict["HLT_e20"] and CutsDict["el20"])) ):
            #print "filling ID lep w/ Pt %f" % el.Pt()
            nlep_fill += 1
            hc.fill(event, "FFID", el, z0, d0, variation)
            if( CutsDict["40mt"] ):
                nlepSR_fill += 1
                hc.fill(event, "FFIDSR", el, z0, d0, variation)
    #if len(elList):
    #    hc.fillN(event, "FFIDN", elList[0], nlep, variation)
    #    hc.fillN(event, "FFIDNfill", elList[0], nlep_fill, variation)
    #    hc.fillN(event, "FFIDSRNfill", elList[0], nlepSR_fill, variation)
    return True
#======================================================================
def FFAIDSR(event, hc, AIDCuts, elList, Z0list, D0list, variation):
    nlep = len(elList)
    nlep_fill = 0
    nlepSR_fill = 0
    for CutsDict, el, z0, d0 in zip(AIDCuts, elList, Z0list, D0list):
        if(CutsDict["HLT_e5"]):
            hc.fill(event, "HLTe5", el, z0, d0, variation)
        if(CutsDict["HLT_e10"]):
            hc.fill(event, "HLTe10", el, z0, d0, variation)
        if(CutsDict["HLT_e15"]):
            hc.fill(event, "HLTe15", el, z0, d0, variation)
        if(CutsDict["HLT_e20"] ):
            hc.fill(event, "HLTe20", el, z0, d0, variation)
        if( ((CutsDict["HLT_e5"] and CutsDict["el5"]) or (CutsDict["HLT_e10"] and CutsDict["el10"]) or (CutsDict["HLT_e15"] and CutsDict["el15"]) or (CutsDict["HLT_e20"] and CutsDict["el20"])) ):
            #print "filling Anti ID lep w/ Pt %f" % el.Pt()
            nlep_fill += 1
            hc.fill(event, "FFAID", el, z0, d0, variation)
            if( CutsDict["40mt"] ):
                nlepSR_fill += 1
                hc.fill(event, "FFAIDSR", el, z0, d0, variation)
    #if len(elList):
    #    hc.fillN(event, "FFAIDN", elList[0], nlep, variation)
    #    hc.fillN(event, "FFAIDNfill", elList[0], nlep_fill, variation)
    #    hc.fillN(event, "FFAIDSRNfill", elList[0], nlepSR_fill, variation)
    return True
#======================================================================
#
def analyze(infile, tree, data, signal, outfile, debug, region, variation):

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

    IDSR=histcollection("FFIDSR", o, 0, data, tree, 0)
    IDSR.addfakecollection("FFIDN")
    IDSR.addfakecollection("FFIDNfill")
    IDSR.addfakecollection("FFIDSRNfill")
    IDSR.addidcollection("FFID")
    IDSR.addidcollection("FFIDSR")
    IDSR.addidcollection("HLTe5")
    IDSR.addidcollection("HLTe10")
    IDSR.addidcollection("HLTe15")
    IDSR.addidcollection("HLTe20")

    AIDSR=histcollection("FFAIDSR", o, 0, data, tree, 0)
    AIDSR.addfakecollection("FFAIDN")
    AIDSR.addfakecollection("FFAIDNfill")
    AIDSR.addfakecollection("FFAIDSRNfill")
    AIDSR.addantiidcollection("FFAID")
    AIDSR.addantiidcollection("FFAIDSR")
    AIDSR.addantiidcollection("HLTe5")
    AIDSR.addantiidcollection("HLTe10")
    AIDSR.addantiidcollection("HLTe15")
    AIDSR.addantiidcollection("HLTe20")

    AID1=histcollection("AID1", o, 0, data, tree, 0)
    AID1.addfakecollection("FFAIDN")
    AID1.addfakecollection("FFAIDNfill")
    AID1.addfakecollection("FFAIDSRNfill")
    AID1.addantiidcollection("FFAID")
    AID1.addantiidcollection("FFAIDSR")
    AID1.addantiidcollection("HLTe5")
    AID1.addantiidcollection("HLTe10")
    AID1.addantiidcollection("HLTe15")
    AID1.addantiidcollection("HLTe20")

    AID2=histcollection("AID2", o, 0, data, tree, 0)
    AID2.addfakecollection("FFAIDN")
    AID2.addfakecollection("FFAIDNfill")
    AID2.addfakecollection("FFAIDSRNfill")
    AID2.addantiidcollection("FFAID")
    AID2.addantiidcollection("FFAIDSR")
    AID2.addantiidcollection("HLTe5")
    AID2.addantiidcollection("HLTe10")
    AID2.addantiidcollection("HLTe15")
    AID2.addantiidcollection("HLTe20")

    AID3=histcollection("AID3", o, 0, data, tree, 0)
    AID3.addfakecollection("FFAIDN")
    AID3.addfakecollection("FFAIDNfill")
    AID3.addfakecollection("FFAIDSRNfill")
    AID3.addantiidcollection("FFAID")
    AID3.addantiidcollection("FFAIDSR")
    AID3.addantiidcollection("HLTe5")
    AID3.addantiidcollection("HLTe10")
    AID3.addantiidcollection("HLTe15")
    AID3.addantiidcollection("HLTe20")

    AID13=histcollection("AID13", o, 0, data, tree, 0)
    AID13.addfakecollection("FFAIDN")
    AID13.addfakecollection("FFAIDNfill")
    AID13.addfakecollection("FFAIDSRNfill")
    AID13.addantiidcollection("FFAID")
    AID13.addantiidcollection("FFAIDSR")
    AID13.addantiidcollection("HLTe5")
    AID13.addantiidcollection("HLTe10")
    AID13.addantiidcollection("HLTe15")
    AID13.addantiidcollection("HLTe20")

    AID12=histcollection("AID12", o, 0, data, tree, 0)
    AID12.addfakecollection("FFAIDN")
    AID12.addfakecollection("FFAIDNfill")
    AID12.addfakecollection("FFAIDSRNfill")
    AID12.addantiidcollection("FFAID")
    AID12.addantiidcollection("FFAIDSR")
    AID12.addantiidcollection("HLTe5")
    AID12.addantiidcollection("HLTe10")
    AID12.addantiidcollection("HLTe15")
    AID12.addantiidcollection("HLTe20")

    AID23=histcollection("AID23", o, 0, data, tree, 0)
    AID23.addfakecollection("FFAIDN")
    AID23.addfakecollection("FFAIDNfill")
    AID23.addfakecollection("FFAIDSRNfill")
    AID23.addantiidcollection("FFAID")
    AID23.addantiidcollection("FFAIDSR")
    AID23.addantiidcollection("HLTe5")
    AID23.addantiidcollection("HLTe10")
    AID23.addantiidcollection("HLTe15")
    AID23.addantiidcollection("HLTe20")

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
        #print "event %i" % eventcount

        #----------------------------
        #define preliminary variables
        #----------------------------

        #qcd cut variables

        obs = observable(event, data)
        IDelectronlist,           IDelectronZ0sinT,           IDelectronD0sig = obs.getIDelectrons()
        AIDelectronlist,          AIDelectronZ0sinT,          AIDelectronD0sig = obs.getAntiIDelectrons()
        failID_electronlist,      failID_electronZ0sinT,      failID_electronD0sig = obs.getAntiIDelectrons1()
        failISO_electronlist,     failISO_electronZ0sinT,     failISO_electronD0sig = obs.getAntiIDelectrons2()
        failD0_electronlist,      failD0_electronZ0sinT,      failD0_electronD0sig = obs.getAntiIDelectrons3()
        failID_ISO_electronlist,  failID_ISO_electronZ0sinT,  failID_ISO_electronD0sig = obs.getAntiIDelectrons12()
        failID_D0_electronlist,   failID_D0_electronZ0sinT,   failID_D0_electronD0sig = obs.getAntiIDelectrons13()
        failISO_D0_electronlist,  failISO_D0_electronZ0sinT,  failISO_D0_electronD0sig = obs.getAntiIDelectrons23()
        cutdict = cuts(obs) 
        IDCuts = cutdict.getCuts(IDelectronlist)
        AIDCuts = cutdict.getCuts(AIDelectronlist)
        failIDCuts = cutdict.getCuts(failID_electronlist)
        failISOCuts = cutdict.getCuts(failISO_electronlist)
        failD0Cuts = cutdict.getCuts(failD0_electronlist)
        failID_ISOCuts = cutdict.getCuts(failID_ISO_electronlist)
        failID_D0Cuts = cutdict.getCuts(failID_D0_electronlist)
        failISO_D0Cuts = cutdict.getCuts(failISO_D0_electronlist)
        print failID_electronlist

        triggers = {}
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20

        #print triggers

        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        if debug:
            if eventcount == 1: 
                if region == 'dilepton':
                    print 'Recalculating generator Weight!!'

        #------------------------------
        #trigger efficiency regions
        #------------------------------
        FFIDSR( obs,  IDSR,   IDCuts,         IDelectronlist,          IDelectronZ0sinT,          IDelectronD0sig, variation)
        FFAIDSR(obs,  AIDSR,  AIDCuts,        AIDelectronlist,         AIDelectronZ0sinT,         AIDelectronD0sig, variation)
        FFAIDSR(obs,  AID1,   failIDCuts,     failID_electronlist,     failID_electronZ0sinT,     failID_electronD0sig, variation)
        FFAIDSR(obs,  AID2,   failISOCuts,    failISO_electronlist,    failISO_electronZ0sinT,    failISO_electronD0sig, variation)
        FFAIDSR(obs,  AID3,   failD0Cuts,     failD0_electronlist,     failD0_electronZ0sinT,     failD0_electronD0sig, variation)
        FFAIDSR(obs,  AID13,  failID_ISOCuts, failID_D0_electronlist,  failID_D0_electronZ0sinT,  failID_D0_electronD0sig, variation)
        FFAIDSR(obs,  AID12,  failID_D0Cuts,  failID_ISO_electronlist, failID_ISO_electronZ0sinT, failID_ISO_electronD0sig, variation)
        FFAIDSR(obs,  AID23,  failISO_D0Cuts, failISO_D0_electronlist, failISO_D0_electronZ0sinT, failISO_D0_electronD0sig, variation)


    print '%i total events' % eventcount
    print "writing histograms for electron fake estimates" 

    IDSR.write()
    AIDSR.write()
    AID1.write() 
    AID2.write()
    AID3.write()
    AID13.write() 
    AID12.write()
    AID23.write()



    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("--input"      , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("-variation"   , action='store', default='', help='set for a systematic varaiation')
    parser.add_argument("--tree"        , action='store', default='')
    parser.add_argument("--isData"      , action='store', default='')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("--outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("--region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    analyze(args.input,  args.tree, args.isData, args.isSignal, args.outfile, args.test, args.region, args.variation)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
