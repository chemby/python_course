raw_string = "київ,оДеса     Львів.житоМИР,уЖгОрОд.....ХарКІВ       , слАвУтИч"
heart_emoji = "\U00002764"

tidy_string = raw_string.replace(",", " ").replace(".", " ").title()
city_list = tidy_string.split()

for city in city_list:
    print(f"Я {heart_emoji} {city}")
