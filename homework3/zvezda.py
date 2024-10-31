
for i in range(10):
    for j in range(10):
        if i == 0 or i == 10 - 1 or j == 0 or j == 10 - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')  
    print()
    
      
