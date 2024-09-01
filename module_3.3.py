def print_params (a=1, b='string',c=True):
    print(a, b, c)
# Параметры по умолчинию
print_params() #1,string,true
print_params(b = 25) #1,25, true
print_params(c=[1, 2, 3]) #1,string,[1,2,3]

#Распаковка
values_list = [2.3, [1, 2, 5], False]
values_dict = {'a': 2, 'b': 5.7, 'c': '4,56'}
print_params(*values_list)
print_params(**values_dict)

#Частичная распаковка
values_list_2 = [2.3, 'Not string']
print_params(*values_list_2, 45) # в подсказке а = 45, по на деле после распаковке с = 45