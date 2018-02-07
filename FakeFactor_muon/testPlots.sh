mkdir plots_test
cd plots_test
#python ../FFPlotter_B.py -FFvar='Pt' -normvar 'MET' --doFF --doCR -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
python ../FFPlotter_B.py -FFvar='Pt' -normvar 'MET' -renormSyst 'MET175' --doFF --doCR -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
..
