#!/usr/bin/env python

import condor
import commands, glob
import time, datetime

exe = '../FFMaker_j100.py'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')
#base_dir = '/export/share/data/sschier/FakeLepton/June22_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_WithMoreIsolationVars/'
base_dir = '/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/'

arg_template = ' -input=%s -tree=top_Nom -outfile=outputHist_ttbar.root -AIDvariation=BLayer -SYSvariation=mtDOWN'
input_files = glob.glob(base_dir+'ttbar_el_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100_mtDOWN/ttbar' % st, nfiles=1)

arg_template = ' -input=%s -tree=wjet_Nom -outfile=outputHist_wjets.root -AIDvariation=BLayer -SYSvariation=mtDOWN'
input_files = glob.glob(base_dir+'wjets_el_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100_mtDOWN/wjets' % st, nfiles=1)

arg_template = ' -input=%s -tree=zjet_Nom -outfile=outputHist_zjets.root -AIDvariation=BLayer -SYSvariation=mtDOWN'
input_files = glob.glob(base_dir+'zjets_el_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100_mtDOWN/zjets' % st, nfiles=1)

arg_template = ' -input=%s -tree=top_Nom -outfile=outputHist_singletop.root -AIDvariation=BLayer -SYSvariation=mtDOWN'
input_files = glob.glob(base_dir+'singletop_el_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100_mtDOWN/singletop' % st, nfiles=1)

arg_template = ' -input=%s -isData=data16 -tree=data -outfile=outputHist_data16.root -AIDvariation=BLayer -SYSvariation=mtDOWN'
input_files = glob.glob(base_dir+'data16_el_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100_mtDOWN/data16' % st, nfiles=1)

arg_template = ' -input=%s -isData=data15 -tree=data -outfile=outputHist_data15.root -AIDvariation=BLayer -SYSvariation=mtDOWN'
input_files = glob.glob(base_dir+'data15_el_skims/job*/skim.root')
condor.run(exe, arg_template, input_files, dirname='%s_j100_mtDOWN/data15' % st, nfiles=1)
