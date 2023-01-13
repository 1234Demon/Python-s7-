def func1(city):
    with open('adr.txt') as f:
        if str(city) in f.read():
            print("true")
        else:
            print('no way')

def func2(id):
    with open('emp.txt',"r") as myfile:
        for line in myfile:
            if str(id) in line[0:3]:
                print(line)
    with open('adr.txt',"r") as myfile:
        for line in myfile:
            if 'id' in line[0:3]:
                print(line)
    with open('email.txt',"r") as myfile:
        for line in myfile:
            if 'id' in line[0:3]:
                print(line)
    with open('phone.txt',"r") as myfile:
        for line in myfile:
            if 'id' in line[0:3]:
                print(line)

# def func4(salary):
#     with open('post.txt',"r") as myfile:
#         for line in myfile:
#             if salary in line[5:]:
#                 print(line)    


def func3(id):
    count = 0
    with open('emp.txt',"r") as myfile:
        for line in myfile:
            if str(id) in line[-3:]:
                count += 1   
    print(f'There are {count} employees in department')


 