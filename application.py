import csv
a_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a_name=["Indigo Airlines","Kohinoor Airlines","Qatar Airlines","AirAsia India","Air India Airlines","Air India Express Airlines","Go First Airlines ","SpiceJet Airlines","Vistara Airlines","Jet Airways","Singapore Airlines","Vistara Airlines","Emirates Airlines","Akash Air","Delta Airlines","Air France","Turkish Airlines","WestJet Airlines","JetBlue Airlines","AirAsia airlines"]
a_type=["International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic"]
a_location=["Russia","Punjab","New York","Delhi","Germany","Pune","China","Mumbai","Maldives","Chennai","Bali","Karnataka","Canada","Goa","Ireland","Sikkim","Brazil","Hariyana","Austria","Benglru"]
tempData = []
for i in range(len(a_id)):
    tempData.append({"a_id":a_id[i],"a_name":a_name[i],"a_type":a_type[i],"a_location":a_location[i]})

def write_csv(data):
    with open('airlinedetials.csv',mode='w',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=["a_id","a_name","a_type","a_location"])
        writer.writeheader()
        writer.writerows(data)

def read_csv():
    with open("flight.csv",mode="r",newline="") as file:
        red=csv.DictReader(file,fieldnames=["b_id","b_name","b_dob","passportno","b_contactno","b_email"])
        return list(red)
def view():
    data = read_csv()
    for i in range(len(data)):
        print("Data ",data[i])