# 1.Enter a pin
# 2.create a customer :
#         add name , email , phone , address
# 3.check customer details
# 4.add balance
# 5.check balance
# 6.withdraw


balance=0
pin1=123
a=True
details={}
while a:
    print('1.Enter a pin')
    print('''2.create a customer :
#         add name , email , phone , address''')
    print('3.check customer details ')
    print('4.add balance')
    print('5.check balance')
    print('6.withdraw')

    choice = int(input("Enter a choice : "))

    if choice == 1:
        pin=int(input("Etner a pin : "))
        print('pin generated')
        pin1=pin
        if pin1==pin:
            print('already exist pin pls enter a new pin')
        print('')


    elif choice == 2:
        pin = int(input("Etner a pin : "))
        if pin == pin1:

            print("create customer details :")
            name = input("Enter a customer name : ")
            email = input("Enter a customer email id : ")
            phone = int(input("Enter a customer mobile no : "))
            address = input("Enter a customer address : ")

            details={'name':name,
                     'email':email,
                     'phone':phone,
                     'address':address}
            print("customer details add successfully")
        else:
            print('Invalid pin')
        print('')

    elif choice == 3:
        print('check customer details first enter pin')
        pin = int(input("Etner a pin : "))
        if pin1 == pin:
            for i in details.items():
                print(i)
        else:
            print('Invalid pin pls enter currect pin')
        print('')

    elif choice == 4:
        pin = int(input("Etner a pin : "))
        amount = int(input('Enter a amount : '))
        if pin1 == pin :
            balance += amount
            pin1=pin
            print('your current balance is : ',amount)

        else:
            print('Invalid pin')

        print('')

    elif choice == 5:
        pin = int(input("Etner a pin : "))
        if pin1 == pin:
            print('your current balance is : ', balance)
        else:
            print('Invalid pin')
        print('')

    elif choice == 6:
        pin = int(input("Etner a pin : "))
        amount = int(input('Enter a amount : '))
        if pin1 == pin:
            balance -= amount
            pin1 = pin
            print('withdraw balance : ',amount)
            print('your current balance is : ', balance)

        else:
            print('Invalid pin')

    else:
        print('Invalid choice pls try again')
    print('')

    # n=input('Enter y for yes or n for no')
    # if n=='y':
    #     a=True
    # else:
    #     a=False







