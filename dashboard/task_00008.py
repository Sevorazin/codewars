'''
Первое столетие охватывает от 1 года до 100 года включительно , второе столетие — от 101 года до 200 года включительно и т. д.
Учитывая год, верните столетие, в котором он находится.
'''

def century(year):
    a = year // 100
    b = year % 100
    if b > 0:
        return f'{year} --> {a+1}'
    else:
        return f'{year} --> {a}'

print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))