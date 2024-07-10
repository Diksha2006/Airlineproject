import csv
def read_csv():
    with open("airlinedetails.csv",mode="r",newline="") as file:
        
        red = csv.DictReader(file)
        return list(red)
print(read_csv())