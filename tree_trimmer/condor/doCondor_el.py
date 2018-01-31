#!/usr/bin/env python

import condor
import commands, glob
import time, datetime

exe = '../tree_trimmer.py'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')

#base_dir = '/export/share/data/sschier/FakeLepton/June22_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_WithMoreIsolationVars/'
base_dir = '/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/'

arg_template = '-s skim %s /export/home/sschier/workarea/tree_trimmer/skims/skim-ff-el.py -t wjet_Nom -b /export/home/sschier/workarea/tree_trimmer/boff/bon-el.txt -o skim.root'
input_files = glob.glob(base_dir+'wjets/*')
condor.run(exe, arg_template, input_files, dirname='wjets_el_skims', nfiles=1)

arg_template = '-s skim %s /export/home/sschier/workarea/tree_trimmer/skims/skim-ff-el.py -t zjet_Nom -b /export/home/sschier/workarea/tree_trimmer/boff/bon-el.txt -o skim.root'
input_files = glob.glob(base_dir+'zjets/*')
condor.run(exe, arg_template, input_files, dirname='zjets_el_skims', nfiles=1)

arg_template = '-s skim %s /export/home/sschier/workarea/tree_trimmer/skims/skim-ff-el.py -t top_Nom -b /export/home/sschier/workarea/tree_trimmer/boff/bon-el.txt -o skim.root'
input_files = glob.glob(base_dir+'singletop/*')
condor.run(exe, arg_template, input_files, dirname='singletop_el_skims', nfiles=1)

arg_template = '-s skim %s /export/home/sschier/workarea/tree_trimmer/skims/skim-ff-el.py -t top_Nom -b /export/home/sschier/workarea/tree_trimmer/boff/bon-el.txt -o skim.root'
input_files = glob.glob(base_dir+'ttbar/*')
condor.run(exe, arg_template, input_files, dirname='ttbar_el_skims', nfiles=1)

arg_template = '-s skim %s /export/home/sschier/workarea/tree_trimmer/skims/skim-ff-el.py -t data -b /export/home/sschier/workarea/tree_trimmer/boff/bon-el.txt -o skim.root'
input_files = glob.glob(base_dir+'data16_13TeV/*')
condor.run(exe, arg_template, input_files, dirname='data16_el_skims', nfiles=1)
input_files = glob.glob(base_dir+'data15_13TeV/*')
condor.run(exe, arg_template, input_files, dirname='data15_el_skims', nfiles=1)
