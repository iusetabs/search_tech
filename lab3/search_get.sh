#!/bin/bash
if [ "$1" == "-h" ]; then
  printf "Usage: `basename $0` \$1 \$2 \$3 \n \$1 = 6, 7 or 8 based on topics \n \$2 = the k factor \n \$3 = the b factor\n"
  exit 0
fi

rm -f search_get_out.csv
wget -r "http://136.206.48.37:8084/IRModelGenerator/TrecBatchQueryExecuterServlet?treccode=$1&simf=BM25&k=$2&b=$3" > search_get_out.csv
lineNo=cat search_get_out.csv | wc -l
printf "Downloaded CSV. Line numbers = $lineNo" 
