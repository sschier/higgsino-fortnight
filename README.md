# higgsino-fortnight

One Paragraph of project description goes here

git clone https://github.com/sschier/higgsino-fortnight.git -b electron_j100


## Getting Started

### Clone Repository

```
git clone https://github.com/sschier/higgsino-fortnight.git -b compressed_v01
```
### Setup
```
SetupATLAS
lsetup ROOT
```

### Run Electron FF histogram maker

```
cd FakeFactor_gradient/condor
```
```
python doCondor_j100.py 
```
Before plotting script can be ran on output, it must be merged:

```
cd 'condor output directory'
source ../hadd.sh
```
This makes a directory called 'run_dir' inside the condor output directory that contains that output.root files for each process.
```
[sschier@atlas02 run_dir]$ ls
outputHist_data.root  outputHist_singletop.root  outputHist_ttbar.root  outputHist_wjets.root  outputHist_zjets.root
```



### Test Electron FF histogram maker

```
python FFMaker_j100.py -input "/export/share/data/sschier/FakeLepton/July4_2017_Stop1L_Dijet_Ntuple_AB_2.4.32_AddAuthor/data16_el_skims/job_000/skim.root" -isData "data16" -tree "data" -outfile "outputHist_310691_j100.root" -AIDvariation "blayer"
```
This will run on the -input sample and give you the -output .root file 
OR

```
source run_Maker.sh
```

### Run Electron Plotting Script
This script makes the final FF plots and prints out FFs bin by bin to the screen or a file.
This script takes in a directory containing your data and MC .root files

For example:
``` 
python ../FFPlotter.py -FFvar='pt' --doFF  --doCR -indir '/export/share/dirac/sschier/HistMaker/Higgsino_analysis/FakeFactor_gradient/condor/201709100528_j100/run_dir'
```
OR
```
source makePlots.sh
```

### Run Muon FF histogram maker

```
cd FakeFactor_muon/condor
```
```
python doCondor_Bj100.py (b-jet requirement)
python doCondor_j100.py (b-jet veto)
```
Before plotting script can be ran on output, it must be merged:
Follow instructions above for electron FFs

### Test Muon FF histogram maker


```
source run_Maker.sh
```

### Run Muon Plotting Script
This script makes the final FF plots and prints out FFs bin by bin to the screen or a file.
This script takes in a directory containing your data and MC .root files

```
source makePlots.sh
```



## Authors

* Sheena Calie Schier

