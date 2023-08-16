from pywebio.input import input as pw_input
from pywebio.input import TEXT
from pywebio.output import put_success, put_error

cat_emoji = "\U0001F408"
dog_emoji = "\U0001F415"
hamster_emoji = "\U0001F439"
fish_emoji = "\U0001F41F"
turtle_emoji = "\U0001F422"

can_animal_swim = False

favourite_animal = pw_input("Назва улюбленої тварини", type=TEXT, required=True).strip(" ;.,<>/?!@#$%^&*()'|:1234567890_-=+").lower()
pet_name = pw_input("Кличка улюбленця", type=TEXT, required=True).strip(" ;.,<>/?!@#$%^&*()'|:1234567890_-=+").title()

if favourite_animal == "риба" or favourite_animal == "черепаха":
    can_animal_swim = True

if can_animal_swim is True:
    put_success("Треба купити акваріум")

print(favourite_animal)

if favourite_animal == "собака":
    put_success(f"Боюсь гавкоту собак, в тому числі й {pet_name} {dog_emoji}")
elif favourite_animal == "кіт":
    put_success(f"Коти ловлять мишей {cat_emoji}")
elif favourite_animal == "хомяк":
    put_success(f"Хомяки маленькі {hamster_emoji}")
elif favourite_animal == "риба":
    put_success(f"Рибку не смажити {fish_emoji}")
elif favourite_animal == "черепаха":
    put_success(f"В неї міцний панцир {turtle_emoji}")
else:
    put_error("Не знаю такий тип тварини")
