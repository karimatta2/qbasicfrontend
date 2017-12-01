#!/bin/bash

clear

echo "Begin Withdraw tests.."
echo "" 
echo "Positive tests withdraw"
echo ""
./qbank.py Accounts.txt TransfileAPos.txt < PosTestsA.txt
./qbank.py Accounts.txt TransfileMPos.txt < PosTestsM.txt

echo ""
echo "Negative tests on withdraw"
./qbank.py Accounts.txt TransfileANeg.txt < NegTestsA.txt
./qbank.py Accounts.txt TransfileMNeg.txt < NegTestsM.txt

