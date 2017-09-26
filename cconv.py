#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
from pprint import pprint

def printCoin(data, curReq):
    theJSON = json.loads(data)
    print "Price:"
    print " $" + str(theJSON['price'][curReq])

    print "Market Cap:"
    print " $" + str(theJSON['market_cap'][curReq])

    print "Volume:"
    print " $" + str(theJSON['volume'][curReq])

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
    curReq = raw_input('What currency type? ').lower()
    #combine main URL with the coin name into one string
    fullUrl = urlData + coinReq
    #open the full URL and then read the data, into a variable
    webUrl2 = urllib2.urlopen(fullUrl)
    data = webUrl2.read()
    #print out data for the coin specified
    printCoin(data, curReq)
    #print coinData


if __name__ == "__main__":
    # calling main function
    main()
