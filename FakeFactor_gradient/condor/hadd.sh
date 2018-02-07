mkdir run_dir
hadd outputHist_data15.root data15/job_*/outputHist_data15.root
hadd outputHist_data16.root data16/job_*/outputHist_data16.root
hadd outputHist_data.root outputHist_data1*.root
mv outputHist_data.root run_dir
hadd outputHist_singletop.root singletop/job_00*/outputHist_singletop.root
mv outputHist_singletop.root run_dir
hadd outputHist_zjets.root zjets/job_00*/outputHist_zjets.root
mv outputHist_zjets.root run_dir
hadd outputHist_wjets.root wjets/job_00*/outputHist_wjets.root
mv outputHist_wjets.root run_dir
cp ttbar/job_000/outputHist_ttbar.root run_dir

