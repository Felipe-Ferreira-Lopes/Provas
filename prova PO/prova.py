def cal_megabytes (bytes):
    megabytes = bytes / 1000
    return megabytes

with open ('usuarios.txt', 'r') as fonte:
    texto = fonte.readlines()
    with open ('relatorio.txt', 'w') as relatorio:
        print('ACME Inc.               Uso do espaco em disco pelos usuarios')
        print('-------------------------------------------------------------------------')
        print('Nr.  Usuario            Espaco utilizado            ''%'' do uso')
        number = 1
        for linha in texto:
            print("{}    {}".format(number,linha))
            number += 1
            cal_megabytes (linha)
            print(cal_megabytes)

