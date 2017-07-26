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
def GetNameFromHistPath(hist_path):

    name = hist_path.replace('.root', '').split('/')[-1].split('_')[1]
    return name
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
def GetDecoHists(file_list, path_list, name_list, debug):
    if debug: print 'getting deco hists'
    hists = {}
    for f_name in file_list:
        #print IsData(name, debug)
        if IsData(f_name, debug):
            f = ROOT.TFile(f_name, 'READ')
            if debug:
                print f.GetName()
            for path, name in zip(path_list, name_list):
                if debug: print path, name, f.GetName()
                h = ROOT.TH1F
                h = f.Get(path)
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
def MakeDataStack(hist_list, lumi, debug):
    hs = ROOT.THStack("hist stack", "hist stack")
    hsum = SumMCHists(hist_list, lumi, debug)
    maxVal = hsum.GetBinContent(hsum.GetMaximumBin())*1000000*lumi
    minVal = 1.
    sortedHistTuple = sorted(hist_list.items(), key=lambda x: x[1].GetBinContent(x[1].GetMaximumBin()))
    if debug:
        print maxVal
        print 'in Data Stack'
        print hist_list
        print sortedHistTuple
    sortedKeyList = sorted(hist_list.keys())
    #colors = [40, 41, 42, 46, 49, 31, 38, 15]
    colors = [5, 3, 8, 2, 4, 7, 9, 51, 6]  #[yellow, Lgreen, Dgreen, red, blue, cyan, indigo, purple, magenta]
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
        h[1].SetMarkerSize(0)
        h[1].Scale(lumi)
        h[1].SetDirectory(0)
        hs.Add(h[1])
    hs.SetMaximum(maxVal)
    hs.SetMinimum(minVal)
    return hs

#======================================================================
def MakeHistStack(hist_list, lumi, debug):
    hs = ROOT.THStack("hist stack", "hist stack")
    hsum = SumMCHists(hist_list, lumi, debug)
    maxVal = hsum.GetBinContent(hsum.GetMaximumBin())*1000000*lumi
    minVal = 1.
    sortedHistTuple = sorted(hist_list.items(), key=lambda x: x[1].GetBinContent(x[1].GetMaximumBin()))
    if debug:
        print maxVal
        print 'in MakeMC'
        print hist_list
        print sortedHistTuple
    sortedKeyList = sorted(hist_list.keys())
    #colors = [40, 41, 42, 46, 49, 31, 38, 15]
    colors = [5, 4, 8, 2, 3, 7, 9, 51, 6]  #[yellow, Lgreen, Dgreen, red, blue, cyan, indigo, purple, magenta]
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
def SetRatioCanvas(name, region, var):
    global logYAxis
    c1 = ROOT.TCanvas("%s_%s_%s" % (name, region, var), "%s_%s" % (name, region), 0, 0, 800, 600)
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
    #l.SetNColumns(2)
    for hist in sortedHistTuple:
        l.AddEntry(hist[1], hist[0], 'f')
    #for hist, name in zip(sortedHistTuple, samples):
    #    l.AddEntry(hist, name, 'f')
    l.AddEntry(dataHist, 'all data', 'l')

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
def plotDeco(lumi, region, var, indir, debug):
    if debug: print "opening output file"
    o=ROOT.TFile("test.root", "RECREATE")
    if debug: print "Getting MC list"
    if var == 'AntiIDelPt':
        data_path = 'FFAIDSR/FFAIDSR_FFAIDSR/h_FFAIDSR_FFAIDSR_%s' % var
        deco_path_list = []
        deco_path_list.append('AID1/AID1_FFAIDSR/h_AID1_FFAIDSR_%s' % var)
        deco_path_list.append('AID2/AID2_FFAIDSR/h_AID2_FFAIDSR_%s' % var)
        deco_path_list.append('AID3/AID3_FFAIDSR/h_AID3_FFAIDSR_%s' % var)
        deco_path_list.append('AID12/AID12_FFAIDSR/h_AID12_FFAIDSR_%s' % var)
        deco_path_list.append('AID13/AID13_FFAIDSR/h_AID13_FFAIDSR_%s' % var)
        deco_path_list.append('AID23/AID23_FFAIDSR/h_AID23_FFAIDSR_%s' % var)
        deco_path_list.append('AID123/AID123_FFAIDSR/h_AID123_FFAIDSR_%s' % var)
    else:
        deco_path_list = []
        data_path = 'FFAIDSR/FFAIDSR_FFAID/h_FFAIDSR_FFAID_%s' % var
        deco_path_list.append('AID1/AID1_FFAID/h_AID1_FFAID_%s' % var)
        deco_path_list.append('AID2/AID2_FFAID/h_AID2_FFAID_%s' % var)
        deco_path_list.append('AID3/AID3_FFAID/h_AID3_FFAID_%s' % var)
        deco_path_list.append('AID12/AID12_FFAID/h_AID12_FFAID_%s' % var)
        deco_path_list.append('AID13/AID13_FFAID/h_AID13_FFAID_%s' % var)
        deco_path_list.append('AID23/AID23_FFAID/h_AID23_FFAID_%s' % var)
        deco_path_list.append('AID123/AID123_FFAID/h_AID123_FFAID_%s' % var)

    deco_name_list = []
    deco_name_list.append('fail_ID')
    deco_name_list.append('fail_ISO')
    deco_name_list.append('fail_D0')
    deco_name_list.append('fail_ID_ISO')
    deco_name_list.append('fail_ID_D0')
    deco_name_list.append('fail_ISO_D0')
    deco_name_list.append('fail_All')

    deco_hist_list = GetDecoHists(GetRootFiles(indir, debug), deco_path_list, deco_name_list, debug)
    if debug: print "Getting data hist"
    if debug: print deco_hist_list
    m_data = GetDataHists(GetRootFiles(indir, debug), data_path, debug)
    m_data.SetMarkerSize(0.5)
    if debug: print "Making deco hist stack"
    m_dstack = MakeDataStack(deco_hist_list, lumi,  debug)
    m_dsum = SumMCHists(deco_hist_list, lumi, debug)
    m_ratio = MakeNewRatio(m_data, m_dsum, debug)
    m_legend = MakeLegend(deco_hist_list, m_data, region)

    #canvas, p1 = SetSingleCanvas('canvas', region)
    canvas, p1, p2 = SetRatioCanvas('deco', region, var)
    p2.cd()
    m_ratio.Draw("P")
    p1.cd()
    m_dstack.Draw("HIST")
    m_data.Draw("HSAME")
    #m_data.Draw("PESAME")
    o.cd()
    #m_hstack.Write()
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
    canvas.Close()
    return True
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

    canvas, p1, p2 = SetRatioCanvas('CR', region, var)
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
    canvas.Print('%s_CR_%s.pdf' % (region, var))
    canvas.Close()
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
    print '*********** %s Fakes Factors in %s ***********' % (region, var)
    if (var == 'Njet' ):
        sum1 = 0.0
        err1 = 0.0
        for x in xrange(3, myRange+1):
            bkSubtract = m_data.GetBinContent(x) - m_hsum.GetBinContent(x)
            bkSubtract_error = m_data.GetBinError(x) - m_hsum.GetBinError(x)
            if x is 3:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            elif x is 4:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            elif x is 5:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            else:
                sum1 += bkSubtract
                err1 += bkSubtract_error
        value_list.append(sum1)
        error_list.append(err1)
    elif (var == 'Nbjet' ):
        sum1 = 0.0
        err1 = 0.0
        for x in xrange(1, myRange+1):
            bkSubtract = m_data.GetBinContent(x) - m_hsum.GetBinContent(x)
            bkSubtract_error = m_data.GetBinError(x) - m_hsum.GetBinError(x)
            if x is 1:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            elif x is 2:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            elif x is 3:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            else:
                sum1 += bkSubtract
                err1 += bkSubtract_error
        value_list.append(sum1)
        error_list.append(err1)
    elif (var == 'HT' ):
        sum1 = 0.0
        err1 = 0.0
        sum2 = 0.0
        err2 = 0.0
        for x in xrange(1, myRange+1):
            bkSubtract = m_data.GetBinContent(x) - m_hsum.GetBinContent(x)
            bkSubtract_error = m_data.GetBinError(x) - m_hsum.GetBinError(x)
            if x < 5:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            elif( x >= 5 and x < 7 ):
                sum1 += bkSubtract
                err1 += bkSubtract_error
            else:
                sum2 += bkSubtract
                err2 += bkSubtract_error
        value_list.append(sum1)
        error_list.append(err1)
        value_list.append(sum2)
        error_list.append(err2)
    elif( var == 'dphi_l1met' or var == 'dphi_j1met'):
        sum1 = 0.0
        err1 = 0.0
        for x in xrange(1, myRange+1):
            bkSubtract = m_data.GetBinContent(x) - m_hsum.GetBinContent(x)
            bkSubtract_error = m_data.GetBinError(x) - m_hsum.GetBinError(x)
            if x < 6:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            else:
                sum1 += bkSubtract
                err1 += bkSubtract_error
        value_list.append(sum1)
        error_list.append(err1)
    elif( var == 'J1pt' ):
        sum1 = 0.0
        err1 = 0.0
        sum2 = 0.0
        err2 = 0.0
        sum3 = 0.0
        err3 = 0.0
        for x in xrange(1, myRange+1):
            bkSubtract = m_data.GetBinContent(x) - m_hsum.GetBinContent(x)
            bkSubtract_error = m_data.GetBinError(x) - m_hsum.GetBinError(x)
            if x is 1:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            elif x is 2:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            elif x is 3:
                value_list.append(bkSubtract)
                error_list.append(bkSubtract_error)
            elif( x is 4 or x is 5 ): 
                sum1 += bkSubtract
                err1 += bkSubtract_error
            elif( x is 6 or x is 7 ):
                sum2 += bkSubtract
                err2 += bkSubtract_error
            else:
                sum3 += bkSubtract
                err3 += bkSubtract_error
        value_list.append(sum1)
        error_list.append(err1)
        value_list.append(sum2)
        error_list.append(err2)
        value_list.append(sum3)
        error_list.append(err3)
    elif (var == 'AntiIDelPt' or var == 'IDelPt' ):
        sum1 = 0.0
        err1 = 0.0
        sum2 = 0.0
        err2 = 0.0
        sum3 = 0.0
        err3 = 0.0
        for x in xrange(1, myRange+1):
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
    elif (var == 'Npv' ):
        sum1 = 0.0
        err1 = 0.0
        sum2 = 0.0
        err2 = 0.0
        sum3 = 0.0
        err3 = 0.0
        sum4 = 0.0
        err4 = 0.0
        sum5 = 0.0
        err5 = 0.0
        for x in xrange(1, myRange+1):
            bkSubtract = m_data.GetBinContent(x) - m_hsum.GetBinContent(x)
            bkSubtract_error = m_data.GetBinError(x) - m_hsum.GetBinError(x)
            #print ' bin %i = %f' % (x, bkSubtract)
            if( x < 6 ):
                sum1 += bkSubtract
                err1 += bkSubtract_error
            elif( x >= 6 and x < 11 ):
                sum2 += bkSubtract
                err2 += bkSubtract_error
            elif( x >= 11 and x < 16 ):
                sum3 += bkSubtract
                err3 += bkSubtract_error
            elif( x >= 16 and x < 21 ):
                sum4 += bkSubtract
                err4 += bkSubtract_error
            elif( x >= 21 ):
                sum5 += bkSubtract
                err5 += bkSubtract_error
        
        value_list.append(sum1)
        error_list.append(err1)
        value_list.append(sum2)
        error_list.append(err2)
        value_list.append(sum3)
        error_list.append(err3)
        value_list.append(sum4)
        error_list.append(err4)
        value_list.append(sum5)
        error_list.append(err5)
    else:
        for x in xrange(1, myRange+1):
            bkSubtract = m_data.GetBinContent(x) - m_hsum.GetBinContent(x)
            bkSubtract_error = m_data.GetBinError(x) - m_hsum.GetBinError(x)
            value_list.append(bkSubtract)
            error_list.append(bkSubtract_error)
    #Last entry for the average fake factor
    error_d = ROOT.Double()
    error_m = ROOT.Double()
    integral_d = m_data.IntegralAndError(1, myRange, error_d)
    integral_m = m_hsum.IntegralAndError(1, myRange, error_m)
    bkSubtract = integral_d - integral_m
    bkSubtract_error = error_d - error_m        
    value_list.append(bkSubtract)
    error_list.append(bkSubtract_error)

    #print value_list
    #print error_list
                
    m_ratio = MakeNewRatio(m_data, m_hsum, debug)
    m_legend = MakeLegend(BGhist_list, m_data, region)
    canvas, p1, p2 = SetRatioCanvas('SR', region, var)
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
    canvas.Print('%s_SR_%s.pdf' % (region, var))
    canvas.Close()
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
    if debug: print var
    if( var == 'Mt' ):
        integral_d = m_data.IntegralAndError(11, 20, error_d) #bins for MT 100-200 GeV
        integral_m = m_hsum.IntegralAndError(11, 20, error_m)
        #integral_d = m_data.IntegralAndError(13, 20, error_d)
        #integral_m = m_hsum.IntegralAndError(13, 20, error_m)
    elif( var == 'MET' ):
        integral_d = m_data.IntegralAndError(13, 15, error_d) #bins for MET >200 GeV
        integral_m = m_hsum.IntegralAndError(13, 15, error_m)

    renorm, error = divideAndError(integral_d, error_d, integral_m, error_m)
    print "normalization factor for %s = %f +- %f" %(region, renorm, error)
    return renorm
#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("-FFvar"        , action='store', default='')
    parser.add_argument("-indir"        , action='store', default='')
    parser.add_argument("-outfile"      , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("--doDeco"      , action='store_true')
    parser.add_argument("--doFF2D"      , action='store_true')
    parser.add_argument("--doFF"        , action='store_true')
    parser.add_argument("--doFFDeco"    , action='store_true')
    parser.add_argument("--doCR"        , action='store_true')
    parser.add_argument("--doCR2D"      , action='store_true')
    parser.add_argument("--doNum"       , action='store_true')
    parser.add_argument("-region"       , action='store', default="SR")
    args=parser.parse_args()

    print "Congratulations!"
    var_list = []
    variables_AID = ['Mt', 'MET',  'AntiIDelPt', 'AntiIDelEta', 'dphi_j1met', 'dphi_l1met', 'Njet', 'Nbjet', 'J1pt', 'HT', 'Mu', 'Npv' ]
    variables_ID = ['Mt', 'MET', 'IDelPt', 'IDelEta', 'dphi_j1met', 'dphi_l1met', 'Njet', 'Nbjet', 'J1pt', 'HT', 'Mu', 'Npv' ]

###################################################################################
    if args.doDeco:
        plotDeco(1.0, 'AID_deco', 'AntiIDelEta', args.indir, args.test)
        plotDeco(1.0, 'AID_deco', 'AntiIDelPt', args.indir, args.test)
        plotDeco(1.0, 'AID_deco', 'Mt', args.indir, args.test)
        plotDeco(1.0, 'AID_deco', 'MET', args.indir, args.test)
        plotDeco(1.0, 'AID_deco', 'Njet', args.indir, args.test)
        plotDeco(1.0, 'AID_deco', 'Nbjet', args.indir, args.test)
        plotDeco(1.0, 'AID_deco', 'dphi_j1met', args.indir, args.test)
        plotDeco(1.0, 'AID_deco', 'dphi_l1met', args.indir, args.test)
###################################################################################
    #Here do FF calc for every combiniation and plot decomposition for all AID electrons
    eta_list = ['07', '137', '152', '201', '247']
    norm_var = 'MET'
    #norm_var = 'Mt'
    ID_norm_path  = 'FFIDSR/FFIDSR_FFID/h_FFIDSR_FFID_%s' % norm_var
    ID_lumi   = renorm(10.0, ID_norm_path,  'ID_norm', norm_var, args.indir, args.test)*10
    AID_norm_path = 'FFAIDSR/FFAIDSR_FFAID/h_FFAIDSR_FFAID_%s' % norm_var
    AID_lumi  = renorm(10.0, AID_norm_path, 'AID_norm',norm_var, args.indir, args.test)*10

    if( args.doFF or args.doFF2D ):
        if( args.FFvar == 'eta' or args.FFvar == 'Eta' ):
            IDFF_var = 'IDelEta'
            AIDFF_var = 'AntiIDelEta'
        elif( args.FFvar == 'pt' or args.FFvar == 'Pt' ):
            IDFF_var = 'IDelPt'
            AIDFF_var = 'AntiIDelPt'
        elif( args.FFvar == 'MET' or args.FFvar == 'met' ):
            IDFF_var = 'MET'
            AIDFF_var = 'MET'
        elif( args.FFvar == 'dphi-jm' or args.FFvar == 'dPhi-jm' or args.FFvar == 'dphi-j1met'):
            IDFF_var = 'dphi_j1met'
            AIDFF_var = 'dphi_j1met'
        elif( args.FFvar == 'dphi-lm' or args.FFvar == 'dPhi-lm' or args.FFvar == 'dphi-l1met'):
            IDFF_var = 'dphi_l1met'
            AIDFF_var = 'dphi_l1met'
        elif( args.FFvar == 'njet' or args.FFvar == 'nJet' or args.FFvar == 'Njet'):
            IDFF_var = 'Njet'
            AIDFF_var = 'Njet'
        elif( args.FFvar == 'nbjet' or args.FFvar == 'nBJet' or args.FFvar == 'Nbjet'):
            IDFF_var = 'Nbjet'
            AIDFF_var = 'Nbjet'
        elif( args.FFvar == 'j1pt' or args.FFvar == 'J1pt' or args.FFvar == 'j1Pt'):
            IDFF_var = 'J1pt'
            AIDFF_var = 'J1pt'
        elif( args.FFvar == 'ht' or args.FFvar == 'HT' or args.FFvar == 'Ht'):
            IDFF_var = 'HT'
            AIDFF_var = 'HT'
        elif( args.FFvar == 'mu' or args.FFvar == 'MU' or args.FFvar == 'Mu'):
            IDFF_var = 'Mu'
            AIDFF_var = 'Mu'
        elif( args.FFvar == 'npv' or args.FFvar == 'NPV' or args.FFvar == 'Npv'):
            IDFF_var = 'Npv'
            AIDFF_var = 'Npv'
        else: 
            print "Which FF var?"
            print "Not calculating fake factros and exiting!"
            sys.exit()

    if args.doFF:
        print 'Making 1D FFs and SR plots'
        ID_SR_path = 'FFIDSR/FFIDSR_FFIDSR/h_FFIDSR_FFIDSR_%s' % IDFF_var
        AID_SR_path = 'FFAIDSR/FFAIDSR_FFAIDSR/h_FFAIDSR_FFAIDSR_%s' % AIDFF_var
        num_list, num_error = plotSR(ID_lumi, ID_SR_path, 'ID', IDFF_var,  args.indir, args.test)
        denom_list, denom_error = plotSR(AID_lumi, AID_SR_path, 'AID', AIDFF_var,  args.indir, args.test)
        print 'Writing FFs'
        FFs, FF_err = divideAndErrors(num_list, num_error, denom_list, denom_error)
        if args.doCR:
            print 'Making 1D CR plots'
            for v in variables_ID:
                ID_CR_path = 'FFIDSR/FFIDSR_FFID/h_FFIDSR_FFID_%s' % v
                if args.test: print "running plot()"
                plotCR(ID_lumi, ID_CR_path, 'ID', v,  args.indir, args.test)
            for v in variables_AID:
                AID_CR_path  = 'FFAIDSR/FFAIDSR_FFAID/h_FFAIDSR_FFAID_%s' % v
                plotCR(AID_lumi, AID_CR_path, 'AID', v,  args.indir, args.test)
        print '1D DONE %s' % args.FFvar 

    if args.doNum:
        AID_num_path = 'FFAIDSR/FFAIDSR_FFAIDSRNfill/h_FFAIDSR_FFAIDSRNfill_n_el'
        ID_num_path = 'FFIDSR/FFIDSR_FFIDSRNfill/h_FFIDSR_FFIDSRNfill_n_el'
        plotCR(10., AID_num_path, 'AID', 'n_el',  args.indir, args.test)
        plotCR(10., ID_num_path, 'ID', 'n_el',  args.indir, args.test)

    if args.doFF2D:
        print 'Making 2D FFs and SR plots'
        #Eta 0.0 - 0.7
        print 'Eta region 0.0 - 0.7'
        ID_SR_path = 'FFIDSR2D/FFIDSR2D_FFIDSREta07/h_FFIDSR2D_FFIDSREta07_%s' % IDFF_var
        num_list, num_error = plotSR(ID_lumi, ID_SR_path, 'ID_eta07', IDFF_var,  args.indir, args.test)

        AID_SR_path = 'FFAIDSR2D/FFAIDSR2D_FFAIDSREta07/h_FFAIDSR2D_FFAIDSREta07_%s' % AIDFF_var
        denom_list, denom_error = plotSR(AID_lumi, AID_SR_path, 'AID_eta07', AIDFF_var,  args.indir, args.test)
        print 'Writing FFs'
        FFs, FF_err = divideAndErrors(num_list, num_error, denom_list, denom_error)


        #Eta 0.7 - 1.37
        print 'Eta region 0.7 - 1.37'
        ID_SR_path = 'FFIDSR2D/FFIDSR2D_FFIDSREta137/h_FFIDSR2D_FFIDSREta137_%s' % IDFF_var
        num_list, num_error = plotSR(ID_lumi, ID_SR_path, 'ID_eta137', IDFF_var,  args.indir, args.test)

        AID_SR_path = 'FFAIDSR2D/FFAIDSR2D_FFAIDSREta137/h_FFAIDSR2D_FFAIDSREta137_%s' % AIDFF_var
        denom_list, denom_error = plotSR(AID_lumi, AID_SR_path, 'AID_eta137', AIDFF_var,  args.indir, args.test)
        print 'Writing FFs'
        FFs, FF_err = divideAndErrors(num_list, num_error, denom_list, denom_error)


        #Eta 1.37 - 1.52
        print 'Eta region 1.37 - 1.52'
        ID_SR_path = 'FFIDSR2D/FFIDSR2D_FFIDSREta152/h_FFIDSR2D_FFIDSREta152_%s' % IDFF_var
        num_list, num_error = plotSR(ID_lumi, ID_SR_path, 'ID_eta152', IDFF_var,  args.indir, args.test)

        AID_SR_path = 'FFAIDSR2D/FFAIDSR2D_FFAIDSREta152/h_FFAIDSR2D_FFAIDSREta152_%s' % AIDFF_var
        denom_list, denom_error = plotSR(AID_lumi, AID_SR_path, 'AID_eta152', AIDFF_var,  args.indir, args.test)
        print 'Writing FFs'
        FFs, FF_err = divideAndErrors(num_list, num_error, denom_list, denom_error)


        #Eta 1.52 - 2.01
        print 'Eta region 1.52 - 2.01'
        ID_SR_path = 'FFIDSR2D/FFIDSR2D_FFIDSREta201/h_FFIDSR2D_FFIDSREta201_%s' % IDFF_var
        num_list, num_error = plotSR(ID_lumi, ID_SR_path, 'ID_eta201', IDFF_var,  args.indir, args.test)

        AID_SR_path = 'FFAIDSR2D/FFAIDSR2D_FFAIDSREta201/h_FFAIDSR2D_FFAIDSREta201_%s' % AIDFF_var
        denom_list, denom_error = plotSR(AID_lumi, AID_SR_path, 'AID_eta201', AIDFF_var,  args.indir, args.test)
        print 'Writing FFs'
        FFs, FF_err = divideAndErrors(num_list, num_error, denom_list, denom_error)


        #Eta 2.01 - 2.47
        print 'Eta region 2.01 - 2.47'
        ID_SR_path = 'FFIDSR2D/FFIDSR2D_FFIDSREta247/h_FFIDSR2D_FFIDSREta247_%s' % IDFF_var
        num_list, num_error = plotSR(ID_lumi, ID_SR_path, 'ID_eta247', IDFF_var,  args.indir, args.test)

        AID_SR_path = 'FFAIDSR2D/FFAIDSR2D_FFAIDSREta247/h_FFAIDSR2D_FFAIDSREta247_%s' % AIDFF_var
        denom_list, denom_error = plotSR(AID_lumi, AID_SR_path, 'AID_eta247', AIDFF_var,  args.indir, args.test)
        print 'Writing FFs'
        FFs, FF_err = divideAndErrors(num_list, num_error, denom_list, denom_error)

    if args.doCR2D:
        print 'Making 2D CR plots'
        IDCR_path_list = []
        IDCR_path_list.append('FFIDSR2D/FFIDSR2D_FFIDEta07/h_FFIDSR2D_FFIDEta07_')
        IDCR_path_list.append('FFIDSR2D/FFIDSR2D_FFIDEta137/h_FFIDSR2D_FFIDEta137_')
        IDCR_path_list.append('FFIDSR2D/FFIDSR2D_FFIDEta152/h_FFIDSR2D_FFIDEta152_')
        IDCR_path_list.append('FFIDSR2D/FFIDSR2D_FFIDEta201/h_FFIDSR2D_FFIDEta201_')
        IDCR_path_list.append('FFIDSR2D/FFIDSR2D_FFIDEta247/h_FFIDSR2D_FFIDEta247_')

        AIDCR_path_list = []
        AIDCR_path_list.append('FFAIDSR2D/FFAIDSR2D_FFAIDEta07/h_FFAIDSR2D_FFAIDEta07_')
        AIDCR_path_list.append('FFAIDSR2D/FFAIDSR2D_FFAIDEta137/h_FFAIDSR2D_FFAIDEta137_')
        AIDCR_path_list.append('FFAIDSR2D/FFAIDSR2D_FFAIDEta152/h_FFAIDSR2D_FFAIDEta152_')
        AIDCR_path_list.append('FFAIDSR2D/FFAIDSR2D_FFAIDEta201/h_FFAIDSR2D_FFAIDEta201_')
        AIDCR_path_list.append('FFAIDSR2D/FFAIDSR2D_FFAIDEta247/h_FFAIDSR2D_FFAIDEta247_')

        for AIDCR, eta in zip(AIDCR_path_list, eta_list):
            for v in variables_AID:
                path = AIDCR+v
                plotCR(AID_lumi, path, 'AID_eta'+eta, v,  args.indir, args.test)
        for IDCR, eta in zip(IDCR_path_list, eta_list):
            for v in variables_ID:
                path = IDCR+v
                plotCR(ID_lumi, path, 'ID_eta'+eta, v, args.indir, args.test)

    if args.test:
        print "Done"

if __name__ == '__main__':
    main(sys.argv[1:])
 #]======================================================================
