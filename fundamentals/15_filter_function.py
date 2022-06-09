accounts =[
    {   
        'id' : 'A0001',
        'name' : 'User 1',
        'Premium account' : True,
    },
    {   
        'id' : 'A0002',
        'name' : 'User 2',
        'Premium account' : False,
    },
    {   
        'id' : 'A0003',
        'name' : 'User 3',
        'Premium account' : True,
    },
]


def isPremiumAccount(account):
    if account['Premium account']:
        return False
    return True

result = filter(isPremiumAccount, accounts)
print(list(result))