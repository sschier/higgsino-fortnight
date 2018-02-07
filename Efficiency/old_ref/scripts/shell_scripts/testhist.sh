mkdir mtautauValidate
cd mtautauValidate
#mkdir testEff
#cd testEff
#mkdir testNewCMS
#cd testNewCMS
#mkdir testCMS
#cd testCMS

python ../CMSMaker.py --test -input "/export/home/sschier/workarea/tree_trimmer/ttbar_skim.root" -tree "ttbar" -outfile "outputHist_ttbar.root"
python ../CMSMaker.py --test -input "/export/home/sschier/workarea/tree_trimmer/Ztt_skim.root" -tree "Ztt" -outfile "outputHist_Ztt.root"
python ../CMSMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.2_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_110_100_2LMET50_MadSpin_processed.root" -tree "MGPy8EG_A14N23LO_SM_N2C1p_110_100_2LMET50_MadSpin" -outfile "outputHist_N2C1p-110-100.root"
python ../CMSMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.2_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_110_100_2LMET50_MadSpin_processed.root" -tree "MGPy8EG_A14N23LO_SM_N2C1m_110_100_2LMET50_MadSpin" -outfile "outputHist_N2C1m-110-100.root"
python ../CMSMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.2_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin_processed.root" -tree "MGPy8EG_A14N23LO_SM_N2N1_110_100_2LMET50_MadSpin" -outfile "outputHist_N2N1-110-100.root"
python ../CMSMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.2_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_120_100_2LMET50_MadSpin_processed.root" -tree "MGPy8EG_A14N23LO_SM_N2C1p_120_100_2LMET50_MadSpin" -outfile "outputHist_N2C1p-120-100.root"
python ../CMSMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.2_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1m_120_100_2LMET50_MadSpin_processed.root" -tree "MGPy8EG_A14N23LO_SM_N2C1m_120_100_2LMET50_MadSpin" -outfile "outputHist_N2C1m-120-100.root"
python ../CMSMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.2_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2N1_120_100_2LMET50_MadSpin_processed.root" -tree "MGPy8EG_A14N23LO_SM_N2N1_120_100_2LMET50_MadSpin" -outfile "outputHist_N2N1-120-100.root"

#python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --tree "MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-103-100.root"
#python ../CMSMaker.py --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --tree "MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-103-100.root"
#python ../EffMaker.py --region "trigger" --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" --tree "MGPy8EG_A14N23LO_SM_N2C1p_103_100_2LMET50_MadSpin" --outfile "outputHist_N2C1p-103-100.root"
#python ../CMSMaker.py --isData --test --input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Bkgs_tree/data16_SusySkimHiggsino_v1.1_SUSY16_tree.root" --tree "data16A" --outfile "outputHist_data16A.root"
#python ../CMSMaker.py --test --input "/export/share/data/sschier/TwoLep_Output/SUSY16_Data/user.sschier.data15_13TeV.periodD.physics_Main_V00_NoSys_s1_t2_tree.root/user.sschier.10848895._000012.tree.root" --isData --tree "tree" --outfile "test_outputHist_Data15.root"
..
