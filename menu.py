import first_start
import read_book
import write
import func
from read import read_emp as r1
from read import read_adr as r2
from read import read_email as r3
from read import read_phone as r4
from read import read_dep as r5
from read import read_post as r6

def menu():
    global fstart
    fstart = 0
    if fstart == 0:
        first_start.first_create
        fstart = 1
        a1 = int(input('Wonna write, read or function? (1-Write, 2-Read, 3-Function) '))
    if a1 == 1:
        a2 = int(input('Which book? (1-employee, 2-adress, 3-email, 4-phone, 5-department, 6-posts) '))
        if a2 == 1:
            emp = r1()
            write.wr_inf(emp, 6, 'emp.txt')
        elif a2 == 2:
            adr = r2()
            write.wr_inf(adr, 6, 'adr.txt')        
        elif a2 == 3:
            email = r3()
            write.wr_inf(email, 0, 'email.txt')    
        elif a2 == 4:
            phone = r4()
            write.wr_inf(phone, 0, 'phone.txt')
        elif a2 == 5:
            dep = r5()
            write.wr_inf(dep, 2, 'dep.txt')
        else:
            post = r6()
            write.wr_inf(post, 2, 'post.txt')
    elif a1 == 2:
        a3 = int(input('Which book? (1-employee, 2-adress, 3-email, 4-phone, 5-department, 6-posts) '))
        if a3 == 1:
            read_book.read('emp.txt')
        elif a3 == 2:
            read_book.read('adr.txt')        
        elif a3 == 3:
            read_book.read('email.txt')    
        elif a3 == 4:
            read_book.read('phone.txt')
        elif a3 == 5:
            read_book.read('dep.txt')
        else:
            read_book.read('post.txt')
    else:
        a4 = int(input('What you want? (1-Find smb from city?, 2-view all information about contact, 3-Number of employees in department) '))
        if a4 == 1:
            func.func1(input('Enter city which you want to find: '))
        elif a4 == 2:
            func.func2(input('Enter ID: '))
        else:
            func.func3(input('Enter ID department'))