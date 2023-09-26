import re
def isIFSCValid(ifsc):
        if not((len(ifsc)==11) and (ifsc[:4].isupper()==True) and (ifsc[:4].isalpha()==True) and (ifsc[4]=='0') and (ifsc[5:].isalnum()==True) and (ifsc[5:].isupper()==True)):
            return False
        else:
            return True

def isBankNameValid(bname):
        for i in bname:
            if not((i.isalpha()==True) or (i.isspace()==True)):
                return False
        return True

def isCityNameValid(city):
        for i in city:
            if not((i.isalpha()==True) or (i.isspace()==True)):
                return False
        return True

def isAgeValid(age):
    if not(age.isdigit()==True and int(age)<100 and int(age)>18):
        return False
    return True

def isAadharValid(aadhar):
    if not(len(aadhar)==12 and aadhar.isdigit()==True):
        return False
    return True

def isGenderValid(gender):
    t=('Male','Female','Transgender','M','F','m','f','MALE','FEMALE','TRANSGENDER','male','female','transgender')
    if not(gender in t):
        return False
    return True


def isAccountTypeValid(acc_type):
    t=('SAVINGS','SALARY','CURRENT','FIXED DEPOSITS','FD','RD','current','salary','savings','rd','fd')
    if not(acc_type in t):
        return False
    return True


def isBalanceValid(bal):
    if not(bal.isdigit()==True and int(bal)>0):
        return False
    return True

def isAddressValid(address):
    for i in address:
            if not((i.isalpha()==True) or (i.isspace()==True) or (i.isalnum()==True)):
                return False
    return True
    
def isAccountNumberValid(acc_no):
    len1=len(acc_no)
    for i in acc_no:
        if not((i.isdigit()==True) and (int(len1)>=11) and (int(len1)<=16)):
            return False
        return True

def isPanValid(pan):
    if not((len(pan)==10) and (pan[:5].isupper()==True) and (pan[:5].isalpha()==True) and (pan[5:9].isdigit()==True) and (pan[9].isalpha()==True) and (pan[9].isupper()==True)):
        return False
    else:
        return True

expr1='^\d{2}-\d{2}-\d{4}$'
def isDOBValid(dob):
    if not(re.match(expr1,dob)):
        return False
    else:
        return True

def isvalidAccountHolderName(acc_name):
    words=acc_name.split()
    for i in words:
        if not i[0].isupper() or not i.isalpha():
            return False
        return True
    
