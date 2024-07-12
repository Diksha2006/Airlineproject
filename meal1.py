import csv
print("\n 1.FOOD MEAL \n 2.SOFT DRUNKS \n 3.DESSERT \n 4.SNACKS \n 5.SALAD")
ch=int(input("ENTER YOUR CHOICE =>"))
if(ch==1):
    print("\n 1.VEGETERAIN \n 2.NON-VEGETERAIN")
    c=int(input("ENTER YOUR CHOICE"))
    if(c==1):
        print("\n 1.VEG ROLL \n 2.PIZZA \n 3.BURGER \n 4.FRENCH FRIES \n 5.PULAV \n 6.PASTA \n 7.DOSA \n 8.TAKOOS \n 9.SITES \n 10.GALIC BREAD")
    else:
        print("\n CHIKAN BURGER \n 2.CHIKAN PIZZA \n 3.CHIKAN BIRYANI \n 4.BUTTER CHIKAN \n 5.NON-VEG ROLL \n 6.CHIKAN HANDI \n 7.CHIKAN TANDURI \n 9.CHIKAN LEGPEICE \n 10.FISHES")
if(ch==2):
    print("\n 1.MAZA \n 2.SLICE \n 3.THUMBSUP \n 4.MILKSHEKE \n 5.MASTANI \n 6.COFFEE \n 7.TEA \n 8.CAPACINO \n 9.CARAMELLE \n 10.LASSI")
if(ch==3):
    print("\n 1.BROAUNI \n 2.DONUT \n 3.ICE-CREAM \n 4.GULABJAMUN \n 5.RASGULLA \n 6.RASMALAI ")
if(ch==4):
    print("\n 1.CHIPS \n 2.POPCORN \n 3.CANDIES \n 4.CRACKERS \n 5.CHEESE \n 6.CHOCOLATE \n 7.MIXED NUTS")
if(ch==5):
    print("\n 1.VEGETABLE SALAD \n 2.MEAT SALAD \n 3.FISH SALAD \n 4.GREEN SALAD \n 5.MIXED SALAD \n 6.FRUIT SALAD \n 7.MACARONI SALAD \n 8.LEAFY GREEN SALAD ")

def main_meal():
    with open ("meal_main.csv",mode='r',newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)
a=main_meal()
print(a)
def sub_meal():
    with open ("meal_sub.csv",mode='r',newline='')as file:
        reader = csv.DictReader(file)
        return list(reader)
b=sub_meal()
print(b)

