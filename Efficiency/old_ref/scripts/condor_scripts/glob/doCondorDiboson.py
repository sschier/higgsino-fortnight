#!/usr/bin/env python

import condor
import commands, glob

exe = 'simpleMaker.py'
base_dir = '/export/share/dirac/sschier/submitDir_bkgndSoft_allSys_fullJES/mc15e/bkgndSoft/trees/wjets/'
arg_template = ' --input=%s --tree=tree --outfile=outputHist_diboson.root'
input_files = glob.glob(base_dir+'*/*')
condor.run(exe, arg_template, input_files, dirname='diboson_run_dir', nfiles=1)
