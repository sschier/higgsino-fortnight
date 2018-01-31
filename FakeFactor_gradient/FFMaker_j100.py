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


########################################################################################
#These function makes sure active trigger corresponds to proper electron pt bin, 
#FF prompt background normalization region cuts
#FF meaasurement region cuts and fills histograms along the way
########################################################################################


########################################################################################
#ID electron histogrms
########################################################################################
#======================================================================
def FFIDSR(event, hc, IDCuts, elList, Z0list, D0list, SYSvariation):
    for CutsDict, el, z0, d0 in zip(IDCuts, elList, Z0list, D0list):
        if( ((CutsDict["HLT_e5"] and CutsDict["el5"]) or (CutsDict["HLT_e10"] and CutsDict["el10"]) or (CutsDict["HLT_e15"] and CutsDict["el15"]) or (CutsDict["HLT_e20"] and CutsDict["el20"])) and CutsDict["j100"] ):
            hc.fill(event, "FFID", el, z0, d0, SYSvariation)
            if( CutsDict["met200"] ):
                hc.fill(event, "FFIDCRmet", el, z0, d0, SYSvariation)
            if( CutsDict["100mt200"] ):
                hc.fill(event, "FFIDCRmt", el, z0, d0, SYSvariation)
            if SYSvariation == 'mtUP':
                if( CutsDict["50mt"] ):
                    hc.fill(event, "FFIDSR", el, z0, d0, SYSvariation)
            elif SYSvariation == 'mtDOWN':
                if( CutsDict["30mt"] ):
                    hc.fill(event, "FFIDSR", el, z0, d0, SYSvariation)
            else:
                if( CutsDict["40mt"] ):
                    hc.fill(event, "FFIDSR", el, z0, d0, SYSvariation)
    return True


########################################################################################
#anti-ID electron histogrms
########################################################################################
#======================================================================
def FFAIDSR(event, hc, AIDCuts, elList, Z0list, D0list, SYSvariation):
    for CutsDict, el, z0, d0 in zip(AIDCuts, elList, Z0list, D0list):
        if( ((CutsDict["HLT_e5"] and CutsDict["el5"]) or (CutsDict["HLT_e10"] and CutsDict["el10"]) or (CutsDict["HLT_e15"] and CutsDict["el15"]) or (CutsDict["HLT_e20"] and CutsDict["el20"])) and CutsDict["j100"] ):
            hc.fill(event, "FFAID", el, z0, d0, SYSvariation)
            if( CutsDict["met200"] ):
                hc.fill(event, "FFAIDCRmet", el, z0, d0, SYSvariation)
            if( CutsDict["100mt200"] ):
                hc.fill(event, "FFAIDCRmt", el, z0, d0, SYSvariation)
            if SYSvariation == 'mtUP':
                if( CutsDict["50mt"] ):
                    hc.fill(event, "FFAIDSR", el, z0, d0, SYSvariation)
            elif SYSvariation == 'mtDOWN':
                if( CutsDict["30mt"] ):
                    hc.fill(event, "FFAIDSR", el, z0, d0, SYSvariation)
            else:
                if( CutsDict["40mt"] ):
                    hc.fill(event, "FFAIDSR", el, z0, d0, SYSvariation)
    return True
#======================================================================
#
def analyze(infile, tree, data, signal, outfile, debug, region, SYSvariation, AIDvariation):

    if debug: print "opening input file"

    f=ROOT.TFile(infile, "RO")
    t=f.Get("%s" %tree)

    if debug: 
        print 'running over file %s' % f.GetName()
        print 'getting events in %s' % t.GetName()

    ########################################################################################
    #create output file
    ########################################################################################

    if debug: print "opening output file"

    o=ROOT.TFile(outfile, "RECREATE")

    if debug: print "..making histograms collections"

    ########################################################################################
    #Add "FF Signal" and "FF Control" regions histogram collections
    ########################################################################################
    IDSR=histcollection("FFIDSR", o, 0, data, tree, 0)
    IDSR.addidcollection("FFID")
    IDSR.addidcollection("FFIDCRmet")
    IDSR.addidcollection("FFIDCRmt")
    IDSR.addidcollection("FFIDSR")

    AIDSR=histcollection("FFAIDSR", o, 0, data, tree, 0)
    AIDSR.addantiidcollection("FFAID")
    AIDSR.addantiidcollection("FFAIDCRmet")
    AIDSR.addantiidcollection("FFAIDCRmt")
    AIDSR.addantiidcollection("FFAIDSR")


    ########################################################################################
    #These hist collections are for making decomposition plots: 
    #1, 2, 3, 12, 13, 23, 123 correspond to "fail cut" combinations
    # 1 = fail ID, 2 = fail ISO, 3 = fail D0
    ########################################################################################
    AID1=histcollection("AID1", o, 0, data, tree, 0)
    AID1.addantiidcollection("FFAID")
    AID1.addantiidcollection("FFAIDCRmet")
    AID1.addantiidcollection("FFAIDCRmt")
    AID1.addantiidcollection("FFAIDSR")

    AID2=histcollection("AID2", o, 0, data, tree, 0)
    AID2.addantiidcollection("FFAID")
    AID2.addantiidcollection("FFAIDCRmet")
    AID2.addantiidcollection("FFAIDCRmt")
    AID2.addantiidcollection("FFAIDSR")

    AID3=histcollection("AID3", o, 0, data, tree, 0)
    AID3.addantiidcollection("FFAID")
    AID3.addantiidcollection("FFAIDCRmet")
    AID3.addantiidcollection("FFAIDCRmt")
    AID3.addantiidcollection("FFAIDSR")

    AID13=histcollection("AID13", o, 0, data, tree, 0)
    AID13.addantiidcollection("FFAID")
    AID13.addantiidcollection("FFAIDCRmet")
    AID13.addantiidcollection("FFAIDCRmt")
    AID13.addantiidcollection("FFAIDSR")

    AID12=histcollection("AID12", o, 0, data, tree, 0)
    AID12.addantiidcollection("FFAID")
    AID12.addantiidcollection("FFAIDCRmet")
    AID12.addantiidcollection("FFAIDCRmt")
    AID12.addantiidcollection("FFAIDSR")

    AID23=histcollection("AID23", o, 0, data, tree, 0)
    AID23.addantiidcollection("FFAID")
    AID23.addantiidcollection("FFAIDCRmet")
    AID23.addantiidcollection("FFAIDCRmt")
    AID23.addantiidcollection("FFAIDSR")

    AID123=histcollection("AID123", o, 0, data, tree, 0)
    AID123.addantiidcollection("FFAID")
    AID123.addantiidcollection("FFAIDCRmet")
    AID123.addantiidcollection("FFAIDCRmt")
    AID123.addantiidcollection("FFAIDSR")

    eventcount = 0

    ########################################################################################
    #loop over events
    ########################################################################################

    if debug: print "looping over events"

    for event in t:
        ########################################################################################
        #bookkeep events
        ########################################################################################

        eventcount +=1
        if debug:
            print '*************************************************'
            print "event %i" % eventcount


        #######################################################################################
        #Here is the handle for the event variables
        #######################################################################################
        obs = observable(event, data)

        #######################################################################################
        # obs.getIDelectrons() returns 3 lists: list of (pt,et,phi) vectors, list z0SinTheta vaalues, list of d0 significance values
        #######################################################################################
        IDelectronlist,           IDelectronZ0sinT,           IDelectronD0sig = obs.getIDelectrons()
        AIDelectronlist,          AIDelectronZ0sinT,          AIDelectronD0sig = obs.getAntiIDelectrons(AIDvariation)
        failID_electronlist,      failID_electronZ0sinT,      failID_electronD0sig = obs.getAntiIDelectrons1(AIDvariation)
        failISO_electronlist,     failISO_electronZ0sinT,     failISO_electronD0sig = obs.getAntiIDelectrons2(AIDvariation)
        failD0_electronlist,      failD0_electronZ0sinT,      failD0_electronD0sig = obs.getAntiIDelectrons3(AIDvariation)
        failID_ISO_electronlist,  failID_ISO_electronZ0sinT,  failID_ISO_electronD0sig = obs.getAntiIDelectrons12(AIDvariation)
        failID_D0_electronlist,   failID_D0_electronZ0sinT,   failID_D0_electronD0sig = obs.getAntiIDelectrons13(AIDvariation)
        failISO_D0_electronlist,  failISO_D0_electronZ0sinT,  failISO_D0_electronD0sig = obs.getAntiIDelectrons23(AIDvariation)
        failAll_electronlist,     failAll_electronZ0sinT,      failAll_electronD0sig = obs.getAntiIDelectrons123(AIDvariation)
        
        if debug:
            print 'AID: %i' % len(AIDelectronlist)
            print 'fail ID: %i' % len(failID_electronlist)
            print 'fail ISO: %i' % len(failISO_electronlist)
            print 'fail D0: %i' % len(failD0_electronlist)
            print 'fail ID ISO: %i' % len(failID_ISO_electronlist)
            print 'fail ID D0: %i' % len(failID_D0_electronlist)
            print 'fail ISO D0: %i' % len(failISO_D0_electronlist)
            print 'fail All: %i' % len(failAll_electronlist)

        #######################################################################################
        #Here you create your cuts dictionary class
        #######################################################################################
        cutdict = cuts(obs) 

        
        #######################################################################################
        #Each instance of getCuts(list) recieves a list of (pt,eta,phi) vectors corresponding 
        #to the electrons you want to use and returns a list of cuts dictionaries 
        #######################################################################################
        IDCuts = cutdict.getCuts(IDelectronlist)
        AIDCuts = cutdict.getCuts(AIDelectronlist)
        failIDCuts = cutdict.getCuts(failID_electronlist)
        failISOCuts = cutdict.getCuts(failISO_electronlist)
        failD0Cuts = cutdict.getCuts(failD0_electronlist)
        failID_ISOCuts = cutdict.getCuts(failID_ISO_electronlist)
        failID_D0Cuts = cutdict.getCuts(failID_D0_electronlist)
        failISO_D0Cuts = cutdict.getCuts(failISO_D0_electronlist)
        failAllCuts = cutdict.getCuts(failAll_electronlist)

        #######################################################################################
        #create triggers dictionary to keep up with which triggers fired per event
        #######################################################################################
        triggers = {}
        HLT_e5, HLT_e10, HLT_e15, HLT_e20 = obs.getTriggers()
        triggers['HLT_e5'] = HLT_e5
        triggers['HLT_e10'] = HLT_e10
        triggers['HLT_e15'] = HLT_e15
        triggers['HLT_e20'] = HLT_e20

        if debug:
            print triggers

        #######################################################################################
        #print out event status
        #######################################################################################
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        if debug:
            if eventcount == 1: 
                if region == 'dilepton':
                    print 'Recalculating generator Weight!!'

        #######################################################################################
        #Select ff ID or AID signal region and fill histograms
        #######################################################################################
        FFIDSR(obs,   IDSR,   IDCuts,         IDelectronlist,          IDelectronZ0sinT,          IDelectronD0sig, SYSvariation)
        FFAIDSR(obs,  AIDSR,  AIDCuts,        AIDelectronlist,         AIDelectronZ0sinT,         AIDelectronD0sig, SYSvariation)
        FFAIDSR(obs,  AID1,   failIDCuts,     failID_electronlist,     failID_electronZ0sinT,     failID_electronD0sig, SYSvariation)
        FFAIDSR(obs,  AID2,   failISOCuts,    failISO_electronlist,    failISO_electronZ0sinT,    failISO_electronD0sig, SYSvariation)
        FFAIDSR(obs,  AID3,   failD0Cuts,     failD0_electronlist,     failD0_electronZ0sinT,     failD0_electronD0sig, SYSvariation)
        FFAIDSR(obs,  AID13,  failID_D0Cuts,  failID_D0_electronlist,  failID_D0_electronZ0sinT,  failID_D0_electronD0sig, SYSvariation)
        FFAIDSR(obs,  AID12,  failID_ISOCuts, failID_ISO_electronlist, failID_ISO_electronZ0sinT, failID_ISO_electronD0sig, SYSvariation)
        FFAIDSR(obs,  AID23,  failISO_D0Cuts, failISO_D0_electronlist, failISO_D0_electronZ0sinT, failISO_D0_electronD0sig, SYSvariation)
        FFAIDSR(obs,  AID123, failAllCuts,    failAll_electronlist,    failAll_electronZ0sinT,    failAll_electronD0sig, SYSvariation)


    print '%i total events' % eventcount
    print "writing histograms for electron fake estimates" 

    #######################################################################################
    #Write histograms
    #######################################################################################
    IDSR.write()
    AIDSR.write()
    AID1.write() 
    AID2.write()
    AID3.write()
    AID13.write() 
    AID12.write()
    AID23.write()
    AID123.write()



    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("-input"      , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("-SYSvariation"   , action='store', default='', help='set for a systematic varaiation')
    parser.add_argument("-AIDvariation"   , action='store', default='', help='set for a anti-ID definition varaiation')
    parser.add_argument("-tree"        , action='store', default='')
    parser.add_argument("-isData"      , action='store', default='')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("-outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("-region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    analyze(args.input,  args.tree, args.isData, args.isSignal, args.outfile, args.test, args.region, args.SYSvariation, args.AIDvariation)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
