import os
import ROOT
from ROOT import TString
ROOT.gROOT.SetBatch(True)
 #------------------------------------------------------------------
class renorm:
    def __init__(self, obs):


        self.weights = {}
        self.obs = obs

    #data samples renormalized to a total of 10 pb^-1
    #data15 and data16 reweighted according to their fractional contribution to the total
    #Weights commented out are for each data set being normalized to 10 pb-1 separately
    def fillWeights(self, data):
        if data == 'data15':
            #self.weights['HLT_e5'] = 3067.5
            #self.weights['HLT_e10'] = 76.33
            #self.weights['HLT_e15'] = 1.887
            #self.weights['HLT_e20'] = 0.9936
            self.weights['HLT_e5'] = 280.368
            self.weights['HLT_e10'] = 6.977
            self.weights['HLT_e15'] = 0.1725
            self.weights['HLT_e20'] = 0.09081

        elif data == 'data16':
            #self.weights['HLT_e5'] = 39.06
            #self.weights['HLT_e10'] = 17.825
            #self.weights['HLT_e15'] = 1.118
            #self.weights['HLT_e20'] = 0.5883
            self.weights['HLT_e5'] = 35.4882
            self.weights['HLT_e10'] = 16.1942
            self.weights['HLT_e15'] = 1.0155
            self.weights['HLT_e20'] = 0.5345

    #############################################################################
    #Picks the lowest pre-sclaed trigger
    #Originally much more complicated by making sure the 
    #lepton pt matched the desired trigger but that is done FF_Maker.py
    #############################################################################
    def getRegion(self, lepPt, triggers):
        region = ''
        if( triggers['HLT_e20'] ):
            region = 'HLT_e20'
        elif( triggers['HLT_e15'] ):
            region = 'HLT_e15'
        elif( triggers['HLT_e10'] ):
            region = 'HLT_e10'
        elif( triggers['HLT_e5'] ): 
            region = 'HLT_e5'
        else: print 'NO REGION'
        #print lepPt, region
        return region

    
    def getTriggerWeights(self, data, lepPt, triggers):
        self.fillWeights(data)
        region = self.getRegion(lepPt, triggers)
        weight = self.weights[region]
        return weight










