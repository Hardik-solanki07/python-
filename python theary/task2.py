# 1.Enter a pin
# 2.add balance
# 3.check balance
# 4.withdraw
balance=0
pin1=0
a=True

while a:
    print("1. Enter a pin")
    print("2.add balance")
    print("3.check balance")
    print("4.withdraw")
    
    choice = int(input("Enter a choice : "))
    
    if choice == 1:
        pin = int(input("Enter a pin : "))
        pin1=pin
        print()
    
        
    elif choice == 2:
        pin = int(input("Enter a pin : "))
        
        if pin1==pin:
            amount = int(input("add balance : "))
            balance+=amount
            pin1=pin
            print("your balance is ",amount)
            print()
        else:
            print("Invalid pin")
           
        
    elif choice == 3:
        pin = int(input("Enter a pin : "))
        print("your balance is ",balance)
        print()
        
    elif choice == 4:
        pin = int(input("Enter a pin : "))
        amount = float(input("withdraw amount: "))
        if amount <= balance:
            balance-=amount
            print("your balance is ",amount)
        else:
            print("Insufficient balance")
        
    else:
        print("Invalid choice , try again")
        
    n=input("Enter 'y' for yes and 'n' for no :")
    if n=='y':
        a=True
    else:
        a=False    
    
        
        
        
    
        
    



