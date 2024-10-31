'''Реализовать программу, в которой пользователь вводит два числа a и b
и требуется вывести все целые числа, расположенные между ними.'''

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 
    
while True:
    a = input('Введите 1-е число:') 
    b = input('Введите 2-е число:') 
    if is_number(a) and is_number(b):
        low = round(min(float(a),float(b)))
        up = round(max(float(a),float(b)))
        for i in range(low+1,up):
            print(i)
        break
    else:
        print('Вы неправильно ввели число')
        break
