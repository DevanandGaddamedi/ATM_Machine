from turtle import width


user_name = "rajshekar"
password = "1994"

customer_name = input("ENTER YOUR NAME :")
customer_password = input("ENTER YOUR PASSWORD :")

if customer_name == user_name and customer_password == password:
    print('''
    1.deposite
    2.withdraw
    3.mini_statement
    4.exit
    ''')
    balance_amount = 100000
    option = int(input("select your option :"))
    if option==1:
        dep = int(input("enter the amount :"))
        balance_amount += dep
        print("total amount :" , balance_amount)
    elif option == 2:
        withd = int(input("enter the amount :"))
        balance_amount -= withd
        print("total amount : " , balance_amount)
    elif option == 3:
        print("-----------------------------------")
        print("user name :" ,user_name)
        print("your balance amount is :" ,balance_amount)
        print("=========> thank you <=========")
        print("-----------------------------------")
    elif option == 4:
        exit()
else:
    print("you entered invalid user name or password")