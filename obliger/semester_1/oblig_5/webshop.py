def print_ware_information(ware):
    #Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.
    print(f'name: {ware['name']}\nprice: {ware['price']}kr\nnumber in stock: {ware['number_in_stock']}\nratings: {ware['ratings']}\ndescription: {ware['description']}\n')
    return 
    
def calculate_average_ware_rating(ware):
    #Returnerer den gjennomsnittlige ratingen for en spesifisert vare.
    total_rating =0
    average_rating =0
    try: #sjekker om varen har ratings og regner ut
        for rating in ware["ratings"]:
                total_rating+=rating
        average_rating+=round(total_rating/len(ware["ratings"]),2)
    except ZeroDivisionError:
        return f'{ware['name']} has no ratings.'
    return average_rating

def get_all_wares_in_stock(all_wares):
    #Returnerer en dictionary med alle varer som er på lager.
    ware_in_stock = {}
    for nested_keys,nested_value in all_wares.items():
        if is_ware_in_stock(nested_value) == False:
            ware_in_stock[nested_keys] = nested_value
    return ware_in_stock #returnerer dictionary

def is_number_of_ware_in_stock(ware,amount):#dictionaryen printes ut
    #Returnerer en Boolean-verdi som representerer om et spesifisert antall av en gitt vare finnes på lager.
    if is_ware_in_stock(ware,amount) == True:
        return True


def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart,number_of_ware):
    #Legger til et spesifisert antall av en gitt vare i en spesifisert handlevogn.
    if ware["number_in_stock"]==0:
        shopping_cart[ware_key] = 1
    
    elif number_of_ware<=ware["number_in_stock"]:
        shopping_cart[ware_key] = number_of_ware
        
    else:
        shopping_cart[ware_key] = ware["number_in_stock"]
       
    return shopping_cart

def calculate_shopping_cart_price(shopping_cart, wares, tax=1.25):
    #Returnerer prisen av en handlevogn basert på varene i den.
    updated_shopping_cart = {} 
    for key,(nested_key,nested_value) in zip(shopping_cart, wares.items()): #bruke zip til å iterere gjennom dictionary-ene samtidig
        if key == nested_key:
            updated_shopping_cart[key] = {'amount' : shopping_cart[key],'price' : nested_value['price']*shopping_cart[key]*tax}
    return updated_shopping_cart

#def can_afford_shopping_cart(shopping_cart_price, wallet):
#    #Returnerer en Boolean-verdi basert på om det er nok penger i en gitt lommebok for å kjøpe en handlevogn.
#    return
#
#def buy_shopping_cart():
#    #Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.#
#    return

#------------------------------------------
# Predefinerte funksjoner
#------------------------------------------
def is_ware_in_stock(ware, number=1):
    #Returnerer en Boolean-verdi som representerer om en vare er på lager.#
    if ware["number_in_stock"] <= number:
        return True
    else:
        return False
def clear_shopping_cart(shopping_cart):
    #Tømmer en handlevogn.#
    shopping_cart.clear()