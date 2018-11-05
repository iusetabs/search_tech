#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import porter2 as port


def createWordsDict(fileName):
	inputFile = open(fileName).read()
	wordsDict = {}
	delims= r'[ "\t,;.?!\r\n]+'
	temp = re.split(delims,inputFile)
	for token in temp:
		token = token.lower()
		if token not in wordsDict:
			wordsDict[token] = 1
		else:
			wordsDict[token] += 1
	return wordsDict

def main():
	try:
		fileName = sys.argv[1]
		wordsDict = createWordsDict(fileName)
		for k,v in wordsDict.iteritems():
			print "Key: " + str(k) + " , Value: " + str(v)
	except:
		print "Error"

if __name__ == '__main__':
	main()

#Author: Piyush Arora
#Have fun, keep coding
