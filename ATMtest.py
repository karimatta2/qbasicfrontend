import os

# a bunch of variables that will make testing easier
# /Users/karimabdallah/Desktop/CISC_327/ATM/ just gonna keep this here
loginPos = '/inputs/1login/positivetests.txt'
loginNeg = '/inputs/1login/negativetests'
createApos = '/inputs/2createacct/agent/positivetests'
createAneg = '/inputs/2createacct/agent/negativetests'
createMpos = '/inputs/2createacct/machine/positivetests'
createMneg = '/inputs/2createacct/machine/negativetests'
deleteApos = '/inputs/3deleteacct/agent/positivetests'
deleteAneg = '/inputs/3deleteacct/agent/negativetests'
deleteMpos = '/inputs/3deleteacct/machine/positivetests'
deleteMneg = '/inputs/3deleteacct/machine/negativetests'
depApos = '/inputs/4deposit/agent/positivetests'
depAneg = '/inputs/4deposit/agent/positivetests'
depMpos = '/inputs/4deposit/agent/positivetests'
depMneg = '/inputs/4deposit/agent/positivetests'
withApos = '/inputs/5withdraw/agent/positivetests'
withAneg = '/inputs/5withdraw/agent/negativetests'
withMpos = '/inputs/5withdraw/machine/positivetests'
withMneg = '/inputs/5withdraw/machine/negativetests'
tranApos = '/inputs/6transfer/agent/positivetests'
tranAneg = '/inputs/6transfer/agent/negativetests'
tranMpos = '/inputs/6transfer/machine/positivetests'
tranMneg = '/inputs/6transfer/machine/negativetests'
logoutApos = '/inputs/7logout/agent/positivetests'
logoutAneg = '/inputs/7logout/agent/negativetests'
logoutMpos = '/inputs/7logout/machine/positivetests'
logoutMneg = '/inputs/7logout/machine/negativetests'

#import qbank.py as atm

def test():
    input('Welcome to this automated test to begin testing hit enter')
    print('Begin Login Testing')
    print('Begin positive testing')
 #   atm.main('accountsLoginPos.txt', 'transLoginPos.txt')
    
test()
