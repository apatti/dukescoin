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
        
    
    def proof_of_work(self):
        '''
        '' find a nonce such that hash(lastBlock.hash|transaction|nonce) has 4 leading zeroes
        '' in real implementation they use Merkle Tree for hashing transactions
        '' in our implementation, we shall hash all transactions together
        '''
        proof = 0
        while True:
            prev_hash=self.last_lahar['previous_hash']
            
            if Lahar.validate_pow(prev_hash,self.transactions,proof) == True:
                break
            
            proof += 1
        
        return proof
    
    @staticmethod
    def validate_pow(prev_hash,current_transactions,proof):
        tran_hash=''
        for transaction in current_transactions:
            tran_hash += hashlib.sha256(json.dumps(transaction,sort_keys=True).encode()).digest()
        
        tran_hash=hashlib.sha256(tran_hash)
        hash = hashlib.sha256(prev_hash+tran_hash+str(proof)).digest()
        return hash[:4]=='0000'