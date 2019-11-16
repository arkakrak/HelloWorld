"""Proszę
sprawdzić
czas
potrzebny
na
przeszukanie
poniższej
listy
pod
kątem - 1.
Proszę
zastosować
wszystkie
sposoby
przeszukania, które
przyjdą
do
głowy.

list comprehention na wykładzie
"""

from random import randint

long_list = [randint(0, 3000) for element in range(1000000)]