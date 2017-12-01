#!/bin/bash

clear

echo "Transfer testing begins now..."
echo ""
echo "Currently doing positive tests on Transfer"
echo ""
./qbank.py accounts.txt transactions.txt < positivetests.txt
./qbank.py accounts.txt transactions2.txt < positivetests2.txt
echo ""
echo "Currently doing negative tests on Transfer"
./qbank.py accounts.txt transactions3.txt < negativetests.txt
./qbank.py accounts.txt transactions4.txt < negativetests2.txt



