from banking.accounts import credit, debit, accountinfo

curbalance = credit.initialbal
curbalance = credit.creditbalance(curbalance, 50)
print(curbalance) # 150
curbalance = debit.debitbalance(curbalance, 20)
print(curbalance) # 130

print("******* Class *******")
userobj1 = accountinfo.user("Devid", "1234")
userobj2 = accountinfo.user("Arun", "5678")
userobj1.printaccdetails(100)
userobj2.printaccdetails(200)
print(userobj2.branch)
print(userobj2.accname)
