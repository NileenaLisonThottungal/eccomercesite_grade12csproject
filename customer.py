# CUSTOMER MODULE
import details
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8")
mycursor=mydb.cursor()
mycursor.execute("use SHOPPING_MALL_")
#creating required tables
mycursor.execute("create table if not exists customer(Sno char(4) primary key,Name_of_the_product varchar(30),category char(20),cost int(6), quantity int)")
mydb.commit()
def Express_Delivery ():
    print(" Grocery items")
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
    mycursor=mydb.cursor()
    print("S no","     Name of product     ","   category of the product  ","  Date of manufacture  ", "  Date of expiry  ","  cost  ","  quantity  ")
    mycursor.execute("select Sno ,space(5),Name_of_the_product ,space(5),category,space(5),Date_of_manufacture ,space(5),Date_of_expiry ,space(5),cost ,space(5), quantity  from grocery")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Freshfood ")
    print("S no","     Name of product     ","   category of the product  ","  Date of manufacture  ", "  Date of expiry  ","  cost  ","  quantity  ")
    mycursor.execute("select Sno ,space(5),Name_of_the_product ,space(5),category,space(5),Date_of_manufacture ,space(5),Date_of_expiry ,space(5),cost ,space(5), quantity  from freshfood")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    while True:
        print("1.Grocery item")
        print("2.Freshfood")
        print("3.Payment")
        print("4.exit")
        print("Inorder to buy Grocery type 1")
        print("Inorder to buy Freshfood type 2")
        c=int(input("ENTER YOUR CHOICE:- "))
        if (c==1):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from grocery where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==2):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from Freshfood where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==3):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("select * from customer")
            myrecords=mycursor.fetchall()
            for x in myrecords:
                print (x)
            print("Total cost")
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("select sum(cost)  from customer")
            myrecords=mycursor.fetchall()
            for x in myrecords:
                print (x)
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("delete from customer")
            mydb.commit()
            
        elif (c==4):
            break
        else:
            print("invalid option")
def Standard_delivery():
    print(" Grocery items")
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
    mycursor=mydb.cursor()
    mycursor.execute("select Sno ,space(5),Name_of_the_product ,space(5),category,space(5),Date_of_manufacture ,space(5),Date_of_expiry ,space(5),cost ,space(5), quantity  from grocery")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Freshfood ")
    print("S no","     Name of product     ","   category of the product  ","  Date of manufacture  ", "  Date of expiry  ","  cost  ","  quantity  ")
    mycursor.execute("select Sno ,space(5),Name_of_the_product ,space(5),category,space(5),Date_of_manufacture ,space(5),Date_of_expiry ,space(5),cost ,space(5), quantity  from freshfood")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Mobile_and_Gadgets  ")
    print("S no","    Name_of_the_item     ","   Brand  ","  Warranty  ", "  cost  ","  quantity  ")
    mycursor.execute("select Sno, space(5),Name_of_the_item ,space(5),Brand ,space(5),Warranty,space(5),cost ,space(5) quantity  from Mobile_and_Gadgets_")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Electronics")
    print("S no","    Name_of_the_item     ","   Brand  ","  Warranty  ","  cost  ","  quantity  ")
    mycursor.execute("select Sno, space(5),Name_of_the_item ,space(5),Brand ,space(5),Warranty,space(5),cost ,space(5) quantity from Electronics")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Home_and_Living")
    print("S no","    Name_of_the_item     ","   Brand  ","  Warranty  ", "  cost  ","  quantity  ")
    mycursor.execute("select Sno, space(5),Name_of_the_item ,space(5),Brand ,space(5),Warranty,space(5),cost ,space(5) quantity from Home_and_Living")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Fashion")
    print("S no","    Name_of_the_item     ","   Brand  ", "  cost  ","  quantity  ")
    mycursor.execute("select Sno, space(5),Name_of_the_item ,space(5),Brand ,space(5),cost ,space(5) quantity from Fashion")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    while True:
        print("1.Grocery item")
        print("2.Freshfood")
        print("3.Mobile & Gadget")
        print("4.Electronics")
        print("5. Home& living")
        print("6.Fashion")
        print("7.Payment")
        print("8.exit")
        c=int(input("ENTER YOUR CHOICE:- "))
        if (c==1):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from grocery where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==2):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from Freshfood where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==3):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_item ,brand, cost, quantity  from Mobile_and_Gadgets where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==4):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_item ,brand, cost, quantity  from Electronics where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==5):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_item ,brand, cost, quantity  from Home_and_Living where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==6):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_item ,brand, cost, quantity  from Fashion where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==7):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("select * from customer")
            myrecords=mycursor.fetchall()
            for x in myrecords:
                print (x)
            print("Total cost")
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("select sum(cost)  from customer")
            myrecords=mycursor.fetchall()
            for x in myrecords:
                print (x)
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("delete from customer")
            mydb.commit()
        elif (c==8):
            break
        else:
            print("invalid option")
def Collect_from_store():
    print(" Grocery items")
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
    mycursor=mydb.cursor()
    mycursor.execute("select Sno ,space(5),Name_of_the_product ,space(5),category,space(5),Date_of_manufacture ,space(5),Date_of_expiry ,space(5),cost ,space(5), quantity  from grocery")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Freshfood ")
    print("S no","     Name of product     ","   category of the product  ","  Date of manufacture  ", "  Date of expiry  ","  cost  ","  quantity  ")
    mycursor.execute("select Sno ,space(5),Name_of_the_product ,space(5),category,space(5),Date_of_manufacture ,space(5),Date_of_expiry ,space(5),cost ,space(5), quantity  from freshfood")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Mobile_and_Gadgets  ")
    print("S no","    Name_of_the_item     ","   Brand  ","  Warranty  ", "  cost  ","  quantity  ")
    mycursor.execute("select Sno, space(5),Name_of_the_item ,space(5),Brand ,space(5),Warranty,space(5),cost ,space(5) quantity  from Mobile_and_Gadgets_")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Electronics")
    print("S no","    Name_of_the_item     ","   Brand  ","  Warranty  ","  cost  ","  quantity  ")
    mycursor.execute("select Sno, space(5),Name_of_the_item ,space(5),Brand ,space(5),Warranty,space(5),cost ,space(5) quantity from Electronics")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Home_and_Living")
    print("S no","    Name_of_the_item     ","   Brand  ","  Warranty  ", "  cost  ","  quantity  ")
    mycursor.execute("select Sno, space(5),Name_of_the_item ,space(5),Brand ,space(5),Warranty,space(5),cost ,space(5) quantity from Home_and_Living")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    print(" Fashion")
    print("S no","    Name_of_the_item     ","   Brand  ", "  cost  ","  quantity  ")
    mycursor.execute("select Sno, space(5),Name_of_the_item ,space(5),Brand ,space(5),cost ,space(5) quantity from Home_and_Living")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print (x)
    while True:
        print("1.Grocery item")
        print("2.Freshfood")
        print("3.Mobile & Gadget")
        print("4.Electronics")
        print("5. Home& living")
        print("6.Fashion")
        print("7.Payment")
        print("8.exit")
        c=int(input("ENTER YOUR CHOICE:- "))
        if (c==1):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from grocery where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==2):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from Freshfood where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==3):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from Mobile_and_Gadgets where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==4):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from Electronics where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==5):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from Home_and_Living where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==6):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            Sno=str(input("Enter serial number:"))
            mycursor.execute("INSERT INTO customer select Sno , Name_of_the_product ,category, cost, quantity  from Fashion where Sno=(%s) ",(Sno,))
            mydb.commit()
            print("Item is inserted into bill successfully")
        elif (c==7):
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("select * from customer")
            myrecords=mycursor.fetchall()
            for x in myrecords:
                print (x)
            print("Total cost")
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("select sum(cost)  from customer")
            myrecords=mycursor.fetchall()
            for x in myrecords:
                print (x)
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8",database="SHOPPING_MALL_")
            mycursor=mydb.cursor()
            mycursor.execute("delete from customer")
            mydb.commit()
        elif (c==8):
            break
        else:
            print("invalid option")
while True:
    print("************************************")
    print("1.Express Delivery (Essential product will be delivered on the same day)")
    print("2.Standard delivery(Essential product will be delivered as per the slot available)")
    print("3.Collect from store(Product delivered on the same day)")
    print("4.Exit")
    print("************************************")
    ch=int(input("Enter your choice"))
    if ch==1:
        Express_Delivery ()
    if ch==2:
        Standard_delivery()
    if ch==3:
        Collect_from_store()
    if ch==4:
        break
