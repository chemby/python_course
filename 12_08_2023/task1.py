past_cities = input('Міста, в яких ти був за минулі 10 років').strip(" ;.,<>/?!@#$%^&*()'|:1234567890_-=+").replace(",", " ").replace(".", " ").title()
future_cities = input('Міста, куди ти хочеш поїхати в наступні 10 років').strip(" ;.,<>/?!@#$%^&*()'|:1234567890_-=+").replace(",", " ").replace(".", " ").title()

past_cities_set = set(past_cities.split())
future_cities_set = set(future_cities.split())

similar = past_cities_set & future_cities_set
similar_cities_string = ', '.join(similar)
if similar_cities_string == '':
    print("Ти відкритий до чогось нового")
else:
    print(f'Тобі, мабуть, дуже сподобалося в містах, які ти повторив в двох циклах вводу, а саме: {similar_cities_string}')
