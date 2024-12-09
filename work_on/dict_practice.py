user_input = str
#user_input = input('Введите числа через пробел: ').split()
user_dict ={}

while user_input != '0':
    user_input = input()
    user_dict[user_input] = int(user_input)

print (user_dict)
#for count_x in user_input:
#    user_dict[count_x[0:3:]]= count_x*2


print (user_dict)