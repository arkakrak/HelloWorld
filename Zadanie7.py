# proszę na dowolnej funkcji przetestować parametry pozycyjne, z nazwami, *args i **kwargs.
# Sprawdzić w jakiej kolejności mogą być ustawiane.
# Czy można bez błędu wywołać poniższą funkcję bez wprowadzania w niej zmian.


def person_print(name, last_name, *others, age):
    formatted_data = "Imię: {}, nazwisko: {}, wiek: {}".format(name, last_name, age)
    others_str = " "
    for arg in others:
        others_str += arg + " "
    print(formatted_data + others_str)


person_print("Jan", "Kowalski", "something", 30)
