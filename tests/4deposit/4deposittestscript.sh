#!/bin/bash
#add accunt list, input tests 
clear

echo "Begin Deposit tests.."
echo "" 
echo "Positive tests deposit"
echo ""
./qbank.py Accounts.txt TransfileAPos.txt < PosTestsA.txt
./qbank.py Accounts.txt TransfileMPos.txt < PosTestsM.txt

echo ""
echo "Negative tests on deposit"
./qbank.py Accounts.txt TransfileANeg.txt < NegTestsA.txt
./qbank.py Accounts.txt TransfileMNeg.txt < NegTestsM.txt

