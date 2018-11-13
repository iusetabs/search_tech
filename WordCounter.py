#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import sys
import re
import porter2 as port

def createWordsDict(fileName):
	inputFile = open(fileName).read()
	wordsDict = {}
	delims= r'[ "\t,;.?!\r\n]+'
	temp = filter(None, re.split(delims,inputFile))
	for token in temp:
		token = port.stem(token.lower())
		if token not in wordsDict and token != None:
			wordsDict[token] = 1
		else:
			wordsDict[token] += 1
	return wordsDict

def get_top_terms(wordsDict, k):
	return sorted(wordsDict.items(), key=operator.itemgetter(1))[-int(k):][::-1]


def main():
	try:
		fileName = sys.argv[1]
		k = 5
		if len(sys.argv) > 2:
			k = int(sys.argv[2])
		wordsDict = get_top_terms(createWordsDict(fileName), k)
		print "The top ", k, " terms are:\n"
		i = 0
		for item in wordsDict:
			print "Rank #", k-k+i+1, " : ", item[0], "\n\tOccurances: ", item[1], "\n"
			i+=1

		print "\n---Done.\n"
	except Exception, err:
		print Exception, err

if __name__ == '__main__':
	main()

#Author: Piyush Arora
#Have fun, keep coding
