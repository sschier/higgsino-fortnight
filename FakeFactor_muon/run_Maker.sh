#python FFMaker.py --test --input "/export/share/data/sschier/FakeLepton/mu_trigger_skims/data16_skim/data310691_skim.root" --isData "data16" --tree "CollectionTree" --outfile "outputHist_310691.root"
#python FFMaker.py --test --input "/export/share/data/sschier/FakeLepton/mu_trigger_skims/data15_skim/data280319_skim.root" --isData "data15" --tree "CollectionTree" --outfile "outputHist_280319.root"
#python FFMaker.py --test --input "/export/share/data/sschier/FakeLepton/mu_trigger_skims/wjets_skim/wjets361101_skim.root" --tree "wjets_22" --outfile "outputHist_361101.root"

#python FFMaker.py --test -input "/export/share/data/sschier/FakeLepton/full_samples_2_4_25/data15_13TeV/data15_13TeV.00280319.data15_13TeV.DAOD_SUSY5.root" -isData "data15" -tree "CollectionTree" -outfile "outputHist_280319.root" -variation "Z0"
#python FFMaker.py --test -input "/export/share/data/sschier/FakeLepton/full_samples_2_4_25/data15_13TeV/data15_13TeV.00280319.data15_13TeV.DAOD_SUSY5.root" -isData "data15" -tree "CollectionTree" -outfile "outputHist_280319.root" -variation "pileup"
python FFMaker.py --test -input "/export/share/data/sschier/FakeLepton/mu_trigger_skims/wjets_skim/wjets361101_skim.root" -tree "wjets_22" -outfile "outputHist_361101.root" -variation "pileup"
