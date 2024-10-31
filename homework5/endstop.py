
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 
summ = 0    
while True:
    a = input('Введите число:')  
    if a == 'end' or a == 'stop':
        print(f'Сумма всех введенных чисел {summ}')
        break 
    if is_number(a):
        summ = summ + float(a)
    else:
        print('Вы неправильно ввели число'),
    print("Чтобы закончить программу напишите 'end' или 'stop'")