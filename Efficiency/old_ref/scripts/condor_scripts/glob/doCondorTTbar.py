#!/usr/bin/env python

import condor
import commands, glob

exe = 'simpleMaker.py'
base_dir = '/export/share/dirac/sschier/submitDir_bkgndSoft_allSys_fullJES/mc15e/bkgndSoft/trees/ttbar/'
arg_template = ' --input=%s --tree=tree --outfile=outputHist_ttbar.root'
input_files = glob.glob(base_dir+'*/*')
condor.run(exe, arg_template, input_files, dirname='ttbar_run_dir', nfiles=1)
