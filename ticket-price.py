price_list = [0, 990, 1390]
discount_rate = 10

def get_price(age):
    if age < 18:
        return price_list[0]
    elif 18 <= age < 25:
        return price_list[1]
    elif age >= 25:
        return price_list[2]


tickets_number = int(input('Введите количество билетов: '))
total_price = 0
for i in range(tickets_number):
    age = int(input(f'Введите возраст {i + 1}-го посетителя: '))
    current = get_price(age)
    print(f'Цена билета: {current}')
    total_price += current

print(f'\nОбщая стоимость: {total_price}')

if tickets_number > 3:
    discount = total_price * discount_rate / 100
    print(f'Стоимость с учетом скидки {discount_rate}%: {int(total_price - discount)}')


