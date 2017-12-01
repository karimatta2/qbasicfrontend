#!/bin/bash

clear

echo "deleteAcc testing begins now..."
echo ""
echo "Currently doing positive tests on deleteAcc"
echo ""
./qbank.py accounts.txt transactionsP.txt < DELpos.txt
echo ""
echo "Currently doing negative tests on deleteAcc"
./qbank.py accounts.txt transactionsN.txt < DELneg.txt
./qbank.py accounts.txt transactionsN2.txt < DELneg2.txt
