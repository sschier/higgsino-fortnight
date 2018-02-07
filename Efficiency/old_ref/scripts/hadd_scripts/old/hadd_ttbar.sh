ls job_00*
hadd hadd_00.root job_00*/outputHist_*.root
ls job_01*
hadd hadd_01.root job_01*/outputHist_*.root
ls job_02*
hadd hadd_02.root job_02*/outputHist_*.root
ls job_03*
hadd hadd_03.root job_03*/outputHist_*.root
ls job_04*
hadd hadd_04.root job_04*/outputHist_*.root
ls job_05*
hadd hadd_05.root job_05*/outputHist_*.root
ls job_06*
hadd hadd_06.root job_06*/outputHist_*.root
ls job_07*
hadd hadd_07.root job_07*/outputHist_*.root

hadd outputHist_ttbar.root hadd_*.root
