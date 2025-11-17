import webshop as ws
from wallet import Wallet
all_wares = {
    "amd_processor": {
    "name": "AMD Ryzen 9 5900X Processor",
    "price": 5590.0,
    "number_in_stock": 50,
    "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
    "description": "All the cores and threads you'll need!",
    },
    "playstation_5": {
    "name": "PlayStation 5",
    "price": 5999.0,
    "number_in_stock": 0,
    "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
    "description": "Next generation console, never in stock!",
    },
    "hdmi_cable": {
    "name": "Belkin Ultra High Speed HDMI Cable - 2m",
    "price": 349.0,
    "number_in_stock": 3,
    "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
    "description": "A high speed overprices HDMI cable!",
    }
}

# Filtrer ut alle varer som er på lager og skriv ut informasjonen for hver av dem
all_wares_in_stock = ws.get_all_wares_in_stock(all_wares)
print('these items are in stock:\n')
for ware in all_wares_in_stock.values():
    ws.print_ware_information(ware)
# Skriv ut den gjennomsnittlige ratingen for varene
print(f"\nAverage rating for the AMD Processor: {ws.calculate_average_ware_rating(all_wares['amd_processor'])}\n")
print(f"\nAverage rating for the playstation 5: {ws.calculate_average_ware_rating(all_wares['playstation_5'])}\n")
print(f"\nAverage rating for the hdmi cable: {ws.calculate_average_ware_rating(all_wares['hdmi_cable'])}\n")

# sjekker om et spesifikt antall varer finnes i lager
for nested_key in all_wares.keys():
    print(f'{nested_key}\n')
if ws.is_number_of_ware_in_stock(all_wares[input('which ware do you want to check that we have in stock? copy the name of the ware from above\n')],int(input('\nhow many do you want to check that we should have?\n'))) == True:
    print('we have less than that in stock.\n')
else:
    print('we have more than that in stock.\n')

# Oppretter en tom handlevogn
shopping_cart = {}

# Forsøker å legge til varene
ws.add_number_of_ware_to_shopping_cart("amd_processor", all_wares["amd_processor"], shopping_cart, int(input('how many amd processors to add in cart?')))
ws.add_number_of_ware_to_shopping_cart ("playstation_5", all_wares["playstation_5"], shopping_cart, int(input('how many playstations to add in cart?')))
ws.add_number_of_ware_to_shopping_cart ("hdmi_cable", all_wares["hdmi_cable"], shopping_cart, int(input('how many hdmi cables to add in cart?')))

# skriver ut handlevognen
print(f"\nThe shopping cart:\n")
for ware,amount in shopping_cart.items():
    print(f"{ware}: {amount} pieces")

# regne ut pris med skatt og antall og printe ut
for nested_key,nested_value in ws.calculate_shopping_cart_price(shopping_cart,all_wares).items():
    print(f'\n{nested_key} : {nested_value}')

# Oppretter en lommebok som inneholder 10000 kr
#wallet = Wallet(10000)

# Forsøker å kjøpe varene i handlevognen
#ws.buy_shopping_cart()

# Skriver ut mengden penger i lommeboka etter kjøpet
#print(f"The amount in the wallet after the purchase: {wallet.get_amount()}")