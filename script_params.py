# Задание 1
from sys import argv

path, ar1, ar2, ar3 = argv
ar1, ar2, ar3 = map(int, argv[1:])
zarplata = ar1 * ar2 + ar3
print(zarplata)