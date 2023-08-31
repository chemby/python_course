from main import vehicle_task


def test_int():
    speed = 10
    weight = 235
    seconds = 342
    expected_result = "Транспортний засіб вагою 235 кг рухався 342 секунд зі швидкістю 10м/сек, і подолав відстань 3420 метрів"
    actual_result = vehicle_task(speed=speed,weight=weight,seconds=seconds)
    assert expected_result == actual_result


def test_float():
    speed = 10.324
    weight = 235.86
    seconds = 342.01
    expected_result = "Транспортний засіб вагою 235.86 кг рухався 342.01 секунд зі швидкістю 10.324м/сек, і подолав відстань 3530.91124 метрів"
    actual_result = vehicle_task(speed=speed, weight=weight, seconds=seconds)
    assert expected_result == actual_result
