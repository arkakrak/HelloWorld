# proszę na dowolnej funkcji przetestować parametry pozycyjne, z nazwami, *args i **kwargs.
# Sprawdzić w jakiej kolejności mogą być ustawiane.
# Czy można bez błędu wywołać poniższą funkcję bez wprowadzania w niej zmian.


def person_print(name, last_name, *others, age):
    formatted_data = "Imię: {}, nazwisko: {}, wiek: {}".format(name, last_name, age)
    others_str = " "
    for arg in others:
        others_str += arg + " "
    print(formatted_data + others_str)


# Syntax Error: positional argument follows keyword argument
# person_print("Jan", "Kowalski", gender="helicopter", 30)

# This works:
person_print("Jan", "Kowalski", "helicopter", age=30)


def my_first_function(*nothing_important, width, length, height):
    print("nothing_important: {}".format(nothing_important))
    print("width: {}".format(width))
    print("length: {}".format(length))
    print("height: {}".format(height))


my_first_function("helicopter", width=80, length=20, height=180)


def my_second_function(width, length, *nothing_important):
    print("width: {}".format(width))
    print("length: {}".format(length))
    print("nothing_important: {}".format(nothing_important))


my_second_function(80, 30, "battle helicopter")
# def my_third_function(something, **kwargs):

# def my_fourth_function(**kwargs, something):