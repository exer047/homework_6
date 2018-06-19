# программа конвертер валют


coefficient = {"usd": 26.1, "eur": 30.2, "rub": 0.39, "gbp": 33.7, "uah": 1}

first_currency = input("Enter first currency: ").lower()
currency_value = int(input("Enter first currency amount: "))
second_currency = input("Enter second currency: ").lower()

result = currency_value * coefficient.get(first_currency) / coefficient.get(second_currency)

print(result)
