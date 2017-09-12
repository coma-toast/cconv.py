#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json


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
    print json.dumps(theJSON, indent=2, separators=(',', ':'))

    #try to print JUST the current type that is requested
    #for i in ...???



def main():
    urlData = "https://coinmarketcap-nexuist.rhcloud.com/api/"
    webUrl = urllib2.urlopen(urlData)
    #print (webUrl.getcode())
    #I will eventually turn this into a try/except thingy
    if (webUrl.getcode() == 200):
        print "Connection successful."
    else:
        print "Received an error from server, cannot retrieve results " + str(webUrl.getcode())
    #prompt user for coin
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
