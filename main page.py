import welcome
while True:
    print("1.Customer")
    print("2.About us")
    print("3.Contact us")
    print("4.Raffle draw")
    print("5.charity")
    print("6.Policies")
    print("7.Suppliers")
    print("8.exit")
    c=int(input("Enter your choice"))
    print("**************************************************************************************************************")
    if (c==1):
        import customer
        print("**************************************************************************************************************")
    elif (c==2):
        while True:
            print("1.Overview")
            print("2.Feedback")
            print("press 0 to move to other options")
            d=int(input("Enter your choice"))
            if (d==0):
                break
            elif (d==1):
                import about_us
            elif (d==2):
                f=input("Enter your feedback")
                print("YOUR FEEDBACK IS", f)
            else:
                print("invalid choice")
            print("**************************************************************************************************************")
    elif (c==3):
        while True:
            print("1.contact information")
            print("press 0 to move to other options")
            d=int(input("Enter your choice"))
            if (d==0):
                break
            elif(d==1):
                import contact_info
            else:
                print("INVALID OPTION")
            print("**************************************************************************************************************")
    elif (c==4):
        import raffle_draw
        print("**************************************************************************************************************")
    elif (c==5):
        while True:
            print("1.online transaction")
            print("2.Direct payment")
            print("press 0 to move to other options")
            d=int(input("Enter your choice"))
            if (d==0):
                break
            elif(d==1):
                import pin
            elif (d==2):
                import pin
                print("Please go to the counter and collect the transaction details")
            print("**************************************************************************************************************")
    elif (c==6):
        while True:
            print("1.Terms and conditions")
            print("2.Return policy")
            print("3.Privacy policy")
            print("4.Service and warranty")
            print("press 0 to move to other options")
            d=int(input("Enter your choice"))
            if (d==0):
                break
            elif(d==1):
                import terms_and_conditions
            elif(d==2):
                import return_policy
            elif(d==3):
                import privacy_policy
            elif(d==4):
                import servic_warranty
                print("**************************************************************************************************************")
    elif (c==7):
        import supplier
    elif (c==8):
        quit()
    else:
        print("Please choose the appropriate option")
        
    
    
            
            
    
