def verify_age(age: int) -> str:
    if age <= 0:
        return "Передано не валідне значення віку"
    elif age <= 18:
        return "Ти дитина"
    elif age <= 65:
        return "Потрібно працювати"
    elif age > 65:
        return "Щасливої пенсії!"


def test_verify_age1():
    age = -14
    expected_result = "Передано не валідне значення віку"
    actual_result = verify_age(age)
    assert expected_result == actual_result

def test_verify_age2():
    age = 9
    expected_result = "Ти дитина"
    actual_result = verify_age(age)
    assert expected_result == actual_result

def test_verify_age3():
    age = 35
    expected_result = "Потрібно працювати"
    actual_result = verify_age(age)
    assert expected_result == actual_result

def test_verify_age4():
    age = 87
    expected_result = "Щасливої пенсії!"
    actual_result = verify_age(age)
    assert expected_result == actual_result
  
