# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 23:15:36 2018

@author: apatti
"""
import hashlib
from time import time
import json

class Lahar:
    def __init__(self):
        self.chain=[]
        self.transactions = []
        #initial block (also called as genesis block)
        self.new_lahar(proof=100,prev_hash=1)
    
    #similar to block
    def new_lahar(self,proof,prev_hash=None):
        lahar = {'index':len(self.chain)+1,
                           'timestamp':time,
                           'transactions':self.transactions,
                           'proof':proof,
                           'previous_hash':prev_hash}
        self.transactions.clear()
        self.chain.append(lahar)
        return lahar
    
    def new_transaction(self,sender,receiver,amount):
        self.transactions.append({'sender':sender,
                                  'receiver':receiver,
                                  'amount':amount})
        return
    
    def last_lahar(self):
        return self.chain[-1]
    
    @staticmethod
    def Hash(lahar):
        return hashlib.sha256(json.dumps(lahar,sort_keys=True).encode()).digest()
        
    def hash_transactions(self):
        tran_hash=''
        for transaction in self.transactions:
            tran_hash += hashlib.sha256(json.dumps(transaction,sort_keys=True).encode()).digest()
        
        return hashlib.sha256(tran_hash)
    
    def proof_of_work(self):
        '''
        '' find a nonce such that hash(lastBlock.hash|transaction|nonce) has 4 leading zeroes
        '' in real implementation they use Merkle Tree for hashing transactions
        '' in our implementation, we shall hash all transactions together
        '''
        proof = 0
        while True:
            prev_hash=self.last_lahar['previous_hash']
            
            hash = hashlib.sha256(prev_hash+self.hash_transactions()+str(proof)).digest()
            if hash[:4]=="0000":
                break
            proof += 1
        
        return proof
    
    @staticmethod
    def validate_pow():
        