#!/usr/bin/env python
import argparse
def main():
    
    parser = argparse.ArgumentParser(description="This is the QBANK ATM")
    parser.add_argument('accounts')
    parser.add_argument('transactions')
    args = parser.parse_args()
    accountFile = args.accounts
    accList = accountsPrep(accountFile)
    transList = []
    
    #now accList is a list of integers and transList is a file
    print('Welcome to the ATM')
    mainFlag = True
    while mainFlag == True:
        loginVar = str(input("Type the word 'login' if you would like to log in to the QBank ATM\n"))
        if loginVar == 'login' or loginVar == 'Login':
            flag = True
            mode = login(accList)
            while flag == True:
                if mode == 'M':
                    #deposit, transfer, withdraw 
                    machineMenu = input("Press [D] to deposit\nPress [W] to withdraw \nPress [T] to transfer\nPress [Q] to logout\n")
                    if machineMenu == 'd' or machineMenu == 'D':
                        deposit(accList, mode, transList)
                    elif machineMenu == 'w' or machineMenu == 'W':
                        withdraw(accList, mode, transList)
                    elif machineMenu == 't' or machineMenu == 'T':
                        transfer(transList, accList, mode)
                    elif machineMenu == 'q' or machineMenu == 'Q':
                        logout(transList)
                        flag = False
                        mainFlag = False
                    else:
                        print("Incorrect input. Try again")
                else:
                    #agent mode so all transactions are allowed
                    agentMenu = input("Press [CA] to create an account.\nPress [DA] to delete an account.\nPress [D] to deposit\nPress [W] to withdraw \nPress [T] to transfer\nPress [Q] to logout\n")
                    if agentMenu == 'ca' or agentMenu == 'CA':
                        createacct(accList)
                    elif agentMenu == 'da' or agentMenu == 'DA':
                        deleteacct(accList)
                    elif agentMenu == 'd' or agentMenu == 'D':
                        deposit(accList, mode, transList)

                    elif agentMenu == 'w' or agentMenu == 'W':
                        withdraw(accList, mode, transList)
                    elif agentMenu == 't' or agentMenu == 'T':
                        transfer(transList, accList, mode)
                    elif agentMenu == 'q' or agentMenu == 'Q':
                        logout(transList)
                        flag = False
                        mainFlag = False
                    else:
                        print("Incorrect input. Try again")
        else:
            print("invalid login")
    with open('accounts.txt', 'w') as accounts:
        for i in accList:
            accounts.write(str(i) + "\n")
    
    with open('transactions.txt', 'w') as transactions:
        for i in transList:
            transactions.write(str(i) + "\n")

    #before returning accList must be turned back into a text file and transactions is already a text file
    return [accounts, transactions]

def accountsPrep(acct):
    accFile = open(acct, 'r')
    with open(acct) as f:
        accList = f.readlines()
    accList = [line.rstrip('\n') for line in open(acct)]
    accList = list(map(int, accList))
    return accList
    
def listToFile(transList):
    #write transList to text file
    
    with open("transList.txt", "w") as output:
        for item in transList:
            output.write(str(item) + "\n")
            output.write("EOS")
    return

def login(accountList):
    #login will take an array of valid accounts and return a list that has
    # a boolean that returns true or false and a character that tells us if
    # the machine is in agent or machine mode
    flag = True
    while flag == True:
        accNum = input("Account Number: ")

        notNumber = False
        try:
            int(accNum)
        except ValueError:
            print("Please enter a valid account number")
            notNumber = True
            
        if notNumber != True:
            if int(accNum) in accountList:
                mode= str(input("Press [M] for machine mode. Press [A] for agent mode.\n"))
                if mode == 'm' or mode == 'M':
                    flag = False
                    currentMode = 'M'
                elif mode == 'a' or mode == 'A':
                    flag = False
                    currentMode = 'A'
                else:
                    print("Wrong input. Please try again")
            else:
                print("Incorrect account number or password. Please try again")
                
    return str(currentMode)

#input = account list; output = new account list after creation
#adds a new valid account into the valid account list
def createacct(accountList): 

    notCreated = True

    while notCreated == True:

        newAccNum = input("New Account Number: ")

        #check all the constraints
        if (newAccNum.isnumeric() == True) and (len(newAccNum) == 7) and (int((newAccNum)[:1]) != 0) and (int(newAccNum) not in accountList):

            newAccNam = input("New Account Name: ")

            if (newAccNam.isalpha() == True) and len(newAccNam) > 2 and len(newAccNam) < 31:
                print("Created Succesfully")
                #update the list (append to the front)
                accountList = [int(newAccNum)] + accountList
                notCreated = False
                print(accountList)
                return accountList
            else:
                print("The account name is not in a right format!\nPlease re-enter...")

        else:
            print("Not a valid account, please re-enter...")





#input = account list; output = new account list after deletion
#deletes an existing valid account from the valid account list
def deleteacct(accountList):

    notDeleted = True

    while notDeleted == True:

        delAccNum = input("Number to be deleted: ")

        #check all the constraints
        if (delAccNum.isnumeric() == True) and (len(delAccNum) == 7) and (int((delAccNum)[:1]) != 0) and (int(delAccNum) in accountList):

            print("Account deleted.")
            notDeleted = False
            #update the list (delete from the list)
            accountList = [x for x in accountList if x != int(delAccNum)]
            print(accountList)
            return accountList

        else:

            print("Not a valid account, please re-enter...")

#Deposit method, takes account list and account mode and translist as inputs
#Method checks to see if the account is valid, after acceptance checks to see
#if deposit amount is valid by checking if the user is in agent or machine mode.
#After successfully passing both tests, method returns transaction file appended
#to original file translist file with updated deposit details
#translist as output
def deposit(accntList,mode, transList): #POS TESTS WORKING, NEG NEEDS FORMATTING - Txt file
    validAcc = False
    validDep = False
    while validAcc == False:
        accNum = input("Account Number: ")
        if int(accNum) in accntList:
            validAcc = True
        else:
            print("Invalid account number, please try again.")
            continue
    completeDep = False
    totalDep = 0
    while completeDep == False:
        depAmount = input("Deposit Amount (including cents): ")
        notNumber = False
        try:#numeric test
            int(depAmount)
        except ValueError:
            print("Please enter a valid account number")
            notNumber = True
        if notNumber == True:
            return
        else:
            if mode == 'm' or mode == 'M':
                if len(str(depAmount))<3:#neg testing
                    print("Invalid deposit amount!")
                    continue
                elif depAmount < 0:
                    print("Invalid deposit amount")
                    continue
                elif depAmount > 100000:
                    print("Invalid deposit amount")
                    continue
                elif depAmount <= 100000 and depAmount >= 0:#positive testing
                    totalDep += depAmount
                    validDep = True
                    complete = input("Enter 1 to complete deposit, Enter 2 to add another deposit")
                    if complete == '1':
                        if totalDep < 100000 and totalDep>0:#pos test
                            return transList.append("DEP "+ str(accNum)+ " " + str(totalDep) + " " + "0000000 " + " *")
                            completeDep = True
                        else: # neg test
                            print("Invalid total deposit amount")
                            return
                    elif complete == '2':
                        continue
                    else:
                        print("Invalid input")
                        continue
                
            elif mode == 'a' or mode == 'A':  
                if depAmount > 99999999:
                    print("Invalid deposit amount!")
                    continue
                elif len(str(depAmount))<3:#neg testing
                    print("Invalid deposit amount!")
                    continue
                elif depAmount < 0:
                    print("Invalid deposit amount")
                    continue
                elif depAmount <= 99999999 and depAmount >= 0: #positive testing
                    totalDep += depAmount
                    validDep = True
                    complete = input("Enter 1 to complete deposit, Enter 2 to add another deposit")
                    if complete == '1':
                        if totalDep > 99999999 and totalDep < 0:#pos test
                            return transList.append("DEP "+ str(accNum)+ " " + str(totalDep) + " " + "0000000 " + " *")    
                            completeDep = True  
                        else: # neg test
                            print("Invalid total deposit amount")
                            
                            return
                    elif complete == '2':
                        continue
                    else:
                        print("Invalid input")
                        continue

#Withdraw method, takes account list and account mode as inputs
#Method checks to see if the account is valid, after acceptance checks to see
#if withdraw amount is valid by checking if the user is in agent or machine mode.
#After successfully passing both tests, method returns transaction file appended
#to original file translist file with updated withdraw details
#translist as output
def withdraw(accntList,mode, transList):
    validAcc = False
    validWith = False
    while validAcc == False:
        accNum = input("Account Number: ")
        if int(accNum) in accntList:
            validAcc = True
        else:
            print("Invalid account number, please try again")
    completeWith = False
    totalWith = 0
    while completeWith == False:
        withAmt = int(input("Withdraw Amount (including cents): "))
        notNumber = False
        try:
            int(depAmount)
        except ValueError:
            print("Please enter a valid account number")
            notNumber = True
        if notNumber == True:
            return
        else:
            if mode == 'm' or mode == 'M':
                if withAmt < 0:
                    print("Invalid Withdraw amount, < 0")
                    continue
                elif len(withAmt) < 3:
                    print("Invalid withdraw amount, < 3 characters")
                    continue
                elif withAmt > 100000:
                    print("Invalid withdraw amount, > $1000 limit")
                    continue
                elif withAmt <= 100000 and withAmt >= 0:#positive testing
                    validWith = True
                    totalWith += withAmt
                    complete = input("Enter 1 to complete deposit, Enter 2 to add another deposit")
                    if complete == '1':
                        if totalWith < 100000 and totalWith > 0:#positie testing
                            return transList.append("WDR "+ str(accNum)+ " " + str(totalWith) + " " + "0000000 " + " *")
                            completeWith = True
                        else:
                            print("Invalid total withdraw amount")
                            continue
                    elif complete == '2':
                        continue
                    else:
                        print("Invalid input")
                        continue 
            
                
            elif mode == 'a' or mode == 'A': 
                #test if withdrawing <$1000 in single session multiple transactions- positive
                if withAmt > 99999999:
                    print("Invalid Withdraw amount, > maximum ($999,999.99)")
                    continue
                elif withAmt < 0:
                    print("Invalid Withdraw amount, < minimum ($0)")
                    continue
                elif len(withAmt) < 3:
                    print("Invalid withdraw amount, < 3 characters")
                    continue
                elif withAmt <= 99999999 and withAmt >= 0:#positive testing
                    validWith = True
                    totalWith += withAmt
                    complete = input("Enter 1 to complete deposit, Enter 2 to add another deposit")
                    if complete == '1':
                        if totalWith < 99999999:#positie testing
                            return transList.append("WDR "+ str(accNum)+ " " + str(totalWith) + " " + "0000000 " + " *")
                            completeWith = True
                        else:
                            print("Invalid total withdraw amount")
                            continue
                    elif complete == '2':
                        continue
                    else:
                        print("Invalid input")
                        continue
            else:
                print("Error, invalid input")

def transfer(transList, accountList, currentMode):
    #transfer from one account to another
    #asks for from account number, to account number, amount to transfer
    #check that account numbers & amount are valid
    #append transaction to transList and return transList

    confirmTrans = True
    while confirmTrans == True:
        fromAcc = input("From account number: ")
        toAcc = input("To account number: ")
        transAmount = input("Amount (in cents, no decimal): ")
        
        
        #check account numbers
        if (int(fromAcc) in accountList) and (int(toAcc) in accountList):

            if(currentMode == 'M'):
                if(transAmount >= 0) and (transAmount <= 100000):
                    newTransaction = "XFR " + toAcc + " " + transAmount + " " + fromAcc + " " + "*"
                    confirmTrans == False
                else:
                    print("Invalid amount. Please enter a value from $0 to $1000.00")

            else: #currentMode == 'A'
                if(transAmount >= 0) and (transAmount <= 99999999):
                    newTransaction = "XFR " + toAcc + " " + transAmount + " " + fromAcc + " " + "*"
                    confirmTrans == False
                else:
                    print("Invalid amount. Please enter a value from $0 to $999 999.99")

        else:
            print("Invalid account number(s). Please try again")

    transList.append(newTransaction)
    return transList

def logout(transList):
    print("You have successfully logged out.")
    transList.append("EOS 0000000 000 0000000 ***")

main()


