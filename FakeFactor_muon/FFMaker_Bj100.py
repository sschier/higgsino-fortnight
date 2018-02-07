#!/usr/bin/env python
#Author: Sheena C Schier
#Created 10May2017 Created to calculate muectron fake factors
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
def FFIDSR(event, hc, IDCuts, muList, Z0list, D0list, SYSvariation):
    #nlep = len(muList)
    #nlep_fill = 0
    #nlepSR_fill = 0
    
    for CutsDict, mu, z0, d0 in zip(IDCuts, muList, Z0list, D0list):
        #if(CutsDict["HLT_mu4"]):
        #    hc.fill(event, "HLTmu4", mu, z0, d0, SYSvariation)
        #if(CutsDict["HLT_mu10"]):
        #    hc.fill(event, "HLTmu10", mu, z0, d0, SYSvariation)
        #if(CutsDict["HLT_mu14"]):
        #    hc.fill(event, "HLTmu14", mu, z0, d0, SYSvariation)
        #if(CutsDict["HLT_mu18"] ):
        #    hc.fill(event, "HLTmu18", mu, z0, d0, SYSvariation)
        if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) and CutsDict["j100"] ):
            #print "filling ID lep w/ Pt %f" % mu.Pt()
            #nlep_fill += 1
            if( CutsDict["bveto"] ):
                hc.fill(event, "FFIDb0", mu, z0, d0, SYSvariation)
                if( CutsDict["met200"] ):
                    hc.fill(event, "FFIDCRmetb0", mu, z0, d0, SYSvariation)
                if( CutsDict["100mt200"] ):
                    hc.fill(event, "FFIDCRmtb0", mu, z0, d0, SYSvariation)
                if SYSvariation == 'mtUP':
                    if( CutsDict["50mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb0", mu, z0, d0, SYSvariation)
                elif SYSvariation == 'mtDOWN':
                    if( CutsDict["30mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb0", mu, z0, d0, SYSvariation)
                elif SYSvariation == 'metSR':
                    if( CutsDict["80met"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb0", mu, z0, d0, SYSvariation)
                else:
                    if( CutsDict["40mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb0", mu, z0, d0, SYSvariation)
            else: 
                hc.fill(event, "FFIDb1", mu, z0, d0, SYSvariation)
                if( CutsDict["met200"] ):
                    hc.fill(event, "FFIDCRmetb1", mu, z0, d0, SYSvariation)
                if( CutsDict["100mt200"] ):
                    hc.fill(event, "FFIDCRmtb1", mu, z0, d0, SYSvariation)
                if SYSvariation == 'mtUP':
                    if( CutsDict["50mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb1", mu, z0, d0, SYSvariation)
                elif SYSvariation == 'mtDOWN':
                    if( CutsDict["30mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb1", mu, z0, d0, SYSvariation)
                elif SYSvariation == 'metSR':
                    if( CutsDict["80met"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb1", mu, z0, d0, SYSvariation)
                else:
                    if( CutsDict["40mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb1", mu, z0, d0, SYSvariation)
    #if len(muList):
    #    hc.fillN(event, "FFIDN", muList[0], nlep,SYSvariation)
    #    hc.fillN(event, "FFIDNfill", muList[0], nlep_fill,SYSvariation)
    #    hc.fillN(event, "FFIDSRNfill", muList[0], nlepSR_fill,SYSvariation)
    return True
#======================================================================
def FFAIDSR(event, hc, AIDCuts, muList, Z0list, D0list, SYSvariation):
    #nlep = len(muList)
    #nlep_fill = 0
    #nlepSR_fill = 0
    for CutsDict, mu, z0, d0 in zip(AIDCuts, muList, Z0list, D0list):
        #if(CutsDict["HLT_mu4"]):
        #    hc.fill(event, "HLTmu4", mu, z0, d0,SYSvariation)
        #if(CutsDict["HLT_mu10"]):
        #    hc.fill(event, "HLTmu10", mu, z0, d0,SYSvariation)
        #if(CutsDict["HLT_mu14"]):
        #    hc.fill(event, "HLTmu14", mu, z0, d0,SYSvariation)
        #if(CutsDict["HLT_mu18"]):
        #    hc.fill(event, "HLTmu18", mu, z0, d0,SYSvariation)
        if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) and CutsDict["j100"]):
            #print "filling Anti ID lep w/ Pt %f" % mu.Pt()
            #print "HLT_mu4 %s" % CutsDict["HLT_mu4"]
            #print "HLT_mu10 %s" % CutsDict["HLT_mu10"]
            #print "HLT_mu14 %s" % CutsDict["HLT_mu14"]
            #print "HLT_mu18 %s" % CutsDict["HLT_mu18"]
            #nlep_fill += 1
            if( CutsDict["bveto"] ):
                hc.fill(event, "FFAIDb0", mu, z0, d0,SYSvariation)
                if( CutsDict["met200"] ):
                    hc.fill(event, "FFAIDCRmetb0", mu, z0, d0, SYSvariation)
                if( CutsDict["100mt200"] ):
                    hc.fill(event, "FFAIDCRmtb0", mu, z0, d0, SYSvariation)
                if SYSvariation == 'mtUP':
                    if( CutsDict["50mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb0", mu, z0, d0,SYSvariation)
                elif SYSvariation == 'mtDOWN':
                    if( CutsDict["30mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb0", mu, z0, d0,SYSvariation)
                elif SYSvariation == 'metSR':
                    if( CutsDict["80met"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb0", mu, z0, d0,SYSvariation)
                else:
                    if( CutsDict["40mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb0", mu, z0, d0,SYSvariation)
            else:
                hc.fill(event, "FFAIDb1", mu, z0, d0,SYSvariation)
                if( CutsDict["met200"] ):
                    hc.fill(event, "FFAIDCRmetb1", mu, z0, d0, SYSvariation)
                if( CutsDict["100mt200"] ):
                    hc.fill(event, "FFAIDCRmtb1", mu, z0, d0, SYSvariation)
                if SYSvariation == 'mtUP':
                    if( CutsDict["50mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb1", mu, z0, d0,SYSvariation)
                elif SYSvariation == 'mtDOWN':
                    if( CutsDict["30mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb1", mu, z0, d0,SYSvariation)
                elif SYSvariation == 'metSR':
                    if( CutsDict["80met"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb1", mu, z0, d0,SYSvariation)
                else:
                    if( CutsDict["40mt"] ):
                        #nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb1", mu, z0, d0,SYSvariation)

        #else:
            #print "not filling Anti ID lep w/ Pt %f" % mu.Pt()
            #print "HLT_mu4 %s" % CutsDict["HLT_mu4"]
            #print "HLT_mu10 %s" % CutsDict["HLT_mu10"]
            #print "HLT_mu14 %s" % CutsDict["HLT_mu14"]
            #print "HLT_mu18 %s" % CutsDict["HLT_mu18"]
    #if len(muList):
    #    hc.fillN(event, "FFAIDN", muList[0], nlep,SYSvariation)
    #    hc.fillN(event, "FFAIDNfill", muList[0], nlep_fill,SYSvariation)
    #    hc.fillN(event, "FFAIDSRNfill", muList[0], nlepSR_fill,SYSvariation)
    return True
#======================================================================
#
def analyze(infile, tree, data, signal, outfile, debug, region, SYSvariation):

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
    #IDSR.addfakecollection("FFIDN")
    #IDSR.addfakecollection("FFIDNfill")
    #IDSR.addfakecollection("FFIDSRNfill")
    IDSR.addidcollection("FFIDb0")
    IDSR.addidcollection("FFIDCRmetb0")
    IDSR.addidcollection("FFIDCRmtb0")
    IDSR.addidcollection("FFIDSRb0")
    IDSR.addidcollection("FFIDb1")
    IDSR.addidcollection("FFIDCRmetb1")
    IDSR.addidcollection("FFIDCRmtb1")
    IDSR.addidcollection("FFIDSRb1")
    #IDSR.addidcollection("HLTmu4")
    #IDSR.addidcollection("HLTmu10")
    #IDSR.addidcollection("HLTmu14")
    #IDSR.addidcollection("HLTmu18")

    AIDSR=histcollection("FFAIDSR", o, 0, data, tree, 0)
    #AIDSR.addfakecollection("FFAIDN")
    #AIDSR.addfakecollection("FFAIDNfill")
    #AIDSR.addfakecollection("FFAIDSRNfill")
    AIDSR.addantiidcollection("FFAIDb0")
    AIDSR.addantiidcollection("FFAIDCRmetb0")
    AIDSR.addantiidcollection("FFAIDCRmtb0")
    AIDSR.addantiidcollection("FFAIDSRb0")
    AIDSR.addantiidcollection("FFAIDb1")
    AIDSR.addantiidcollection("FFAIDCRmetb1")
    AIDSR.addantiidcollection("FFAIDCRmtb1")
    AIDSR.addantiidcollection("FFAIDSRb1")
    #AIDSR.addantiidcollection("HLTmu4")
    #AIDSR.addantiidcollection("HLTmu10")
    #AIDSR.addantiidcollection("HLTmu14")
    #AIDSR.addantiidcollection("HLTmu18")


    AID1=histcollection("AID1", o, 0, data, tree, 0)
    AID1.addantiidcollection("FFAIDb0")
    AID1.addantiidcollection("FFAIDCRmetb0")
    AID1.addantiidcollection("FFAIDCRmtb0")
    AID1.addantiidcollection("FFAIDSRb0")
    AID1.addantiidcollection("FFAIDb1")
    AID1.addantiidcollection("FFAIDCRmetb1")
    AID1.addantiidcollection("FFAIDCRmtb1")
    AID1.addantiidcollection("FFAIDSRb1")

    AID2=histcollection("AID2", o, 0, data, tree, 0)
    AID2.addantiidcollection("FFAIDb0")
    AID2.addantiidcollection("FFAIDCRmetb0")
    AID2.addantiidcollection("FFAIDCRmtb0")
    AID2.addantiidcollection("FFAIDSRb0")
    AID2.addantiidcollection("FFAIDb1")
    AID2.addantiidcollection("FFAIDCRmetb1")
    AID2.addantiidcollection("FFAIDCRmtb1")
    AID2.addantiidcollection("FFAIDSRb1")

    AID12=histcollection("AID12", o, 0, data, tree, 0)
    AID12.addantiidcollection("FFAIDb0")
    AID12.addantiidcollection("FFAIDCRmetb0")
    AID12.addantiidcollection("FFAIDCRmtb0")
    AID12.addantiidcollection("FFAIDSRb0")
    AID12.addantiidcollection("FFAIDb1")
    AID12.addantiidcollection("FFAIDCRmetb1")
    AID12.addantiidcollection("FFAIDCRmtb1")
    AID12.addantiidcollection("FFAIDSRb1")

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
        sigMuList = obs.getMuVectors()
        IDmuonlist, IDmuonZ0sinT, IDmuonD0sig = obs.getSigMuons()
        #IDmuonlist, IDmuonZ0sinT, IDmuonD0sig = obs.getIDmuons()
        #AIDmuonlist, AIDmuonZ0sinT, AIDmuonD0sig = obs.getAntiIDmuons(sigMuList, SYSvariation, debug)
        AIDmuonlist, AIDmuonZ0sinT, AIDmuonD0sig = obs.getAntiIDmuons(debug)
        failISO_muonlist, failISO_muonZ0sinT, failISO_muonD0sig = obs.getAntiIDMuons1(debug)
        failD0_muonlist, failD0_muonZ0sinT, failD0_muonD0sig = obs.getAntiIDMuons2(debug)
        failISO_D0_muonlist, failISO_D0_muonZ0sinT, failISO_D0_muonD0sig = obs.getAntiIDMuons12(debug)
        if debug: 
            print '**** %i:%i ****' % (len(AIDmuonlist), (len(failISO_muonlist)+len(failD0_muonlist)+len(failISO_D0_muonlist))) 
            if len(AIDmuonlist) != (len(failISO_muonlist)+len(failD0_muonlist)+len(failISO_D0_muonlist)):
                print "BAAAAD"
                print 'AID: %i' % len(AIDmuonlist)
                if len(AIDmuonlist) > 1:
                    print AIDmuonlist[0].Eta(), AIDmuonlist[1].Eta()
                print 'failISO: %i' % len(failISO_muonlist)
                print failISO_muonlist
                print 'failD0: %i' % len(failD0_muonlist)
                print 'failISO_D0: %i' % len(failISO_D0_muonlist)

        cutdict = cuts(obs) 
        IDCuts = cutdict.getCuts(IDmuonlist)
        AIDCuts = cutdict.getCuts(AIDmuonlist)
        #print 'AID cuts:'
            
        failISOCuts = cutdict.getCuts(failISO_muonlist)
        failD0Cuts = cutdict.getCuts(failD0_muonlist)
        failISO_D0Cuts = cutdict.getCuts(failISO_D0_muonlist)

        triggers = {}
        HLT_mu4, HLT_mu10, HLT_mu14, HLT_mu18 = obs.getTriggers()
        triggers['HLT_mu4'] = HLT_mu4
        triggers['HLT_mu10'] = HLT_mu10
        triggers['HLT_mu14'] = HLT_mu14
        triggers['HLT_mu18'] = HLT_mu18

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
        FFIDSR( obs,    IDSR,     IDCuts,         IDmuonlist, IDmuonZ0sinT, IDmuonD0sig, SYSvariation)
        if debug: print "FILLING ALL AID"
        FFAIDSR(obs,    AIDSR,    AIDCuts,        AIDmuonlist, AIDmuonZ0sinT, AIDmuonD0sig, SYSvariation)
        if debug: print "FILLING AID 1"
        FFAIDSR(obs,    AID1,     failISOCuts,    failISO_muonlist, failISO_muonZ0sinT, failISO_muonD0sig, SYSvariation)
        if debug: print "FILLING AID 2"
        FFAIDSR(obs,    AID2,     failD0Cuts,     failD0_muonlist, failD0_muonZ0sinT, failD0_muonD0sig, SYSvariation)
        if debug: print "FILLING AID 12"
        FFAIDSR(obs,    AID12,    failISO_D0Cuts, failISO_D0_muonlist, failISO_D0_muonZ0sinT, failISO_D0_muonD0sig, SYSvariation)


    print '%i total events' % eventcount
    print "writing histograms for muon fake estimates" 

    IDSR.write()
    AIDSR.write()
    AID1.write()
    AID2.write()
    AID12.write()

    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("-input"       , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("-SYSvariation"   , action='store', default='', help='set for a systematic variation')
    parser.add_argument("-norm"        , action='store', default='Mt', help='set for a normalization var')
    parser.add_argument("-tree"        , action='store', default='')
    parser.add_argument("-isData"      , action='store', default='')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("-outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("-region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    analyze(args.input,  args.tree, args.isData, args.isSignal, args.outfile, args.test, args.region, args.SYSvariation)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
