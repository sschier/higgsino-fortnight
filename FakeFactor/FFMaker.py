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
        if( CutsDict["40mt"] ):
            hc.fill(event, "FFIDSR")
    return True
#======================================================================
def FFAIDSR(event, hc, CutsDict):
    if( CutsDict["1el"] and ((CutsDict["HLT_e5"] and CutsDict["antiidel5"]) or (CutsDict["HLT_e10"] and CutsDict["antiidel10"]) or (CutsDict["HLT_e15"] and CutsDict["antiidel15"]) or (CutsDict["HLT_e20"] and CutsDict["antiidel20"])) ):
        hc.fill(event, "FFAID")
        if( CutsDict["40mt"] ):
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

    CR=histcollection("FFCR", o, debug, data, tree, DSID, sumWhist, 0)
    CR.addfakecollection("all")
    CR.addfakecollection("idel")
    CR.addfakecollection("antiidel")
    CR.addfakecollection("FFCR")

    IDSR=histcollection("FFIDSR", o, debug, data, tree, DSID, sumWhist, 0)
    IDSR.addfakecollection("FFID")
    IDSR.addidcollection("FFIDSR")

    AIDSR=histcollection("FFAIDSR", o, debug, data, tree, DSID, sumWhist, 0)
    AIDSR.addfakecollection("FFAID")
    AIDSR.addantiidcollection("FFAIDSR")

    SR=histcollection("FFSR", o, debug, data, tree, DSID, sumWhist, 0)
    SR.addfakecollection("FFSR")
    SR.addfakecollection("HLT_e5_idel")
    SR.addfakecollection("HLT_e5_idel5")
    SR.addfakecollection("HLT_e10_idel")
    SR.addfakecollection("HLT_e10_idel10")
    SR.addfakecollection("HLT_e15_idel")
    SR.addfakecollection("HLT_e15_idel15")
    SR.addfakecollection("HLT_e20_idel")
    SR.addfakecollection("HLT_e20_idel20")
    SR.addfakecollection("HLT_antiide5")
    SR.addfakecollection("HLT_antiide10")
    SR.addfakecollection("HLT_antiide15")
    SR.addfakecollection("HLT_antiide20")

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

        #obs = observable(event)
        #met2 = obs.getMET()/1000.
        #print met2
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
        AntiIDel2_pt = -99.
        baseel_pt = event.baseel_pt[0]/1000.
        baseel_d0sig = event.baseel_d0sig
        baseel_z0sinTheta = event.baseel_z0sinTheta
        baseel_eta = event.baseel_eta
        baseel_isoTight = event.baseel_isoTight
        baseel_idTight = event.baseel_idTight
        n_baseel = event.n_baseel

        #print n_baseel
        for x in xrange(n_baseel):
            #if( (baseel_idTight[x] == 0 and baseel_isoTight[x]) or (baseel_isoTight[x] == 0 and baseel_idTight[x]) ):
            if( baseel_idTight[x] == 0 or baseel_isoTight[x] == 0 ):
                #print "have antiID on %s" % x
                AntiIDel_pt = event.baseel_pt[x]/1000.
                break
       # if( (baseel_idTight[0] == 0 and baseel_isoTight[0]) or (baseel_isoTight[0] == 0 and baseel_idTight[0]) ):
       #     AntiIDel_pt = baseel_pt
        if len(event.el_pt) > 0:
            IDel_pt = event.el_pt[0]/1000.

        #Make dictionary of cuts
        Cuts = {}

        if( n_baseel >= 1 ):
            Cuts["1el"] = True
        else: Cuts["1el"] = False

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

        if( AntiIDel_pt > 0. and AntiIDel_pt < 10 ):
            Cuts["antiidel5"] = True
        else: Cuts["antiidel5"] = False

        if( IDel_pt > 0. and IDel_pt < 10 ):
            Cuts["idel5"] = True
        else: Cuts["idel5"] = False

        if( AntiIDel_pt >= 10. and AntiIDel_pt < 15 ):
            Cuts["antiidel10"] = True
        else: Cuts["antiidel10"] = False

        if( IDel_pt >= 10. and IDel_pt < 15 ):
            Cuts["idel10"] = True
        else: Cuts["idel10"] = False

        if( AntiIDel_pt >= 15. and AntiIDel_pt < 20 ):
            Cuts["antiidel15"] = True
        else: Cuts["antiidel15"] = False

        if( IDel_pt >= 15. and IDel_pt < 20 ):
            Cuts["idel15"] = True
        else: Cuts["idel15"] = False

        if( AntiIDel_pt >= 20. ):
            Cuts["antiidel20"] = True
        else: Cuts["antiidel20"] = False

        if( IDel_pt >= 20. ):
            Cuts["idel20"] = True
        else: Cuts["idel20"] = False

        if( IDel_pt > 0. ):
            Cuts["idel"] = True
        else: Cuts["idel"] = False

        if( AntiIDel_pt > 0. ):
            Cuts["antiidel"] = True
        else: Cuts["antiidel"] = False


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
        FFIDSR( event,  IDSR,  Cuts)
        FFAIDSR(event,  AIDSR, Cuts)
        FFSR(   event,  SR,    Cuts) 


    if debug: print eventcount
    print "writing histograms for electron fake estimates" 

    CR.write()
    IDSR.write()
    AIDSR.write()
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
