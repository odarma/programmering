#oppgave 7 finner du nederst i siden

from datetime import date
car_register = {
    "toyotaBZ4X": {
    "brand": "Toyota",
    "model": "Corolla",
    "price": 96_000,
    "year": 2012,
    "month": 8,
    "new": False,
    "km": 163_000
    },
    "pugeot408": {
    "brand": "Pugeot",
    "model": "408",
    "price": 330_000,
    "year": 2019,
    "month": 1,
    "new": False,
    "km": 40_000
    },
    "audiRS3": {
    "brand": "Audi",
    "model": "RS3",
    "price": 473_000,
    "year": 2022,
    "month": 2,
    "new": True,
    "km": 0
    },
}
NEW_CAR_REGISTRATION_FEE = 10783
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000
def print_car_information(car):
    # Oppgave 3.1
    print(f'brand: {car['brand']}\nmodel: {car['model']}\nprice: {car['price']}kr\nmanufactured: {car['month']} - {car['year']}')
    if is_new(car) == True:
        print('condition: new')
    else:
        print('condition: used')
    return 

def create_car(car_register, brand, model, price, year, month, new, km):
    # Oppgave 3.2
    car_register[brand + model] = {'brand' : brand, 'model' : model, 'price' : price, 'year' : year, 'month' : month, 'new' : new, 'km' : km}
    return car_register

def get_car_age(car):
    # Oppgave 3.3
    for x,y in car.items():
        print(f'{y['brand']} {y['model']} is {2025 - y['year']} years old')
    return

def rent_car_monthly_price(car):
    # Oppgave 3.4
    monthly_price = (calculate_total_price(car)*RENT_CAR_PERCENTAGE)/12
    if is_new(car) == True:
        monthly_price+=RENT_NEW_CAR__FEE
    return round(monthly_price,2)

def next_eu_control(car):
    # Oppgave 3.5
    year = 0
    for x in range(car['year'],date.today().year+2,2):
        year = x
    return date(year,car['month'],1)

def calculate_total_price(car):
    # Oppgave 3.6
    total_price = car['price']
    age=date.today().year-car['year']
    if is_new(car) == True:
        total_price+=NEW_CAR_REGISTRATION_FEE
    else:
        if 0<=age<=3:
            total_price+=6681
        elif 4<=age<=11:
            total_price+=4034
        elif 12<=age<=29:
            total_price+=1729
    return total_price

def is_new(car):
    return car['new']

if __name__ == '__main__':
    print(f'{create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)}\n')
    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)
    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.\n")
    audi = car_register['audiRS3']
    print_car_information(audi)
    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.\n")
    get_car_age(car_register)


class info_about_car:
    def __init__(self,brand, model, price, year, month, new, km):
        pass

    def print_in_clear_format(self):
        pass # denne metoden passer i klassen fordi da kan infoen vises med god oversikt

    