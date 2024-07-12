from tickitbooking import booking,view,write_csv,search,search1,deletedata,updatedata,flighttype
from meal1 import main_meal,sub_meal,meals
from application import write_csv,read_csv,view
print("1.LOGIN AS ADMIN...\n 2.LOGIN AS CUSTOMER...")
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
    cnt=1
    while(cnt!=0):
                print("_______________________WELCOME TO AIRLINE MANAGEMENT SYSTEM_______________________________")
                print("\n 1.VIEW AIRLINES \n 2.TICKET BOOKING \n 3.VEIW BOOKINGS \n 4.VIEW MEALS \n 5.UPDATE TICKET DETIALS \n 6.CANCEL TICKET \n 7.SEARCH SEAT \n 8.SEARCH FLIGHT")
                ch=int(input("ENTER YOUR CHOICE=>"))
                if(ch==1):
                    print("----------------------------------THE DETIALS OF AIRLINES ARE AS FOLLOWS-----------------------------------------")
                    read_csv()
                    view()
                if(ch==2):
                    print("----------------------------------TICKET BOOKING-----------------------------------------")
                    flighttype()
                    booking()
                if(ch==3):
                    print("----------------------------------VEIW BOOKINGS-----------------------------------------")
                    view()
                if(ch==4):
                    print("----------------------------------VEIW MEALS-----------------------------------------")
                    meals()
                    main_meal()
                    sub_meal()
                if(ch==5):
                    print("----------------------------------UPDATE TICKET DETIALS-----------------------------------------")
                    updatedata()
                if(ch==6):
                    print("----------------------------------CANCEL TICKIT-----------------------------------------")
                    deletedata()
                if(ch==7):
                    print("----------------------------------SEARCH SEAT-----------------------------------------")
                    search()
                if(ch==8):
                    print("----------------------------------SEARCH FLIGHT-----------------------------------------")
                    search1()
                if(ch==9):
                    print("----------------------------------EXIT-----------------------------------------")
                    cnt=0
    

