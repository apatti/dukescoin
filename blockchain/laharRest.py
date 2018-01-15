# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 23:15:36 2018

@author: apatti
"""
from lahar import *
from flask import Flask,jsonify,request
import json
import requests

app = Flask(__name__)
lahar = Lahar()

@app.route('/mine',methods=['GET'])
def mineLahar():
    return 'mining'

@app.route('/transactions',method=['POST'])
def create_new_transaction():
    transaction = request.request_json()
    required_fields = ['sender','receiver','amount']
    if not all(k in transaction for k in required_fields):
        return jsonify({'message':'Missing values'}),400
    
    lahar.new_transaction(sender=transaction['sender'],
                          receiver=transaction['receiver'],
                          amount=transaction['amount'])
    response = {'message':'Transaction added'}
    return jsonify(response),201

@app.route('/chain',method=['GET'])
def get_full_chain():
    response = {'chain':lahar.chain,'length':len(lahar.chain)}
    return jsonify(response),200


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8053)