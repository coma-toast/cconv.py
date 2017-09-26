#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
from pprint import pprint


#import requests


#coinmarketcap is weird, i'll try it again later
#from coinmarketcap import Market

#coinmarketcap = Market()
#currencyType = "USD"
#coinmarketcap.ticker(currencyType, limit=3, convert='EUR')


def printCoin(data):
    theJSON = json.loads(data)
    #print theJSON

    #for i in theJSON["market_cap"]:

    #This works, but dumps ALL currencies:
    #print json.dumps(theJSON, indent=2, separators=(',', ':'))

    #try to print JUST the currency type that is requested
    #for i in ...???
    #https://docs.python.org/2/library/json.html
    #https://stackoverflow.com/questions/9093684/how-to-print-particular-json-value-in-python
    #for symbol in theJSON:
    #    json.dumps({})

    #This also works, but dumps all currencies in one big text block
    #print theJSON
    print "Market Cap:"
    print(theJSON['market_cap'])



def main():
    urlData = "https://coinmarketcap-nexuist.rhcloud.com/api/"
    webUrl = urllib2.urlopen(urlData)
    #print (webUrl.getcode())
    #I will eventually turn this into a try/except thingy
    if (webUrl.getcode() == 200):
        print "Connection successful."
    else:
        print "Received an error from server, cannot retrieve results " + str(webUrl.getcode())
    #prompt user for coin, currency
    coinReq = raw_input('What coin you want to see? ')
    curReq = raw_input('What currency type? ')
    #combine main URL with the coin name into one string
    fullUrl = urlData + coinReq
    #open the full URL and then read the data, into a variable
    webUrl2 = urllib2.urlopen(fullUrl)
    data = webUrl2.read()
    #print out data for the coin specified
    printCoin(data)
    #print coinData




if __name__ == "__main__":
    # calling main function
    main()
