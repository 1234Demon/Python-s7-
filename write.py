def wr_inf(inf, z, nfile):
    with open(nfile, 'a') as file:
        for i in range(len(inf)):
            if i == z:
                file.write(f'{inf[i]}')
            else:
                file.write(f'{inf[i]}, ')

        file.write('\n')

