def first_create():
    a = ['ID', 'surname', 'name', 'partronymic name', 'date of birth', 'ID post', 'ID department']
    with open('emp.txt', 'a') as file:
        file.write('\n')
        for i in range(len(a)):
            if i == 6:
                file.write(a[i])
            else:
                file.write(f'{a[i]}, ')

        file.write('\n')
    
    b = ['ID', 'city', 'street', 'house number', 'house block number', 'house block letter', 'flat number']
    with open('adr.txt', 'a') as file:
        file.write('\n')
        for i in range(len(b)):
            if i == 6:
                file.write(b[i])
            else:
                file.write(f'{b[i]}, ')

        file.write('\n')
    
    c = ['ID', 'email']
    with open('email.txt', 'a') as file:
        file.write('\n')
        for i in range(len(c)):
            if i == 1:
                file.write(c[i])
            else:
                file.write(f'{c[i]}, ')  

        file.write('\n')  
    
    d = ['ID', 'phone number']
    with open('phone.txt', 'a') as file:
        file.write('\n')
        for i in range(len(d)):
            if i == 1:
                file.write(d[i])
            else:
                file.write(f'{d[i]}, ')

        file.write('\n')

    e = ['ID department', 'ID of superior', 'name of department'] 
    with open('dep.txt', 'a') as file:
        file.write('\n')
        for i in range(len(e)):
            if i == 2:
                file.write(e[i])
            else:
                file.write(f'{e[i]}, ')

        file.write('\n')

    f = ['ID of superior', 'name of post', 'salary']
    with open('post.txt', 'a') as file:
        file.write('\n')
        for i in range(len(f)):
            if i == 2:
                file.write(f[i])
            else:
                file.write(f'{f[i]}, ')

        file.write('\n')
