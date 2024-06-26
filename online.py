def Online_customer():
    Shipping_Details=input("Enter your Shipping details")
    Location=input("Enter your location")
while True:
    print("************************************")
    print("1.Online")
    print("2.exit")
    print("************************************")
    ch=int(input("If you are an online customer then press 1, For exit press 2"))
    if ch==1:
        Online_customer()
    elif ch==2:
        break
    else:
        print("choose appropriate option")
