
# Muons, skim-mu-tau-01 (with trigger req)
tree_trimmer.py - -k CollectionTree,tauMeta/TrigConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-mu-tau-01.py /export/share/diskvault/reece/D3PDs/data12_8TeV/data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443_tid01224649_00/NTUP_TAU.01224649._000099.root.1 >> out/data12_8TeV.Muons.skim-mu-tau-01.log
mv skim.root out/data12_8TeV.Muons.skim-mu-tau-01.root

# Muons, skim-mu-tau-02
tree_trimmer.py - -k CollectionTree,tauMeta/TrigConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-mu-tau-02.py /export/share/diskvault/reece/D3PDs/data12_8TeV/data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443_tid01224649_00/NTUP_TAU.01224649._000099.root.1 >> out/data12_8TeV.Muons.skim-mu-tau-02.log
mv skim.root out/data12_8TeV.Muons.skim-mu-tau-02.root

# Muons, skim-mu-tau-02, boff-04
tree_trimmer.py - -B boff/boff-04.txt -M 3000 -k CollectionTree,tauMeta/TrigConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-mu-tau-02.py /export/share/diskvault/reece/D3PDs/data12_8TeV/data12_8TeV.00212993.physics_Muons.merge.NTUP_TAU.r4065_p1278_p1443_tid01224649_00/NTUP_TAU.01224649._000099.root.1 >> out/data12_8TeV.Muons.skim-mu-tau-02-boff-04.log
mv skim.root out/data12_8TeV.Muons.skim-mu-tau-02-boff-04.root

# Egamma, skim-el-tau-02
tree_trimmer.py - -k CollectionTree,tauMeta/TrigConfTree,tauMeta/BunchConfTree -t tau -s skim skims/skim-el-tau-02.py /export/share/diskvault/reece/D3PDs/data12_8TeV/data12_8TeV.00213092.physics_Egamma.merge.NTUP_TAU.r4065_p1278_p1443_tid01224626_00/NTUP_TAU.01224626._000068.root.1 >> out/data12_8TeV.Egamma.skim-el-tau-02.log
v skim.root out/data12_8TeV.Egamma.skim-el-tau-02.root

