def read_emp():
    emp = []
    print('Avaible employees:')
    with open('emp.txt', 'r') as file: print(*file)
    emp.append(input('\nEnter ID: '))
    emp.append(input('Enter surname: '))
    emp.append(input('Enter name: '))
    emp.append(input('Enter partronymic name: '))
    emp.append(input('Enter date of birth: '))
    print('Avaible posts:')
    with open('post.txt', 'r') as file: print(*file)
    emp.append(input('\nEnter ID post: '))
    print('Avaible departments:')
    with open('dep.txt', 'r') as file: print(*file)
    emp.append(input('Enter ID department: '))
    print(emp)
    return emp

def read_adr():
    adr = []
    print('Avaible employees:')
    with open('emp.txt', 'r') as file: print(*file)
    adr.append(input('\nEnter ID: '))
    adr.append(input('Enter city: '))
    adr.append(input('Enter street: '))
    adr.append(input('Enter house number: '))
    adr.append(input('Enter house block number: '))
    adr.append(input('Enter house block letter: '))
    adr.append(input('Enter flat number: '))
    print(adr)
    return adr

def read_email():
    email = []
    print('Avaible employees:')
    with open('emp.txt', 'r') as file: print(*file)
    email.append(input('\nEnter ID: '))
    email.append(input('Enter email: '))
    print(email)
    return email

def read_phone():
    phone = []
    print('Avaible employees:')
    with open('emp.txt', 'r') as file: print(*file)
    phone.append(input('\nEnter ID: '))
    phone.append(input('Enter phone number: '))
    print(phone)
    return phone

def read_dep():
    dep = []
    print('Avaible departments:')
    with open('dep.txt', 'r') as file: print(*file)
    dep.append(input('\nEnter ID department: '))
    print('Avaible employees:')
    with open('emp.txt', 'r') as file: print(*file)
    dep.append(input('\nEnter ID of superior: '))
    dep.append(input('Enter name of department: '))
    print(dep)
    return dep

def read_post():
    post = []
    print('Avaible employees:')
    with open('emp.txt', 'r') as file: print(*file)
    post.append(input('\nEnter ID of superior: '))
    post.append(input('Enter name of post: '))
    post.append(input('Enter salary: '))
    print(post)
    return post
