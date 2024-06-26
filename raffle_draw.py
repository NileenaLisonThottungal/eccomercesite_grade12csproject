while True:
            print("1.prizes")
            print("2.Entry")
            print("3.Winners")
            print("press 0 to move to other options")
            c=int(input("Enter your choice"))
            if (c==0):
                break
            elif (c==1):
                print("PRIZES ARE--")
                print("1st prize is car & Qr 10000")
                print("2nd prize is bike & Qr1000")
                print("3rd prize is Laptop & 1000 qr gift voucher")

            elif(c==2):
                n=input("Enter your name:- ")
                e=input("Enter your email id")
                import random
                print("Your lucky number is =   ",random.randint(1,100))
            elif(c==3):
                import random
                print("Lucky number of the 1st prize winner is =   ",random.randint(1,100))
                print("Lucky number of the 2nd prize winner is =   ",random.randint(1,100))
                print("Lucky number of the 3rd prize winner is =   ",random.randint(1,100))
            else:
                print("choose appropriate option")
