
prun --exec "python tree_trimmer.py - -M 4000 -t tau -s skim skims/skim-mu-tau-02.py %IN" --inDS data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443/ --outDS user.reece.data12_8TeV.00212993.Muons.r4065_p1278_p1443.skim-mu-tau-02.test11/ --outputs skim.root --athenaTag=17.3.1 --nGBPerJob=MAX --nFiles=1 --express

# prun --exec "python tree_trimmer.py - -M 4000 -k CollectionTree,tauMeta/TrigConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-mu-tau-02.py %IN" --inDS data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443/ --outDS user.reece.data12_8TeV.00212993.Muons.r4065_p1278_p1443.skim-mu-tau-02.test10/ --outputs skim.root --athenaTag=17.3.1 --nGBPerJob=MAX --nFiles=1 --express

# prun --exec "python tree_trimmer.py - -k CollectionTree,tauMeta/Trig    ConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-mu-tau-02.py %IN" --inDS data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443/ --outDS user.reece.data12_8TeV.00212993.Muons.r4065_p1278_p1443.skim-mu-tau-02.test09/ --outputs skim.root --athenaTag=17.3.1 --nGBPerJob=MAX --nFiles=1 --express

# prun --exec "python tree_trimmer.py - -B boff/boff-04.txt -M 3000 -k CollectionTree,tauMeta/TrigConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-mu-tau-02.py %IN" --inDS data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443/ --outDS user.reece.data12_8TeV.00212993.Muons.r4065_p1278_p1443.skim-mu-tau-02.test08/ --outputs skim.root --athenaTag=17.3.1 --nGBPerJob=MAX --nFiles=1 --express

# prun  --exec "python tree_trimmer.py - -k CollectionTree,tauMeta/TrigConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-mu-tau-02.py %IN" --inDS data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443/ --outDS user.reece.data12_8TeV.00212993.Muons.r4065_p1278_p1443.skim-mu-tau-01.test07/ --outputs skim.root --athenaTag=17.3.1 --nGBPerJob=MAX --nFiles=1 --express


# prun  --exec "python tree_trimmer.py - -B boff/boff-04.txt -M 3000 -k CollectionTree,tauMeta/TrigConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-mu-tau-01.py %IN" --inDS data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443/ --outDS user.reece.data12_8TeV.00212993.Muons.r4065_p1278_p1443.skim-mu-tau-01.test02/ --outputs skim.root --athenaTag=17.3.1 --nGBPerJob=MAX --nFiles=1 --express
