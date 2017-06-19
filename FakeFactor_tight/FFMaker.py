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


#======================================================================
def FFIDSR(event, hc, IDCuts, elList):
    for CutsDict, el in zip(IDCuts, elList):
        if( ((CutsDict["HLT_e5"] and CutsDict["idel5"]) or (CutsDict["HLT_e10"] and CutsDict["idel10"]) or (CutsDict["HLT_e15"] and CutsDict["idel15"]) or (CutsDict["HLT_e20"] and CutsDict["idel20"])) ):
            hc.fill(event, "FFID", el)
            if( CutsDict["40mtID"] ):
                hc.fill(event, "FFIDSR", el)
    return True
#======================================================================
def FFAIDSR(event, hc, AIDCuts, elList):
    for CutsDict, el in zip(AIDCuts, elList):
        if( ((CutsDict["HLT_e5"] and CutsDict["antiidel5"]) or (CutsDict["HLT_e10"] and CutsDict["antiidel10"]) or (CutsDict["HLT_e15"] and CutsDict["antiidel15"]) or (CutsDict["HLT_e20"] and CutsDict["antiidel20"])) ):
            hc.fill(event, "FFAID", el)
            if( CutsDict["40mtAID"] ):
                hc.fill(event, "FFAIDSR", el)
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

    IDSR=histcollection("FFIDSR", o, 0, data, tree, 0)
    IDSR.addidcollection("FFID")
    IDSR.addidcollection("FFIDSR")

    AIDSR=histcollection("FFAIDSR", o, 0, data, tree, 0)
    AIDSR.addantiidcollection("FFAID")
    AIDSR.addantiidcollection("FFAIDSR")

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
        IDelectronlist = obs.getIDelectronList()
        AIDelectronlist = obs.getAntiIDelectronList()
        #if len(electronlist) >= 0 :
        #    print len(electronlist)
        #    for el in electronlist:
        #        print el.Pt()
        cutdict = cuts(obs) 
        IDCuts = cutdict.getIDCuts(IDelectronlist)
        AIDCuts = cutdict.getAIDCuts(AIDelectronlist)


        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        if debug:
            if eventcount == 1: 
                if region == 'dilepton':
                    print 'Recalculating generator Weight!!'

        #------------------------------
        #trigger efficiency regions
        #------------------------------
        FFIDSR( obs,  IDSR,  IDCuts, IDelectronlist)
        FFAIDSR(obs,  AIDSR, AIDCuts, AIDelectronlist)


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
