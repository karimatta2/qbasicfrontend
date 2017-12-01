#!/bin/bash

clear

echo "Logout testing begins now..."
echo ""
echo "Aside: login only has negative tests"
echo ""
echo "Now we will apply the negative tests to logout"
echo ""

./qbank.py accounts.txt transactions1.txt < negativetests1.txt
./qbank.py accounts.txt transactions2.txt < negativetests2.txt
./qbank.py accounts.txt transactions3.txt < negativetests3.txt
./qbank.py accounts.txt transactions4.txt < negativetests4.txt
./qbank.py accounts.txt transactions5.txt < negativetests5.txt
