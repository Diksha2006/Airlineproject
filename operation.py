import csv
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
           