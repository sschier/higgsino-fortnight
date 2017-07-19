#!/usr/bin/env python

#IMPORTS
import ROOT
from ROOT import RooStats
import sys, copy, os
import argparse, subprocess, commands
import math
from functions import *

#GLOBAL VARIABLES
logYAxis = True

#ATLAS STYLE
ROOT.gROOT.LoadMacro("/export/home/sschier/workarea/atlasstyle-00-03-05/AtlasUtils.C")
ROOT.gROOT.LoadMacro("/export/home/sschier/workarea/atlasstyle-00-03-05/AtlasStyle.C")
ROOT.gROOT.LoadMacro("/export/home/sschier/workarea/atlasstyle-00-03-05/AtlasLabels.C")
ROOT.SetAtlasStyle()
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gROOT.ForceStyle()

mc_names = ['zjets', 'ttbar', 'wjets', 'singletop']
data_names = ['data']
ROOT.gROOT.SetBatch(True)
#======================================================================
def GetRootFiles(dir, debug):
    file_list = []
    if not dir.endswith("/"): dir = dir + "/"
    #status, files = commands.getstatusoutput('ls ' + dir)
    files = commands.getoutput('ls ' + dir)
    files = files.split("\n")
    if debug: print files
    for f in files:
        if f.endswith(".root"): file_list += [dir + f]
    if debug: 
        print dir
        print file_list
    return file_list
#======================================================================
def GetNameFromFileName(file_name_str):

    dsid = file_name_str.replace('.root', '').split('/')[-1].split('_')[1]
    return dsid
#======================================================================
def IsData(file_name, debug):
    isData = False
    if debug: print 'in isData'
    name = file_name.replace('.root', '').split('/')[-1].split('_')
    if debug: print name
    for n in name:
        if n in data_names:
            isData =  True
        if debug: print isData
    return isData    

#======================================================================
def IsBkgnd(file_name):
    isBkgnd = False
    name = file_name.replace('.root', '').split('/')[-1].split('_')
    for n in name:
        if n in mc_names:
            isBkgnd =  True
    return isBkgnd    

#======================================================================
def GetDataHists(file_list, hist_path, debug):
    if debug: print 'getting data hists'
    #hists = []
    iter = 0
    for name in file_list:
        #print IsData(name, debug)
        if IsData(name, debug):
            f = ROOT.TFile(name, 'READ')
            if debug:
                print f.GetName()
            h = f.Get(hist_path)
            isTH1 = True
            try: isTH1 = 'TH1' in h.ClassName()
            except: 
                isTH1 = False
            if not isTH1:
                f.Close()
                continue
            h.SetDirectory(0)
            f.Close()
            iter = iter + 1

    return h
#======================================================================
def GetBGHists(file_list, hist_path, debug):
    if debug: print 'getting bg hists'
    hists = {}
    for string in file_list:
        name = GetNameFromFileName(string)
        if debug:
            print '***************'
            print name
            print '**************'
            print IsBkgnd(string)
        if IsBkgnd(string):
            f = ROOT.TFile(string, 'READ')
            if debug: print 'file is %s' % f
            h = f.Get(hist_path)
            if debug: print h
            isTH1 = True
            try: isTH1 = 'TH1' in h.ClassName()
            except: 
                isTH1 = False
            if not isTH1:
                f.Close()
                continue
            h.SetDirectory(0)
            hists[name] = copy.deepcopy(h)
            hists[name].SetDirectory(0)
            f.Close()

    if debug:
        for k in hists:
            print hists[k]
    return hists
#======================================================================
def SumMCHists(hist_list, lumi, debug):
    if debug:
        print 'in SumMC'
        print hist_list
    sortedHistTuple = sorted(hist_list.items(), key=lambda x: x[1].GetBinContent(x[1].GetMaximumBin()))
    base = ROOT.TH1F('base', '',5, 250., 700)
    for h, x in zip(sortedHistTuple, xrange(10)):
        h[1].SetDirectory(0)
        if x is 0:
            base = copy.deepcopy(h[1])
            base.SetDirectory(0)
            #base.Scale(lumi)
        else:
            base.Add(h[1])
    return base
#======================================================================
#======================================================================
def MakeHistStack(hist_list, lumi, debug):
    hs = ROOT.THStack("hist stack", "hist stack")
    hsum = SumMCHists(hist_list, lumi, debug)
    maxVal = hsum.GetBinContent(hsum.GetMaximumBin())*10000*lumi
    minVal = 1.
    sortedHistTuple = sorted(hist_list.items(), key=lambda x: x[1].GetBinContent(x[1].GetMaximumBin()))
    if debug:
        print maxVal
        print 'in MakeMC'
        print hist_list
        print sortedHistTuple
    sortedKeyList = sorted(hist_list.keys())
    colors = [40, 41, 42, 46, 49, 31, 38, 15]
    #colors = [5, 3, 8, 2, 4, 7, 9, 51, 6]  #[yellow, Lgreen, Dgreen, red, blue, cyan, indigo, purple, magenta]
    markers = [33, 34, 20, 21, 29, 31, 23, 26, 25]     #[diamond, cross, circle, square, star, cross-hair, triangleup, opentriangledown, open-square
    colormap = {}
    markermap = {}
    for k, c, m in zip(sortedKeyList, colors, markers):
        colormap[k] = c
        markermap[k] = m
    if debug: print colormap

    for h in sortedHistTuple:
        if debug: print "adding hist to stack"
        #hist = h.Clone("hist")
        h[1].SetFillColor(colormap[h[0]])
        h[1].SetMarkerColor(colormap[h[0]])
        h[1].SetMarkerStyle(markermap[h[0]])
        h[1].SetMarkerSize()
        h[1].Scale(lumi)
        h[1].SetDirectory(0)
        hs.Add(h[1])
    hs.SetMaximum(maxVal)
    hs.SetMinimum(minVal)
    return hs

#======================================================================
def DataCanvas(region):
    global logYAxis
    c2 = ROOT.TCanvas("data_%s" % region, "data_%s" % region, 0, 0, 600, 600)
    #c1.Divide(1,2,0,0)
    p1 = ROOT.TPad("p1", "p1", 0, 0.3, 1, 1.0)
    p1.SetBottomMargin(0)
    if logYAxis: p1.SetLogy(ROOT.kTRUE)
    c2.cd(1)
    p1.Draw()

    return c2, p1
#======================================================================
def SetRatioCanvas(name, region):
    global logYAxis
    c1 = ROOT.TCanvas("%s_%s" % (name, region), "%s_%s" % (name, region), 0, 0, 800, 600)
    #c1.Divide(1,2,0,0)
    p1 = ROOT.TPad("p1", "p1", 0, 0.35, 1, 1.0)
    p1.SetBottomMargin(0.01)
    if logYAxis: p1.SetLogy(ROOT.kTRUE)
    c1.cd(1)
    p1.Draw()
    primarytextscale=1./(p1.GetWh()*p1.GetAbsHNDC());
    p2 = ROOT.TPad("p2", "p2", 0, 0.0, 1, 0.344)
    p2.SetTopMargin(0.05)
    p2.SetBottomMargin(0.37)
    c1.cd(2)
    p2.Draw()
    ratiotextscale=1./(p2.GetWh()*p2.GetAbsHNDC());

    return c1, p1, p2

#======================================================================
def SetSingleCanvas(name, region):
    global logYAxis
    c1 = ROOT.TCanvas("%s_%s" % (name, region), "%s_%s" % (name, region), 0, 0, 800, 800)
    #c1.Divide(1,2,0,0)
    p1 = ROOT.TPad("p1", "p1", 0, 0.3, 1, 1.0)
    #p1.SetBottomMargin(0)
    if logYAxis: p1.SetLogy(ROOT.kTRUE)
    c1.cd(1)
    p1.Draw()

    return c1, p1
#======================================================================
def SetCanvas(name, region):
    global logYAxis
    c1 = ROOT.TCanvas("%s_%s" % (name, region), "%s_%s" % (name, region), 0, 0, 600, 600)
    #c1.Divide(1,2,0,0)
    p1 = ROOT.TPad("p1", "p1", 0, 0.3, 1, 1.0)
    p1.SetBottomMargin(0)
    if logYAxis: p1.SetLogy(ROOT.kTRUE)
    c1.cd(1)
    p1.Draw()
    p2 = ROOT.TPad("p2", "p2", 0, 0.0, 1, 0.3)
    p2.SetTopMargin(0)
    p2.SetBottomMargin(0.3)
    c1.cd(2)
    p2.Draw()

    return c1, p1, p2

#======================================================================
def MakeLegend(bkgndHists, dataHist, region):

    #sortedHistTuple = sorted(bkgndHists, key=lambda x: x.GetBinContent(x.GetMaximumBin()))
    sortedHistTuple = sorted(bkgndHists.items(), key=lambda x: x[1].GetBinContent(x[1].GetMaximumBin()), reverse=True)

    l = ROOT.TLegend(0.8, 0.7, 0.91, 0.95)
    for hist in sortedHistTuple:
        l.AddEntry(hist[1], hist[0], 'f')
    #for hist, name in zip(sortedHistTuple, samples):
    #    l.AddEntry(hist, name, 'f')
    l.AddEntry(dataHist, 'data', 'l')

    return l

#======================================================================
def MakeNewRatio(topHist, bottomHist, debug):
    if debug:
        print '**debuging ratio plot'
        print bottomHist.GetBinContent(bottomHist.GetMaximumBin())
        print topHist.GetBinContent(topHist.GetMaximumBin())
    rh = copy.deepcopy(topHist)
    rh.SetDirectory(0)
    rh.Divide(bottomHist)
    rh.SetMinimum(0)
    rh.SetMaximum(10)
    if debug: print topHist.GetXaxis().GetTitle()
    rh.GetXaxis().SetTitle(str(topHist.GetXaxis().GetTitle()))
    rh.GetXaxis().SetLabelSize(0.12)
    rh.GetYaxis().SetLabelSize(0.12)
    rh.GetYaxis().SetNdivisions(8)
    rh.GetXaxis().SetTitleSize(0.16)
    rh.GetYaxis().SetTitleSize(0.16)
    rh.GetXaxis().SetTitleOffset(0.9)
    rh.GetYaxis().SetTitleOffset(0.39)
    rh.GetYaxis().SetTitle("Data/MC")


    return rh
#======================================================================
def MakeRatio(bkgndHist, dataHist):

    rh = copy.deepcopy(dataHist)
    rh.SetDirectory(0)
    rh.Divide(bkgndHist)
    rh.SetMinimum(0.5)
    rh.SetMaximum(1.5)

    return rh
#======================================================================
def plotCR(lumi, path, region, var, indir, debug):
    if debug: print "opening output file"
    o=ROOT.TFile("test.root", "RECREATE")
    if debug: print "Getting MC list"
    BGhist_list = GetBGHists(GetRootFiles(indir, debug), path, debug)
    if debug: print "Getting data hist"
    m_data = GetDataHists(GetRootFiles(indir, debug), path, debug)
    myRange = m_data.GetNbinsX()
    if debug: print "Making MC hist stack"
    m_hstack = MakeHistStack(BGhist_list, lumi,  debug)
    m_hsum = SumMCHists(BGhist_list, lumi, debug)
    m_ratio = MakeNewRatio(m_data, m_hsum, debug)
    m_legend = MakeLegend(BGhist_list, m_data, region)

    canvas, p1, p2 = SetRatioCanvas('canvas', region)
    p2.cd()
    m_ratio.Draw("P")
    p1.cd()
    m_hstack.Draw("HIST")
    m_data.Draw("PESAME")
    o.cd()
    m_hstack.Write()
    canvas.Write()
    canvas.cd()
    m_legend.Draw()
    ROOT.gStyle.SetLegendBorderSize(0)
    ROOT.gROOT.ForceStyle()
    #ROOT.myText(       0.41,  0.85, 1, "2.5fb^{-1}@ #sqrt{s}= 13 TeV")
    #ROOT.myText(       0.41,  0.80, 1, "data16PeriodK")
    #ROOT.myText(       0.41,  0.85, 1, "%s" % region)
    ROOT.ATLASLabel(0.41,0.90,"Internal")
    #raw_input("-->")
    canvas.Print('%s_%s.pdf' % (region, var))
    return True
#======================================================================
def plotSR(lumi, sample_path, region, variable, indir, debug):
    if debug: print "opening output file"
    o=ROOT.TFile("test.root", "RECREATE")
    if debug: print "Setting variable to plot"
    var = variable
    path = sample_path
    value_list = []
    error_list = []
    if debug: print "Getting MC list"
    BGhist_list = GetBGHists(GetRootFiles(indir, debug), path, debug)
    if debug: print "Getting data hist"
    m_data = GetDataHists(GetRootFiles(indir, debug), path, debug)
    myRange = m_data.GetNbinsX()
    if debug: print "Making MC hist stack"
    m_hstack = MakeHistStack(BGhist_list, lumi,  debug)
    m_hsum = SumMCHists(BGhist_list, lumi, debug)
    print '*********** %s electron ***********' % region
    sum1 = 0.0
    err1 = 0.0
    sum2 = 0.0
    err2 = 0.0
    sum3 = 0.0
    err3 = 0.0
    for x in xrange(myRange):
        bkSubtract = m_data.GetBinContent(x) - m_hsum.GetBinContent(x)
        bkSubtract_error = m_data.GetBinError(x) - m_hsum.GetBinError(x)
        #print ' bin %i = %f' % (x, bkSubtract)
        if( x > 5 and x <= 10 ):
            value_list.append(bkSubtract)
            error_list.append(bkSubtract_error)
        elif( x > 10 and x <= 15 ):
            sum1 += bkSubtract
            err1 += bkSubtract_error
        elif( x > 15 and x <= 20 ):
            sum2 += bkSubtract
            err2 += bkSubtract_error
        elif( x > 20 ):
            sum3 += bkSubtract
            err3 += bkSubtract_error
    
    value_list.append(sum1)
    error_list.append(err1)
    value_list.append(sum2)
    error_list.append(err2)
    value_list.append(sum3)
    error_list.append(err3)
    print value_list
    print error_list
                
    m_ratio = MakeNewRatio(m_data, m_hsum, debug)
    m_legend = MakeLegend(BGhist_list, m_data, region)
    canvas, p1, p2 = SetRatioCanvas('canvas', region)
    p2.cd()
    m_ratio.Draw("P")
    p1.cd()
    m_hstack.Draw("HIST")
    m_data.Draw("PESAME")
    o.cd()
    m_hstack.Write()
    canvas.Write()

    canvas.cd()
    m_legend.Draw()
    ROOT.gStyle.SetLegendBorderSize(0)
    ROOT.gROOT.ForceStyle()
    #ROOT.myText(       0.41,  0.85, 1, "2.5fb^{-1}@ #sqrt{s}= 13 TeV")
    #ROOT.myText(       0.41,  0.80, 1, "data16PeriodK")
    #ROOT.myText(       0.41,  0.85, 1, "%s" % region)
    ROOT.ATLASLabel(0.41,0.90,"Internal")
    #raw_input("-->")
    canvas.Print('%s_%s.pdf' % (region, var))
    return value_list, error_list
#======================================================================
def renorm(lumi, path, region, var, indir, debug):
    if debug: print "opening output file"
    BGhist_list = GetBGHists(GetRootFiles(indir, debug), path, debug)
    m_data = GetDataHists(GetRootFiles(indir, debug), path, debug)
    m_hstack = MakeHistStack(BGhist_list, lumi,  debug)
    m_hsum = SumMCHists(BGhist_list, lumi, debug)
    error_d = ROOT.Double()
    error_m = ROOT.Double()
    #integral_d = m_data.IntegralAndError(11, 20, error_d) #bins for MT 100-200 GeV
    #integral_m = m_hsum.IntegralAndError(11, 20, error_m)
    #integral_d = m_data.IntegralAndError(13, 20, error_d)
    #integral_m = m_hsum.IntegralAndError(13, 20, error_m)
    integral_d = m_data.IntegralAndError(13, 15, error_d) #bins for MET >200 GeV
    integral_m = m_hsum.IntegralAndError(13, 15, error_m)

    renorm, error = divideAndError(integral_d, error_d, integral_m, error_m)
    print "normalization factor for %s = %f +- %f" %(region, renorm, error)
    return renorm
#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("-vars"          , action='store', default='')
    parser.add_argument("-indir"        , action='store', default='')
    parser.add_argument("-outfile"      , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("-region"       , action='store', default="SR")
    args=parser.parse_args()

    print "Congratulations!"
    var_list = []
    variables = ['Mt', 'MET',  'AntiIDelPt']
    variables1 = ['Mt', 'MET', 'IDelPt']

    #AID_norm_path = 'FFAIDSR/FFAIDSR_FFAID/h_FFAIDSR_FFAID_Mt'
    #ID_norm_path  = 'FFIDSR/FFIDSR_FFID/h_FFIDSR_FFID_Mt'
    AID_norm_path = 'FFAIDSR/FFAIDSR_FFAID/h_FFAIDSR_FFAID_MET'
    ID_norm_path  = 'FFIDSR/FFIDSR_FFID/h_FFIDSR_FFID_MET'
    AID_lumi  = renorm(10.0, AID_norm_path, 'AID_norm', 'MET', args.indir, args.test)*10
    ID_lumi   = renorm(10.0, ID_norm_path,  'ID_norm',  'MET', args.indir, args.test)*10
    #AID_lumi  = renorm(10.0, AID_norm_path, 'AID_norm', 'Mt', args.indir, args.test)*10
    #ID_lumi   = renorm(10.0, ID_norm_path,  'ID_norm',  'Mt', args.indir, args.test)*10
    print "AID lumi %f" % AID_lumi
    print "ID lumi %f" % ID_lumi

    var_list = variables
    for v in var_list:
        AIDSR_skim_path = 'FFAIDSR/FFAIDSR_FFAID/h_FFAIDSR_FFAID_%s' % v
        if args.test: print "running plot()"
        plotCR(AID_lumi, AIDSR_skim_path, 'FFAID_skim', v,  args.indir, args.test)
    var_list = variables1
    for v in var_list:
        IDSR_skim_path = 'FFIDSR/FFIDSR_FFID/h_FFIDSR_FFID_%s' % v
        if args.test: print "running plot()"
        plotCR(ID_lumi, IDSR_skim_path, 'FFID_skim', v,  args.indir, args.test)

    AIDSRSR_MET_path = 'FFAIDSR/FFAIDSR_FFAIDSR/h_FFAIDSR_FFAIDSR_MET' 
    IDSRSR_MET_path = 'FFIDSR/FFIDSR_FFIDSR/h_FFIDSR_FFIDSR_MET'
    AIDSRSR_skim_path = 'FFAIDSR/FFAIDSR_FFAIDSR/h_FFAIDSR_FFAIDSR_AntiIDelPt'
    IDSRSR_skim_path = 'FFIDSR/FFIDSR_FFIDSR/h_FFIDSR_FFIDSR_IDelPt'

    plotCR(AID_lumi, AIDSRSR_MET_path, 'AIDSR_skim', 'MET',  args.indir, args.test)
    plotCR(ID_lumi, IDSRSR_MET_path, 'IDSR_skim', 'MET',  args.indir, args.test)

    num_list, num_error = plotSR(ID_lumi, IDSRSR_skim_path, 'IDSR_skim', 'IDelPt',  args.indir, args.test)
    denom_list, denom_error = plotSR(AID_lumi, AIDSRSR_skim_path, 'AIDSR_skim', 'AntiIDelPt',  args.indir, args.test)

    FFs, FF_err = divideAndErrors(num_list, num_error, denom_list, denom_error)


    if args.test:
        print "Done"

if __name__ == '__main__':
    main(sys.argv[1:])
 #]======================================================================
