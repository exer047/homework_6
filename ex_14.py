# Написать прогамму конвертер для 5 валют

UAH_USD = 26
UAH_EUR = 30
UAH_RUB = 0.422
UAH_GBP = 35


first_currency = input("Enter currency: ")
currency_value = int(input("Enter currency value: "))
second_currency = input("Enter result currency: ")

def const_checker_second():
    if second_currency.lower() == "usd":
        second_coefficiene = UAH_USD
    elif second_currency.lower() == "eur":
        second_coefficiene = UAH_EUR
    elif second_currency.lower() == "rub":
        second_coefficiene = UAH_RUB
    elif second_currency.lower() == "gbp":
        second_coefficiene = UAH_GBP
    return second_coefficiene

def const_checker_first():
    if first_currency.lower() == "usd":
        first_coefficiene = UAH_USD
    elif first_currency.lower() == "eur":
        first_coefficiene = UAH_EUR
    elif first_currency.lower() == "rub":
        first_coefficiene = UAH_RUB
    elif first_currency.lower() == "gbp":
        first_coefficiene = UAH_GBP
    return first_coefficiene


def any_to_any(value):
    first = value * const_checker_first()
    second = first / const_checker_second()
    result = second
    return result

def any_to_uah(value):
    result = value * const_checker_second()
    return result


def uah_to_any(value):
    result = value / const_checker_second()
    return result

print(uah_to_any(currency_value))