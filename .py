#Bank Account Program Making Which is Show  Transaction of Acoount
import random
Branch_Name="SCOUT LAND LANDON UK"
Account_Holder_FullName=input("Enter The Name")
Account_No=''.join([str(random.randint(0, 9)) for _ in range(12)])
print("Account No Check:",Account_No)

Debit_Crd_Number=''.join([str(random.randint(0, 9)) for _ in range(12)])
print("Grenrated Debit Card Number:",Debit_Crd_Number)


Deposit=float(input("Enter The Amount To Deposit:"))
Balance=Deposit

print("Acccount Created", end=" " "Information Given Below")
print("Bank of Scoutland", Branch_Name)
print(Account_Holder_FullName)
print(Account_No)

if isinstance(Deposit, float):
    print("Deposited Into Account ",Deposit)
    print("Corrent Availble Balance into A/c",Balance)

Check_Debit_Card=input("Enter Debit Card Number:")  
Debit=int(input("Amount wants :"))
  
if Debit_Crd_Number == Check_Debit_Card:
    print("Avaiable Balance int A/c",Balance)
    if Balance >0:
        Availble_Balance=Balance-Debit 
        if Availble_Balance >=0:
            print("Transaction Successfully Completely",Availble_Balance)
        else:
            print("Can't Reach This Transcation Check Balance:",Balance)
    else:
        print("Not Avaible Balance To Transiction Complete")
        if "Wants to Check Balance" == "YES":
            print(Account_No,"Updated Balance",Balance)
        else:
            print(Debit,"Successful Complete Transcation",Balance,)
else:
    print("Debit Card Will Be Blocked Connect With Branch")
    
    print("Bank of ScoutLand of Landon Uk")

