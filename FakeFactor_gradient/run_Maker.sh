
python FFMaker_j100.py  -input "/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/data16_el_skims/job_000/skim.root" -isData "data16" -tree "data" -outfile "outputHist_310691_j100.root" -AIDvariation "blayer" 


#Examples of running systematics on FF measurement region
#python FFMaker_j100.py  -input "/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/data16_el_skims/job_000/skim.root" -isData "data16" -tree "data" -outfile "outputHist_310691_mtUP.root" -AIDvariation "blayer" -variation "mtUP"
#python FFMaker_j100.py  -input "/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/data16_el_skims/job_000/skim.root" -isData "data16" -tree "data" -outfile "outputHist_310691_mtDOWN.root" -AIDvariation "blayer" -variation "mtDOWN"

#Examples of running with alternate anti-ID variations
#python FFMaker_j100.py  -input "/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/data16_el_skims/job_000/skim.root" -isData "data16" -tree "data" -outfile "outputHist_310691.root" -AIDvariation "medium"
#python FFMaker_j100.py  -input "/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/data16_el_skims/job_000/skim.root" -isData "data16" -tree "data" -outfile "outputHist_310691.root" -AIDvariation "blayer"
#python FFMaker_j100.py --test -input "/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/data16_el_skims/job_000/skim.root" -isData "data16" -tree "data" -outfile "outputHist_310691.root" -AIDvariation "mediumD0sig"
#python FFMaker_j100.py  -input "/export/home/sschier/workarea/tree_trimmer/condor/data16_el_skims/job_000/skim.root" -isData "data16" -tree "data" -outfile "outputHist_310691.root" -AIDvariation "blayer"
