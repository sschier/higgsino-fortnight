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
        #Data15 is 9.14% of the 36 fb^-1
        if data == 'data15':
            #self.weights['HLT_mu4'] = 34.84
            #self.weights['HLT_mu10'] = 4.237
            #self.weights['HLT_mu14'] = 0.728
            #self.weights['HLT_mu18'] = 0.381
            self.weights['HLT_mu4'] = 3.184
            self.weights['HLT_mu10'] = 0.387
            self.weights['HLT_mu14'] = 0.0665
            self.weights['HLT_mu18'] = 0.0348

        #Data16 is 90.86% of the 36 fb^-1
        elif data == 'data16':
            #self.weights['HLT_mu4'] = 21.23
            #self.weights['HLT_mu10'] = 1.768
            #self.weights['HLT_mu14'] = 0.40
            #self.weights['HLT_mu18'] = 0.203
            self.weights['HLT_mu4'] = 19.29
            self.weights['HLT_mu10'] = 1.606
            self.weights['HLT_mu14'] = 0.362
            self.weights['HLT_mu18'] = 0.185

    def getRegion(self, lepPt, triggers):
        region = ''
        #if( triggers['HLT_mu4'] and lepPt < 10. ):
        #    region = 'HLT_mu4'
        #elif( triggers['HLT_mu10'] and lepPt >= 10. and lepPt < 15. ):
        #    region = 'HLT_mu10'
        #elif( triggers['HLT_mu14'] and lepPt >= 15. and lepPt < 20. ):
        #    region = 'HLT_mu14'
        #elif( triggers['HLT_mu18'] and lepPt >= 20. ):
        #    region = 'HLT_mu18'
        #else: print 'NO REGION'
        if( triggers['HLT_mu18'] ):
            region = 'HLT_mu18'
            #if lepPt < 20: print '***** trigger = 20 and pt = %f' %lepPt
        elif( triggers['HLT_mu14'] ):
            region = 'HLT_mu14'
            #if lepPt < 15: print '***** trigger = 15 and pt = %f' %lepPt
        elif( triggers['HLT_mu10'] ):
            region = 'HLT_mu10'
            #if lepPt < 10: print '***** trigger = 10 and pt = %f' %lepPt
        elif( triggers['HLT_mu4'] ): 
            region = 'HLT_mu4'
        else: print 'NO REGION'
        #print lepPt, region
        return region

    
    def getTriggerWeights(self, data, lepPt, triggers):
        self.fillWeights(data)
        region = self.getRegion(lepPt, triggers)
        weight = self.weights[region]
        return weight










