import os
import ROOT
from ROOT import TString
ROOT.gROOT.SetBatch(True)
 #------------------------------------------------------------------
class renorm:
    def __init__(self, obs):


        self.weights = {}
        self.obs = obs

    def fillWeights(self, data):
        if data == 'data15':
            self.weights['HLT_e5'] = 3067.5
            self.weights['HLT_e10'] = 76.33
            self.weights['HLT_e15'] = 1.887
            self.weights['HLT_e20'] = 0.9936

        elif data == 'data16':
            self.weights['HLT_e5'] = 39.06
            self.weights['HLT_e10'] = 17.825
            self.weights['HLT_e15'] = 1.118
            self.weights['HLT_e20'] = 0.5883

    def getRegion(self, lepPt, triggers):
        region = ''
        if( triggers['HLT_e5'] and lepPt < 10. ):
            region = 'HLT_e5'
        elif( triggers['HLT_e10'] and lepPt >= 10. and lepPt < 15. ):
            region = 'HLT_e10'
        elif( triggers['HLT_e15'] and lepPt >= 15. and lepPt < 20. ):
            region = 'HLT_e15'
        elif( triggers['HLT_e20'] and lepPt >= 20. ):
            region = 'HLT_e20'
        else: print 'NO REGION'
        return region

    
    def getTriggerWeights(self, data, lepPt, triggers):
        self.fillWeights(data)
        print self.weights['HLT_e5']
        region = self.getRegion(lepPt, triggers)
        #print '*************'
        #print self.weights[region]
        #print lepPt
        #print '*************'
        weight = self.weights[region]
        return weight










