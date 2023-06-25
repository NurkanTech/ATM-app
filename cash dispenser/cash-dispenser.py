NurkanAccount={
         'name':'nurkan k',
         'accountNo': '124563',
         'balance': 3000,
         'addAccount': 2000
}
mAccount={
         'name':'m',
         'accountNo': '444563',
         'balance': 2000,
         'addAccount': 1000
}
nAccount={
         'name':'n',
         'accountNo': '444563',
         'balance': 2000,
         'addAccount': 1000
}

def withdraw_money(account,amount):
    print(f"Hello {account['name']}")

    if (account['balance']>= amount):
        account['balance']-= amount
        print('You can take money.')
        balance_inquiry(NurkanAccount)

    else:
        total=account['balance']+account['addAccount']

        if (total>=amount):
            addAccountUse=input(' Use additional account? (yes \ no)')

            if addAccountUse=='y':
                addAccountUse_amount=amount-account['balance']
                account['balance']=0
                account['addAccount']-=addAccountUse_amount
                print('You can take money.')
                balance_inquiry(NurkanAccount)

            else:
                print(f"{account['accountNo']} in your account no {account['balance']} exists. ")
        else:
            print('Sorry, insufficient balance.')
            balance_inquiry(NurkanAccount)

def balance_inquiry(account):
    print(f"{account['accountNo']} in your account no {account['balance']} TL exists. addAccount your limit if {account['addAccount']} exists.")

withdraw_money(NurkanAccount,1000)

print('*'*15)

withdraw_money(NurkanAccount,2000)
withdraw_money(NurkanAccount,1800) # insufficient balance
