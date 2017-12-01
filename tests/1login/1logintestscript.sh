#!/bin/bash

clear

echo "Login testing begins now..."
echo ""
echo "Currently doing positive tests on Login"
echo ""
./qbank.py accounts.txt transactions.txt < positivetests.txt
./qbank.py accounts.txt transactions2.txt < positivetests2.txt
echo ""
echo "Currently doing negative tests on Login"
./qbank.py accounts.txt transactionsN.txt < negativetests.txt



