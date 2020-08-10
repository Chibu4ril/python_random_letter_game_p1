import random

aphabet = 'abcdefghijklmnopqrstuvwxyz'

list_alpha = list(aphabet)
list_int = len(list_alpha)

random_num = random.randrange(list_int)

alpha_index = aphabet[random_num]

new = []
i = len(new) 
while i < 4:
    print(new.extend(alpha_index))
    if i == 3:
        break
    i += 1