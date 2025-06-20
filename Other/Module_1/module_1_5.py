immutable_var = 'Земля', 'Марс', 2024, 3.4
print('Immutable tuple:', immutable_var)
# immutable_var[0]="Луна" # в этом месте интерпретатор выдаст ошибку из-за того, что кортеж - это неизменяемая
# # упорядоченная коллекция
# print(immutable_var)
mutable_list = ['Земля', 'Марс', 2024, 3.4]
print('Mutable list:', mutable_list)
mutable_list[0]="Луна"
print('New mutable list:', mutable_list)

