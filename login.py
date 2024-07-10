print("1.LOGIN AS ADMIN.../n 2.LOGIN AS CUSTOMER...")
ch=int(input("ENTER YOUR CHOICE=>"))
if(ch==1):
    count=3
    while(count!=0):
        uname=input("ENTER THE USERNAME=>")
        upass=input("ENTER THE PASSWORD=>")
        if(uname=="admin" and upass=="1234"):
            print("YOU HAVE SUCCESSFULLY LOGGED IN...")
            count=1
        elif(uname!="admin" and upass!="1234"):
            print("LOG IN UNSUCCESSFUL... \n RE-ENTER THE VALLID USERNAME AND PASSWORD... ")
        elif(uname!="admin"):
            print("AUTHENTICATION FALIURE...")
            print("RE-ENTER THE VALLID USERNAME..")
        elif(upass!="1234"):
            print("AUTHENTICATION FALIURE...")
            print("RE-ENTER THE VALLID PASSWORD..")
        count-=1
        if(count!=0):
            print("REMAINING ATTEMPTS=",count)
            print("YOU CAN TRY AGAIN...")
else:
    print("------------------------------------------WELCOME TO AIRLINE MANAGEMENT SYSTEM-----------------------------------------------------------")
    print("1.VIEW AIRLINE DETAILS.../n SELECT CLASS /n TICKET BOOKING... /n VIEW TICKET DETAILS... /n VIEW THE MEALS...")
    ch=int(input("ENTER YOUR CHOICE=>"))
    

