#python CutflowMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_105_100_2LMET50_MadSpin_SusySkimHiggsino_v1.1_SUSY16_tree.root" -tree "MGPy8EG_A14N23LO_SM_N2C1p_105_100_2LMET50_MadSpin" > Cutflow_N2C1p_105_100.txt

#python CutflowMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.2_SUSY16_Signal_tree/MGPy8EG_A14N23LO_SM_N2C1p_105_100_2LMET50_MadSpin_processed.root" -tree "MGPy8EG_A14N23LO_SM_N2C1p_105_100_2LMET50_MadSpin" > Cutflow_N2C1p_105_100_v1.2.txt


python CutflowMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.2_SUSY16_Bkgs_tree/diboson3L_SusySkimHiggsino_v1.2_SUSY16_tree.root" -tree "diboson3L" > Cutflow_363491_v1.2.txt

python CutflowMaker.py --test -input "/export/share/data/sschier/Higgsino/CommonTuples/SusySkimHiggsino_v1.1_SUSY16_Bkgs_tree/diboson_SusySkimHiggsino_v1.1_SUSY16_tree.root" -tree "diboson" > Cutflow_363491_v1.1.txt

