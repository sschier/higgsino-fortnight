mkdir effHists_N2N1_83_80
cd effHists_N2N1_83_80
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_83_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_83_80_2LMET50_MadSpin" --outfile "outputHist_N2C1p-83-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_83_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_83_80_2LMET50_MadSpin" --outfile "outputHist_N2C1m-83-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_83_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_83_80_2LMET50_MadSpin" --outfile "outputHist_N2N1-83-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_83_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_83_80_2LMET50_MadSpin" --outfile "outputHist_C1C1-83-80.root"
mkdir ../effHists_N2N1_grid
hadd ../effHists_N2N1_grid/outputHist_N2N1-83-80.root outputHist_N2C1p-83-80.root outputHist_N2C1m-83-80.root outputHist_N2N1-83-80.root outputHist_C1C1-83-80.root
..

mkdir effHists_N2N1_85_80
cd effHists_N2N1_85_80
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_85_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_85_80_2LMET50_MadSpin" --outfile "outputHist_N2C1p-85-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_85_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_85_80_2LMET50_MadSpin" --outfile "outputHist_N2C1m-85-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_85_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_85_80_2LMET50_MadSpin" --outfile "outputHist_N2N1-85-80.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-85-80.root outputHist_N2C1p-85-80.root outputHist_N2C1m-85-80.root outputHist_N2N1-85-80.root
..

mkdir effHists_N2N1_90_80
cd effHists_N2N1_90_80
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_90_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_90_80_2LMET50_MadSpin" --outfile "outputHist_N2C1p-90-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_90_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_90_80_2LMET50_MadSpin" --outfile "outputHist_N2C1m-90-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_90_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_90_80_2LMET50_MadSpin" --outfile "outputHist_N2N1-90-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_90_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_90_80_2LMET50_MadSpin" --outfile "outputHist_C1C1-90-80.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-90-80.root outputHist_N2C1p-90-80.root outputHist_N2C1m-90-80.root outputHist_N2N1-90-80.root outputHist_C1C1-90-80.root
..

mkdir effHists_N2N1_100_80
cd effHists_N2N1_100_80
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_100_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_100_80_2LMET50_MadSpin" --outfile "outputHist_N2C1p-100-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_100_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_100_80_2LMET50_MadSpin" --outfile "outputHist_N2C1m-100-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_100_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_100_80_2LMET50_MadSpin" --outfile "outputHist_N2N1-100-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_100_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_100_80_2LMET50_MadSpin" --outfile "outputHist_C1C1-100-80.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-100-80.root outputHist_N2C1p-100-80.root outputHist_N2C1m-100-80.root outputHist_N2N1-100-80.root outputHist_C1C1-100-80.root
..

mkdir effHists_N2N1_120_80
cd effHists_N2N1_120_80
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_120_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_120_80_2LMET50_MadSpin" --outfile "outputHist_N2C1p-120-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_120_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_120_80_2LMET50_MadSpin" --outfile "outputHist_N2C1m-120-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_120_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_120_80_2LMET50_MadSpin" --outfile "outputHist_N2N1-120-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_120_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_120_80_2LMET50_MadSpin" --outfile "outputHist_C1C1-120-80.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-120-80.root outputHist_N2C1p-120-80.root outputHist_N2C1m-120-80.root outputHist_N2N1-120-80.root outputHist_C1C1-120-80.root
..

mkdir effHists_N2N1_140_80
cd effHists_N2N1_140_80
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_140_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_140_80_2LMET50_MadSpin" --outfile "outputHist_N2C1p-140-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_140_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_140_80_2LMET50_MadSpin" --outfile "outputHist_N2C1m-140-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_140_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_140_80_2LMET50_MadSpin" --outfile "outputHist_N2N1-140-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_140_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_140_80_2LMET50_MadSpin" --outfile "outputHist_C1C1-140-80.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-140-80.root outputHist_N2C1p-140-80.root outputHist_N2C1m-140-80.root outputHist_N2N1-140-80.root outputHist_C1C1-140-80.root
..

mkdir effHists_N2N1_180_80
cd effHists_N2N1_180_80
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_180_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_180_80_2LMET50_MadSpin" --outfile "outputHist_N2C1p-180-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_180_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_180_80_2LMET50_MadSpin" --outfile "outputHist_N2C1m-180-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_180_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_180_80_2LMET50_MadSpin" --outfile "outputHist_N2N1-180-80.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_180_80_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_180_80_2LMET50_MadSpin" --outfile "outputHist_C1C1-180-80.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-180-80.root outputHist_N2C1p-180-80.root outputHist_N2C1m-180-80.root outputHist_N2N1-180-80.root outputHist_C1C1-180-80.root
..





mkdir effHists_N2N1_103_100
cd effHists_N2N1_103_100
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-103-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_103_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-103-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_103_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-103-100.root"
hadd ../effHists_N2N1_grid/outputHist_N2N1-103-100.root outputHist_N2C1p-103-100.root outputHist_N2C1m-103-100.root outputHist_N2N1-103-100.root
..

mkdir effHists_N2N1_105_100
cd effHists_N2N1_105_100
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_105_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-105-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_105_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-105-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_105_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-105-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_105_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-105-100.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-105-100.root outputHist_N2C1p-105-100.root outputHist_N2C1m-105-100.root outputHist_N2N1-105-100.root outputHist_C1C1-105-100.root
..

mkdir effHists_N2N1_110_100
cd effHists_N2N1_110_100
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_110_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_110_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-110-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_110_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_110_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-110-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-110-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_110_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_110_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-110-100.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-110-100.root outputHist_N2C1p-110-100.root outputHist_N2C1m-110-100.root outputHist_N2N1-110-100.root outputHist_C1C1-110-100.root
..

mkdir effHists_N2N1_120_100
cd effHists_N2N1_120_100
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_120_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_120_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-120-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_120_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_120_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-120-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_120_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_120_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-120-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_120_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_120_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-120-100.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-120-100.root outputHist_N2C1p-120-100.root outputHist_N2C1m-120-100.root outputHist_N2N1-120-100.root outputHist_C1C1-120-100.root
..

mkdir effHists_N2N1_140_100
cd effHists_N2N1_140_100
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_140_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_140_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-140-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_140_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_140_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-140-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_140_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_140_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-140-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_140_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_140_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-140-100.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-140-100.root outputHist_N2C1p-140-100.root outputHist_N2C1m-140-100.root outputHist_N2N1-140-100.root outputHist_C1C1-140-100.root
..

mkdir effHists_N2N1_160_100
cd effHists_N2N1_160_100
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_160_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_160_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-160-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_160_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_160_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-160-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_160_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_160_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-160-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_160_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_160_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-160-100.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-160-100.root outputHist_N2C1p-160-100.root outputHist_N2C1m-160-100.root outputHist_N2N1-160-100.root outputHist_C1C1-160-100.root
..

mkdir effHists_N2N1_200_100
cd effHists_N2N1_200_100
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_200_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_200_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-200-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_200_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_200_100_2LMET50_MadSpin" --outfile "outputHist_N2C1m-200-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_200_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_200_100_2LMET50_MadSpin" --outfile "outputHist_N2N1-200-100.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_200_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_200_100_2LMET50_MadSpin" --outfile "outputHist_C1C1-200-100.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-200-100.root outputHist_N2C1p-200-100.root outputHist_N2C1m-200-100.root outputHist_N2N1-200-100.root outputHist_C1C1-200-100.root
..




mkdir effHists_N2N1_155_150
cd effHists_N2N1_155_150
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_155_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_155_150_2LMET50_MadSpin" --outfile "outputHist_N2C1p-155-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_155_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_155_150_2LMET50_MadSpin" --outfile "outputHist_N2C1m-155-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_155_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_155_150_2LMET50_MadSpin" --outfile "outputHist_N2N1-155-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_155_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_155_150_2LMET50_MadSpin" --outfile "outputHist_C1C1-155-150.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-155-150.root outputHist_N2C1p-155-150.root outputHist_N2C1m-155-150.root outputHist_N2N1-155-150.root outputHist_C1C1-155-150.root
..

mkdir effHists_N2N1_160_150
cd effHists_N2N1_160_150
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_160_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_160_150_2LMET50_MadSpin" --outfile "outputHist_N2C1p-160-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_160_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_160_150_2LMET50_MadSpin" --outfile "outputHist_N2C1m-160-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_160_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_160_150_2LMET50_MadSpin" --outfile "outputHist_N2N1-160-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_160_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_160_150_2LMET50_MadSpin" --outfile "outputHist_C1C1-160-150.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-160-150.root outputHist_N2C1p-160-150.root outputHist_N2C1m-160-150.root outputHist_N2N1-160-150.root outputHist_C1C1-160-150.root
..

mkdir effHists_N2N1_170_150
cd effHists_N2N1_170_150
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_170_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_170_150_2LMET50_MadSpin" --outfile "outputHist_N2C1p-170-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_170_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_170_150_2LMET50_MadSpin" --outfile "outputHist_N2C1m-170-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_170_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_170_150_2LMET50_MadSpin" --outfile "outputHist_N2N1-170-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_170_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_170_150_2LMET50_MadSpin" --outfile "outputHist_C1C1-170-150.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-170-150.root outputHist_N2C1p-170-150.root outputHist_N2C1m-170-150.root outputHist_N2N1-170-150.root outputHist_C1C1-170-150.root
..

mkdir effHists_N2N1_190_150
cd effHists_N2N1_190_150
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_190_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_190_150_2LMET50_MadSpin" --outfile "outputHist_N2C1p-190-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_190_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_190_150_2LMET50_MadSpin" --outfile "outputHist_N2C1m-190-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_190_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_190_150_2LMET50_MadSpin" --outfile "outputHist_N2N1-190-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_190_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_190_150_2LMET50_MadSpin" --outfile "outputHist_C1C1-190-150.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-190-150.root outputHist_N2C1p-190-150.root outputHist_N2C1m-190-150.root outputHist_N2N1-190-150.root outputHist_C1C1-190-150.root
..

mkdir effHists_N2N1_210_150
cd effHists_N2N1_210_150
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_210_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_210_150_2LMET50_MadSpin" --outfile "outputHist_N2C1p-210-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_210_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_210_150_2LMET50_MadSpin" --outfile "outputHist_N2C1m-210-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_210_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_210_150_2LMET50_MadSpin" --outfile "outputHist_N2N1-210-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_210_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_210_150_2LMET50_MadSpin" --outfile "outputHist_C1C1-210-150.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-210-150.root outputHist_N2C1p-210-150.root outputHist_N2C1m-210-150.root outputHist_N2N1-210-150.root outputHist_C1C1-210-150.root
..

mkdir effHists_N2N1_250_150
cd effHists_N2N1_250_150
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_250_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_250_150_2LMET50_MadSpin" --outfile "outputHist_N2C1p-250-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_250_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_250_150_2LMET50_MadSpin" --outfile "outputHist_N2C1m-250-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_250_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_250_150_2LMET50_MadSpin" --outfile "outputHist_N2N1-250-150.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_250_150_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_250_150_2LMET50_MadSpin" --outfile "outputHist_C1C1-250-150.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-250-150.root outputHist_N2C1p-250-150.root outputHist_N2C1m-250-150.root outputHist_N2N1-250-150.root outputHist_C1C1-250-150.root
..






mkdir effHists_N2N1_205_200
cd effHists_N2N1_205_200
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_205_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_205_200_2LMET50_MadSpin" --outfile "outputHist_N2C1p-205-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_205_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_205_200_2LMET50_MadSpin" --outfile "outputHist_N2C1m-205-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_205_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_205_200_2LMET50_MadSpin" --outfile "outputHist_N2N1-205-200.root"
hadd ../effHists_N2N1_grid/outputHist_N2N1-205-200.root outputHist_N2C1p-205-200.root outputHist_N2C1m-205-200.root outputHist_N2N1-205-200.root
..

mkdir effHists_N2N1_210_200
cd effHists_N2N1_210_200
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_210_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_210_200_2LMET50_MadSpin" --outfile "outputHist_N2C1p-210-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_210_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_210_200_2LMET50_MadSpin" --outfile "outputHist_N2C1m-210-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_210_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_210_200_2LMET50_MadSpin" --outfile "outputHist_N2N1-210-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_210_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_210_200_2LMET50_MadSpin" --outfile "outputHist_C1C1-210-200.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-210-200.root outputHist_N2C1p-210-200.root outputHist_N2C1m-210-200.root outputHist_N2N1-210-200.root outputHist_C1C1-210-200.root
..

mkdir effHists_N2N1_220_200
cd effHists_N2N1_220_200
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_220_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_220_200_2LMET50_MadSpin" --outfile "outputHist_N2C1p-220-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_220_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_220_200_2LMET50_MadSpin" --outfile "outputHist_N2C1m-220-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_220_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_220_200_2LMET50_MadSpin" --outfile "outputHist_N2N1-220-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_220_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_220_200_2LMET50_MadSpin" --outfile "outputHist_C1C1-220-200.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-220-200.root outputHist_N2C1p-220-200.root outputHist_N2C1m-220-200.root outputHist_N2N1-220-200.root outputHist_C1C1-220-200.root
..

mkdir effHists_N2N1_240_200
cd effHists_N2N1_240_200
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_240_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_240_200_2LMET50_MadSpin" --outfile "outputHist_N2C1p-240-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_240_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_240_200_2LMET50_MadSpin" --outfile "outputHist_N2C1m-240-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_240_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_240_200_2LMET50_MadSpin" --outfile "outputHist_N2N1-240-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_240_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_240_200_2LMET50_MadSpin" --outfile "outputHist_C1C1-240-200.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-240-200.root outputHist_N2C1p-240-200.root outputHist_N2C1m-240-200.root outputHist_N2N1-240-200.root outputHist_C1C1-240-200.root
..

mkdir effHists_N2N1_260_200
cd effHists_N2N1_260_200
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_260_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_260_200_2LMET50_MadSpin" --outfile "outputHist_N2C1p-260-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_260_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_260_200_2LMET50_MadSpin" --outfile "outputHist_N2C1m-260-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_260_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_260_200_2LMET50_MadSpin" --outfile "outputHist_N2N1-260-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_260_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_260_200_2LMET50_MadSpin" --outfile "outputHist_C1C1-260-200.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-260-200.root outputHist_N2C1p-260-200.root outputHist_N2C1m-260-200.root outputHist_N2N1-260-200.root outputHist_C1C1-260-200.root
..

mkdir effHists_N2N1_300_200
cd effHists_N2N1_300_200
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_300_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_300_200_2LMET50_MadSpin" --outfile "outputHist_N2C1p-300-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_300_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_300_200_2LMET50_MadSpin" --outfile "outputHist_N2C1m-300-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_300_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_300_200_2LMET50_MadSpin" --outfile "outputHist_N2N1-300-200.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_300_200_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_300_200_2LMET50_MadSpin" --outfile "outputHist_C1C1-300-200.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-300-200.root outputHist_N2C1p-300-200.root outputHist_N2C1m-300-200.root outputHist_N2N1-300-200.root outputHist_C1C1-300-200.root
..





mkdir effHists_N2N1_255_250
cd effHists_N2N1_255_250
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_255_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_255_250_2LMET50_MadSpin" --outfile "outputHist_N2C1p-255-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_255_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_255_250_2LMET50_MadSpin" --outfile "outputHist_N2C1m-255-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_255_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_255_250_2LMET50_MadSpin" --outfile "outputHist_N2N1-255-250.root"
hadd ../effHists_N2N1_grid/outputHist_N2N1-255-250.root outputHist_N2C1p-255-250.root outputHist_N2C1m-255-250.root outputHist_N2N1-255-250.root
..

mkdir effHists_N2N1_260_250
cd effHists_N2N1_260_250
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_260_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_260_250_2LMET50_MadSpin" --outfile "outputHist_N2C1p-260-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_260_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_260_250_2LMET50_MadSpin" --outfile "outputHist_N2C1m-260-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_260_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_260_250_2LMET50_MadSpin" --outfile "outputHist_N2N1-260-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_260_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_260_250_2LMET50_MadSpin" --outfile "outputHist_C1C1-260-250.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-260-250.root outputHist_N2C1p-260-250.root outputHist_N2C1m-260-250.root outputHist_N2N1-260-250.root outputHist_C1C1-260-250.root
..

mkdir effHists_N2N1_270_250
cd effHists_N2N1_270_250
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_270_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_270_250_2LMET50_MadSpin" --outfile "outputHist_N2C1p-270-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_270_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_270_250_2LMET50_MadSpin" --outfile "outputHist_N2C1m-270-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_270_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_270_250_2LMET50_MadSpin" --outfile "outputHist_N2N1-270-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_270_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_270_250_2LMET50_MadSpin" --outfile "outputHist_C1C1-270-250.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-270-250.root outputHist_N2C1p-270-250.root outputHist_N2C1m-270-250.root outputHist_N2N1-270-250.root outputHist_C1C1-270-250.root
..

mkdir effHists_N2N1_290_250
cd effHists_N2N1_290_250
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_290_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_290_250_2LMET50_MadSpin" --outfile "outputHist_N2C1p-290-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_290_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_290_250_2LMET50_MadSpin" --outfile "outputHist_N2C1m-290-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_290_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_290_250_2LMET50_MadSpin" --outfile "outputHist_N2N1-290-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_290_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_290_250_2LMET50_MadSpin" --outfile "outputHist_C1C1-290-250.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-290-250.root outputHist_N2C1p-290-250.root outputHist_N2C1m-290-250.root outputHist_N2N1-290-250.root outputHist_C1C1-290-250.root
..

mkdir effHists_N2N1_310_250
cd effHists_N2N1_310_250
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_310_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_310_250_2LMET50_MadSpin" --outfile "outputHist_N2C1p-310-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_310_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_310_250_2LMET50_MadSpin" --outfile "outputHist_N2C1m-310-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_310_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_310_250_2LMET50_MadSpin" --outfile "outputHist_N2N1-310-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_310_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_310_250_2LMET50_MadSpin" --outfile "outputHist_C1C1-310-250.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-310-250.root outputHist_N2C1p-310-250.root outputHist_N2C1m-310-250.root outputHist_N2N1-310-250.root outputHist_C1C1-310-250.root
..

mkdir effHists_N2N1_350_250
cd effHists_N2N1_350_250
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_350_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_350_250_2LMET50_MadSpin" --outfile "outputHist_N2C1p-350-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_350_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_350_250_2LMET50_MadSpin" --outfile "outputHist_N2C1m-350-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_350_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_350_250_2LMET50_MadSpin" --outfile "outputHist_N2N1-350-250.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_350_250_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_350_250_2LMET50_MadSpin" --outfile "outputHist_C1C1-350-250.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-350-250.root outputHist_N2C1p-350-250.root outputHist_N2C1m-350-250.root outputHist_N2N1-350-250.root outputHist_C1C1-350-250.root
..





mkdir effHists_N2N1_305_300
cd effHists_N2N1_305_300
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_305_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_305_300_2LMET50_MadSpin" --outfile "outputHist_N2C1p-305-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_305_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_305_300_2LMET50_MadSpin" --outfile "outputHist_N2C1m-305-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_305_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_305_300_2LMET50_MadSpin" --outfile "outputHist_N2N1-305-300.root"
hadd ../effHists_N2N1_grid/outputHist_N2N1-305-300.root outputHist_N2C1p-305-300.root outputHist_N2C1m-305-300.root outputHist_N2N1-305-300.root
..

mkdir effHists_N2N1_310_300
cd effHists_N2N1_310_300
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_310_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_310_300_2LMET50_MadSpin" --outfile "outputHist_N2C1p-310-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_310_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_310_300_2LMET50_MadSpin" --outfile "outputHist_N2C1m-310-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_310_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_310_300_2LMET50_MadSpin" --outfile "outputHist_N2N1-310-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_310_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_310_300_2LMET50_MadSpin" --outfile "outputHist_C1C1-310-300.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-310-300.root outputHist_N2C1p-310-300.root outputHist_N2C1m-310-300.root outputHist_N2N1-310-300.root outputHist_C1C1-310-300.root
..

mkdir effHists_N2N1_320_300
cd effHists_N2N1_320_300
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_320_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_320_300_2LMET50_MadSpin" --outfile "outputHist_N2C1p-320-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_320_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_320_300_2LMET50_MadSpin" --outfile "outputHist_N2C1m-320-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_320_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_320_300_2LMET50_MadSpin" --outfile "outputHist_N2N1-320-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_320_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_320_300_2LMET50_MadSpin" --outfile "outputHist_C1C1-320-300.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-320-300.root outputHist_N2C1p-320-300.root outputHist_N2C1m-320-300.root outputHist_N2N1-320-300.root outputHist_C1C1-320-300.root
..

mkdir effHists_N2N1_340_300
cd effHists_N2N1_340_300
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_340_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_340_300_2LMET50_MadSpin" --outfile "outputHist_N2C1p-340-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_340_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_340_300_2LMET50_MadSpin" --outfile "outputHist_N2C1m-340-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_340_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_340_300_2LMET50_MadSpin" --outfile "outputHist_N2N1-340-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_340_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_340_300_2LMET50_MadSpin" --outfile "outputHist_C1C1-340-300.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-340-300.root outputHist_N2C1p-340-300.root outputHist_N2C1m-340-300.root outputHist_N2N1-340-300.root outputHist_C1C1-340-300.root
..

mkdir effHists_N2N1_360_300
cd effHists_N2N1_360_300
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_360_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_360_300_2LMET50_MadSpin" --outfile "outputHist_N2C1p-360-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_360_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_360_300_2LMET50_MadSpin" --outfile "outputHist_N2C1m-360-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_360_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_360_300_2LMET50_MadSpin" --outfile "outputHist_N2N1-360-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_360_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_360_300_2LMET50_MadSpin" --outfile "outputHist_C1C1-360-300.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-360-300.root outputHist_N2C1p-360-300.root outputHist_N2C1m-360-300.root outputHist_N2N1-360-300.root outputHist_C1C1-360-300.root
..

mkdir effHists_N2N1_400_300
cd effHists_N2N1_400_300
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_400_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_400_300_2LMET50_MadSpin" --outfile "outputHist_N2C1p-400-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_400_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_400_300_2LMET50_MadSpin" --outfile "outputHist_N2C1m-400-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_400_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_400_300_2LMET50_MadSpin" --outfile "outputHist_N2N1-400-300.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_400_300_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_400_300_2LMET50_MadSpin" --outfile "outputHist_C1C1-400-300.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-400-300.root outputHist_N2C1p-400-300.root outputHist_N2C1m-400-300.root outputHist_N2N1-400-300.root outputHist_C1C1-400-300.root
..





mkdir effHists_N2N1_405_400
cd effHists_N2N1_405_400
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_405_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_405_400_2LMET50_MadSpin" --outfile "outputHist_N2C1p-405-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_405_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_405_400_2LMET50_MadSpin" --outfile "outputHist_N2C1m-405-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_405_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_405_400_2LMET50_MadSpin" --outfile "outputHist_N2N1-405-400.root"
hadd ../effHists_N2N1_grid/outputHist_N2N1-405-400.root outputHist_N2C1p-405-400.root outputHist_N2C1m-405-400.root outputHist_N2N1-405-400.root
..

mkdir effHists_N2N1_410_400
cd effHists_N2N1_410_400
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_410_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_410_400_2LMET50_MadSpin" --outfile "outputHist_N2C1p-410-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_410_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_410_400_2LMET50_MadSpin" --outfile "outputHist_N2C1m-410-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_410_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_410_400_2LMET50_MadSpin" --outfile "outputHist_N2N1-410-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_410_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_410_400_2LMET50_MadSpin" --outfile "outputHist_C1C1-410-400.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-410-400.root outputHist_N2C1p-410-400.root outputHist_N2C1m-410-400.root outputHist_N2N1-410-400.root outputHist_C1C1-410-400.root
..

mkdir effHists_N2N1_420_400
cd effHists_N2N1_420_400
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_420_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_420_400_2LMET50_MadSpin" --outfile "outputHist_N2C1p-420-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_420_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_420_400_2LMET50_MadSpin" --outfile "outputHist_N2C1m-420-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_420_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_420_400_2LMET50_MadSpin" --outfile "outputHist_N2N1-420-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_420_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_420_400_2LMET50_MadSpin" --outfile "outputHist_C1C1-420-400.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-420-400.root outputHist_N2C1p-420-400.root outputHist_N2C1m-420-400.root outputHist_N2N1-420-400.root outputHist_C1C1-420-400.root
..

mkdir effHists_N2N1_440_400
cd effHists_N2N1_440_400
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_440_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_440_400_2LMET50_MadSpin" --outfile "outputHist_N2C1p-440-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_440_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_440_400_2LMET50_MadSpin" --outfile "outputHist_N2C1m-440-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_440_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_440_400_2LMET50_MadSpin" --outfile "outputHist_N2N1-440-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_440_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_440_400_2LMET50_MadSpin" --outfile "outputHist_C1C1-440-400.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-440-400.root outputHist_N2C1p-440-400.root outputHist_N2C1m-440-400.root outputHist_N2N1-440-400.root outputHist_C1C1-440-400.root
..

mkdir effHists_N2N1_460_400
cd effHists_N2N1_460_400
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_460_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_460_400_2LMET50_MadSpin" --outfile "outputHist_N2C1p-460-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_460_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_460_400_2LMET50_MadSpin" --outfile "outputHist_N2C1m-460-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_460_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_460_400_2LMET50_MadSpin" --outfile "outputHist_N2N1-460-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_460_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_460_400_2LMET50_MadSpin" --outfile "outputHist_C1C1-460-400.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-460-400.root outputHist_N2C1p-460-400.root outputHist_N2C1m-460-400.root outputHist_N2N1-460-400.root outputHist_C1C1-460-400.root
..

mkdir effHists_N2N1_500_400
cd effHists_N2N1_500_400
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_500_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1p_500_400_2LMET50_MadSpin" --outfile "outputHist_N2C1p-500-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_500_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2C1m_500_400_2LMET50_MadSpin" --outfile "outputHist_N2C1m-500-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_500_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_N2N1_500_400_2LMET50_MadSpin" --outfile "outputHist_N2N1-500-400.root"
python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_C1C1_500_400_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --isSignal --tree "MGPy8EG_A14N23LO_SM_C1C1_500_400_2LMET50_MadSpin" --outfile "outputHist_C1C1-500-400.root"
 hadd ../effHists_N2N1_grid/outputHist_N2N1-500-400.root outputHist_N2C1p-500-400.root outputHist_N2C1m-500-400.root outputHist_N2N1-500-400.root outputHist_C1C1-500-400.root
..
