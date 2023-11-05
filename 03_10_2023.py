raw_list = [123,"test", 123.123, 921, "23", 962] * 10

string_list = map(lambda item: str(item), raw_list)
print(list(string_list))



raw_list2 = [123,"test", 123.123, 921, "23.234", 962.12301, 12] * 10

int_list = filter(lambda item: type(item) == int, raw_list2)
print(list(int_list))
