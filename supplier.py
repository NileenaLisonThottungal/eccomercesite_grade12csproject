#SUPPLIER MODULE
def supplier_login():
    user=input("Enter your username")
    #Minimum 8 characters.
    #The alphabets must be between [a-z]
    #At least one alphabet should be of Upper Case [A-Z]
    #At least 1 number or digit between [0-9].
    #At least 1 character from [ _ or @ or $ ]
    l, u, p, d = 0, 0, 0, 0
    s = input("Enter your password")
    if (len(s) >= 8):
        for i in s:
            # counting lowercase alphabets
            if (i.islower()):
                l+=1
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1
            # counting digits
            if (i.isdigit()):
                d+=1
            # counting the mentioned special characters
            if(i=='@'or i=='$' or i=='_'):
                p+=1
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
        print("Valid Password.........WELCOME")
    else:
        print("Invalid Password")
    print("*****************************************************")
    import stock
def About_us():
    import about_us
while True:
    print("1.SUPPLIER LOGIN")
    print("2.ABOUT US")
    print("3.EXIT")
    c=int(input("ENTER A NUMBER"))
    if c==1:
        supplier_login()
    if c==2:
        About_us()
    if c==3:
        break
    else:
        print("invalid option")
        
        
        
        
