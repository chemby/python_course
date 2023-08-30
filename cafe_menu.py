from decimal import Decimal
from pywebio.input import input, FLOAT
from pywebio.output import put_success, put_warning

money_per_kkal = 0.32541

OSTRICH_EGG = 118
RABBIT = 197
SEA_BASS = 123
SWEET_RED_PEPPER = 26
PARSLEY = 45
BANANAS = 87
WAFFLES = 425
BREAD = 246
PISTACHIOS = 555
KEFIR = 51

energy = 0

portion_ostrich_egg = input(f"Страусине Яйце, обсяг {OSTRICH_EGG} кКал/100гр", type=FLOAT)
portion_ostrich_egg_energy = (float(portion_ostrich_egg) * OSTRICH_EGG) / 100
energy = energy + portion_ostrich_egg_energy
put_success(f'Замовлено {portion_ostrich_egg} грам\n'
            f'Калорійність порції {portion_ostrich_egg_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_rabbit = input(f"Кролик, обсяг {RABBIT} кКал/100гр", type=FLOAT)
portion_rabbit_energy = (float(portion_rabbit) * RABBIT) / 100
energy = energy + portion_rabbit_energy
put_success(f'Замовлено {portion_rabbit} грам\n'
            f'Калорійність порції {portion_rabbit_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_sea_bass = input(f"Окунь морський, обсяг {SEA_BASS} кКал/100гр", type=FLOAT)
portion_sea_bass_energy = (float(portion_sea_bass) * SEA_BASS) / 100
energy = energy + portion_sea_bass_energy
put_success(f'Замовлено {portion_sea_bass} грам\n'
            f'Калорійність порції {portion_sea_bass_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_red_pepper = input(f"Перець червоний солодкий, обсяг {SWEET_RED_PEPPER} кКал/100гр", type=FLOAT)
portion_red_pepper_energy = (float(portion_red_pepper) * SWEET_RED_PEPPER) / 100
energy = energy + portion_red_pepper_energy
put_success(f'Замовлено {portion_red_pepper} грам\n'
            f'Калорійність порції {portion_red_pepper_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_parsley = input(f"Петрушка (зелень), обсяг {PARSLEY} кКал/100гр", type=FLOAT)
portion_parsley_energy = (float(portion_parsley) * PARSLEY) / 100
energy = energy + portion_parsley_energy
put_success(f'Замовлено {portion_parsley} грам\n'
            f'Калорійність порції {portion_parsley_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_bananas = input(f"Банани, обсяг {BANANAS} кКал/100гр", type=FLOAT)
portion_bananas_energy = (float(portion_bananas) * BANANAS) / 100
energy = energy + portion_bananas_energy
put_success(f'Замовлено {portion_bananas} грам\n'
            f'Калорійність порції {portion_bananas_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_waffles = input(f"Вафлі, обсяг {WAFFLES} кКал/100гр", type=FLOAT)
portion_waffles_energy = (float(portion_waffles) * WAFFLES) / 100
energy = energy + portion_waffles_energy
put_success(f'Замовлено {portion_waffles} грам\n'
            f'Калорійність порції {portion_waffles_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_bread = input(f"Хліб пшеничний з борошна I сорту, обсяг {BREAD} кКал/100гр", type=FLOAT)
portion_bread_energy = (float(portion_bread) * BREAD) / 100
energy = energy + portion_bread_energy
put_success(f'Замовлено {portion_bread} грам\n'
            f'Калорійність порції {portion_bread_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_pistachios = input(f"Фісташки, обсяг {PISTACHIOS} кКал/100гр", type=FLOAT)
portion_pistachios_energy = (float(portion_pistachios) * PISTACHIOS) / 100
energy = energy + portion_pistachios_energy
put_success(f'Замовлено {portion_pistachios} грам\n'
            f'Калорійність порції {portion_pistachios_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

portion_kefir = input(f"Кефір 2,5%, обсяг {KEFIR} кКал/100гр", type=FLOAT)
portion_kefir_energy = (float(portion_kefir) * KEFIR) / 100
energy = energy + portion_kefir_energy
put_success(f'Замовлено {portion_kefir} грам\n'
            f'Калорійність порції {portion_kefir_energy} кКал\n'
            f'Загальна калорійність {energy} кКал')

if energy < 1000:
    put_warning("Ви, мабуть залишитеся голодним")
elif energy < 1500:
    put_warning("Це саме ваш варіант вечері")
else:
    put_warning("Ви стільки не зїсте")

cost = Decimal(money_per_kkal * energy).quantize(Decimal('0.01'))
put_success(f'Загальна вартість замовлення - {cost} грн')
