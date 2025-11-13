def print_ware_information(ware):
    #Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.
    #print(f'{ware[0]}: {ware[1]}')
    #print(f'{ware}')
    return 
    
def calculate_average_ware_rating(ware):
    #Returnerer den gjennomsnittlige ratingen for en spesifisert vare.
    total_rating =0
    average_rating =0
    for rating in ware["ratings"]:
            total_rating+=rating
    average_rating+=total_rating/len(ware["ratings"])
    return average_rating

def get_all_wares_in_stock(all_wares):
    #Returnerer en dictionary med alle varer som er på lager.
    for nested_keys,nested_value in all_wares.items():
        if is_ware_in_stock(nested_value) == True:
            print(nested_value.items())
            #return nested_value #returnerer en dictionary

def is_number_of_ware_in_stock(ware, number_of_ware):
    #Returnerer en Boolean-verdi som representerer om et spesifisert antall av en gitt vare finnes på lager.
    return


def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart,number_of_ware):
    #Legger til et spesifisert antall av en gitt vare i en spesifisert handlevogn.
    return

def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
    #Returnerer prisen av en handlevogn basert på varene i den.
    return

def can_afford_shopping_cart(shopping_cart_price, wallet):
    #Returnerer en Boolean-verdi basert på om det er nok penger i en gitt lommebok for å kjøpe en handlevogn.
    return

def buy_shopping_cart():
    #Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.#
    return

#------------------------------------------
# Predefinerte funksjoner
#------------------------------------------
def is_ware_in_stock(ware):
    #Returnerer en Boolean-verdi som representerer om en vare er på lager.#
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False
def clear_shopping_cart(shopping_cart):
    #Tømmer en handlevogn.#
    shopping_cart.clear()