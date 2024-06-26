#DETAILS MODULE
l=input("Enter your first name")
for i in l:
    if (l.isalpha()):
        print("verified")
    else:
        print("Write a proper name")
    break
m=input("Enter your middle name:-")
for i in m:
    if (m.isalpha()):
        print("verified")
    else:
        print("Write a proper name")
        break
n=input("Enter your last name:-")
for i in n:
    if (n.isalpha()):
        print("verified")
    else:
        print("Write a proper name")
        break
p=input("Enter your phone number")
for i in p:
    if (p.isdigit()):
        print("verified")
    else:
        print("Write a proper phone number")
        break
e=input("Enter your email id")
for i in e:
    if (i=="@"):
        print("verified")
    else:
        print("Write a proper email id")
        break

                

    

    
