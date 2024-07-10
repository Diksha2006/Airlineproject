import csv
b_id=[]
b_name=[]
b_dob=[]
passportno=[]
b_contactno=[]
b_email=[]
def flighttype():
    print("\n1. DOMESTIC FLIGHT \n 2. INTERNATIONAL FLIGHT")
    ch=int(input("ENTER YOUR CHOICE=>"))
    if(ch==1):
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
        elif(s=="goa" and d=="pune"):
            print("AIRLINE NAME=INDIGO \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=6000")
            print("\n")
            print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=3000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=5000")
            print("\n") 
        elif(s=="mumbai" and d=="hariyana"):
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=6000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=4000") 
            print("\n")   
        elif(s=="hariyana" and d=="mumbai"): 
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
        elif(s=="gujrat" and d=="panjab"):
            print("AIRLINE NAME=ROYAL AIR MACRO \n FLIGHT TIME=2:20PM TO 2:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 10:30AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=SOUTHWEST AIRLINE\n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 1:00PM TO 1:30PM \n 11:30AM TO 12:10PM \n PRICE=4000")
            print("\n")
            print("AIRLINE NAME=LATAM BRASIL \n FLIGHT TIME=1:20PM TO 1:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=ALASKA AIRLINE\n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=7000")
            print("\n")
        elif(s=="panjab" and d=="gujrat"):
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=6000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=3000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=5000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=4000")
            print("\n")
        else:
            print("NO FLIGHTS ARE AVAILABLE FROM THE ENTERED SOURCE TO DESTINATION..\n WE WISH YOU HAD THE GOOD TIME AHEAD..")
    
    else:
        s=input("ENTER YOUR SOURCE=>")
        d=input("ENTER YOUR DESTINATION=>")
        if(s=="mumbai" and d=="bali"):
            print("AIRLINE NAME=INDIGO \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=25000")
            print("\n")
            print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=60000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=30000")
            print("\n")
            print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=35000")
        elif(s=="bali" and d=="mumbai"):
            print("AIRLINE NAME=INDIGO \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=40000")
            print("\n")
            print("AIRLINE NAME=KOHINUR \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=50000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=55000")
            print("\n")
            print("AIRLINE NAME=QATER \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=45000")
            print("\n") 
        elif(s=="goa" and d=="maldives"):
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=2:20PM TO 2:50PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 7:00AM TO 7:30AM \n 9:10AM TO 10:00PM \n PRICE=45000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS \n FLIGHT TIME=3:20PM TO 3:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 12:00PM TO 12:50PM \n 2:30AM TO 3:10PM \n PRICE=35000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=4:20PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00PM TO 8:50PM \n 10:00AM TO 10:30AM \n 12:10AM TO 1:00PM \n PRICE=30000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 8:00AM TO 8:00AM \n 10:10AM TO 10:50PM \n PRICE=60000") 
            print("\n")   
        elif(s=="maldives" and d=="goa"): 
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=30000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=35000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=40000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=55000")
            print("\n")
        elif(s=="surat" and d=="russia"):
            print("AIRLINE NAME=ROYAL AIR MACRO \n FLIGHT TIME=2:20PM TO 2:50PM \n 5:00PM TO 5:50PM \n 7:00PM TO 7:50PM \n 10:30AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=30000")
            print("\n")
            print("AIRLINE NAME=SOUTHWEST AIRLINE\n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 1:00PM TO 1:30PM \n 11:30AM TO 12:10PM \n PRICE=20000")
            print("\n")
            print("AIRLINE NAME=LATAM BRASIL \n FLIGHT TIME=1:20PM TO 1:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=65000")
            print("\n")
            print("AIRLINE NAME=ALASKA AIRLINE\n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=70000")
            print("\n")
        elif(s=="russia" and d=="surat"):
            print("AIRLINE NAME=AIRASIA INDIA \n FLIGHT TIME=1:20PM TO 1:50PM \n 2:00PM TO 2:50PM \n 3:00PM TO 3:50PM \n 10:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=25000")
            print("\n")
            print("AIRLINE NAME=AIRINDIA EXPRESS\n FLIGHT TIME=2:20PM TO 2:50PM \n 3:00PM TO 3:50PM \n 5:00PM TO 5:50PM \n 11:00PM TO 12:00PM \n 1:30AM TO 2:10PM \n PRICE=60000")
            print("\n")
            print("AIRLINE NAME=WEST JET \n FLIGHT TIME=3:20PM TO 3:50PM \n 4:00PM TO 4:50PM \n 6:00PM TO 6:50PM \n 9:00AM TO 9:30AM \n 11:10AM TO 12:00PM \n PRICE=74000")
            print("\n")
            print("AIRLINE NAME=JETBLUE \n FLIGHT TIME=2:30PM TO 3:10PM \n 4:00PM TO 4:50PM \n 5:00PM TO 5:50PM \n 12:00AM TO 11:00AM \n 12:10AM TO 1:00PM \n PRICE=40000")
            print("\n")
        else:
            print("NO FLIGHTS ARE AVAILABLE FROM THE ENTERED SOURCE TO DESTINATION..\n WE WISH YOU HAD THE GOOD TIME AHEAD..")
    

def booking():
    cnt=101
    def book():    
        n=input("ENTER THE NAME=")
        b_name.append(n)
        d=input("ENTER THE BIRTH_OF_DATE=")
        b_dob.append(d)
        p=int(input("ENTER THE PASSPORT_NUMBER="))
        passportno.append(p)
        c=int(input("ENTER THE BOOKING CONTACT_NUMBER="))
        b_contactno.append(c)
        e=input("ENTER THE EMAIL_ID=")
        b_email.append(e) 
        print("BOOKING ID=>",cnt)
        b_id.append(cnt)
    c=cnt+1
    with open ('bookflight.csv',mode='w',newline='') as file:
        writer=csv.writer(file)
        for i in range (len(b_id)):
            writer.writerow(("\t",b_id[i], "\t",b_name[i],"\t",b_dob[i],"\t",passportno[i],"\t",b_contactno[i],"\t",b_email[i]))
def view():
    for i in range(len(b_id)):
        print("\t",b_id[i], "\t",b_name[i],"\t",b_dob[i],"\t",passportno[i],"\t",b_contactno[i],"\t",b_email[i])
flighttype()
booking()
view()



