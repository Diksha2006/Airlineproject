import csv
b_id=[]
b_name=[]
b_dob=[]
passportno=[]
b_contactno=[]
b_email=[]
def flighttype():
    print("\n 1. DOMESTIC FLIGHT \n 2. INTERNATIONAL FLIGHT")
    ch=int(input("ENTER YOUR CHOICE=>"))
    print("\n 1.ECONOMY CLASS  \n 2.BUSINESS CLASS")
    c=int(input("ENTER YOUR CHOICE TO SELECT THE CLASS TYPE=>"))
    if(ch==1 and c==1):
        s=input("ENTER YOUR SOURCE=>")
        d=input("ENTER YOUR DESTINATION=>")
        if(s=="pune" and d=="goa"):
            print("AIRLINE NAME=INDIGO \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=6000")
            print("\n")
            print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=7000")
            print("\n")
            print("\n 1.INDIGO \n 2.KOHINUR \n 3.AIRINDIA \n 4.QATER")
            ch=int(input("ENTER YOUR CHOICE"))
            if(ch==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH INDIGO AIRLINES..")
            elif(ch==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH KOHINUR AIRLINES..")
            elif(ch==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA AIRLINES..")
            elif(ch==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH QATER AIRLINES..")    



        elif(s=="goa" and d=="pune"):
            print("AIRLINE NAME=INDIGO \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=6000")
            print("\n")
            print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=3000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=5000")
            print("\n") 
            print("\n 1.INDIGO \n 2.KOHINUR \n 3.AIRINDIA \n 4.QATER")
            ch1=int(input("ENTER YOUR CHOICE"))
            if(ch1==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH INDIGO AIRLINES..")
            elif(ch1==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH KOHINUR AIRLINES..")
            elif(ch1==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA AIRLINES..")
            elif(ch1==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH QATER AIRLINES..")    



        elif(s=="mumbai" and d=="hariyana"):
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=6000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=4000") 
            print("\n") 
            print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET \n 4.JETBLUE")
            ch2=int(input("ENTER YOUR CHOICE"))
            if(ch2==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
            elif(ch2==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
            elif(ch2==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
            elif(ch2==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")    

  
        elif(s=="hariyana" and d=="mumbai"): 
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
            print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET \n 4.JETBLUE")
            ch3=int(input("ENTER YOUR CHOICE"))
            if(ch3==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
            elif(ch3==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
            elif(ch3==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
            elif(ch3==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")    

        elif(s=="gujrat" and d=="panjab"):
            print("AIRLINE NAME=ROYAL AIR MACRO \n FLIGHT TIME=2:20PM TO 2:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 10:30AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=SOUTHWEST AIRLINE\n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 1:00PM TO 1:30PM \n 11:30AM TO 12:10PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=LATAM BRASIL \n FLIGHT TIME=1:20PM TO 1:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=ALASKA AIRLINE\n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=7000")
            print("\n")
            print("\n 1.ROYAL AIR MACRO \n 2.SOUTHWEST AIRLINE \n 3.LATAM BRASIL \n 4.ALASKA AIRLINE")
            ch4=int(input("ENTER YOUR CHOICE"))
            if(ch4==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH ROYAL AIR MACRO AIRLINES..")
            elif(ch4==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH SOUTHWEST AIRLINES..")
            elif(ch4==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH LATAM BRASIL AIRLINES..")
            elif(ch4==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH ALASKA  AIRLINES..")    

        elif(s=="panjab" and d=="gujrat"):
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=6000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=3000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
            print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET\n 4.JETBLUE")
            ch5=int(input("ENTER YOUR CHOICE"))
            if(ch5==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
            elif(ch5==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
            elif(ch5==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
            elif(ch5==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")  

            
        else:
            print("NO FLIGHTS ARE AVAILABLE FROM THE ENTERED SOURCE TO DESTINATION..\n WE WISH YOU HAD THE GOOD TIME AHEAD..")
    
    else:
        s=input("ENTER YOUR SOURCE=>")
        d=input("ENTER YOUR DESTINATION=>")
        if(s=="mumbai" and d=="bali"):
            print("AIRLINE NAME=INDIGO \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=205000")
            print("\n")
            print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=600000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=305000")
            print("\n")
            print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=307000")
            print("\n")
            print("\n 1.INDIGO \n 2.KOHINUR \n 3.WEST JET\n 4.QATER")
            ch6=int(input("ENTER YOUR CHOICE"))
            if(ch6==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH INDIGO AIRLINES..")
            elif(ch6==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH KOHINUR AIRLINES..")
            elif(ch6==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
            elif(ch6==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH QATER AIRLINES..")  



        elif(s=="bali" and d=="mumbai"):
            print("AIRLINE NAME=INDIGO \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=40000")
            print("\n")
            print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=50000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=55000")
            print("\n")
            print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=45000")
            print("\n")
            print("\n 1.INDIGO \n 2.KOHINUR \n 3.WEST JET\n 4.QATER") 
            ch7=int(input("ENTER YOUR CHOICE"))
            if(ch7==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH INDIGO AIRLINES..")
            elif(ch7==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH KOHINUR AIRLINES..")
            elif(ch7==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
            elif(ch7==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH QATER AIRLINES..")  





        elif(s=="goa" and d=="maldives"):
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=45000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=35000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=30000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=60000") 
            print("\n") 
            print("\n 1.AIRASIA INDIA\n 2.AIRINDIA EXPRESS  \n 3.WEST JET\n 4.JETBLUE") 
            ch8=int(input("ENTER YOUR CHOICE"))
            if(ch8==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
            elif(ch8==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
            elif(ch8==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
            elif(ch8==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")  


        elif(s=="maldives" and d=="goa"): 
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=30000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=35000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=40000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=55000")
            print("\n")
            print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET \n 4.JETBLUE")
            ch9=int(input("ENTER YOUR CHOICE"))
            if(ch9==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
            elif(ch9==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
            elif(ch9==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
            elif(ch9==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")  

        elif(s=="surat" and d=="russia"):
            print("AIRLINE NAME=ROYAL AIR MACRO \n FLIGHT TIME=2:20PM TO 2:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 10:30AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=30000")
            print("\n")
            print("AIRLINE NAME=SOUTHWEST AIRLINE\n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 1:00PM TO 1:30PM \n 11:30AM TO 12:10PM \n PRICE=20000")
            print("\n")
            print("AIRLINE NAME=LATAM BRASIL \n FLIGHT TIME=1:20PM TO 1:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=65000")
            print("\n")
            print("AIRLINE NAME=ALASKA AIRLINE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=70000")
            print("\n")
            print("\n 1.ROYAL AIR MACRO \n 2.SOUTHWEST AIRLINE  \n 3.LATAM BRASIL\n 4.ALASKA AIRLINE") 
            ch10=int(input("ENTER YOUR CHOICE"))
            if(ch10==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH ROYAL AIR MACRO  AIRLINES..")
            elif(ch10==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH SOUTHWEST AIRLINES..")
            elif(ch10==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH LATAM BRASIL AIRLINES..")
            elif(ch10==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH ALASKA AIRLINES..")  
            

        elif(s=="russia" and d=="surat"):
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=25000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=60000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=78000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=40000")
            print("\n")
            print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET \n 4.JETBLUE ")  
            ch11=int(input("ENTER YOUR CHOICE"))
            if(ch11==1):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
            elif(ch11==2):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
            elif(ch11==3):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
            elif(ch11==4):
                booking()
                print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")  
            

        else:
            print("NO FLIGHTS ARE AVAILABLE FROM THE ENTERED SOURCE TO DESTINATION..\n WE WISH YOU HAD THE GOOD TIME AHEAD..")
        if(ch==1 and c==2):
            s=input("ENTER YOUR SOURCE=>")
            d=input("ENTER YOUR DESTINATION=>")
            if(s=="pune" and d=="goa"):
                print("AIRLINE NAME=INDIGO \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=13000")
                print("\n")
                print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=150000")
                print("\n")
                print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=16000")
                print("\n")
                print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=17000")
                print("\n")
                print("\n 1.INDIGO \n 2.KOHINUR \n 3.AIRINDIA \n 4.QATER")
                ch=int(input("ENTER YOUR CHOICE"))
                if(ch==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH INDIGO AIRLINES..")
                elif(ch==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH KOHINUR AIRLINES..")
                elif(ch==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA AIRLINES..")
                elif(ch==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH QATER AIRLINES..")    



            elif(s=="goa" and d=="pune"):
                print("AIRLINE NAME=INDIGO \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=16000")
                print("\n")
                print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=13000")
                print("\n")
                print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=14000")
                print("\n")
                print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=15000")
                print("\n") 
                print("\n 1.INDIGO \n 2.KOHINUR \n 3.AIRINDIA \n 4.QATER")
                ch1=int(input("ENTER YOUR CHOICE"))
                if(ch1==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH INDIGO AIRLINES..")
                elif(ch1==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH KOHINUR AIRLINES..")
                elif(ch1==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA AIRLINES..")
                elif(ch1==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH QATER AIRLINES..")    



            elif(s=="mumbai" and d=="hariyana"):
                print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=50000")
                print("\n")
                print("AIRLINE NAME=AIRINDIA EXPRESS \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=60000")
                print("\n")
                print("AIRLINE NAME=WEST JET \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=40000")
                print("\n")
                print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=40000") 
                print("\n") 
                print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET \n 4.JETBLUE")
                ch2=int(input("ENTER YOUR CHOICE"))
                if(ch2==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
                elif(ch2==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
                elif(ch2==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
                elif(ch2==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")    

    
            elif(s=="hariyana" and d=="mumbai"): 
                print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=50100")
                print("\n")
                print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=41000")
                print("\n")
                print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=50100")
                print("\n")
                print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=41000")
                print("\n")
                print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET \n 4.JETBLUE")
                ch3=int(input("ENTER YOUR CHOICE"))
                if(ch3==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
                elif(ch3==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
                elif(ch3==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
                elif(ch3==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")    

            elif(s=="gujrat" and d=="panjab"):
                print("AIRLINE NAME=ROYAL AIR MACRO \n FLIGHT TIME=2:20PM TO 2:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 10:30AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=15000")
                print("\n")
                print("AIRLINE NAME=SOUTHWEST AIRLINE\n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 1:00PM TO 1:30PM \n 11:30AM TO 12:10PM \n PRICE=14000")
                print("\n")
                print("AIRLINE NAME=LATAM BRASIL \n FLIGHT TIME=1:20PM TO 1:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=15000")
                print("\n")
                print("AIRLINE NAME=ALASKA AIRLINE\n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=17000")
                print("\n")
                print("\n 1.ROYAL AIR MACRO \n 2.SOUTHWEST AIRLINE \n 3.LATAM BRASIL \n 4.ALASKA AIRLINE")
                ch4=int(input("ENTER YOUR CHOICE"))
                if(ch4==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH ROYAL AIR MACRO AIRLINES..")
                elif(ch4==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH SOUTHWEST AIRLINES..")
                elif(ch4==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH LATAM BRASIL AIRLINES..")
                elif(ch4==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH ALASKA  AIRLINES..")    

            elif(s=="panjab" and d=="gujrat"):
                print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=61000")
                print("\n")
                print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=13000")
                print("\n")
                print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=51000")
                print("\n")
                print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=40010")
                print("\n")
                print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET\n 4.JETBLUE")
                ch5=int(input("ENTER YOUR CHOICE"))
                if(ch5==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
                elif(ch5==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
                elif(ch5==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
                elif(ch5==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")  

                
            else:
                print("NO FLIGHTS ARE AVAILABLE FROM THE ENTERED SOURCE TO DESTINATION..\n WE WISH YOU HAD THE GOOD TIME AHEAD..")
        
        else:
            s=input("ENTER YOUR SOURCE=>")
            d=input("ENTER YOUR DESTINATION=>")
            if(s=="mumbai" and d=="bali"):
                print("AIRLINE NAME=INDIGO \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=205000")
                print("\n")
                print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=600000")
                print("\n")
                print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=305000")
                print("\n")
                print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=307000")
                print("\n")
                print("\n 1.INDIGO \n 2.KOHINUR \n 3.WEST JET\n 4.QATER")
                ch6=int(input("ENTER YOUR CHOICE"))
                if(ch6==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH INDIGO AIRLINES..")
                elif(ch6==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH KOHINUR AIRLINES..")
                elif(ch6==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
                elif(ch6==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH QATER AIRLINES..")  



            elif(s=="bali" and d=="mumbai"):
                print("AIRLINE NAME=INDIGO \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=490000")
                print("\n")
                print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=590000")
                print("\n")
                print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=565000")
                print("\n")
                print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=425000")
                print("\n")
                print("\n 1.INDIGO \n 2.KOHINUR \n 3.WEST JET\n 4.QATER") 
                ch7=int(input("ENTER YOUR CHOICE"))
                if(ch7==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH INDIGO AIRLINES..")
                elif(ch7==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH KOHINUR AIRLINES..")
                elif(ch7==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
                elif(ch7==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH QATER AIRLINES..")  





            elif(s=="goa" and d=="maldives"):
                print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=450000")
                print("\n")
                print("AIRLINE NAME=AIRINDIA EXPRESS \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=350000")
                print("\n")
                print("AIRLINE NAME=WEST JET \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=300000")
                print("\n")
                print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=600000") 
                print("\n") 
                print("\n 1.AIRASIA INDIA\n 2.AIRINDIA EXPRESS  \n 3.WEST JET\n 4.JETBLUE") 
                ch8=int(input("ENTER YOUR CHOICE"))
                if(ch8==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
                elif(ch8==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
                elif(ch8==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
                elif(ch8==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")  


            elif(s=="maldives" and d=="goa"): 
                print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=300000")
                print("\n")
                print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=305000")
                print("\n")
                print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=490000")
                print("\n")
                print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=550000")
                print("\n")
                print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET \n 4.JETBLUE")
                ch9=int(input("ENTER YOUR CHOICE"))
                if(ch9==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
                elif(ch9==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
                elif(ch9==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
                elif(ch9==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")  

            elif(s=="surat" and d=="russia"):
                print("AIRLINE NAME=ROYAL AIR MACRO \n FLIGHT TIME=2:20PM TO 2:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 10:30AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=305000")
                print("\n")
                print("AIRLINE NAME=SOUTHWEST AIRLINE\n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 1:00PM TO 1:30PM \n 11:30AM TO 12:10PM \n PRICE=205000")
                print("\n")
                print("AIRLINE NAME=LATAM BRASIL \n FLIGHT TIME=1:20PM TO 1:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=650500")
                print("\n")
                print("AIRLINE NAME=ALASKA AIRLINE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=705000")
                print("\n")
                print("\n 1.ROYAL AIR MACRO \n 2.SOUTHWEST AIRLINE  \n 3.LATAM BRASIL\n 4.ALASKA AIRLINE") 
                ch10=int(input("ENTER YOUR CHOICE"))
                if(ch10==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH ROYAL AIR MACRO  AIRLINES..")
                elif(ch10==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH SOUTHWEST AIRLINES..")
                elif(ch10==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH LATAM BRASIL AIRLINES..")
                elif(ch10==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH ALASKA AIRLINES..")  
                

            elif(s=="russia" and d=="surat"):
                print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=250500")
                print("\n")
                print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=600500")
                print("\n")
                print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=780500")
                print("\n")
                print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=405000")
                print("\n")
                print("\n 1.AIRASIA INDIA \n 2.AIRINDIA EXPRESS \n 3.WEST JET \n 4.JETBLUE ")  
                ch11=int(input("ENTER YOUR CHOICE"))
                if(ch11==1):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRASIA INDIA AIRLINES..")
                elif(ch11==2):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH AIRINDIA EXPRESS AIRLINES..")
                elif(ch11==3):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH WEST JET AIRLINES..")
                elif(ch11==4):
                    booking()
                    print("THANK YOU FOR BOOKING YOUR FLIGHT WITH JETBLUE AIRLINES..")  
                

            else:
                print("NO FLIGHTS ARE AVAILABLE FROM THE ENTERED SOURCE TO DESTINATION..\n WE WISH YOU HAD THE GOOD TIME AHEAD..")
        


def booking():
    cnt=101 
    n=input("ENTER THE NAME=")
    b_name.append(n)
    d=input("ENTER THE BIRTH_OF_DATE=")
    b_dob.append(d)
    p=(input("ENTER THE PASSPORT_NUMBER="))
    if(len(p)<=12):
        if(len(p)==12):
          passportno.append(p)
        else:
          print("ENTER THE VALLID PASSPORT NUMBER (CONSISTS WITH 12 DIGITS....)")
    c=(input("ENTER THE BOOKING CONTACT_NUMBER="))
    if(len(c)<=10):

        if(len(c)==10):
             b_contactno.append(c)
        else:
             print("ENTER THE VALLID CONTACT NUMBER (CONSISTS WITH 10 DIGITS....)")

    e=input("ENTER THE EMAIL_ID=")
    b_email.append(e) 
    print("BOOKING ID=>",cnt)
    b_id.append(cnt)
    print("TO VIEW THE TICKET DETIALS THE USERID WILL BE YOUR ENTERED EMAIL ID AND PASSWORD WILL BE CONTACT NUMBER....")
    c=int(input("PRESS 1 TO VEIW THE TICKIT DETIALS OR PRESS ANY DIGIT TO CONTINUE=>"))
    if(c==1):
        view()
    else:
        print("TICKIT BOOKED SUCCESSFULLY....")
    c=cnt+1
    with open ('bookflight.csv',mode='w',newline='') as file:
        writer=csv.writer(file)
        for i in range (len(b_id)):
            writer.writerow(("\t",b_id[i], "\t",b_name[i],"\t",b_dob[i],"\t",passportno[i],"\t",b_contactno[i],"\t",b_email[i]))
def view():
    #count=3
    #cnt=0
    #while(count!=0):
        #uname=input("ENTER THE USERNAME=>")
        #upass=input("ENTER THE PASSWORD=>")
        #if(uname==b_email[cnt] and upass==b_contactno[cnt]):
            #print("TICKET DETIALS CAN BE FETCHED SUCESSFULLY...")
            #count=1
        #elif(uname!=b_email[cnt] and upass!=b_contactno[cnt]):
            #print("\n RE-ENTER THE VALLID USERNAME AND PASSWORD... ")
        #elif(uname!=b_email[cnt]):
            #print("AUTHENTICATION FALIURE...")
           # print("RE-ENTER THE VALLID USERNAME..")
        #elif(upass!=b_contactno[cnt]):
            #print("AUTHENTICATION FALIURE...")
            #print("RE-ENTER THE VALLID PASSWORD..")
        #count-=1
        #if(count!=0):
            #print("REMAINING ATTEMPTS=",count)
            #print("YOU CAN TRY AGAIN...")
    #cnt+=1
    for i in range(len(b_id)):
        print("\t",b_id[i], "\t",b_name[i],"\t",b_dob[i],"\t",passportno[i],"\t",b_contactno[i],"\t",b_email[i])
flighttype()

def search(a_id,a_name,a_type,a_location):
    print("_______________SEARCH RECORDS_________________ ")
    t1=input("ENTER THE FLIGHT TO BE SEARCH:-")
    
    for i in range (len(a_id)):
        if(t1==a_id):
            print("\t",a_id[i],"\t",a_name[i],"\t",a_type[i],"\t",a_location[i])

def search1(b_id,b_name,b_dob,passportno,b_contactno,b_email):
    print("_______________SEARCH RECORDS_________________ ")
    t2=input("ENTER THE TICIT BOOKING TO BE SEARCH:-")
    for i in range (len(b_id)):
        if(t2==b_id):
           print ("\t",b_id[i], "\t",b_name[i],"\t",b_dob[i],"\t",passportno[i],"\t",b_contactno[i],"\t",b_email[i])

def deletedata(b_id,b_name,b_dob,passportno,b_contactno,b_email):
    dele=input("ENTER THE BOOKING ID FOR THE RECORD TO BE DELETED=>")
    for i in range (len(b_id)):
       if(b_id[i]==dele):
          b_id.remove(b_id[i])
          b_name.remove(b_name[i])
          b_dob.remove(b_dob[i])
          passportno.remove(passportno[i])
          b_contactno.remove(b_contactno[i])
          b_email.remove(b_email[i])
          break  

    with open('bookflight.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(b_id)):
            writer.writerow(("\t",b_id[i], "\t",b_name[i],"\t",b_dob[i],"\t",passportno[i],"\t",b_contactno[i],"\t",b_email[i]))
           

def updatedata(b_id,b_name=None,b_dob=None,passportno=None,b_contactno=None,b_email=None):
    print("CLICK ON 1-4 OPTION WHICH ARE TO BE UPDATED....")
    print("1.UPADTE BOOKING ID \n 2.UPDATE B_NMAE \n 3.UPDATE B_DOB \n 4.UPDATE PASSPORTNO \n 5.B_CONTACTNO \n 6.B_EMAIL")
    ch=int(input("ENTER YOUR CHOICE=>"))
    findr=input("ENTER THE BOOKING ID TO BE FOUND=>")
    for i in range (len(b_id)):
       if(b_id[i]==findr):
           if(ch==1):
               id=input("ENTER THE TIKET ID TO BE UPDATED=>")
               b_id[i]=id
           elif(ch==2):
               n=input("ENTER THE NAME TO BE UPDATED=>")
               b_name[i]=n
           elif(ch==3):
               d=input("ENTER THE DOB TO BE UPDATED=>")
               b_dob[i]=d
           elif(ch==4):
               pno=input("ENTER THE PASSPORT NO TO BE UPDATED=>")
               passportno[i]=pno
           elif(ch==5):
               cno=input("ENTER THE DUEDATE TO BE UPDATED=>")
               b_contactno[i]=cno
           elif(ch==6):
               e=input("ENTER THE EMAIL TO BE UPDATED=>")
               b_email[i]=e

    with open('bookflight.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(b_id)):
            writer.writerow(("\t", b_id[i],   "\t"  ,b_name[i],   "\t"  ,b_dob[i],   "\t"  ,passportno[i],   "\t"  ,b_contactno[i], "\t"  ,b_email[i]))