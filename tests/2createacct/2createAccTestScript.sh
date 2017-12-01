#!/bin/bash

clear

echo "createAcc testing begins now..."
echo ""
echo "Currently doing positive tests on createAcc"
echo ""
./qbank.py accounts.txt transactionsP.txt < CREpos.txt
echo ""
echo "Currently doing negative tests on createAcc"
./qbank.py accounts.txt transactionsN.txt < CREneg.txt
./qbank.py accounts.txt transactionsN2.txt < CREneg2.txt
./qbank.py accounts.txt transactionsN3.txt < CREneg3.txt
