#!/usr/bin/env python
"""
overlay_higgsino.py

author: Sheena Schier <sheena.schier@cern.ch>
created: 2016-01-01

"""
#------------------------------------------------------------------------------

## std
import optparse
import os
import time
import math

## ROOT
import ROOT
#ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = 1001
import rootlogon

##ATLAS STYLE
ROOT.gROOT.LoadMacro("atlasstyle-00-03-05/AtlasUtils.C")
ROOT.gROOT.LoadMacro("atlasstyle-00-03-05/AtlasStyle.C")
ROOT.gROOT.LoadMacro("atlasstyle-00-03-05/AtlasLabels.C")
ROOT.SetAtlasStyle()

## my modules
# import sigdigs
# import ascii_table
# import latex_table


timestamp = time.strftime('%Y-%m-%d-%Hh%M')


#_____________________________________________________________________________
def options():
    parser = optparse.OptionParser(description="options")
    parser.add_option('-S', '--no-signal', dest='no_signal', action='store_true', default=False)
    return parser.parse_args()

#______________________________________________________________________________
def main():
    ops, args = options()

    paths = []
    sample_names = []
    line_colors = []
    draw_options = []

    files = []
    hists = []
    hist_paths = []

    region = 'select'
    #region = 'EWsignal'
    #region = 'stopsignal'
    selection = 'dilepton'
    #selection = 'all'
    #selection = 'highmet'
   # selection = 'lowmet'
    hist_type = 'nLep_signal'
    hist_type = 'nJet30'
    hist_type = 'qlql'
    hist_type = 'lep_type'
    hist_type = 'Lep1Pt'
    #hist_type = 'Lep2Pt'
    #hist_type = 'Jet1Pt'
    #hist_type = 'Jet2Pt'
    #hist_type = 'mll'
    #hist_type = 'ptll'
    #hist_type = 'MET'
    #hist_type = 'dphi_j1met'
    #hist_type = 'dphi_j2met'
    #hist_type = 'dphi_l1met'
    #hist_type = 'MTauTau4'
    xTitle = 'ambiguous'
    if hist_type == 'nLep_signal': xTitle = 'Lepton Count'
    if hist_type == 'nJet30': xTitle = 'Jet Count'
    if hist_type == 'qlql': xTitle = 'Q_{l}Q_{l}'
    if hist_type == 'mll': xTitle = 'Dilepton Invariant Mass'
    if hist_type == 'ptll': xTitle = 'Dilepton Transverse Momentum'
    if hist_type == 'MET': xTitle = 'MET'
    if hist_type == 'lep_type': xTitle = 'Lepton Type'
    if hist_type == 'Lep1Pt': xTitle = 'Lep_{1} P_{T}'
    if hist_type == 'Lep2Pt': xTitle = 'Lep_{2} P_{T}'
    if hist_type == 'Jet1Pt': xTitle = 'Jet_{1} P_{T}'
    if hist_type == 'Jet2Pt': xTitle = 'Jet_{2} P_{T}'
    if hist_type == 'dphi_j1met': xTitle = '#Delta#phi_{leadJet-MET}'
    if hist_type == 'dphi_j2met': xTitle = '#Delta#phi_{Jet2-MET}'
    if hist_type == 'dphi_l1met': xTitle = '#Delta#phi_{leadLep-MET}'
    if hist_type == 'MTauTau4': xTitle = 'M_{#tau#tau}'


########################################################################
#### add paths, sample names, line colors, and draw options here ####
########################################################################

    ##Set path to point the directory where your root file is that contains the histogram you want to grab
    ##Choose a uniqu sample name that will appear in the legend


    #paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/output_393002.root']
    paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/1softLNoElISO_939002.root']
    #paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/1softLNoElISO_939002_stop.root']
    sample_names += ['C1N1 120_100']
    line_colors += [ROOT.kCyan]
    draw_options += ['HSAME']

    #paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/output_393001.root']
    paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/1softLNoElISO_939001.root']
    #paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/1softLNoElISO_939001_stop.root']
    sample_names += ['C1N1 110_100']
    line_colors += [ROOT.kMagenta + 1]
    draw_options += ['HSAME']

   # paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/1softLNoElISO_939003.root']
   # sample_names += ['C1N1 140_100']
   # line_colors += [ROOT.kOrange+9]
   # draw_options += ['HSAME']

    #paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/output_393000.root']
    paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/1softLNoElISO_939000.root']
    #paths += ['/export/home/sschier/workarea/HistMaker/SUSY-analysis/1softLNoElISO_939000_stop.root']
    sample_names += ['C1N1 105_100']
    line_colors += [ROOT.kBlue-1]
    draw_options += ['HSAME']

##############################################################################
#### If histogram paths are all different then need to fill list #########
#########################################################################

    # Most often the hist_path will just be the name of the histogram

   # hist_path = 'select/select_dilepton/h_select_dilepton_Lep1Pt'
    #hist_path = 'select/select_dilepton/h_select_dilepton_MET'
    #hist_path = 'select/select_dilepton/h_select_dilepton_mll'
    #hist_path = 'select/select_dilepton/h_select_dilepton_nLep_signal'
    #hist_path = 'select/select_dilepton/h_select_dilepton_%s' % hist_type
    hist_path = '%s/%s_%s/h_%s_%s_%s' % (region, region, selection, region, selection, hist_type)
    hist_name = os.path.basename(hist_path)

    if hist_type == 'ptll': binFactor = 5
    print hist_type
    #if hist_type == 'Lep1Pt': binFactor = 5
    if hist_type == 'Lep2Pt': binFactor = 5
    if hist_type == 'Jet1Pt': binFactor = 5
    if hist_type == 'Jet2Pt': binFactor = 5
    if hist_type == 'MET': binFactor = 2
    if hist_type == 'dphi_j2met': binFactor = 2
    if hist_type == 'dphi_l1met': binFactor = 2
    else: binFactor = 1

###################################################################
####  Print paths with names for sanity check

    for s, p in zip(sample_names, paths):
        print('%s = %s' % (s, p))

###################################################################
####  Load files and histogrmas into list #########################

    for p in paths:
        files += [ROOT.TFile(p)]

    for f in files:
        hists += [f.Get(hist_path)]

        #Use this if need to normalize one sample to another in some control region
   # for x in xrange(len(integrals)):
   #     factors += [(integrals[0] / integrals[x])]

#### Canvas 1 ####
    canvas = ROOT.TCanvas('c1', 'c1', 700, 500)
    #canvas.SetLogy(10)
    canvas.cd()

#### DRAW ####
    for hist, color, option in zip(hists, line_colors, draw_options):
        h = hist
        h.SetLineColor(color)
        h.SetMarkerColor(color)
        h.SetMarkerSize(1)
        h.SetLineWidth(2)
        h.SetStats(0)
        h.SetXTitle(xTitle)
        #h.SetXTitle("subleading jet p_{T}")
        #h.SetXTitle("#Delta#phi_{jet1-met}")
        #h.SetXTitle("dilepton invariant mass [GeV]")
        #h.Rebin(binFactor)
        #h.Sumw2()
        #h.Rebin(2)
        #h.Scale(scale)
        h.Draw(option)

#### LEGEND ####
    #legend = ROOT.TLegend(0.25,0.60,0.45,0.80)
    legend = ROOT.TLegend(0.65,0.65,0.85,0.85)
    #legend = ROOT.TLegend(0.55,0.55,0.75,0.75)
    for h, sn in zip(hists, sample_names):
        legend.AddEntry(h, sn, "lp")
        legend.SetBorderSize(0)
    legend.Draw()


#### LABELS ####

    #ROOT.ATLASLabel(0.5, 0.5,"Work in progress")
    #ROOT.myText(       0.5,  0.45, 1, "mc15c #sqrt{s}= 13 TeV")
    #ROOT.ATLASLabel(0.2, 0.9,"Work in progress")
    #ROOT.myText(       0.2,  0.85, 1, "mc15c #sqrt{s}= 13 TeV")
    ROOT.ATLASLabel(0.6, 0.9,"Work in progress")
    ROOT.myText(       0.6,  0.85, 1, "mc15c #sqrt{s}= 13 TeV")

    canvas.SaveAs('%s.png' % hist_name)
    canvas.SaveAs('%s.tex' % hist_name)
    canvas.SaveAs('%s.pdf' % hist_name)
    raw_input("-->")


#______________________________________________________________________________
if __name__ == '__main__': main()

