#!/usr/bin/env python

#IMPORTS
import ROOT
from ROOT import RooStats
import sys, copy, os
import argparse, subprocess, commands
import math

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
def IsData(file_name):
    isData = False
    print 'in isData'
    name = file_name.replace('.root', '').split('/')[-1].split('_')
    print name
    for n in name:
        if n in data_names:
            isData =  True
        print isData
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
        print IsData(name)
        if IsData(name):
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
        print '***************'
        print name
        print '**************'
        if debug: print IsBkgnd(string)
        if IsBkgnd(string):
            f = ROOT.TFile(string, 'READ')
            if debug: print 'file is %s' % f
            h = f.Get(hist_path)
            print h
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
def SumMCHists(hist_list, lumi):
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
    hsum = SumMCHists(hist_list, lumi)
    maxVal = hsum.GetBinContent(hsum.GetMaximumBin())*100*lumi
    print maxVal
    sortedHistTuple = sorted(hist_list.items(), key=lambda x: x[1].GetBinContent(x[1].GetMaximumBin()))
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
def MakeNewRatio(topHist, bottomHist):
    print '**debuging ratio plot'
    print bottomHist.GetBinContent(bottomHist.GetMaximumBin())
    print topHist.GetBinContent(topHist.GetMaximumBin())
    rh = copy.deepcopy(topHist)
    rh.SetDirectory(0)
    rh.Divide(bottomHist)
    rh.SetMinimum(0)
    rh.SetMaximum(10)
    print topHist.GetXaxis().GetTitle()
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
def plotCR(sample_path, region, variable, indir, debug):
    if debug: print "opening output file"
    o=ROOT.TFile("test.root", "RECREATE")
    print "Setting variable to plot"
    var = variable
    #lumi = 36000.
    lumi = 21.67
    #To renormalize data to 10fb, multiply by 0.2777
    print "Getting MC list"
    #MChist_list = GetMCHists(GetRootFiles(indir, 0), sample_path, debug)
    BGhist_list = GetBGHists(GetRootFiles(indir, 0), sample_path, debug)
    print "Getting data hist"
    m_data = GetDataHists(GetRootFiles(indir, 1), sample_path, debug)
    #m_data.Scale(0.00028)
    print "Making MC hist stack"
    m_hstack = MakeHistStack(BGhist_list, lumi,  debug)
    m_hsum = SumMCHists(BGhist_list, lumi)
    print m_hsum.GetBinContent(m_hsum.GetMaximumBin())
    m_ratio = MakeNewRatio(m_data, m_hsum)
    m_legend = MakeLegend(BGhist_list, m_data, region)
    #canvas, p1, p2 = SetCanvas('%s' % var, region)
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
def plot(sample_path, region, variable, lumi, indir, debug):
    ROOT.gStyle.SetLegendBorderSize(0)
    ROOT.gROOT.ForceStyle()
    if debug: print "opening output file"
    var = variable
    BGhist_list = GetBGHists(GetRootFiles(indir, 0), sample_path, debug)
    m_signals   = GetSignalHists(GetRootFiles(indir, 0), sample_path, debug)

    sortedKeyList = sorted(m_signals.keys(), reverse=True)
    print sortedKeyList
    #m_data      = GetDataHists(GetRootFiles(indir, 0), sample_path, debug)
    m_hstack    = MakeHistStack(BGhist_list, lumi, debug)
    m_hsum      = SumMCHists(BGhist_list, lumi)
    m_legend    = MakeSignalLegend(BGhist_list, m_signals, region)
    

    #signal colors and styles
    line_colors = [2, 3, 4, 5]
    line_styles = [5, 6, 7, 8]
    newlist = []

    canvas, p1, p2 = SetCanvas('canvas', region)
    p1.cd()
    #m_hstack.Scale(36000)
    #m_hstack.Draw("HIST")
    m_hstack.Draw("HIST")
    for sh, lc, ls in zip(sortedKeyList, line_colors, line_styles):
        m_signals[sh].SetLineColor(lc)
        m_signals[sh].SetMarkerColor(lc)
        m_signals[sh].SetLineStyle(ls)
        m_signals[sh].SetLineWidth(2)
        m_signals[sh].SetMarkerSize(0)
        m_signals[sh].Scale(lumi)
        #m_signals[sh].GetYaxis().SetTitle("Events / 2 GeV")
        m_signals[sh].Draw("HSAME")
        newlist.append(copy.deepcopy(m_signals[sh]))
    for hist in newlist:
        hist.SetMarkerSize(1)
        
    p2.cd()
    m_zn1 = MakeZn(newlist[0], m_hsum, 0.20)
    m_zn1.Draw("HISTP0")
    m_zn2 = MakeZn(newlist[1], m_hsum, 0.20)
    m_zn2.Draw("HISTP0SAME")

    p1.cd()
    canvas.cd()
    m_legend.Draw()
    ROOT.myText(       0.21,  0.85, 1, "36.0fb^{-1}@ #sqrt{s}= 13 TeV")
    #ROOT.myText(       0.41,  0.80, 1, "data16PeriodK")
    #ROOT.myText(       0.41,  0.85, 1, "%s" % region)
    ROOT.ATLASLabel(0.21,0.90,"Internal")
    #c2, p3 = DataCanvas(region)
    #m_data.Draw()
    #raw_input("-->")
    canvas.Print('%s_%s.pdf' % (region, var))
    return True
#======================================================================
def plotSR(sample_path, region, variable, indir, debug):
    ROOT.gStyle.SetLegendBorderSize(0)
    ROOT.gROOT.ForceStyle()
    if debug: print "opening output file"
    o=ROOT.TFile("test.root", "RECREATE")
    var = variable
    #Lists of histograms
    BGhist_list = GetBGHists(GetRootFiles(indir, 0), sample_path, debug)

    #Plottable objects
    m_signals   = GetSignalHists(GetRootFiles(indir, 0), sample_path, debug)
    print m_signals
    sortedKeyList = sorted(m_signals.keys(), reverse=True)
    print sortedKeyList
    #m_data      = GetDataHists(GetRootFiles(indir, 0), sample_path, debug)
    m_hstack    = MakeHistStack(BGhist_list, debug)
    m_hsum      = SumMCHists(BGhist_list)
    #m_ratio     = MakeNewRatio(m_data, m_hsum)
    #m_legend    = MakeLegend(BGhist_list, m_data, region)
    #m_legend    = MakeLegend(BGhist_list, region)
    m_legend    = MakeSignalLegend(BGhist_list, m_signals, region)
    

    #signal colors and styles
    line_colors = [2, 3, 4, 5]
    line_styles = [5, 6, 7, 8]
    newlist = []

    canvas, p1, p2 = SetRatioCanvas('canvas', region)
    p1.cd()
    m_hstack.Draw("HIST")
    for sh, lc, ls in zip(sortedKeyList, line_colors, line_styles):
        m_signals[sh].SetLineColor(lc)
        m_signals[sh].SetMarkerColor(lc)
        m_signals[sh].SetLineStyle(ls)
        m_signals[sh].SetLineWidth(5)
        m_signals[sh].SetMarkerSize(0)
        m_signals[sh].GetYaxis().SetTitle("Events / 2 GeV")
        m_signals[sh].Draw("HSAME")
        newlist.append(copy.deepcopy(m_signals[sh]))
    for hist in newlist:
        hist.SetMarkerSize(1)
        
    p2.cd()
    m_zn1 = MakeZn(newlist[0], m_hsum, 0.20)
    m_zn1.Draw("HISTP0")
    m_zn2 = MakeZn(newlist[1], m_hsum, 0.20)
    m_zn2.Draw("HISTP0SAME")
    m_zn3 = MakeZn(newlist[2], m_hsum, 0.20)
    m_zn3.Draw("HISTP0SAME")
    m_zn4 = MakeZn(newlist[3], m_hsum, 0.20)
    m_zn4.Draw("HISTP0SAME")
    #m_ratio.Draw("P")
        
    o.cd()
    m_hstack.Write()
    canvas.Write()

    p1.cd()
    canvas.cd()
    m_legend.Draw()
    ROOT.myText(       0.21,  0.85, 1, "36.3fb^{-1}@ #sqrt{s}= 13 TeV")
    #ROOT.myText(       0.41,  0.80, 1, "data16PeriodK")
    #ROOT.myText(       0.41,  0.85, 1, "%s" % region)
    ROOT.ATLASLabel(0.21,0.90,"Internal")
    #c2, p3 = DataCanvas(region)
    #m_data.Draw()
    #raw_input("-->")
    canvas.Print('%s_%s.pdf' % (region, var))
    return True
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
    variables = ['Mt', 'MET', 'IDelPt', 'AntiIDelPt']
    variables1 = ['elpt']

    if args.vars == '0': var_list = variables
    elif args.vars == '1': var_list = variables1

    var_list = variables
    for v in var_list:
        #print v
        skim_path = 'FFCR/FFCR_all/h_FFCR_all_%s' % v
        #IDSR_skim_path = 'FFCR/FFCR_idel/h_FFCR_idel_%s' % v
        #AIDSR_skim_path = 'FFCR/FFCR_antiidel/h_FFCR_antiidel_%s' % v
        IDSR_skim_path = 'FFIDSR/FFIDSR_FFID/h_FFIDSR_FFID_%s' % v
        AIDSR_skim_path = 'FFAIDSR/FFAIDSR_FFAID/h_FFAIDSR_FFAID_%s' % v

        if args.test: print "running plot()"
        plotCR(skim_path, 'skim', v,  args.indir, args.test)
        plotCR(IDSR_skim_path, 'FFCRID_skim', v,  args.indir, args.test)
        plotCR(AIDSR_skim_path, 'FFCRAID_skim', v,  args.indir, args.test)
    IDSRSR_skim_path = 'FFIDSR/FFIDSR_FFIDSR/h_FFIDSR_FFIDSR_IDelPt'
    AIDSRSR_skim_path = 'FFAIDSR/FFAIDSR_FFAIDSR/h_FFAIDSR_FFAIDSR_AntiIDelPt'
    plotCR(IDSRSR_skim_path, 'IDSR_skim', 'IDelPt',  args.indir, args.test)
    plotCR(AIDSRSR_skim_path, 'AIDSR_skim', 'AntiIDelPt',  args.indir, args.test)

    #path = 'mtt/mtt_validation/h_mtt_validation_MTauTau'
    #plot(path, 'validate', 'MTauTau', 36000, args.indir, args.test) 


    if args.test:
        print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
