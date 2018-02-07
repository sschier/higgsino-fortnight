mkdir hists_SUSY16_p2949_v02/
source ../scripts/hadd_scripts/hadd_dataByPeriod.sh
mv outputHist_data.root hists_SUSY16_p2949_v02/
#cd wjets_run_dir
#source ../../scripts/hadd_scripts/hadd_wjets.sh
#cp outputHist_wjets.root ../hists_SUSY16_p2949_v02/
#..
#cd zjets_run_dir
#source ../../scripts/hadd_scripts/hadd_zjets.sh
#cp outputHist_zjets.root ../hists_SUSY16_p2949_v02/
#..
#cd ttbar_run_dir
#source ../../scripts/hadd_scripts/hadd_ttbar.sh
#cp outputHist_ttbar.root ../hists_SUSY16_p2949_v02/
#..
#cd dy_run_dir
#source ../../scripts/hadd_scripts/hadd_dy.sh
#cp outputHist_dy.root ../hists_SUSY16_p2949_v02/
#..
#cd diboson_run_dir
#source ../../scripts/hadd_scripts/hadd_diboson.sh
#cp outputHist_diboson.root ../hists_SUSY16_p2949_v02/
#..
#cd singletop_run_dir
#source ../../scripts/hadd_scripts/hadd_singletop.sh
#cp outputHist_singletop.root ../hists_SUSY16_p2949_v02/
#..
cd ttv_run_dir_201703231908
source ../../scripts/hadd_scripts/hadd_ttv.sh
cp outputHist_ttv.root ../hists_SUSY16_p2949_v02/
..
cd triboson_run_dir_201703231908
source ../../scripts/hadd_scripts/hadd_triboson.sh
cp outputHist_triboson.root ../hists_SUSY16_p2949_v02/
..
#cd vgamma_run_dir_201703231908
#source ../../scripts/hadd_scripts/hadd_vgamma.sh
#cp outputHist_vgamma.root ../hists_SUSY16_p2949_v02/
#..
cd rare_run_dir_201703231908
source ../../scripts/hadd_scripts/hadd_rare.sh
cp outputHist_rare.root ../hists_SUSY16_p2949_v02/
..
