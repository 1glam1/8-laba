def symma(n2):
    n3 = int(n2)

    if (int(n3 / 100000) % 10) == 1:
        u = 'сто'
    elif (int(n3 / 100000) % 10) == 2:
        u = 'двести'
    elif (int(n3 / 100000) % 10) == 3:
        u = 'триста'
    elif (int(n3 / 100000) % 10) == 4:
        u = 'четыреста'
    elif (int(n3 / 100000) % 10) == 5:
        u = 'пятьсот'
    elif (int(n3 / 100000) % 10) == 6:
        u = 'шестьсот'
    elif (int(n3 / 100000) % 10) == 7:
        u = 'семьсот'
    elif (int(n3 / 100000) % 10) == 8:
        u = 'восемьсот'
    elif (int(n3 / 100000) % 10) == 9:
        u = 'девятьсот'
    elif (int(n3 / 100000) % 10) == 0:
        u = ''

    if int(n3 / 10000) % 10 == 1:
        if int(n3 / 1000) % 10 == 0:
            i = 'десять'
        elif int(n3 / 1000) % 10 == 1:
            i = 'одиннадцать'
        elif int(n3 / 1000) % 10 == 2:
            i = 'двенадцать'
        elif int(n3 / 1000) % 10 == 3:
            i = 'тринадцать'
        elif int(n3 / 1000) % 10 == 4:
            i = 'четырнадцать'
        elif int(n3 / 1000) % 10 == 5:
            i = 'пятнадцать'
        elif int(n3 / 1000) % 10 == 6:
            i = 'шестнадцать'
        elif int(n3 / 1000) % 10 == 7:
            i = 'семнадцать'
        elif int(n3 / 1000) % 10 == 8:
            i = 'восемнадцать'
        elif int(n3 / 1000) % 10 == 9:
            i = 'девятнадцать'

    elif int(n3 / 10000) % 10 == 2:
        i = 'двадцать'
    elif int(n3 / 10000) % 10 == 3:
        i = 'тридцать'
    elif int(n3 / 10000) % 10 == 4:
        i = 'сорок'
    elif int(n3 / 10000) % 10 == 5:
        i = 'пятьдесят'
    elif int(n3 / 10000) % 10 == 6:
        i = 'шестьдесят'
    elif int(n3 / 10000) % 10 == 7:
        i = 'семьдесят'
    elif int(n3 / 10000) % 10 == 8:
        i = 'восемьдесят'
    elif int(n3 / 10000) % 10 == 9:
        i = 'девяноста'
    elif int(n3 / 10000) % 10 == 0:
        i = ''

    if (int(n3 / 10000) % 10) != 1:
        if (int(n3 / 1000) % 10) == 1:
            r = 'одна тысяча'
        elif (int(n3 / 1000) % 10) == 2:
            r = 'две тысячи'
        elif (int(n3 / 1000) % 10) == 3:
            r = 'три тысячи'
        elif (int(n3 / 1000) % 10) == 4:
            r = 'четыре тысячи'
        elif (int(n3 / 1000) % 10) == 5:
            r = 'пять тысяч'
        elif (int(n3 / 1000) % 10) == 6:
            r = 'шесть тысяч'
        elif (int(n3 / 1000) % 10) == 7:
            r = 'семь тысяч'
        elif (int(n3 / 1000) % 10) == 8:
            r = 'восемь тысяч'
        elif (int(n3 / 1000) % 10) == 9:
            r = 'девять тысяч'
        elif (int(n3 / 1000) % 10) == 0:
            r = ''

    if (int(n3 / 100) % 10) == 1:
        h = 'сто'
    elif (int(n3 / 100) % 10) == 2:
        h = 'двести'
    elif (int(n3 / 100) % 10) == 3:
        h = 'триста'
    elif (int(n3 / 100) % 10) == 4:
        h = 'четыреста'
    elif (int(n3 / 100) % 10) == 5:
        h = 'пятьсот'
    elif (int(n3 / 100) % 10) == 6:
        h = 'шестьсот'
    elif (int(n3 / 100) % 10) == 7:
        h = 'семьсот'
    elif (int(n3 / 100) % 10) == 8:
        h = 'восемьсот'
    elif (int(n3 / 100) % 10) == 9:
        h = 'девятьсот'
    elif (int(n3 / 100) % 10) == 0:
        h = ''

    if int(n3 / 10) % 10 == 1:
        if (n3 % 10) == 0:
            m = 'десять'
        elif (n3 % 10) == 1:
            m = 'одиннадцать'
        elif (n3 % 10) == 2:
            m = 'двенадцать'
        elif (n3 % 10) == 3:
            m = 'тринадцать'
        elif (n3 % 10) == 4:
            m = 'четырнадцать'
        elif (n3 % 10) == 5:
            m = 'пятнадцать'
        elif (n3 % 10) == 6:
            m = 'шестнадцать'
        elif (n3 % 10) == 7:
            m = 'семнадцать'
        elif (n3 % 10) == 8:
            m = 'восемнадцать'
        elif (n3 % 10) == 9:
            m = 'девятнадцать'

    elif int(n3 / 10) % 10 == 2:
        m = 'двадцать'
    elif int(n3 / 10) % 10 == 3:
        m = 'тридцать'
    elif int(n3 / 10) % 10 == 4:
        m = 'сорок'
    elif int(n3 / 10) % 10 == 5:
        m = 'пятьдесят'
    elif int(n3 / 10) % 10 == 6:
        m = 'шестьдесят'
    elif int(n3 / 10) % 10 == 7:
        m = 'семьдесят'
    elif int(n3 / 10) % 10 == 8:
        m = 'восемьдесят'
    elif int(n3 / 10) % 10 == 9:
        m = 'девяноста'
    elif int(n3 / 10) % 10 == 0:
        m = ''

    if (int(n3 / 10) % 10) != 1:
        if (n3 % 10) == 1:
            l = 'один рубль'
        elif (n3 % 10) == 2:
            l = 'два рубля'
        elif (n3 % 10) == 3:
            l = 'три рубля'
        elif (n3 % 10) == 4:
            l = 'четыре рубля'
        elif (n3 % 10) == 5:
            l = 'пять рублей'
        elif (n3 % 10) == 6:
            l = 'шесть рублей'
        elif (n3 % 10) == 7:
            l = 'семь рублей'
        elif (n3 % 10) == 8:
            l = 'восемь рублей'
        elif (n3 % 10) == 9:
            l = 'девять рублей'
        elif (n3 % 10) == 0:
            l = ''

    w = ''
    if int(n3 // 10000) >= 1 == 0:
        w = 'тысяч'

    p = ''
    if int(n3 % 10) == 0:
        p = 'рублей'

    print(f'Сумма: {u} {i} {r} {w} {h} {m} {l} {p}')

def keys1(a, value):
    for k, v in a.items():
        if v == value:
            return k

def taxi(n):
    sort = {}
    c = 0
    km = {}
    for i in range(n):
        while True:
            try:
                n2 = int(input(f'Введите расстояние от работы до дома для {i+1} сотрудника: '))
                km[i+1] = n2
                break   
            except ValueError:
                print('Введено неверное значение!')
        c += 1

    c1 = 0
    car = {}
    for i in range(n):
        while True:
            try:
                n3 = int(input(f'Введите тариф в рублях для {i+1} машины: '))
                car[i+1] = n3
                break
            except ValueError:
                print('Введено неверное значение!')
        c1 += 1

    car1 = sorted(car.values(), reverse=True)                                          
    km1 = sorted(km.values())
    for i in range(n):
        a1 = car1[i]
        b1 = km1[i]

        a = keys1(car, a1)
        b = keys1(km, b1)

        sort[b] = a
        
        del car[a]
        del km[b]
    
    sort1 = sorted(sort.values())

    person = []
    for i in range(n):
        a2 = sort1[i]
        a3 = keys1(sort, a2)
        person.append(str(a3))

    summa = 0
    for i in range(n):                                       
        sum = car1[i] * km1[i]
        summa += sum

    print('Порядок рассадки сотрудников:',' '.join(person))
    print('Сумма:',summa,'руб.')
    symma(summa)
    
while True:
    try:
        n = int(input('Введите количество сотрудников: '))
        if 1 <= n <= 1000:
            break
        else:
            print('Введенно неверное значение!')
    except ValueError:
        print('Введено неверное значение!')
taxi(n)
