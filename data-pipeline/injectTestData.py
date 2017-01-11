#!/usr/bin/env python3

# 
import os 
import sys

import argparse
import binascii

sys.path.append(os.path.abspath('../'))
from config import *
sys.path.pop()

import datetime
import logging 
import pika
import time
    
if __name__ == '__main__':
    # parse the command line arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument('exchange', 
        choices = ['data-pipeline-in', 'plugins-out'], 
        help = 'the name of the exchange into which the data is injected')
    argParser.add_argument('--period', 
        default = 3, 
        type = float,
        help = 'number of seconds between messages')
    argParser.add_argument('--num_messages', 
        default = 10, 
        type = int,
        help = 'number of messages to send')
    argParser.add_argument('--num_params', 
        default = 1, 
        type = int,
        help = 'number of parameters to send with each message')
    argParser.add_argument('--node_id', 
        default = '0000000000000000', 
        help = 'node id ')
    args = argParser.parse_args()
    print('args = ', args)
    
    # set up rabbitmq
    connection = pika.BlockingConnection(pika_params)
    channel = connection.channel()
    channel.basic_qos(prefetch_count=1)

    # loop through messages
    nMessages = 0
    while args.num_messages == 0 or nMessages < args.num_messages:
    
        print('injecting sample #', nMessages)
        ts = int(datetime.datetime.utcnow().timestamp() * 1000)
        
        if args.exchange == 'data-pipeline-in':
            myProperties = pika.BasicProperties(
                    reply_to    = args.node_id,
                    timestamp   = ts,
                    app_id      = 'testsensor:v1:0',
                    type        = 'param'
            )
        else:    #args.exchange == 'plugins-out':
            myProperties = pika.BasicProperties(
                    reply_to    = args.node_id,
                    timestamp   = ts,
                    app_id      = 'testsensor:v1:0',
                    type        = 'PR103J2',
                    headers     = { 
                                    'meta_id'    : '0',
                                    'unit'       : 'unit0',
                    }
            )
        print('properties = ', myProperties)
        dataList = []
        for iParam in range(args.num_params):
            dataList.append('"temperature":"{}"'.format(iParam, nMessages))
        data = '{' + ','.join(dataList) + '}'
        print('data = ', data)

        channel.basic_publish(exchange = args.exchange, 
                                properties = myProperties, 
                                routing_key = '', 
                                body = data)
        print('after publish...')

        nMessages += 1
        time.sleep(args.period)

    print('DONE injecting {} samples of test data...'.format(nMessages))
    
