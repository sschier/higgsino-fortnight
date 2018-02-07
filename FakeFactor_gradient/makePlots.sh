mkdir plots_201709100528_j100
cd plots_201709100528_j100
#python ../FFPlotter.py -FFvar='pt' --doFF  --doCR -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
#python ../FFPlotter.py -FFvar='pt' --doDeco -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
python ../FFPlotter.py -FFvar='nbjet' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
python ../FFPlotter.py -FFvar='njet' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
python ../FFPlotter.py -FFvar='eta' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
python ../FFPlotter.py -FFvar='dphi-jm' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
python ../FFPlotter.py -FFvar='dphi-lm' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
python ../FFPlotter.py -FFvar='ht' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
python ../FFPlotter.py -FFvar='mu' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
python ../FFPlotter.py -FFvar='npv' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
..
#mkdir plots_201709100548_j100_mtUP
#cd plots_201709100548_j100_mtUP
#python ../FFPlotter.py -FFvar='pt' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100548_j100_mtUP/run_dir'
#..
#mkdir plots_201709100550_j100_mtDOWN
#cd plots_201709100550_j100_mtDOWN
#python ../FFPlotter.py -FFvar='pt' --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100550_j100_mtDOWN/run_dir'
#..
#mkdir plots_201709100528_j100_renormSyst
#cd plots_201709100528_j100_renormSyst
#python ../FFPlotter.py -FFvar='pt' --doFF -renorm 'up' -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
#python ../FFPlotter.py -FFvar='pt' --doFF -renorm 'down' -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
#python ../FFPlotter.py -FFvar='pt' --doFF -renorm 'MET150' -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
#python ../FFPlotter.py -FFvar='pt' --doFF -normvar 'Mt' -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
#..
