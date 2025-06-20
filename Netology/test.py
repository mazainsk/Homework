from statistics import mean

my_dict = {'k1': [1], 'k2': [1, 2]}
avr_dict = dict((k, mean(my_dict[k])) for k in my_dict.keys())
print(avr_dict)
my_dict.setdefault('k3', []).append(3)
avr_dict.update(k3=mean(my_dict['k3']))
print(my_dict)
print(avr_dict)
