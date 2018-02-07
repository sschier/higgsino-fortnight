#!/usr/bin/env python

import condor
import commands, glob
import time, datetime

exe = '../FFMaker_j100.py'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')
base_dir = '/export/share/data/sschier/FakeLepton/June22_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_WithMoreIsolationVars/'

arg_template = ' -input=%s -tree=top_Nom -outfile=outputHist_ttbar.root'
input_files = glob.glob(base_dir+'ttbar_mu_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100/ttbar' % st, nfiles=1)

arg_template = ' -input=%s -tree=wjet_Nom -outfile=outputHist_wjets.root'
input_files = glob.glob(base_dir+'wjets_mu_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100/wjets' % st, nfiles=1)

arg_template = ' -input=%s -tree=zjet_Nom -outfile=outputHist_zjets.root'
input_files = glob.glob(base_dir+'zjets_mu_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100/zjets' % st, nfiles=1)

arg_template = ' -input=%s -tree=top_Nom -outfile=outputHist_singletop.root'
input_files = glob.glob(base_dir+'singletop_mu_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100/singletop' % st, nfiles=1)

arg_template = ' -input=%s -isData=data16 -tree=data -outfile=outputHist_data16.root'
input_files = glob.glob(base_dir+'data16_mu_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100/data16' % st, nfiles=1)

arg_template = ' -input=%s -isData=data15 -tree=data -outfile=outputHist_data15.root'
input_files = glob.glob(base_dir+'data15_mu_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100/data15' % st, nfiles=1)
