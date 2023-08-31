def vehicle_task(seconds: int | float, speed: int | float, weight: int | float ) -> str:
    if seconds < 0 or speed < 0 or weight < 0:
        raise ValueError("Values can't be lower than 0")

    meters_passed = seconds * speed
    return f"Транспортний засіб вагою {weight} кг рухався {seconds} секунд зі швидкістю {speed}м/сек, і подолав відстань {meters_passed} метрів"

print(vehicle_task(seconds=342,weight=235,speed=10))
