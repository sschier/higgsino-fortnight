mkdir hists_N2N1_103_100
cd hists_N2N1_103_100
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-103-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_103_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-103-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_103_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-103-100.root"
mkdir ../hists_N2N1_SRgrid
hadd ../hists_N2N1_SRgrid/outputHist_N2N1-103-100.root outputHist_N2C1p-103-100.root outputHist_N2C1m-103-100.root outputHist_N2N1-103-100.root
..

mkdir hists_N2N1_105_100
cd hists_N2N1_105_100
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_105_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-105-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_105_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-105-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_105_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-105-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_105_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-105-100.root"
 hadd ../hists_N2N1_SRgrid/outputHist_N2N1-105-100.root outputHist_N2C1p-105-100.root outputHist_N2C1m-105-100.root outputHist_N2N1-105-100.root outputHist_C1C1-105-100.root
..

mkdir hists_N2N1_110_100
cd hists_N2N1_110_100
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_110_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_110_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-110-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_110_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_110_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-110-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-110-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_110_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_110_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-110-100.root"
 hadd ../hists_N2N1_SRgrid/outputHist_N2N1-110-100.root outputHist_N2C1p-110-100.root outputHist_N2C1m-110-100.root outputHist_N2N1-110-100.root outputHist_C1C1-110-100.root
..

mkdir hists_N2N1_120_100
cd hists_N2N1_120_100
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_120_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_120_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-120-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_120_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_120_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-120-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_120_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_120_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-120-100.root"
python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_120_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_120_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-120-100.root"
 hadd ../hists_N2N1_SRgrid/outputHist_N2N1-120-100.root outputHist_N2C1p-120-100.root outputHist_N2C1m-120-100.root outputHist_N2N1-120-100.root outputHist_C1C1-120-100.root
..
