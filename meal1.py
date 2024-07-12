import csv
def main_meal():
    with open ("meal_main.csv",mode='r',newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def sub_meal():
    with open ("meal_sub.csv",mode='r',newline='')as file:
        reader = csv.DictReader(file)
        return list(reader)
mainMeal = main_meal()
subMeal=sub_meal()
def meals():
    print(mainMeal)
    for i in range(len(mainMeal)):
        print(i+1,mainMeal[i]["meal_name"])
    ch=(input("ENTER YOUR CHOICE =>"))
    for i in range(len(subMeal)):
        if(ch==subMeal[i]["meal_id"]):
            print(i+1,subMeal[i]["meal_name"])
   



