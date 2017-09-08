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
def FFIDSR(event, hc, IDCuts, muList, Z0list, D0list, variation):
    nlep = len(muList)
    nlep_fill = 0
    nlepSR_fill = 0
    
    for CutsDict, mu, z0, d0 in zip(IDCuts, muList, Z0list, D0list):
        if(CutsDict["HLT_mu4"]):
            hc.fill(event, "HLTmu4", mu, z0, d0, variation)
        if(CutsDict["HLT_mu10"]):
            hc.fill(event, "HLTmu10", mu, z0, d0, variation)
        if(CutsDict["HLT_mu14"]):
            hc.fill(event, "HLTmu14", mu, z0, d0, variation)
        if(CutsDict["HLT_mu18"] ):
            hc.fill(event, "HLTmu18", mu, z0, d0, variation)
        if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
            #print "filling ID lep w/ Pt %f" % mu.Pt()
            nlep_fill += 1
            if( CutsDict["bveto"] ):
                hc.fill(event, "FFIDb0", mu, z0, d0, variation)
                if variation == 'mtUP':
                        nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb0", mu, z0, d0, variation)
                elif variation == 'mtDOWN':
                        nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb0", mu, z0, d0, variation)
                else:
                    if( CutsDict["40mt"] ):
                        nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb0", mu, z0, d0, variation)
            else: 
                hc.fill(event, "FFIDb1", mu, z0, d0, variation)
                if variation == 'mtUP':
                        nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb1", mu, z0, d0, variation)
                elif variation == 'mtDOWN':
                        nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb1", mu, z0, d0, variation)
                else:
                    if( CutsDict["40mt"] ):
                        nlepSR_fill += 1
                        hc.fill(event, "FFIDSRb1", mu, z0, d0, variation)
    #if len(muList):
    #    hc.fillN(event, "FFIDN", muList[0], nlep,variation)
    #    hc.fillN(event, "FFIDNfill", muList[0], nlep_fill,variation)
    #    hc.fillN(event, "FFIDSRNfill", muList[0], nlepSR_fill,variation)
    return True
#======================================================================
def FFAIDSR(event, hc, AIDCuts, muList, Z0list, D0list, variation):
    nlep = len(muList)
    nlep_fill = 0
    nlepSR_fill = 0
    for CutsDict, mu, z0, d0 in zip(AIDCuts, muList, Z0list, D0list):
        if(CutsDict["HLT_mu4"]):
            hc.fill(event, "HLTmu4", mu, z0, d0,variation)
        if(CutsDict["HLT_mu10"]):
            hc.fill(event, "HLTmu10", mu, z0, d0,variation)
        if(CutsDict["HLT_mu14"]):
            hc.fill(event, "HLTmu14", mu, z0, d0,variation)
        if(CutsDict["HLT_mu18"]):
            hc.fill(event, "HLTmu18", mu, z0, d0,variation)
        if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
            #print "filling Anti ID lep w/ Pt %f" % mu.Pt()
            #print "HLT_mu4 %s" % CutsDict["HLT_mu4"]
            #print "HLT_mu10 %s" % CutsDict["HLT_mu10"]
            #print "HLT_mu14 %s" % CutsDict["HLT_mu14"]
            #print "HLT_mu18 %s" % CutsDict["HLT_mu18"]
            nlep_fill += 1
            if( CutsDict["bveto"] ):
                hc.fill(event, "FFAIDb0", mu, z0, d0,variation)
                if variation == 'mtUP':
                    if( CutsDict["50mt"] ):
                        nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb0", mu, z0, d0,variation)
                elif variation == 'mtDOWN':
                    if( CutsDict["30mt"] ):
                        nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb0", mu, z0, d0,variation)
                else:
                    if( CutsDict["40mt"] ):
                        nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb0", mu, z0, d0,variation)
            else:
                hc.fill(event, "FFAIDb1", mu, z0, d0,variation)
                if variation == 'mtUP':
                    if( CutsDict["50mt"] ):
                        nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb1", mu, z0, d0,variation)
                elif variation == 'mtDOWN':
                    if( CutsDict["30mt"] ):
                        nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb1", mu, z0, d0,variation)
                else:
                    if( CutsDict["40mt"] ):
                        nlepSR_fill += 1
                        hc.fill(event, "FFAIDSRb1", mu, z0, d0,variation)

        #else:
            #print "not filling Anti ID lep w/ Pt %f" % mu.Pt()
            #print "HLT_mu4 %s" % CutsDict["HLT_mu4"]
            #print "HLT_mu10 %s" % CutsDict["HLT_mu10"]
            #print "HLT_mu14 %s" % CutsDict["HLT_mu14"]
            #print "HLT_mu18 %s" % CutsDict["HLT_mu18"]
    #if len(muList):
    #    hc.fillN(event, "FFAIDN", muList[0], nlep,variation)
    #    hc.fillN(event, "FFAIDNfill", muList[0], nlep_fill,variation)
    #    hc.fillN(event, "FFAIDSRNfill", muList[0], nlepSR_fill,variation)
    return True
#======================================================================
def FFIDSR2D(event, hc, IDCuts, muList, Z0list, D0list, variation):
    for CutsDict, mu, z0, d0 in zip(IDCuts, muList, Z0list, D0list):
        if( CutsDict["muEta07"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFIDEta07b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta07b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta07b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta07b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFIDEta07b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta07b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta07b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta07b1", mu, z0, d0, variation)
        elif( CutsDict["muEta137"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFIDEta137b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta137b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta137b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta137b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFIDEta137b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta137b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta137b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta137b1", mu, z0, d0, variation)
        elif( CutsDict["muEta152"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFIDEta152b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta152b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta152b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta152b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFIDEta152b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta152b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta152b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta152b1", mu, z0, d0, variation)
        elif( CutsDict["muEta201"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFIDEta201b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta201b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta201b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta201b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFIDEta201b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta201b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta201b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta201b1", mu, z0, d0, variation)
        elif( CutsDict["muEta247"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFIDEta247b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta247b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta247b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta247b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFIDEta247b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFIDSREta247b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFIDSREta247b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFIDSREta247b1", mu, z0, d0, variation)
    return True
#======================================================================
def FFAIDSR2D(event, hc, AIDCuts, muList, Z0list, D0list, variation):
    for CutsDict, mu, z0, d0 in zip(AIDCuts, muList, Z0list, D0list):
        if( CutsDict["muEta07"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFAIDEta07b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta07b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta07b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta07b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFAIDEta07b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta07b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta07b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta07b1", mu, z0, d0, variation)
        elif( CutsDict["muEta137"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFAIDEta137b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta137b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta137b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta137b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFAIDEta137b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta137b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta137b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta137b1", mu, z0, d0, variation)
        elif( CutsDict["muEta152"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFAIDEta152b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta152b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta152b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta152b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFAIDEta152b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta152b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta152b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta152b1", mu, z0, d0, variation)
        elif( CutsDict["muEta201"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFAIDEta201b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta201b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta201b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta201b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFAIDEta201b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta201b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta201b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta201b1", mu, z0, d0, variation)
        elif( CutsDict["muEta247"] ):
            if( ((CutsDict["HLT_mu4"] and CutsDict["mu5"]) or (CutsDict["HLT_mu10"] and CutsDict["mu10"]) or (CutsDict["HLT_mu14"] and CutsDict["mu15"]) or (CutsDict["HLT_mu18"] and CutsDict["mu20"])) ):
                if( CutsDict["bveto"] ):
                    hc.fill(event, "FFAIDEta247b0", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta247b0", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta247b0", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta247b0", mu, z0, d0, variation)
                else:
                    hc.fill(event, "FFAIDEta247b1", mu, z0, d0, variation)
                    if variation == 'mtUP':
                        if( CutsDict["50mt"] ):
                            hc.fill(event, "FFAIDSREta247b1", mu, z0, d0, variation)
                    elif variation == 'mtDOWN':
                        if( CutsDict["30mt"] ):
                            hc.fill(event, "FFAIDSREta247b1", mu, z0, d0, variation)
                    else:
                        if( CutsDict["40mt"] ):
                            hc.fill(event, "FFAIDSREta247b1", mu, z0, d0, variation)
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
    IDSR.addidcollection("FFIDb0")
    IDSR.addidcollection("FFIDSRb0")
    IDSR.addidcollection("FFIDb1")
    IDSR.addidcollection("FFIDSRb1")
    IDSR.addidcollection("HLTmu4")
    IDSR.addidcollection("HLTmu10")
    IDSR.addidcollection("HLTmu14")
    IDSR.addidcollection("HLTmu18")

    AIDSR=histcollection("FFAIDSR", o, 0, data, tree, 0)
    AIDSR.addfakecollection("FFAIDN")
    AIDSR.addfakecollection("FFAIDNfill")
    AIDSR.addfakecollection("FFAIDSRNfill")
    AIDSR.addantiidcollection("FFAIDb0")
    AIDSR.addantiidcollection("FFAIDSRb0")
    AIDSR.addantiidcollection("FFAIDb1")
    AIDSR.addantiidcollection("FFAIDSRb1")
    AIDSR.addantiidcollection("HLTmu4")
    AIDSR.addantiidcollection("HLTmu10")
    AIDSR.addantiidcollection("HLTmu14")
    AIDSR.addantiidcollection("HLTmu18")

    IDSR2D=histcollection("FFIDSR2D", o, 0, data, tree, 0)
    IDSR2D.addidcollection("FFIDEta07b0")
    IDSR2D.addidcollection("FFIDSREta07b0")
    IDSR2D.addidcollection("FFIDEta137b0")
    IDSR2D.addidcollection("FFIDSREta137b0")
    IDSR2D.addidcollection("FFIDEta152b0")
    IDSR2D.addidcollection("FFIDSREta152b0")
    IDSR2D.addidcollection("FFIDEta201b0")
    IDSR2D.addidcollection("FFIDSREta201b0")
    IDSR2D.addidcollection("FFIDEta247b0")
    IDSR2D.addidcollection("FFIDSREta247b0")
    IDSR2D.addidcollection("FFIDEta07b1")
    IDSR2D.addidcollection("FFIDSREta07b1")
    IDSR2D.addidcollection("FFIDEta137b1")
    IDSR2D.addidcollection("FFIDSREta137b1")
    IDSR2D.addidcollection("FFIDEta152b1")
    IDSR2D.addidcollection("FFIDSREta152b1")
    IDSR2D.addidcollection("FFIDEta201b1")
    IDSR2D.addidcollection("FFIDSREta201b1")
    IDSR2D.addidcollection("FFIDEta247b1")
    IDSR2D.addidcollection("FFIDSREta247b1")

    AIDSR2D=histcollection("FFAIDSR2D", o, 0, data, tree, 0)
    AIDSR2D.addantiidcollection("FFAIDEta07b0")
    AIDSR2D.addantiidcollection("FFAIDSREta07b0")
    AIDSR2D.addantiidcollection("FFAIDEta137b0")
    AIDSR2D.addantiidcollection("FFAIDSREta137b0")
    AIDSR2D.addantiidcollection("FFAIDEta152b0")
    AIDSR2D.addantiidcollection("FFAIDSREta152b0")
    AIDSR2D.addantiidcollection("FFAIDEta201b0")
    AIDSR2D.addantiidcollection("FFAIDSREta201b0")
    AIDSR2D.addantiidcollection("FFAIDEta247b0")
    AIDSR2D.addantiidcollection("FFAIDSREta247b0")
    AIDSR2D.addantiidcollection("FFAIDEta07b1")
    AIDSR2D.addantiidcollection("FFAIDSREta07b1")
    AIDSR2D.addantiidcollection("FFAIDEta137b1")
    AIDSR2D.addantiidcollection("FFAIDSREta137b1")
    AIDSR2D.addantiidcollection("FFAIDEta152b1")
    AIDSR2D.addantiidcollection("FFAIDSREta152b1")
    AIDSR2D.addantiidcollection("FFAIDEta201b1")
    AIDSR2D.addantiidcollection("FFAIDSREta201b1")
    AIDSR2D.addantiidcollection("FFAIDEta247b1")
    AIDSR2D.addantiidcollection("FFAIDSREta247b1")

    AID1=histcollection("AID1", o, 0, data, tree, 0)
    AID1.addfakecollection("FFAIDN")
    AID1.addfakecollection("FFAIDNfill")
    AID1.addfakecollection("FFAIDSRNfill")
    AID1.addantiidcollection("FFAIDb0")
    AID1.addantiidcollection("FFAIDSRb0")
    AID1.addantiidcollection("FFAIDb1")
    AID1.addantiidcollection("FFAIDSRb1")
    AID1.addantiidcollection("HLTmu4")
    AID1.addantiidcollection("HLTmu10")
    AID1.addantiidcollection("HLTmu14")
    AID1.addantiidcollection("HLTmu18")

    AID2=histcollection("AID2", o, 0, data, tree, 0)
    AID2.addfakecollection("FFAIDN")
    AID2.addfakecollection("FFAIDNfill")
    AID2.addfakecollection("FFAIDSRNfill")
    AID2.addantiidcollection("FFAIDb0")
    AID2.addantiidcollection("FFAIDSRb0")
    AID2.addantiidcollection("FFAIDb1")
    AID2.addantiidcollection("FFAIDSRb1")
    AID2.addantiidcollection("HLTmu4")
    AID2.addantiidcollection("HLTmu10")
    AID2.addantiidcollection("HLTmu14")
    AID2.addantiidcollection("HLTmu18")

    AID12=histcollection("AID12", o, 0, data, tree, 0)
    AID12.addfakecollection("FFAIDN")
    AID12.addfakecollection("FFAIDNfill")
    AID12.addfakecollection("FFAIDSRNfill")
    AID12.addantiidcollection("FFAIDb0")
    AID12.addantiidcollection("FFAIDSRb0")
    AID12.addantiidcollection("FFAIDb1")
    AID12.addantiidcollection("FFAIDSRb1")
    AID12.addantiidcollection("HLTmu4")
    AID12.addantiidcollection("HLTmu10")
    AID12.addantiidcollection("HLTmu14")
    AID12.addantiidcollection("HLTmu18")

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
        #AIDmuonlist, AIDmuonZ0sinT, AIDmuonD0sig = obs.getAntiIDmuons(sigMuList, variation, debug)
        AIDmuonlist, AIDmuonZ0sinT, AIDmuonD0sig = obs.getAntiIDmuons(variation, debug)
        failISO_muonlist, failISO_muonZ0sinT, failISO_muonD0sig = obs.getAntiIDMuons1(variation, debug)
        failD0_muonlist, failD0_muonZ0sinT, failD0_muonD0sig = obs.getAntiIDMuons2(variation, debug)
        failISO_D0_muonlist, failISO_D0_muonZ0sinT, failISO_D0_muonD0sig = obs.getAntiIDMuons12(variation, debug)
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
        FFIDSR( obs,    IDSR,     IDCuts,         IDmuonlist, IDmuonZ0sinT, IDmuonD0sig, variation)
        if debug: print "FILLING ALL AID"
        FFAIDSR(obs,    AIDSR,    AIDCuts,        AIDmuonlist, AIDmuonZ0sinT, AIDmuonD0sig, variation)
        FFIDSR2D( obs,  IDSR2D,   IDCuts,         IDmuonlist, IDmuonZ0sinT, IDmuonD0sig, variation)
        FFAIDSR2D(obs,  AIDSR2D,  AIDCuts,        AIDmuonlist, AIDmuonZ0sinT, AIDmuonD0sig, variation)
        if debug: print "FILLING AID 1"
        FFAIDSR(obs,    AID1,     failISOCuts,    failISO_muonlist, failISO_muonZ0sinT, failISO_muonD0sig, variation)
        if debug: print "FILLING AID 2"
        FFAIDSR(obs,    AID2,     failD0Cuts,     failD0_muonlist, failD0_muonZ0sinT, failD0_muonD0sig, variation)
        if debug: print "FILLING AID 12"
        FFAIDSR(obs,    AID12,    failISO_D0Cuts, failISO_D0_muonlist, failISO_D0_muonZ0sinT, failISO_D0_muonD0sig, variation)


    print '%i total events' % eventcount
    print "writing histograms for muon fake estimates" 

    IDSR.write()
    AIDSR.write()
    IDSR2D.write()
    AIDSR2D.write()
    AID1.write()
    AID2.write()
    AID12.write()

    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("-input"       , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("-variation"   , action='store', default='', help='set for a systematic varaiation')
    parser.add_argument("-tree"        , action='store', default='')
    parser.add_argument("-isData"      , action='store', default='')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("-outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("-region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    analyze(args.input,  args.tree, args.isData, args.isSignal, args.outfile, args.test, args.region, args.variation)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
