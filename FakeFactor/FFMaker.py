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
def FFCR(event, hc, CutsDict):
    if( CutsDict["1el"] and CutsDict["electronTriggers"] ):
        hc.fill(event, "all")
        if( CutsDict["idel"] ):
            hc.fill(event, "idel")
        if( CutsDict["antiidel"] ):
            hc.fill(event, "antiidel")
        if( CutsDict["100mt200"] ):
            hc.fill(event, "FFCR")
            return True
    else: return False
#======================================================================
def FFIDSR(event, hc, CutsDict):
    if( CutsDict["1el"] and ((CutsDict["HLT_e5"] and CutsDict["idel5"]) or (CutsDict["HLT_e10"] and CutsDict["idel10"]) or (CutsDict["HLT_e15"] and CutsDict["idel15"]) or (CutsDict["HLT_e20"] and CutsDict["idel20"])) ):
        hc.fill(event, "FFID")
        if( CutsDict["40mtID"] ):
            hc.fill(event, "FFIDSR")
    return True
#======================================================================
def FFAIDSR(event, hc, CutsDict):
    if( CutsDict["1el"] and ((CutsDict["HLT_e5"] and CutsDict["antiidel5"]) or (CutsDict["HLT_e10"] and CutsDict["antiidel10"]) or (CutsDict["HLT_e15"] and CutsDict["antiidel15"]) or (CutsDict["HLT_e20"] and CutsDict["antiidel20"])) ):
        hc.fill(event, "FFAID")
        if( CutsDict["40mtAID"] ):
            hc.fill(event, "FFAIDSR")
    return True
#======================================================================
def FFSR(event, hc, CutsDict):
    if( CutsDict["1el"] and CutsDict["electronTriggers"] and CutsDict["40mt"] ):
        hc.fill(event, "FFSR")
        if( CutsDict["HLT_e5"] and CutsDict["antiidel5"] ):
            hc.fill(event, "HLT_antiide5")
        if( CutsDict["HLT_e5"] and CutsDict["idel"] ):
            hc.fill(event, "HLT_e5_idel")
            if(CutsDict["idel5"] ):
                hc.fill(event, "HLT_e5_idel5")
        if( CutsDict["HLT_e10"] and CutsDict["antiidel10"] ):
            hc.fill(event, "HLT_antiide10")
        if( CutsDict["HLT_e10"] and CutsDict["idel"] ):
            hc.fill(event, "HLT_e10_idel")
            if(CutsDict["idel10"] ):
                hc.fill(event, "HLT_e10_idel10")
        if( CutsDict["HLT_e15"] and CutsDict["antiidel15"] ):
            hc.fill(event, "HLT_antiide15")
        if( CutsDict["HLT_e15"] and CutsDict["idel"] ):
            hc.fill(event, "HLT_e15_idel")
            if(CutsDict["idel15"] ):
                hc.fill(event, "HLT_e15_idel15")
        if( CutsDict["HLT_e20"] and CutsDict["antiidel20"] ):
            hc.fill(event, "HLT_antiide20")
        if( CutsDict["HLT_e20"] and CutsDict["idel"] ):
            hc.fill(event, "HLT_e20_idel")
            if(CutsDict["idel20"] ):
                hc.fill(event, "HLT_e20_idel20")

        return True
    else: return False
#======================================================================
#======================================================================
#
def analyze(infile, weightfile, tree, data, signal, outfile, debug, region):

    if debug: print "opening input file"

    f=ROOT.TFile(infile, "RO")
    fw=ROOT.TFile(weightfile, "RO")

    if debug: print f.GetName()

    #get sum of weights hist
    #if data: sumWhist = f.Get("weighted__AOD")
    #elif signal: sumWhist = f.Get("weighted__AOD")
    #else: sumWhist = fw.Get("weighted__AOD")
    #print sumWhist.GetName()

    t=f.Get("%s" %tree)

    if data:
        sumWhist = fw.Get("weighted__AOD")
    else:
        sumWhist = f.Get("weighted__AOD") 


    if debug: print t.GetName()


    #-------------------------
    #create output file
    #-------------------------


    if debug: print "opening output file"

    o=ROOT.TFile(outfile, "RECREATE")

    if debug: print "..making histograms collections"

    #CR=histcollection("FFCR", o, debug, data, tree, sumWhist, 0)
    #CR.addfakecollection("all")
    #CR.addfakecollection("idel")
    #CR.addfakecollection("antiidel")
    #CR.addfakecollection("FFCR")

    IDSR=histcollection("FFIDSR", o, debug, data, tree, sumWhist, 0)
    IDSR.addidcollection("FFID")
    IDSR.addidcollection("FFIDSR")

    AIDSR=histcollection("FFAIDSR", o, debug, data, tree, sumWhist, 0)
    AIDSR.addantiidcollection("FFAID")
    AIDSR.addantiidcollection("FFAIDSR")

    #SR=histcollection("FFSR", o, debug, data, tree, sumWhist, 0)
    #SR.addfakecollection("FFSR")
    #SR.addfakecollection("HLT_e5_idel")
    #SR.addfakecollection("HLT_e5_idel5")
    #SR.addfakecollection("HLT_e10_idel")
    #SR.addfakecollection("HLT_e10_idel10")
    #SR.addfakecollection("HLT_e15_idel")
    #SR.addfakecollection("HLT_e15_idel15")
    #SR.addfakecollection("HLT_e20_idel")
    #SR.addfakecollection("HLT_e20_idel20")
    #SR.addfakecollection("HLT_antiide5")
    #SR.addfakecollection("HLT_antiide10")
    #SR.addfakecollection("HLT_antiide15")
    #SR.addfakecollection("HLT_antiide20")

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
        cutdict = cuts(obs) 
        Cuts = cutdict.getCutsDict()


        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        if debug:
            if eventcount == 1: 
                if region == 'dilepton':
                    print 'Recalculating generator Weight!!'

        #------------------------------
        #trigger efficiency regions
        #------------------------------
        #FFCR(   obs,  CR,    Cuts) 
        FFIDSR( obs,  IDSR,  Cuts)
        FFAIDSR(obs,  AIDSR, Cuts)
        #FFSR(   obs,  SR,    Cuts) 


    if debug: print eventcount
    print "writing histograms for electron fake estimates" 

    #CR.write()
    IDSR.write()
    AIDSR.write()
    #SR.write()

    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("--input"      , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("--weight"      , action='store', default='', help='root file containing sum of weights hist')
    parser.add_argument("--tree"        , action='store', default='')
    parser.add_argument("--isData"      , action='store', default='')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("--outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("--region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    analyze(args.input, args.weight, args.tree, args.isData, args.isSignal, args.outfile, args.test, args.region)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
