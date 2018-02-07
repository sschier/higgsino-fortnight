#!/usr/bin/env python

import condor
import commands, glob

exe = 'simpleMaker.py'
base_dir = '/export/share/dirac/sschier/submitDir_bkgndSoft_allSys_fullJES/mc15e/bkgndSoft/trees/singletop/'
arg_template = ' --input=%s --tree=tree --outfile=outputHist_singletop.root'
input_files = glob.glob(base_dir+'*/*')
condor.run(exe, arg_template, input_files, dirname='singletop_run_dir', nfiles=1)
#condor.run(exe, arg_template, input_files, dirname='my_run_dir', n_files=1)
