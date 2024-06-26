#STOCK
#https://www.webmd.com/food-recipes/guide/grocery-list#1
#https://www.gadgetsnow.com/mobile-phones/Samsung
#http://www.shudhrestaurant.com/menu.html
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", charset="utf8")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists SHOPPING_MALL_")
mycursor.execute("use SHOPPING_MALL_")
#creating required tables 
mycursor.execute("create table if not exists Grocery(Sno char(4) primary key,Name_of_the_product varchar(30),category char(20),Date_of_manufacture date,Date_of_expiry date,cost int(6), quantity int)")
mycursor.execute("create table if not exists FreshFood(Sno char(4) primary key,Name_of_the_product varchar(30),category char(20),Date_of_manufacture date,Date_of_expiry char(20),cost int(6), quantity int)")
mycursor.execute("create table if not exists Mobile_and_Gadgets_ (Sno char(4) primary key,Name_of_the_item varchar(30),Brand char(20),Warranty char(20),cost int(6), quantity int)")
mycursor.execute("create table if not exists Electronics(Sno char(4) primary key,Name_of_the_item varchar(30),Brand char(20),Warranty char(20),cost int(6), quantity int)")
mycursor.execute("create table if not exists Home_and_Living(Sno char(4) primary key,Name_of_the_item varchar(30),Brand char(20),Warranty char(20),cost int(6), quantity int)")
mycursor.execute("create table if not exists Fashion(Sno char(4) primary key,Name_of_the_item varchar(30),Brand char(20),cost int(6), quantity int)")
mydb.commit()
while(True):
    
    print("1.Insert Grocery items")
    print("2.Insert FreshFood")
    print("3.Insert Mobile and Gadgets")
    print("4.Insert Electronics")
    print("5.Insert Home Appliances")
    print("6.Insert Fashion")
    print("7.Exit")
    ch=int(input("Enter your choice:"))
    
#PROCEDURE FOR INSERTING GROCERY
    if(ch==1):
        print("All information regarding the product are to be filled")
        Sno=str(input("Enter Serial number:"))
        Name_of_the_product=input("Enter Name of the product(limit 30 characters):")
        category=input("Enter the category of product:")
        Date_of_manufacture=str(input("Enter Date of manufacture:"))
        Date_of_expiry=str(input("Enter Date of expiry:"))
        cost=int(input("Enter the cost"))
        quantity=int(input("Enter the Quantity"))
        mycursor.execute("insert into grocery values('"+Sno+"','"+Name_of_the_product+"','"+category+"','"+Date_of_manufacture+"','"+Date_of_expiry+"','"+str(cost)+"','"+str(quantity)+"')")
        mydb.commit()
        print("GROCERY ITEM IS SUCCESSFULLY INSERTED!!!")
    elif (ch==2):
        print("All information regarding the product are to be filled")
        print("Quantity has to be mentioned in kg ie only the number")
        Sno=str(input("Enter Serial number:"))
        Name_of_the_product=input("Enter Name of the product(limit 30 characters):")
        category=input("Enter the category of product:")
        Date_of_manufacture=str(input("Enter Date of manufacture:"))
        Date_of_expiry=str(input("Enter Date of expiry:"))
        cost=int(input("Enter the cost"))
        quantity=int(input("Enter the Quantity"))
        mycursor.execute("insert into freshfood values('"+Sno+"','"+Name_of_the_product+"','"+category+"','"+Date_of_manufacture+"','"+Date_of_expiry+"','"+str(cost)+"','"+str(quantity)+"')")
        mydb.commit()
        print("FRESH FOOD IS SUCCESSFULLY INSERTED!!!")
    elif (ch==3):
        print("All information regarding the product are to be filled")
        Sno=str(input("Enter Serial number:"))
        Name_of_the_item=input("Enter Name of the item(limit 30 characters):")
        Brand=input("Enter the brand name:")
        warranty=int(input("Enter the warranty"))
        cost=int(input("Enter the cost"))
        quantity=int(input("Enter the Quantity"))
        mycursor.execute("insert into Mobile_and_gadgets_ values('"+Sno+"','"+Name_of_the_item+"','"+Brand+"','"+str(warranty)+"','"+str(cost)+"','"+str(quantity)+"')")
        mydb.commit()
        print("ITEM IS SUCCESSFULLY INSERTED!!!")
    elif (ch==4):
        print("All information regarding the product are to be filled")
        Sno=str(input("Enter Serial number:"))
        Name_of_the_item=input("Enter Name of the product(limit 30 characters):")
        Brand=input("Enter the brand name:")
        warranty=int(input("Enter the warranty"))
        cost=int(input("Enter the cost"))
        quantity=int(input("Enter the Quantity"))
        mycursor.execute("insert into Electronics values('"+Sno+"','"+Name_of_the_item+"','"+Brand+"','"+str(warranty)+"','"+str(cost)+"','"+str(quantity)+"')")
        mydb.commit()
        print("ITEM IS SUCCESSFULLY INSERTED!!!")
    elif (ch==5):
        print("All information regarding the product are to be filled")
        Sno=str(input("Enter Serial number:"))
        Name_of_the_item=input("Enter Name of the product(limit 30 characters):")
        Brand=input("Enter the brand name:")
        warranty=int(input("Enter the warranty"))
        cost=int(input("Enter the cost"))
        quantity=int(input("Enter the Quantity"))
        mycursor.execute("insert into Home_and_Living values('"+Sno+"','"+Name_of_the_item+"','"+Brand+"','"+str(warranty)+"','"+str(cost)+"','"+str(quantity)+"')")
        mydb.commit()
        print("ITEM IS SUCCESSFULLY INSERTED!!!")
    elif (ch==6):
        print("All information regarding the product are to be filled")
        Sno=str(input("Enter Serial number:"))
        Name_of_the_item=input("Enter Name of the product(limit 30 characters):")
        Brand=input("Enter Brand name:")
        cost=int(input("Enter the cost"))
        quantity=int(input("Enter the Quantity"))
        mycursor.execute("insert into fashion values('"+Sno+"','"+Name_of_the_item+"','"+Brand+"','"+str(cost)+"','"+str(quantity)+"')")
        mydb.commit()
        print("ITEM IS SUCCESSFULLY INSERTED!!!")
    elif(ch==7):
        break
    
        

        
