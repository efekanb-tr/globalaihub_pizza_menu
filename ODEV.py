import csv
import os

class Pizza:
    def __init__(self):
        self.cost = 10
        self.description = "Sade Pizza"
    
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
    
class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
        self.cost = 20

class Margarita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza"
        self.cost = 25

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk Pizza"
        self.cost = 18

PIZZA_CODES = {
    1: Klasik(),
    2: Margarita(),
    3: TurkPizza(),
    4: Pizza()
}

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ', ' + Pizza.get_description(self)
    

class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.cost = 3

class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar"
        self.cost = 4

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri"
        self.cost = 5

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
        self.cost = 6

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan"
        self.cost = 7

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır"
        self.cost = 8

def select_sauce(pizza):
    SAUCE_CODES = {
        11: Zeytin(pizza),
        12: Mantar(pizza),
        13: KeciPeyniri(pizza),
        14: Et(pizza),
        15: Sogan(pizza),
        16: Misir(pizza)
    }

    return SAUCE_CODES

def open_and_print_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)

def select_order():
    pizza_type = int(input("Lütfen pizza tipini seçiniz: "))
    sauce = int(input("Lütfen sosu seçiniz: "))

    return pizza_type, sauce

def get_customer_credentials():
    tckn = str(input("TC Kimlik numaranızı giriniz: "))
    cc = str(input("Kredi kartı numaranızı giriniz: "))
    cc_password = str(input("Kredi kartı şifrenizi giriniz: "))

    customer_creds = {
        'tckn': tckn,
        'cc': cc,
        'cc_password': cc_password
    }

    return customer_creds

def write_to_db(data_to_write):
    db_name = 'Orders_Database.csv'

    file_exists = os.path.isfile(db_name)

    with open(db_name, 'a', encoding='utf-8') as db:
        fieldnames = list(data_to_write.keys())

        writer = csv.DictWriter(db, fieldnames=fieldnames, lineterminator='\n')

        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data_to_write)

    print("Bilgileriniz kaydedilmiştir.")


def main():
    open_and_print_file('Menu.txt')
    pizza_type, sauce = select_order()

    selected_pizza = PIZZA_CODES[pizza_type]
    selected_pizza_with_sauce = select_sauce(selected_pizza)[sauce]

    total_cost = selected_pizza_with_sauce.get_cost()
    selected_description = selected_pizza_with_sauce.get_description()

    order_text = f"{total_cost} tutarındaki {selected_description} siparişinizi onaylamak için lütfen bilgilerinizi girin."
    print(order_text)

    customer_credentials = get_customer_credentials()

    write_to_db(customer_credentials)
    

    

if __name__ == '__main__':
    main()