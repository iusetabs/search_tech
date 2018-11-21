#!/bin/bash
rm -f search_get_out.csv
wget -r "http://136.206.48.37:8084/IRModelGenerator/TrecBatchQueryExecuterServlet?treccode=6&simf=BM25&k=$1&b=$2" > search_get_out.csv
lineNo=cat search_get_out.csv | wc -l
echo "Downloaded CSV. Line numbers = $lineNo" 
