def base_converter(decimal_number, new_base):
    if decimal_number <= 0:
        return ''
    else:
        return base_converter(decimal_number // new_base, new_base) + str(decimal_number % new_base)

num = int(input('Enter decimal number: '))
base = int(input('Enter base to be converted to: '))

new = base_converter(num, base)
print(new)
