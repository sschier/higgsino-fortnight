#!/usr/bin/env python

import condor
import commands, glob
import time, datetime

exe = '../FFMaker.py'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')
base_dir = '/export/share/data/sschier/FakeLepton/mu_trigger_skims/'

arg_template = ' -input=%s -variation=pileup -tree=ttbar -outfile=outputHist_ttbar.root'
input_files = glob.glob(base_dir+'ttbar_skim/*')
condor.run(exe, arg_template, input_files, dirname='ttbar_pileup_run_dir_%s' % st, nfiles=1)

arg_template = ' -input=%s -variation=pileup -tree=wjets_22 -outfile=outputHist_wjets.root'
input_files = glob.glob(base_dir+'wjets_skim/*')
condor.run(exe, arg_template, input_files, dirname='wjets_pileup_run_dir_%s' % st, nfiles=1)

arg_template = ' -input=%s -variation=pileup -tree=zjets_22 -outfile=outputHist_zjets.root'
input_files = glob.glob(base_dir+'zjets_skim/*')
condor.run(exe, arg_template, input_files, dirname='zjets_pileup_run_dir_%s' % st, nfiles=1)

arg_template = ' -input=%s -variation=pileup -tree=singletop -outfile=outputHist_singletop.root'
input_files = glob.glob(base_dir+'singletop_skim/*')
condor.run(exe, arg_template, input_files, dirname='singletop_pileup_run_dir_%s' % st, nfiles=1)

base_dir = '/export/share/data/sschier/FakeLepton/full_samples_2_4_25/'
#base_dir = '/export/share/data/sschier/FakeLepton/June16_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_data/'
arg_template = ' -input=%s -variation=pileup -isData=data16 -tree=CollectionTree -outfile=outputHist_data16.root'
input_files = glob.glob(base_dir+'data16_13TeV/*')
#input_files = glob.glob(base_dir+'data16_skim/*')
condor.run(exe, arg_template, input_files, dirname='data16_pileup_run_dir_%s' % st, nfiles=1)

arg_template = ' -input=%s -variation=pileup -isData=data15 -tree=CollectionTree -outfile=outputHist_data15.root'
input_files = glob.glob(base_dir+'data15_13TeV/*')
#input_files = glob.glob(base_dir+'data15_skim/*')
condor.run(exe, arg_template, input_files, dirname='data15_pileup_run_dir_%s' % st, nfiles=1)
