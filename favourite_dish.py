from pywebio.input import input as pw_input
from pywebio.input import TEXT
from pywebio.output import put_success

favourite_dish = pw_input("Яка твоя улюблена страва?", type=TEXT).lower()
put_success(f"О, я теж люблю {favourite_dish} \U0001F60A")
