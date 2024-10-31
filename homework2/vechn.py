
while True:
    a = input('Введите 1-е целое число:') 
    b = input('Введите 2-е целое число:') 
    if a == 'end' or b == 'end':
        break 
    if a.isdigit() and b.isdigit():
        int(a),
        int(b)
        print(f'Сумма {a} и {b}:{int(a)+int(b)}')
    else:
        print('Вы неправильно ввели целое число'),
  
    print("Чтобы закончить программу напишите 'end' в 'a' или 'b'")
    