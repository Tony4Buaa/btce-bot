# Copyright (c) 2013-2017 CodeReclaimers, LLC

class TraderBase(object):
    def __init__(self, pairs):
        self.pairs = pairs
    
    def onNewDepth(self, t, pair, asks, bids):
        pass

    def onNewTradeHistory(self, t, pair, trades):
        pass
        
    def onLoopEnd(self, t):
        pass
    
    def onExit(self):
        pass
    
