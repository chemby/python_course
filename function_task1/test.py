from main import add_string_letters_to_array

def test_add_letters_to_array():
    string = "hello"
    expected_result = ['h','e','l','l','o']
    actual_result = add_string_letters_to_array(string)
    assert expected_result == actual_result

def test_exclude_non_alpha_and_m_n_letters():
    string = "?./mqNet!342"
    expected_result = ['q', 'e', 't']
    actual_result = add_string_letters_to_array(string)
    assert expected_result == actual_result

def test_exceed_100_items():
    string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    expected_result = 100
    actual_result = len(add_string_letters_to_array(string))
    assert expected_result == actual_result
