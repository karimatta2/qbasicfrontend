#!/bin/bash

clear

#cd inputs
#cd 1login 

echo "Login testing begins now..."
echo "Currently doing positive tests on Login"
./qbank.py accounts.txt transactions.txt < positivetests.txt
#for i in positivetests.txt
#do 
 #   ./qbank.py accounts.txt transactions.txt





