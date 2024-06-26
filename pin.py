p=input("Enter your Account Number")
    #Minimum 8 characters.
    #The alphabets must be between [a-z]
    #At least one alphabet should be of Upper Case [A-Z]
    #At least 1 number or digit between [0-9].
    #At least 1 character from [ _ or @ or $ ]
l, u, p, d = 0, 0, 0, 0
s = input("Enter your OTP")
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
    print("Valid Pincode.........WELCOME")
    a=int(input("ENTER THE AMOUNT TO BE TRANSFERRED"))
    print("Transaction successfully completed, Amount=",a)
else:
    print("Invalid pincode")
