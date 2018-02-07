#mkdir plots_Deco
#cd plots_Deco
#python ../FFPlotter.py  -vars='0'  --doDeco -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707201713_nominal/run_dir'
#..

#mkdir plots_201707201315_nominal
#cd plots_201707201315_nominal
#python ../FFPlotter.py  -FFvar='Eta'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707201315_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='MET'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707201315_nominal/run_dir'
#..
#mkdir plots_201707221942_normMET
#cd plots_201707221942_normMET
#mkdir plots_201707221942_nominal
#cd plots_201707221942_nominal
#python ../FFPlotter.py  -FFvar='Pt' --doDeco   -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707281513_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='Pt' --doCR  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='Eta'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
##python ../FFPlotter.py  -FFvar='MET'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='dphi-jm'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='dphi-lm'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='njet'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='nbjet'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='j1pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='ht'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='mu'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py  -FFvar='npv'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'
#python ../FFPlotter.py -FFvar='pt' --doFF2D --doCR2D -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707221942_nominal/run_dir'

##These were for final deco plots
#mkdir plots_201707281513_nominal
#cd plots_201707281513_nominal
#python ../FFPlotter.py  -FFvar='Pt' --doDeco   -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707281513_nominal/run_dir'
#..

##These are for systematic variations
#mkdir systematics/nominal_mtUP
#cd systematics/nominal_mtUP
#python ../../FFPlotter.py  -FFvar='Pt' --doFF --doFF2D   -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707310024_nominal_mtUP/run_dir'
#...
#mkdir systematics/nominal_mtDOWN
#cd systematics/nominal_mtDOWN
#python ../../FFPlotter.py  -FFvar='Pt' --doFF --doFF2D   -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707310023_nominal_mtDOWN/run_dir'
#...
#mkdir systematics/prompt_sub_X12
#cd systematics/prompt_sub_X12
#python ../../FFPlotter.py  -FFvar='Pt' --doFF --doFF2D   -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707281513_nominal/run_dir'
#...
#mkdir systematics/renorm_Mt_80_180
#cd systematics/renorm_Mt_80_180
#python ../../FFPlotter.py  -FFvar='Pt' --doFF --doFF2D   -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201707281513_nominal/run_dir'
#...
#mkdir plots_201708171212_bjetBins
#cd plots_201708171212_bjetBins
#python ../FFPlotter_B.py  -FFvar='Pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171212_bjetBins/run_dir'
#python ../FFPlotter_B.py  -FFvar='j1pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171212_bjetBins/run_dir'
#..
#mkdir plots_201708171348_bjetBinsj75
#cd plots_201708171348_bjetBinsj75
#python ../FFPlotter_B.py  -FFvar='Pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171348_bjetBinsj75/run_dir'
#..
#mkdir plots_201708171349_bjetBinsj100
#cd plots_201708171349_bjetBinsj100
#python ../FFPlotter_B.py  -FFvar='Pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171349_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='Eta'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171349_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='njet'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171349_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='Ht'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171349_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='Mu'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171349_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='npv'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171349_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='dphi-jm'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171349_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='dphi-lm'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201708171349_bjetBinsj100/run_dir'
#..
#mkdir plots_201709100535_bjetBinsj100
#cd plots_201709100535_bjetBinsj100
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF --doCR --doCRmt --doCRmet -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#echo "NEXT: kinematic variation"
#python ../FFPlotter_B.py  -FFvar='Eta'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='njet'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='Ht'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='Mu'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='npv'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='dphi-jm'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='dphi-lm'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#..
#echo "NEXT: mt UP"
#mkdir plots_201709100544_bjetBinsj100_mtUP
#cd plots_201709100544_bjetBinsj100_mtUP
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100544_bjetBinsj100_mtUP/run_dir'
#..
#echo "NEXT: mt down"
#mkdir plots_201709100546_bjetBinsj100_mtDOWN
#cd plots_201709100546_bjetBinsj100_mtDOWN
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100546_bjetBinsj100_mtDOWN/run_dir'
#..
#echo "NEXT: renorm systematics"
#mkdir plots_201709100535_bjetBinsj100_renormSyst
#cd plots_201709100535_bjetBinsj100_renormSyst
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF -renorm 'up' -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF -renorm 'down' -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#..
#echo "NEXT: Renorm in MET"
#mkdir plots_201709100535_bjetBinsj100_normMET
#cd plots_201709100535_bjetBinsj100_normMET
#python ../FFPlotter_B.py -FFvar='Pt' -normvar 'MET'  --doFF --doCR --doCRmt --doCRmet -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#..

mkdir plots_official_bjetBinsj100
cd plots_official_bjetBinsj100
python ../FFPlotter_B.py -FFvar='Pt'  --doDeco -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF --doCR --doCRmt --doCRmet -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#echo "NEXT: kinematic variation"
#python ../FFPlotter_B.py  -FFvar='Eta'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='njet'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
##python ../FFPlotter_B.py  -FFvar='Ht'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='Mu'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='npv'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='dphi-jm'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py  -FFvar='dphi-lm'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
..
#echo "NEXT: mt UP"
#mkdir plots_official_bjetBinsj100_mtUP
#cd plots_official_bjetBinsj100_mtUP
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100544_bjetBinsj100_mtUP/run_dir'
#..
#echo "NEXT: mt down"
#mkdir plots_official_bjetBinsj100_mtDOWN
#cd plots_official_bjetBinsj100_mtDOWN
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100546_bjetBinsj100_mtDOWN/run_dir'
#..
#echo "NEXT: renorm systematics"
#mkdir plots_official_bjetBinsj100_renormSyst
#cd plots_official_bjetBinsj100_renormSyst
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF -renormSyst 'up' -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#python ../FFPlotter_B.py -FFvar='Pt'  --doFF -renormSyst 'down' -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#..
#echo "NEXT: Renorm in MET"
#mkdir plots_official_bjetBinsj100_METdown
#cd plots_official_bjetBinsj100_METdown
#python ../FFPlotter_B.py -FFvar='Pt' -renormSyst 'MET175'  --doFF --doCR -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_muon/condor/201709100535_bjetBinsj100/run_dir'
#..
