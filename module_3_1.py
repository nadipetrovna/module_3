#count_calls - счетчик вызова функций
#string_info - информация о строке
#is_contains - проверка наличия строки в списке
calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info (a):
    count_calls()
    len_a = len(a)
    str_a_caps = a.upper()
    str_a_lower = a.lower()
    string_a = len_a, str_a_caps, str_a_lower
    return string_a
def is_contains(a, b):
    count_calls()
    if a.lower() in str(b).lower():
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
