#mkdir lepEffHists_N2N1
#cd lepEffHists_N2N1
#python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/InclTwoLepPackage/Runs/Higgsinos_N2N1_105_100_T_06_09/data-tree/mc15_13TeV.393506.MGPy8EG_A14N23LO_SM_N2N1_105_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHist_N2N1-105-100.root"
#python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/InclTwoLepPackage/Runs/Higgsinos_N2N1_110_100_T_06_09/data-tree/mc15_13TeV.393507.MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHist_N2N1-110-100.root"
#python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/InclTwoLepPackage/Runs/Higgsinos_N2N1_120_100_T_06_09/data-tree/mc15_13TeV.393508.MGPy8EG_A14N23LO_SM_N2N1_120_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHist_N2N1-120-100.root"
#python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/InclTwoLepPackage/Runs/HiggsinoTruth_N2N1_105_100_T_06_09/data-tree/mc15_13TeV.393506.MGPy8EG_A14N23LO_SM_N2N1_105_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHistTruth_N2N1-105-100.root"
#python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/InclTwoLepPackage/Runs/HiggsinoTruth_N2N1_110_100_T_06_09/data-tree/mc15_13TeV.393507.MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHistTruth_N2N1-110-100.root"
#python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/InclTwoLepPackage/Runs/HiggsinoTruth_N2N1_120_100_T_06_09/data-tree/mc15_13TeV.393508.MGPy8EG_A14N23LO_SM_N2N1_120_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHistTruth_N2N1-120-100.root"
#..

mkdir lepEffCorrHists_N2N1
cd lepEffCorrHists_N2N1
#python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/SusySkimHiggsino/Higgsinos_N2N1_110_100_T_06_09/data-tree/mc15_13TeV.393507.MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHist_N2N1-110-100.root"
python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/SusySkimHiggsino/HiggsinoIso_N2N1_110_100_T_06_09/data-tree/mc15_13TeV.393507.MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHist_N2N1-110-100.root"
python ../EffMaker.py --region "dilepton" --test --input "/export/share/dirac/sschier/InclTwoLepPackage/Runs/HiggsinoTruth_N2N1_110_100_T_06_09/data-tree/mc15_13TeV.393507.MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin.merge.DAOD_SUSY16.e5512_a766_a821_r7676_p2952.root" --isSignal --tree "tree" --outfile "outputHistTruth_N2N1-110-100.root"
..
