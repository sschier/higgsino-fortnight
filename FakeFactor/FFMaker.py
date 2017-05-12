#!/usr/bin/env python
#Author: Sheena C Schier
#Created 10May2017 Created to calculate electron fake factors


import sys, os, subprocess, getopt
import re, time, copy, math, array
import argparse, commands
import ROOT
from ROOT import TString
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?

#local imports
from histograms import *
from observables import *
from renormalize import *


#======================================================================
def FFCR(event, hc, CutsDict):
    if( CutsDict["electronTriggers"] == True and CutsDict["100mt200"] == True ):
        hc.fill(event, "FFCR")
        return True
    else: return False
#======================================================================
def FFSR(event, hc, CutsDict):
    if( CutsDict["electronTriggers"] and CutsDict["40mt"] ):
        hc.fill(event, "FFSR")
    if( CutsDict["HLT_e5"] and CutsDict["el5"] ):
        hc.fill(event, "HLT_e5")
    if( CutsDict["HLT_e10"] and CutsDict["el10"] ):
        hc.fill(event, "HLT_e10")
    if( CutsDict["HLT_e15"] and CutsDict["el15"] ):
        hc.fill(event, "HLT_e15")
    if( CutsDict["HLT_e20"] and CutsDict["el20"] ):
        hc.fill(event, "HLT_e20")

        return True
    else: return False
#======================================================================
#======================================================================
#
def analyze(infile, weightfile, tree, DSID, data, signal, outfile, debug, region):

    if debug: print "opening input file"

    f=ROOT.TFile(infile, "RO")
    fw=ROOT.TFile(weightfile, "RO")

    if debug: print f.GetName()

    #get sum of weights hist
    #if data: sumWhist = f.Get("weighted__AOD")
    #elif signal: sumWhist = f.Get("weighted__AOD")
    #else: sumWhist = fw.Get("weighted__AOD")
    #print sumWhist.GetName()

    if data:
        t=f.Get("%s" %tree)
        sumWhist = fw.Get("weighted__AOD")
    else:
        t=f.Get("%s_NoSys" % tree) 
        sumWhist = f.Get("weighted__AOD") 


    if debug: print t.GetName()


    #-------------------------
    #create output file
    #-------------------------


    if debug: print "opening output file"

    o=ROOT.TFile(outfile, "RECREATE")

    if debug: print "..making histograms collections"

    CR=histcollection("FFCR", o, debug, data, tree, DSID, sumWhist, 0)
    CR.addfakecollection("FFCR")

    SR=histcollection("FFSR", o, debug, data, tree, DSID, sumWhist, 0)
    SR.addfakecollection("FFSR")
    SR.addfakecollection("HLT_e5")
    SR.addfakecollection("HLT_e10")
    SR.addfakecollection("HLT_e15")
    SR.addfakecollection("HLT_e20")

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

        #----------------------------
        #define preliminary variables
        #----------------------------

        #qcd cut variables
        met = event.met/1000.
        mt = event.mt/1000.
        #trigger variables
        HLT_e5 = event.HLT_e5_lhvloose
        HLT_e10 = event.HLT_e10_lhvloose_L1EM7
        HLT_e15 = event.HLT_e15_lhvloose_L1EM13VH
        HLT_e20 = event.HLT_e20_lhvloose
        #electron variables
        IDel_pt = -99.
        AntiIDel_pt = -99.
        baseel_pt = event.baseel_pt[0]/1000.
        baseel_d0sig = event.baseel_d0sig
        baseel_z0sinTheta = event.baseel_z0sinTheta
        baseel_eta = event.baseel_eta
        baseel_isoTight = event.baseel_isoTight
        baseel_idTight = event.baseel_idTight

        if( baseel_idTight[0] == 0 or baseel_isoTight[0] == 0 ):
            AntiIDel_pt = baseel_pt
        if len(event.el_pt) > 0:
            IDel_pt = event.el_pt[0]/1000.

        #print 'met = %f' % met
        #print 'MT = %f' % mt
        #print 'base el pt = %f' % baseel_pt[0]
        #print len(baseel_pt)

        #Make dictionary of cuts
        Cuts = {}


        if( mt < 40. ):
            Cuts["40mt"] = True
        else:
            Cuts["40mt"] = False

        if( mt > 100. and mt < 200. ):
            Cuts["100mt200"] = True
        else: 
            Cuts["100mt200"] = False

        if( HLT_e5 or HLT_e10 or HLT_e15 or HLT_e20 ):
            Cuts["electronTriggers"] = True
        else: 
            Cuts["electronTriggers"] = False

        if( HLT_e5 ):
            Cuts["HLT_e5"] = True
        else: Cuts["HLT_e5"] = False

        if( HLT_e10 ):
            Cuts["HLT_e10"] = True
        else: Cuts["HLT_e10"] = False

        if( HLT_e15 ):
            Cuts["HLT_e15"] = True
        else: Cuts["HLT_e15"] = False

        if( HLT_e20 ):
            Cuts["HLT_e20"] = True
        else: Cuts["HLT_e20"] = False

        if( baseel_pt >= 5. and baseel_pt < 10 ):
            Cuts["el5"] = True
        else: Cuts["el5"] = False

        if( baseel_pt >= 10. and baseel_pt < 15 ):
            Cuts["el10"] = True
        else: Cuts["el10"] = False

        if( baseel_pt >= 15. and baseel_pt < 20 ):
            Cuts["el15"] = True
        else: Cuts["el15"] = False

        if( baseel_pt >= 20. ):
            Cuts["el20"] = True
        else: Cuts["el20"] = False

        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        if debug:
            if eventcount == 1: 
                if region == 'dilepton':
                    print 'Recalculating generator Weight!!'

        #------------------------------
        #trigger efficiency regions
        #------------------------------
        FFCR(   event,  CR,    Cuts) 
        FFSR(   event,  SR,    Cuts) 


    if debug: print eventcount
    print "writing histograms for electron fake estimates" 

    CR.write()
    SR.write()

    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("--input"      , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("--weight"      , action='store', default='', help='root file containing sum of weights hist')
    parser.add_argument("--tree"        , action='store', default='')
    parser.add_argument("--DSID"        , action='store', default='')
    parser.add_argument("--isData"      , action='store_true')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("--outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("--region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    if args.test:
        print args.DSID

    analyze(args.input, args.weight, args.tree, args.DSID, args.isData, args.isSignal, args.outfile, args.test, args.region)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
