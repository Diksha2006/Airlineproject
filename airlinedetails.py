import csv
a_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a_name=["Indigo Airlines","Kohinoor Airlines","Qatar Airlines","AirAsia India","Air India Airlines","Air India Express Airlines","Go First Airlines ","SpiceJet Airlines","Vistara Airlines","Jet Airways","Singapore Airlines","Vistara Airlines","Emirates Airlines","Akash Air","Delta Airlines","Air France","Turkish Airlines","WestJet Airlines","JetBlue Airlines","AirAsia airlines"]
a_type=["International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic","International","Domestic"]
a_location=["Russia","Punjab","New York","Delhi","Germany","Pune","China","Mumbai","Maldives","Chennai","Bali","Karnataka","Canada","Goa","Ireland","Sikkim","Brazil","Hariyana","Austria","Benglru"]
try:
    with open('airlinedetails.csv',mode='r',newline='') as file:
      reader=csv.reader(file)
      for row in reader:
          a_id.append(row[0])
          a_name.append(row[1])
          a_type.append(row[2])
          a_location.append(row[3])
except FileNotFoundError:
    print("file does not exit")
with open('airlinedetails.csv',mode='a',newline='') as file:
    writer=csv.writer(file)
    for i in range(len(a_id)):
        writer.writerow(("\t",a_id[i],"\t",a_name[i],"\t",a_type[i],"\t",a_location[i]))
        