import re

bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''

pattern_1 = re.compile('Niebieski')
result_1 = pattern_1.search(bridge_of_death)
print(result_1)
print(result_1.start())
print(result_1.span())
print(result_1.group())


