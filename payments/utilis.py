import uuid

def generate_reference():
        return str(uuid.uuid4()).replace('-', '')[:12]

def calculate_fee(amount):
    if amount < 100:
        return 2
    elif amount < 1000:
        return amount * 0.015
    return amount * 0.01


def convert_currency(amount, from_currency, to_currency):
     rates = {
          'KES': 1,
          'USD': 130,
          'EUR':140,
     }

     return (amount/ rates[from_currency])*rates[to_currency]

def validate_mobile_money(number):
     return number.startswith('07') and len(number) == 10
