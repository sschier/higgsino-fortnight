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
#from Effhistograms import *
from observables import *
from renormalize import *


#======================================================================
def doSeqCutflow(CutsDict, CutflowDict_unweighted, CutflowDict_weighted, weight):
    
    if( CutsDict["363491"] == False ):
        return False

    if( CutsDict["2baseLep"] == False ):
        return False
    else:
        CutflowDict_unweighted["2baseLep"] += 1
        CutflowDict_weighted["2baseLep"] += 1.0*weight

    if( CutsDict["2sigLep"] == False ):
        return False
    else:
        CutflowDict_unweighted["2sigLep"] += 1
        CutflowDict_weighted["2sigLep"] += 1.0*weight

    if( CutsDict["SFOS"] == False ):
        return False
    else:
        CutflowDict_unweighted["SFOS"] += 1
        CutflowDict_weighted["SFOS"] += 1.0*weight

    if( CutsDict["lep1Pt50"] == False ):
        return False
    else:
        CutflowDict_unweighted["lep1Pt50"] += 1
        CutflowDict_weighted["lep1Pt50"] += 1.0*weight

    if( CutsDict["1sigJet"] == False ):
        return False
    else:
        CutflowDict_unweighted["1sigJet"] += 1
        CutflowDict_weighted["1sigJet"] += 1.0*weight

    if( CutsDict["jet1Pt150"] == False ):
        return False
    else:
        CutflowDict_unweighted["jet1Pt150"] += 1
        CutflowDict_weighted["jet1Pt150"] += 1.0*weight

    if( CutsDict["bVeto"] == False ):
        return False
    else:
        CutflowDict_unweighted["bVeto"] += 1
        CutflowDict_weighted["bVeto"] += 1.0*weight

    if( CutsDict["MET150"] == False ):
        return False
    else:
        CutflowDict_unweighted["MET150"] += 1
        CutflowDict_weighted["MET150"] += 1.0*weight

    if( CutsDict["dphiJetMET"] == False ):
        return False
    else:
        CutflowDict_unweighted["dphiJetMET"] += 1
        CutflowDict_weighted["dphiJetMET"] += 1.0*weight

    if( CutsDict["50Mll"] == False ):
        return False
    else:
        CutflowDict_unweighted["50Mll"] += 1
        CutflowDict_weighted["50Mll"] += 1.0*weight

    if( CutsDict["Rll"] == False ):
        return False
    else:
        CutflowDict_unweighted["Rll"] += 1
        CutflowDict_weighted["Rll"] += 1.0*weight

    if( CutsDict["Mtautau"] == False ):
        return False
    else:
        CutflowDict_unweighted["Mtautau"] += 1
        CutflowDict_weighted["Mtautau"] += 1.0*weight

    return True
#======================================================================
def doNonSeqCutflow(CutsDict, CutflowDict_unweighted, CutflowDict_weighted, weight):

    if( CutsDict["363491"] == False ):
        return False
    #else: print "363491"

    if( CutsDict["1baseEl"] == True ):
        CutflowDict_unweighted["1baseEl"] += 1
        CutflowDict_weighted["1baseEl"] += 1.0*weight

    if( CutsDict["1sigEl"] == True ):
        CutflowDict_unweighted["1sigEl"] += 1
        CutflowDict_weighted["1sigEl"] += 1.0*weight

    if( CutsDict["1baseMu"] == True ):
        CutflowDict_unweighted["1baseMu"] += 1
        CutflowDict_weighted["1baseMu"] += 1.0*weight

    if( CutsDict["1sigMu"] == True ):
        CutflowDict_unweighted["1sigMu"] += 1
        CutflowDict_weighted["1sigMu"] += 1.0*weight

    if( CutsDict["2baseEl"] == True ):
        CutflowDict_unweighted["2baseEl"] += 1
        CutflowDict_weighted["2baseEl"] += 1.0*weight

    if( CutsDict["2sigEl"] == True ):
        CutflowDict_unweighted["2sigEl"] += 1
        CutflowDict_weighted["2sigEl"] += 1.0*weight

    if( CutsDict["2baseMu"] == True ):
        CutflowDict_unweighted["2baseMu"] += 1
        CutflowDict_weighted["2baseMu"] += 1.0*weight

    if( CutsDict["2sigMu"] == True ):
        CutflowDict_unweighted["2sigMu"] += 1
        CutflowDict_weighted["2sigMu"] += 1.0*weight

    if( CutsDict["2baseLep"] == True ):
        CutflowDict_unweighted["2baseLep"] += 1
        CutflowDict_weighted["2baseLep"] += 1.0*weight

    if( CutsDict["2sigLep"] == True ):
        CutflowDict_unweighted["2sigLep"] += 1
        CutflowDict_weighted["2sigLep"] += 1.0*weight

    if( CutsDict["3baseEl"] == True ):
        CutflowDict_unweighted["3baseEl"] += 1
        CutflowDict_weighted["3baseEl"] += 1.0*weight

    if( CutsDict["3sigEl"] == True ):
        CutflowDict_unweighted["3sigEl"] += 1
        CutflowDict_weighted["3sigEl"] += 1.0*weight

    if( CutsDict["3baseMu"] == True ):
        CutflowDict_unweighted["3baseMu"] += 1
        CutflowDict_weighted["3baseMu"] += 1.0*weight

    if( CutsDict["3sigMu"] == True ):
        CutflowDict_unweighted["3sigMu"] += 1
        CutflowDict_weighted["3sigMu"] += 1.0*weight

    if( CutsDict["3baseLep"] == True ):
        CutflowDict_unweighted["3baseLep"] += 1
        CutflowDict_weighted["3baseLep"] += 1.0*weight

    if( CutsDict["3sigLep"] == True ):
        CutflowDict_unweighted["3sigLep"] += 1
        CutflowDict_weighted["3sigLep"] += 1.0*weight

    if( CutsDict["1sigJet"] == True ):
        CutflowDict_unweighted["1sigJet"] += 1
        CutflowDict_weighted["1sigJet"] += 1.0*weight

    if( CutsDict["bVeto"] == True ):
        CutflowDict_unweighted["bVeto"] += 1
        CutflowDict_weighted["bVeto"] += 1.0*weight

    if( CutsDict["1muTrig"] == True ):
        CutflowDict_unweighted["1muTrig"] += 1
        CutflowDict_weighted["1muTrig"] += 1.0*weight

    if( CutsDict["2muTrig"] == True ):
        CutflowDict_unweighted["2muTrig"] += 1
        CutflowDict_weighted["2muTrig"] += 1.0*weight

    if( CutsDict["METTrig"] == True ):
        CutflowDict_unweighted["METTrig"] += 1
        CutflowDict_weighted["METTrig"] += 1.0*weight


    return True
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

    if data:
        t=f.Get("%s" %tree)
        sumWhist = fw.Get("weighted__AOD")
    else:
        t=f.Get("%s_NoSys" % tree) 
        sumWhist = f.Get("weighted__AOD") 


    if debug: print t.GetName()

    t.SetBranchStatus("trigWeight_metTrig", 0)
    t.SetBranchStatus("trigMatch_metTrig", 1)
    t.SetBranchStatus("trigWeight_singleMuonTrig", 0)
    t.SetBranchStatus("trigMatch_singleMuonTrig", 1)
    t.SetBranchStatus("trigWeight_singleElectronTrig", 0)
    t.SetBranchStatus("trigMatch_singleElectronTrig", 1)
    t.SetBranchStatus("HLT_2mu4_j85_xe50_mht_emul", 1)
    t.SetBranchStatus("HLT_mu4_j125_xe90_mht_emul", 1)
    t.SetBranchStatus("mu",1) 
    t.SetBranchStatus("nVtx",1) 
    t.SetBranchStatus("nLep_base",1)
    t.SetBranchStatus("nLep_signal",1) 
    t.SetBranchStatus("lep1Flavor",1) 
    t.SetBranchStatus("lep1Charge",1) 
    t.SetBranchStatus("lep1Pt",1) 
    t.SetBranchStatus("lep1Eta",1) 
    t.SetBranchStatus("lep1Phi",1) 
    t.SetBranchStatus("lep1M",1) 
    t.SetBranchStatus("lep1D0",1) 
    t.SetBranchStatus("lep1D0Sig",1) 
    t.SetBranchStatus("lep1Z0",1) 
    t.SetBranchStatus("lep1Z0SinTheta",1) 
    t.SetBranchStatus("lep1PassOR",1) 
    t.SetBranchStatus("lep1Type",1) 
    t.SetBranchStatus("lep1Origin",1) 
    t.SetBranchStatus("lep1NPix",0) 
    t.SetBranchStatus("lep1PassBL",0) 
    t.SetBranchStatus("lep1VeryLoose",0) 
    t.SetBranchStatus("lep1Loose",0) 
    t.SetBranchStatus("lep1Medium",0) 
    t.SetBranchStatus("lep1Tight",0) 
    t.SetBranchStatus("lep1IsoLoose",0) 
    t.SetBranchStatus("lep1IsoTight",0) 
    t.SetBranchStatus("lep1IsoGradient",0) 
    t.SetBranchStatus("lep1IsoGradientLoose",0) 
    t.SetBranchStatus("lep1IsoLooseTrackOnly",0) 
    t.SetBranchStatus("lep1IsoFixedCutLoose",0) 
    t.SetBranchStatus("lep1IsoFixedCutTight",0) 
    t.SetBranchStatus("lep1IsoFixedCutTightTrackOnly",0) 
    t.SetBranchStatus("lep1Ptcone20",0) 
    t.SetBranchStatus("lep1Ptcone30",0) 
    t.SetBranchStatus("lep1Ptcone40",0) 
    t.SetBranchStatus("lep1Signal",1) 
    t.SetBranchStatus("lep1MatchesTrigger",1) 
    t.SetBranchStatus("lep2Flavor",1) 
    t.SetBranchStatus("lep2Charge",1) 
    t.SetBranchStatus("lep2Pt",1) 
    t.SetBranchStatus("lep2Eta",1) 
    t.SetBranchStatus("lep2Phi",1) 
    t.SetBranchStatus("lep2M",1) 
    t.SetBranchStatus("lep2D0",1) 
    t.SetBranchStatus("lep2D0Sig",1) 
    t.SetBranchStatus("lep2Z0",1) 
    t.SetBranchStatus("lep2Z0SinTheta",1) 
    t.SetBranchStatus("lep2PassOR",1) 
    t.SetBranchStatus("lep2Type",1) 
    t.SetBranchStatus("lep2Origin",1) 
    t.SetBranchStatus("lep2NPix",0) 
    t.SetBranchStatus("lep2PassBL",0) 
    t.SetBranchStatus("lep2VeryLoose",0) 
    t.SetBranchStatus("lep2Loose",0) 
    t.SetBranchStatus("lep2Medium",0) 
    t.SetBranchStatus("lep2Tight",0) 
    t.SetBranchStatus("lep2IsoLoose",0) 
    t.SetBranchStatus("lep2IsoTight",0) 
    t.SetBranchStatus("lep2IsoGradient",0) 
    t.SetBranchStatus("lep2IsoGradientLoose",0) 
    t.SetBranchStatus("lep2IsoLooseTrackOnly",0) 
    t.SetBranchStatus("lep2IsoFixedCutLoose",0) 
    t.SetBranchStatus("lep2IsoFixedCutTight",0) 
    t.SetBranchStatus("lep2IsoFixedCutTightTrackOnly",0) 
    t.SetBranchStatus("lep2Signal",1) 
    t.SetBranchStatus("lep2MatchesTrigger",1) 
    t.SetBranchStatus("lep3Flavor",1) 
    t.SetBranchStatus("lep3Charge",1) 
    t.SetBranchStatus("lep3Pt",1) 
    t.SetBranchStatus("lep3Eta",1) 
    t.SetBranchStatus("lep3Phi",1) 
    t.SetBranchStatus("lep3M",1) 
    t.SetBranchStatus("lep3D0",1) 
    t.SetBranchStatus("lep3D0Sig",1) 
    t.SetBranchStatus("lep3Z0",1) 
    t.SetBranchStatus("lep3Z0SinTheta",1) 
    t.SetBranchStatus("lep3PassOR",1) 
    t.SetBranchStatus("lep3Type",1) 
    t.SetBranchStatus("lep3Origin",1) 
    t.SetBranchStatus("lep3NPix",0) 
    t.SetBranchStatus("lep3PassBL",0) 
    t.SetBranchStatus("lep3VeryLoose",0) 
    t.SetBranchStatus("lep3Loose",0) 
    t.SetBranchStatus("lep3Medium",0) 
    t.SetBranchStatus("lep3Tight",0) 
    t.SetBranchStatus("lep3IsoLoose",0) 
    t.SetBranchStatus("lep3IsoTight",0) 
    t.SetBranchStatus("lep3IsoGradient",0) 
    t.SetBranchStatus("lep3IsoGradientLoose",0) 
    t.SetBranchStatus("lep3IsoLooseTrackOnly",0) 
    t.SetBranchStatus("lep3IsoFixedCutLoose",0) 
    t.SetBranchStatus("lep3IsoFixedCutTight",0) 
    t.SetBranchStatus("lep3IsoFixedCutTightTrackOnly",0) 
    t.SetBranchStatus("lep3Signal",1) 
    t.SetBranchStatus("lep3MatchesTrigger",1) 
    t.SetBranchStatus("lep4Flavor",1) 
    t.SetBranchStatus("lep4Charge",1) 
    t.SetBranchStatus("lep4Pt",1) 
    t.SetBranchStatus("lep4Eta",1) 
    t.SetBranchStatus("lep4Phi",1) 
    t.SetBranchStatus("lep4M",1) 
    t.SetBranchStatus("lep4D0",1) 
    t.SetBranchStatus("lep4D0Sig",1) 
    t.SetBranchStatus("lep4Z0",1) 
    t.SetBranchStatus("lep4Z0SinTheta",1) 
    t.SetBranchStatus("lep4PassOR",1) 
    t.SetBranchStatus("lep4Type",1) 
    t.SetBranchStatus("lep4Origin",1) 
    t.SetBranchStatus("lep4NPix",0) 
    t.SetBranchStatus("lep4PassBL",0) 
    t.SetBranchStatus("lep4VeryLoose",0) 
    t.SetBranchStatus("lep4Loose",0) 
    t.SetBranchStatus("lep4Medium",0) 
    t.SetBranchStatus("lep4Tight",0) 
    t.SetBranchStatus("lep4IsoLoose",0) 
    t.SetBranchStatus("lep4IsoTight",0) 
    t.SetBranchStatus("lep4IsoGradient",0) 
    t.SetBranchStatus("lep4IsoGradientLoose",0) 
    t.SetBranchStatus("lep4IsoLooseTrackOnly",0) 
    t.SetBranchStatus("lep4IsoFixedCutLoose",0) 
    t.SetBranchStatus("lep4IsoFixedCutTight",0) 
    t.SetBranchStatus("lep4IsoFixedCutTightTrackOnly",0) 
    t.SetBranchStatus("lep4Signal",1) 
    t.SetBranchStatus("lep4MatchesTrigger",1) 
    t.SetBranchStatus("nJet30",1) 
    t.SetBranchStatus("nJet25",1) 
    t.SetBranchStatus("nTotalJet",0) 
    t.SetBranchStatus("nBJet30_MV2c10",1) 
    t.SetBranchStatus("nBJet30_MV2c10_FixedCutBEff_60",0) 
    t.SetBranchStatus("nBJet30_MV2c10_FixedCutBEff_70",0) 
    t.SetBranchStatus("nBJet30_MV2c10_FixedCutBEff_85",0) 
    t.SetBranchStatus("DecayModeTTbar",0) 
    t.SetBranchStatus("jetPt",1)
    t.SetBranchStatus("jetEta",1)
    t.SetBranchStatus("jetPhi",1)
    t.SetBranchStatus("jetM",1)
    t.SetBranchStatus("met_Et",1) 
    t.SetBranchStatus("met_Phi",1) 
    t.SetBranchStatus("TST_Et",0) 
    t.SetBranchStatus("TST_Phi",0) 
    t.SetBranchStatus("deltaPhi_MET_TST_Phi",0) 
    t.SetBranchStatus("mt",1) 
    t.SetBranchStatus("meffInc30",1) 
    t.SetBranchStatus("Ht30",1) 
    t.SetBranchStatus("hadronicWMass",0) 
    t.SetBranchStatus("hadronicWPt",0) 
    t.SetBranchStatus("LepAplanarity",0) 
    t.SetBranchStatus("JetAplanarity",0) 
    t.SetBranchStatus("amt2",0) 
    t.SetBranchStatus("amt2b",0) 
    t.SetBranchStatus("amt2bWeight",0) 
    t.SetBranchStatus("mt2tau",0) 
    t.SetBranchStatus("mt2lj",0) 
    t.SetBranchStatus("mbb", 0)
    t.SetBranchStatus("mt_lep1",0)
    t.SetBranchStatus("mt_lep2",0)
    t.SetBranchStatus("mt_lep3",0)
    t.SetBranchStatus("mt_lep4",0)
    t.SetBranchStatus("METOverHT",1)
    t.SetBranchStatus("METOverJ1pT",1)
    t.SetBranchStatus("DPhiJ1Met",1)
    t.SetBranchStatus("mll",1)
    t.SetBranchStatus("Rll",1)
    t.SetBranchStatus("MSqTauTau_1",1)
    t.SetBranchStatus("MSqTauTau_2",1)
    t.SetBranchStatus("RjlOverEl",1)
    t.SetBranchStatus("LepCosThetaLab",0)
    t.SetBranchStatus("LepCosThetaCoM",0)
    t.SetBranchStatus("mt2leplsp_0",0)
    t.SetBranchStatus("mt2leplsp_25",0)
    t.SetBranchStatus("mt2leplsp_50",0)
    t.SetBranchStatus("mt2leplsp_75",0)
    t.SetBranchStatus("mt2leplsp_90",0)
    t.SetBranchStatus("mt2leplsp_95",0)
    t.SetBranchStatus("mt2leplsp_100",0)
    t.SetBranchStatus("mt2leplsp_105",0)
    t.SetBranchStatus("mt2leplsp_110",0)
    t.SetBranchStatus("mt2leplsp_115",0)
    t.SetBranchStatus("mt2leplsp_120",0)
    t.SetBranchStatus("mt2leplsp_150",0)
    t.SetBranchStatus("pileupWeight",1) 
    t.SetBranchStatus("leptonWeight",1) 
    t.SetBranchStatus("eventWeight",1) 
    t.SetBranchStatus("jvtWeight",1) 
    t.SetBranchStatus("bTagWeight",1) 
    t.SetBranchStatus("genWeight",1) 
    t.SetBranchStatus("genWeightUp",0) 
    t.SetBranchStatus("genWeightDown",0) 
    t.SetBranchStatus("SherpaVjetsNjetsWeight",1)
    t.SetBranchStatus("HLT_mu4",1)
    t.SetBranchStatus("HLT_2mu4",1)
    t.SetBranchStatus("HLT_2mu10",0)
    t.SetBranchStatus("HLT_2mu4_j85_xe50_mht",1)
    t.SetBranchStatus("HLT_mu4_j125_xe90_mht",1)
    t.SetBranchStatus("HLT_xe70",0) 
    t.SetBranchStatus("HLT_xe70_mht",0) 
    t.SetBranchStatus("HLT_xe70_mht_wEFMu",0) 
    t.SetBranchStatus("HLT_xe70_tc_lcw",0) 
    t.SetBranchStatus("HLT_xe70_tc_lcw_wEFMu",0) 
    t.SetBranchStatus("HLT_xe80_tc_lcw_L1XE50",0) 
    t.SetBranchStatus("HLT_xe90_tc_lcw_L1XE50",0) 
    t.SetBranchStatus("HLT_xe90_mht_L1XE50",0) 
    t.SetBranchStatus("HLT_xe90_mht_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe90_tc_lcw_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_tc_lcw_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_mht_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_tc_lcw_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_mht_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_tc_em_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_tc_em_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_mht_L1XE50",1)
    t.SetBranchStatus("HLT_xe90_mht_L1XE50",0)
    t.SetBranchStatus("HLT_j85_L1J40",1)
    t.SetBranchStatus("HLT_j125_L1J50",1)
    t.SetBranchStatus("HLT_e26_lhtight_nod0_ivarloose",0)
    t.SetBranchStatus("HLT_e60_lhmedium_nod0",0)
    t.SetBranchStatus("HLT_e60_medium",0)
    t.SetBranchStatus("HLT_e140_lhloose_nod0",0)
    t.SetBranchStatus("HLT_mu26_ivarmedium",0)
    t.SetBranchStatus("ttbarNNLOWeight", 1)
    t.SetBranchStatus("ttbarNNLOWeightUp", 0)
    t.SetBranchStatus("ttbarNNLOWeightDown", 0)
    t.SetBranchStatus("truthTopPt",0)
    t.SetBranchStatus("truthAntiTopPt",0)
    t.SetBranchStatus("truthTtbarPt",0)
    t.SetBranchStatus("truthTtbarM",0)
    t.SetBranchStatus("x1",0)
    t.SetBranchStatus("x2",0)
    t.SetBranchStatus("pdf1",0)
    t.SetBranchStatus("pdf2",0)
    t.SetBranchStatus("scalePDF",0)
    t.SetBranchStatus("id1",0) 
    t.SetBranchStatus("id2",0) 
    t.SetBranchStatus("PRWHash",0) 
    t.SetBranchStatus("EventNumber",1) 
    t.SetBranchStatus("xsec",1) 
    t.SetBranchStatus("TrueHt",0) 
    t.SetBranchStatus("DatasetNumber",1) 
    t.SetBranchStatus("RunNumber",0) 
    t.SetBranchStatus("RandomRunNumber",1) 
    t.SetBranchStatus("FS",0) 

    #-------------------------
    #create output file
    #-------------------------


    if debug: print "opening output file"

    o=ROOT.TFile(outfile, "RECREATE")

    if debug: print "initializing cut flows"

    SeqCutflow = {}
    WeightedSeqCutflow = {}
    NonSeqCutflow = {}
    WeightedNonSeqCutflow = {}

    SeqCutflow["2baseLep"] = 0.0
    SeqCutflow["2sigLep"] = 0.0
    SeqCutflow["SFOS"] = 0.0
    SeqCutflow["lep1Pt50"] = 0.0
    SeqCutflow["1sigJet"] = 0.0
    SeqCutflow["jet1Pt150"] = 0.0
    SeqCutflow["bVeto"] = 0.0
    SeqCutflow["MET150"] = 0.0
    SeqCutflow["dphiJetMET"] = 0.0
    SeqCutflow["50Mll"] = 0.0
    SeqCutflow["Rll"] = 0.0
    SeqCutflow["Mtautau"] = 0.0

    WeightedSeqCutflow["2baseLep"] = 0.0
    WeightedSeqCutflow["2sigLep"] = 0.0
    WeightedSeqCutflow["SFOS"] = 0.0
    WeightedSeqCutflow["lep1Pt50"] = 0.0
    WeightedSeqCutflow["1sigJet"] = 0.0
    WeightedSeqCutflow["jet1Pt150"] = 0.0
    WeightedSeqCutflow["bVeto"] = 0.0
    WeightedSeqCutflow["MET150"] = 0.0
    WeightedSeqCutflow["dphiJetMET"] = 0.0
    WeightedSeqCutflow["50Mll"] = 0.0
    WeightedSeqCutflow["Rll"] = 0.0
    WeightedSeqCutflow["Mtautau"] = 0.0

    NonSeqCutflow["1baseEl"] = 0.0
    NonSeqCutflow["1sigEl"] = 0.0
    NonSeqCutflow["1baseMu"] = 0.0
    NonSeqCutflow["1sigMu"] = 0.0
    NonSeqCutflow["2baseEl"] = 0.0
    NonSeqCutflow["2sigEl"] = 0.0
    NonSeqCutflow["2baseMu"] = 0.0
    NonSeqCutflow["2sigMu"] = 0.0
    NonSeqCutflow["2baseLep"] = 0.0
    NonSeqCutflow["2sigLep"] = 0.0
    NonSeqCutflow["3baseEl"] = 0.0
    NonSeqCutflow["3sigEl"] = 0.0
    NonSeqCutflow["3baseMu"] = 0.0
    NonSeqCutflow["3sigMu"] = 0.0
    NonSeqCutflow["3baseLep"] = 0.0
    NonSeqCutflow["3sigLep"] = 0.0
    NonSeqCutflow["1sigJet"] = 0.0
    NonSeqCutflow["bVeto"] = 0.0
    NonSeqCutflow["1muTrig"] = 0.0
    NonSeqCutflow["2muTrig"] = 0.0
    NonSeqCutflow["METTrig"] = 0.0

    WeightedNonSeqCutflow["1baseEl"] = 0.0
    WeightedNonSeqCutflow["1sigEl"] = 0.0
    WeightedNonSeqCutflow["1baseMu"] = 0.0
    WeightedNonSeqCutflow["1sigMu"] = 0.0
    WeightedNonSeqCutflow["2baseEl"] = 0.0
    WeightedNonSeqCutflow["2sigEl"] = 0.0
    WeightedNonSeqCutflow["2baseMu"] = 0.0
    WeightedNonSeqCutflow["2sigMu"] = 0.0
    WeightedNonSeqCutflow["2baseLep"] = 0.0
    WeightedNonSeqCutflow["2sigLep"] = 0.0
    WeightedNonSeqCutflow["3baseEl"] = 0.0
    WeightedNonSeqCutflow["3sigEl"] = 0.0
    WeightedNonSeqCutflow["3baseMu"] = 0.0
    WeightedNonSeqCutflow["3sigMu"] = 0.0
    WeightedNonSeqCutflow["3baseLep"] = 0.0
    WeightedNonSeqCutflow["3sigLep"] = 0.0
    WeightedNonSeqCutflow["1sigJet"] = 0.0
    WeightedNonSeqCutflow["bVeto"] = 0.0
    WeightedNonSeqCutflow["1muTrig"] = 0.0
    WeightedNonSeqCutflow["2muTrig"] = 0.0
    WeightedNonSeqCutflow["METTrig"] = 0.0

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

        #Initialize TLorentz vectors
        lep1Vec = ROOT.TLorentzVector()
        lep2Vec = ROOT.TLorentzVector()
        lep3Vec = ROOT.TLorentzVector()
        lep4Vec = ROOT.TLorentzVector()
        jet1Vec = ROOT.TLorentzVector()
        jet2Vec = ROOT.TLorentzVector()

        MET = event.met_Et
        MET_Phi = event.met_Phi
        Meff = event.meffInc30
        Ht30 = event.Ht30
        if event.jetPt.size() > 0: jet1Vec.SetPtEtaPhiM(event.jetPt[0], event.jetEta[0], event.jetPhi[0], event.jetM[0])
        if event.jetPt.size() > 1: jet2Vec.SetPtEtaPhiM(event.jetPt[1], event.jetEta[1], event.jetPhi[1], event.jetM[1])
        #dphi_j1met = TVector2.Phi_mpi_pi(jet1Vec.Phi() - MET_Phi) 
        dphi_j1met = event.DPhiJ1Met
        dphi_j2met = TVector2.Phi_mpi_pi(jet2Vec.Phi() - MET_Phi) 
        #metTrigger = event.trigMatch_metTrig
        metTrigger = event.HLT_xe110_mht_L1XE50
        dimuonTrigger = event.HLT_2mu4_j85_xe50_mht_emul
        muonTrigger = event.HLT_mu4_j125_xe90_mht_emul
        nBaseLep = event.nLep_base
        nSigLep  = event.nLep_signal
        nJet25 = event.nJet25
        if event.jetPt.size() > 0: jet1Pt = event.jetPt[0]
        if event.jetPt.size() > 1: jet2Pt = event.jetPt[1]
        lep1Vec.SetPtEtaPhiM(event.lep1Pt, event.lep1Eta, event.lep1Phi, event.lep1M)
        lep2Vec.SetPtEtaPhiM(event.lep2Pt, event.lep2Eta, event.lep2Phi, event.lep2M)
        lep3Vec.SetPtEtaPhiM(event.lep3Pt, event.lep3Eta, event.lep3Phi, event.lep3M)
        lep4Vec.SetPtEtaPhiM(event.lep4Pt, event.lep4Eta, event.lep4Phi, event.lep4M)
        lep1Flavor = event.lep1Flavor
        lep1Charge = event.lep1Charge
        lep1Signal = event.lep1Signal
        lep2Flavor = event.lep2Flavor
        lep2Charge = event.lep2Charge
        lep2Signal = event.lep2Signal
        lep3Flavor = event.lep3Flavor
        lep3Charge = event.lep3Charge
        lep3Signal = event.lep3Signal
        lep4Flavor = event.lep4Flavor
        lep4Charge = event.lep4Charge
        lep4Signal = event.lep4Signal
        nBTag = event.nBJet30_MV2c10
        RunNumer = event.RandomRunNumber
        DatasetNumber = event.DatasetNumber

        obs = observable()
        #index1, index2 = obs.findSignalPairs(event) #Decide leading and subeading lepton based on opposite sign match
        #if (index1 == 0 or index2 == 0):
        #    continue
        #print index1, index2
        mtautau = -999
        dR_l1l2 = -999.
        if (nSigLep > 1):
            mtautau = obs.calcMtautau(event) #Calculate mtautau
            dR_l1l2  = lep2Vec.DeltaR(lep1Vec)

        #lep1Vec, lep1Charge, lep1Flavor, lep1Signal = obs.getLep1TLVChargeFlavorSignal(event)
        #lep2Vec, lep2Charge, lep2Flavor, lep2Signal = obs.getLep2TLVChargeFlavorSignal(event)
        #print "lep1 info: pt = %f, eta = %f, charge = %i, type = %i" % (lep1Vec.Pt(), lep1Vec.Eta(), lep1Charge, lep1Flavor)
        #print "lep2 info: pt = %f, eta = %f, charge = %i, type = %i" % (lep2Vec.Pt(), lep2Vec.Eta(), lep2Charge, lep2Flavor)

        #Calculate dilepton variables
        lepPairVec = lep1Vec + lep2Vec
        mll = lepPairVec.M()
        ptll = lepPairVec.Pt()
        dimuFlag = 0
        if(lep1Flavor == 2 and lep2Flavor == 2):
            dimuFlag = 1
        qlql = lep1Charge*lep2Charge
        dphi_l1met = TVector2.Phi_mpi_pi(lep1Vec.Phi() - MET_Phi)
        dphi_l2met = TVector2.Phi_mpi_pi(lep2Vec.Phi() - MET_Phi)
        MT_l1met = TMath.Sqrt(2*lep1Vec.Pt()*MET*(1-TMath.Cos(dphi_l1met)))
        MT_l2met = TMath.Sqrt(2*lep2Vec.Pt()*MET*(1-TMath.Cos(dphi_l2met)))

        lumi = 36075
        if data:
            totalWeight = 1.0
        else:
            #totalWeight = float(event.pileupWeight*event.eventWeight*event.leptonWeight*event.jvtWeight*event.bTagWeight)
            #totalWeight = float(event.eventWeight)
            totalWeight = float(event.pileupWeight*event.eventWeight*event.leptonWeight*event.jvtWeight*event.bTagWeight*event.genWeight*lumi) #TODO: NO TRIGGER WEIGHT!!


        #Make dictionary of cuts
        Cuts = {}

        if( nBaseLep > 0):
            Cuts["1baseLep"] = True
        else: Cuts["1baseLep"] = False

        if( nSigLep > 0 ):
            Cuts["1sigLep"] = True
        else: Cuts["1sigLep"] = False

        if( nBaseLep > 1):
            Cuts["2baseLep"] = True
        else: Cuts["2baseLep"] = False

        if( nSigLep > 1 ):
            Cuts["2sigLep"] = True
        else: Cuts["2sigLep"] = False

        if( nBaseLep == 3):
            Cuts["3baseLep"] = True
        else: Cuts["3baseLep"] = False

        if( nSigLep == 3 ):
            Cuts["3sigLep"] = True
        else: Cuts["3sigLep"] = False

        if( lep1Flavor == lep2Flavor and qlql == -1 ):
            Cuts["SFOS"] = True
        else: Cuts["SFOS"] = False

        if( lep1Vec.Pt() < 50. ):
            Cuts["lep1Pt50"] = True
        else: Cuts["lep1Pt50"] = False

        if( nJet25 > 0 ):
            Cuts["1sigJet"] = True
        else: Cuts["1sigJet"] = False

        if( jet1Pt > 105. ):
            Cuts["Jet105"] = True
        else: Cuts["Jet105"] = False

        if( jet1Pt > 145. ):
            Cuts["Jet145"] = True
        else: Cuts["Jet145"] = False
            
        if( jet1Pt > 150. ):
            Cuts["jet1Pt150"] = True
        else: Cuts["jet1Pt150"] = False

        if( dphi_j1met > 2.5 ):
            Cuts["dphiJetMET"] = True
        else: Cuts["dphiJetMET"] = False

        if( dR_l1l2 < 1.5 ):
            Cuts["Rll"] = True
        else: Cuts["Rll"] = False
            
        if( qlql == -1 ): 
            Cuts["opSign"] = True
        else: 
            Cuts["opSign"] = False

        if( MET > 150. ): 
            Cuts["MET150"] = True
        else: 
            Cuts["MET150"] = False

        if( Ht30 <= 0.0 ): 
            Cuts["METoverHt"] = False
        elif( MET/Ht30 >= 0.6 and MET/Ht30 <= 1.4 ): 
            Cuts["METoverHt"] = True
        else: 
            Cuts["METoverHt"] = False

        if( Ht30 > 100. ): 
            Cuts["HT100"] = True
        else: 
            Cuts["HT100"] = False

        if( ptll > 3.0 ): 
            Cuts["ptll3"] = True
        else: 
            Cuts["ptll3"] = False

        if( mll >= 4. and mll <=60. ):
            Cuts["4mll60"] = True
        else:
            Cuts["4mll60"] = False

        if( mll < 50. ):
            Cuts["50Mll"] = True
        else:
            Cuts["50Mll"] = False

        if( lep1Vec.Pt() < 30. and lep2Vec.Pt() < 30. ):
            Cuts["lepPt30"] = True
        else: 
            Cuts["lepPt30"] = False

        if( lep1Vec.Pt() < 50. and lep2Vec.Pt() < 50. ):
            Cuts["lepPt50"] = True
        else: 
            Cuts["lepPt50"] = False

        if( nBTag == 0 ):
            Cuts["bVeto"] = True
        else: 
            Cuts["bVeto"] = False

        if( MT_l1met < 70. and MT_l2met < 70 ):
            Cuts["70MtLepMET"] = True
        else: 
            Cuts["70MtLepMET"] = False

        if( mtautau < 0. ): #or mtautau >= 160.):
            Cuts["Mtautau"] = True
        else: 
            Cuts["Mtautau"] = False

        if(MET > 125. and MET <= 200.):
            Cuts["125MET200"] = True
        else: 
            Cuts["125MET200"] = False

        if(MET > 200. and MET <= 250.):
            Cuts["200MET250"] = True
        else: 
            Cuts["200MET250"] = False

        if( MET > 250. ):
            Cuts["MET250"] = True
        else: 
            Cuts["MET250"] = False

        if( metTrigger ):
            Cuts["METTrig"] = True
        else: 
            Cuts["METTrig"] = False

        if( dimuonTrigger ):
            Cuts["2muTrig"] = True
        else: 
            Cuts["2muTrig"] = False

        if( muonTrigger ):
            Cuts["1muTrig"] = True
        else: 
            Cuts["1muTrig"] = False

        if( dimuonTrigger and jet1Pt > 105. ):
            Cuts["dimuTriggerANDjet"] = True
        else: 
            Cuts["dimuTriggerANDjet"] = False

        if( muonTrigger and jet1Pt > 145.):
            Cuts["muTriggerANDjet"] = True
        else: 
            Cuts["muTriggerANDjet"] = False

        if ( (muonTrigger and jet1Pt > 145.) or (dimuonTrigger and jet1Pt > 105.) or metTrigger ):
            Cuts["ORTrigger"] = True
        else:
            Cuts["ORTrigger"] = False

        if( lep1Flavor == 2 and lep2Flavor == 2):
            Cuts["mumuEvent"] = True
        else: 
            Cuts["mumuEvent"] = False

        if( lep1Flavor == 1 and lep2Flavor == 1):
            Cuts["eeEvent"] = True
        else: 
            Cuts["eeEvent"] = False

        if( lep1Flavor == 1 or lep2Flavor == 1 or lep3Flavor == 1 or lep4Flavor == 1 ):
            Cuts["1baseEl"] = True
        else: Cuts["1baseEl"] = False

        if( (lep1Flavor == 1 and lep1Signal) or (lep2Flavor == 1 and lep2Signal) or (lep3Flavor == 1 and lep3Signal) or (lep4Flavor == 1 and lep4Signal) ):
            Cuts["1sigEl"] = True
        else: Cuts["1sigEl"] = False

        if( lep1Flavor == 2 or lep2Flavor == 2 or lep3Flavor == 2 or lep4Flavor == 2 ):
            Cuts["1baseMu"] = True
        else: Cuts["1baseMu"] = False

        if( (lep1Flavor == 2 and lep1Signal) or (lep2Flavor == 2 and lep2Signal) or (lep3Flavor == 2 and lep3Signal) or (lep4Flavor == 2 and lep4Signal) ):
            Cuts["1sigMu"] = True
        else: Cuts["1sigMu"] = False

        if( (lep1Flavor == 1 and lep2Flavor == 1) or (lep1Flavor == 1 and lep3Flavor == 1) or (lep1Flavor == 1 and lep4Flavor == 1) or (lep2Flavor == 1 and lep3Flavor == 1) or(lep2Flavor == 1 and lep4Flavor == 1) or (lep4Flavor == 1 and lep4Flavor == 1) ):
            Cuts["2baseEl"] = True
        else: Cuts["2baseEl"] = False

        if( (lep1Flavor == 1 and lep1Signal and lep2Flavor == 1 and lep2Signal) or (lep1Flavor == 1 and lep1Signal and lep3Flavor == 1 and lep3Signal) or (lep1Flavor == 1 and lep1Signal and lep4Flavor == 1 and lep4Signal) or (lep2Flavor == 1 and lep2Signal and lep3Flavor == 1 and lep3Signal) or(lep2Flavor == 1 and lep2Signal and lep4Flavor == 1 and lep4Signal) or (lep3Flavor == 1 and lep3Signal and lep4Flavor == 1 and lep4Signal) ):
            Cuts["2sigEl"] = True
        else: Cuts["2sigEl"] = False

        if( (lep1Flavor == 2 and lep2Flavor == 2) or (lep1Flavor == 2 and lep3Flavor == 2) or (lep1Flavor == 2 and lep4Flavor == 2) or (lep2Flavor == 2 and lep3Flavor == 2) or(lep2Flavor == 2 and lep4Flavor == 2) or (lep4Flavor == 2 and lep4Flavor == 2) ):
            Cuts["2baseMu"] = True
        else: Cuts["2baseMu"] = False

        if( (lep1Flavor == 2 and lep1Signal and lep2Flavor == 2 and lep2Signal) or (lep1Flavor == 2 and lep1Signal and lep3Flavor == 2 and lep3Signal) or (lep1Flavor == 2 and lep1Signal and lep4Flavor == 2 and lep4Signal) or (lep2Flavor == 2 and lep2Signal and lep3Flavor == 2 and lep3Signal) or(lep2Flavor == 2 and lep2Signal and lep4Flavor == 2 and lep4Signal) or (lep3Flavor == 2 and lep3Signal and lep4Flavor == 2 and lep4Signal) ):
            Cuts["2sigMu"] = True
        else: Cuts["2sigMu"] = False

        if( (lep1Flavor == 1 and lep2Flavor == 1 and lep3Flavor == 1 and lep4Flavor != 1) or (lep1Flavor == 1 and lep2Flavor == 1 and lep4Flavor == 1 and lep3Flavor != 1) or (lep1Flavor == 1 and lep4Flavor == 1 and lep3Flavor == 1 and lep2Flavor != 1) or (lep1Flavor != 1 and lep2Flavor == 1 and lep3Flavor == 1 and lep4Flavor == 1) ):
            Cuts["3baseEl"] = True
        else: Cuts["3baseEl"] = False

        if( (lep1Flavor == 1 and lep1Signal and lep2Flavor == 1 and lep2Signal and lep3Flavor == 1 and lep3Signal and lep4Flavor != 1) or (lep1Flavor == 1 and lep1Signal and lep2Flavor == 1 and lep2Signal and lep3Flavor != 1 and lep4Flavor == 1 and lep4Signal) or (lep1Flavor == 1 and lep1Signal and lep2Flavor != 1 and lep3Flavor == 1 and lep3Signal and lep4Flavor == 1 and lep4Signal) or (lep1Flavor != 1 and lep2Flavor == 1 and lep2Signal and lep3Flavor == 1 and lep3Signal and lep4Flavor == 1 and lep4Signal) ):
            Cuts["3sigEl"] = True
        else: Cuts["3sigEl"] = False

        if( (lep1Flavor == 2 and lep2Flavor == 2 and lep3Flavor == 2 and lep4Flavor != 2) or (lep1Flavor == 2 and lep2Flavor == 2 and lep4Flavor == 2 and lep3Flavor != 2) or (lep1Flavor == 2 and lep4Flavor == 2 and lep3Flavor == 2 and lep2Flavor != 2) or (lep1Flavor != 2 and lep2Flavor == 2 and lep3Flavor == 2 and lep4Flavor ==2) ):
            Cuts["3baseMu"] = True
        else: Cuts["3baseMu"] = False

        if( (lep1Flavor == 2 and lep1Signal and lep2Flavor == 2 and lep2Signal and lep3Flavor == 2 and lep3Signal and lep4Flavor != 2) or (lep1Flavor == 2 and lep1Signal and lep2Flavor == 2 and lep2Signal and lep3Flavor != 2 and lep4Flavor == 2 and lep4Signal) or (lep1Flavor == 2 and lep1Signal and lep2Flavor != 2 and lep3Flavor == 2 and lep3Signal and lep4Flavor == 2 and lep4Signal) or (lep1Flavor != 2 and lep2Flavor == 2 and lep2Signal and lep3Flavor == 2 and lep3Signal and lep4Flavor == 2 and lep4Signal) ):
            Cuts["3sigMu"] = True
        else: Cuts["3sigMu"] = False

        if( DatasetNumber == 363491 ):
            Cuts["363491"] = True
        else: Cuts["363491"] = False


        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount

        doSeqCutflow(Cuts, SeqCutflow, WeightedSeqCutflow, totalWeight)
        doNonSeqCutflow(Cuts, NonSeqCutflow, WeightedNonSeqCutflow, totalWeight)
        #print totalWeight


    print "printing cutflows..  you should probably write a tex file"

    #Loop over dictionaries here and print out values 
    print "UNWEIGHTED SEQUENTIAL CUTFLOW:"
    for k in SeqCutflow.keys():
        print '%s : %i' % (k, SeqCutflow[k])

    print "WEIGHTED SEQUENTIAL CUTFLOW:"
    for k in WeightedSeqCutflow.keys():
        print '%s : %f' % (k, WeightedSeqCutflow[k])


    print "UNWEIGHTED NONSEQUENTIAL CUTFLOW:"
    for k in NonSeqCutflow.keys():
        print '%s : %i' % (k, NonSeqCutflow[k])

    print "WEIGHTED NONSEQUENTIAL CUTFLOW:"
    for k in WeightedNonSeqCutflow.keys():
        print '%s : %f' % (k, WeightedNonSeqCutflow[k])

    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("-input"      , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("-weight"      , action='store', default='', help='root file containing sum of weights hist')
    parser.add_argument("-tree"        , action='store', default='')
    parser.add_argument("--isData"      , action='store_true')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("-outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("-region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    analyze(args.input, args.weight, args.tree, args.isData, args.isSignal, args.outfile, args.test, args.region)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
