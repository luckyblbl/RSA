import random

def prostoe(a,b):                          #Функция для нахождения простого числа
    flag = 0
    while flag != 1:
        p = random.randrange(a+1, b, 2)
        for i in range(2, p):
            if p % i == 0:
                flag = 0
                break
            else:
                flag = 1
    return p



def exp(Fn):                      #  Находим экспоненту которая удовлетворяет условиям (Должна быть взаимно простая)

    flag = 0
    while flag != 1:
        z = prostoe(0, 20)
        if Fn % z != 0:
            flag = 1
        else:
            flag = 0
    return z


def secret(n,e,Fn):                         #Находит секретный ключ для расшифровки
    i = 2
    while i < n:
        if (i * e) % Fn == 1:
            d = i
            break
        i += 1
    return d


def Alice():
    p = prostoe(100, 1000)              #   Рандомим два простых числа
    q = prostoe(100, 1000)              #
    Fn = (p - 1) * (q - 1)              #   Находим функцию Эйлера
    n = p * q                           # Находим публичную переменную
    e = exp(Fn)                         # Находим публичное число е
    d = secret(n, e, Fn)                # Находит секретный ключ для расшифровки
    return n,e,d


def Alice_deshifr(d,public_c,n):        #Расшифровывает сообщение с помощью ключей
    sms=[]
    for i in range(len(public_c)):
        otvet=public_c[i]**d%n          #Формула для расшифровки
        sms.append(chr(otvet))
    return sms



def Bob(n,e,pol):                       #Шифровка отсылаемого сообщения
    public_c=[]
    for i in range(len(pol)):
        text = ord(pol[i])
        c = text ** e % n
        public_c.append(c)
    return public_c


def Vvod():                             #Собраны главные функции
    n, e, d = Alice()
    pol = input()
    public_c = Bob(n, e, pol)
    Vivod=Alice_deshifr(d, public_c, n)
    return Vivod

def Vivod(sms):                     #Вывод принятого сообшения
    for i in sms:
        print(i, end='')


def main():
    sms=Vvod()      #Вводим сообщение для передачи
    Vivod(sms)      #Ответ

if __name__ == '__main__':
    main()










