#!/usr/bin/env python

import condor
import commands, glob
import time, datetime

exe = '../FFMaker.py'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')
base_dir = '/export/share/data/sschier/FakeLepton/mu_trigger_skims/'

arg_template = ' -input=%s -tree=ttbar -outfile=outputHist_ttbar.root'
input_files = glob.glob(base_dir+'ttbar_skim/*.root')
condor.run(exe, arg_template, input_files, dirname='ttbar_run_dir_%s' % st, nfiles=1)

arg_template = ' -input=%s -tree=wjets_22 -outfile=outputHist_wjets.root'
input_files = glob.glob(base_dir+'wjets_skim/*.root')
condor.run(exe, arg_template, input_files, dirname='wjets_run_dir_%s' % st, nfiles=1)

arg_template = ' -input=%s -tree=zjets_22 -outfile=outputHist_zjets.root'
input_files = glob.glob(base_dir+'zjets_skim/*.root')
condor.run(exe, arg_template, input_files, dirname='zjets_run_dir_%s' % st, nfiles=1)

arg_template = ' -input=%s -tree=singletop -outfile=outputHist_singletop.root'
input_files = glob.glob(base_dir+'singletop_skim/*.root')
condor.run(exe, arg_template, input_files, dirname='singletop_run_dir_%s' % st, nfiles=1)

#base_dir = '/export/share/data/sschier/FakeLepton/June16_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_data/'
base_dir = '/export/share/data/sschier/FakeLepton/full_samples_2_4_25/'
arg_template = ' -input=%s -isData=data16 -tree=CollectionTree -outfile=outputHist_data16.root'
input_files = glob.glob(base_dir+'data16_13TeV/*.root')
condor.run(exe, arg_template, input_files, dirname='data16_run_dir_%s' % st, nfiles=1)

arg_template = ' -input=%s -isData=data15 -tree=CollectionTree -outfile=outputHist_data15.root'
input_files = glob.glob(base_dir+'data15_13TeV/*.root')
condor.run(exe, arg_template, input_files, dirname='data15_run_dir_%s' % st, nfiles=1)
