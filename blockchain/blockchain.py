# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 23:15:36 2018

@author: apatti
"""
import hashlib
from time import time
import json

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.transactions = []
        #initial block (also called as genesis block)
        self.new_block(proof=100,prev_hash=1)
    
    def new_block(self,proof,prev_hash=None):
        block = {'index':len(self.chain)+1,
                           'timestamp':time,
                           'transactions':self.transactions,
                           'proof':proof,
                           'previous_hash':prev_hash}
        self.transactions.clear()
        self.chain.append(block)
        return block
    
    def new_transaction(self,sender,receiver,amount):
        self.transactions.append({'sender':sender,
                                  'receiver':receiver,
                                  'amount':amount})
        return
        
    
    @staticmethod
    def Hash(block):
        pass
    