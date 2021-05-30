#Python 3.8
#pip install boto3

from config import SystemConfig
from backup import BackupDir
from backup import BackupMySQL

print('Bem vindo ao sistema de backup\n\n')
while True:
    print('===== MENU =====')
    print('1 - Iniciar backup do diretório: ' + SystemConfig.dir_to_upload())
    print('2 - Iniciar backup do banco de dados')
    print('0 - Sair')

    option = str(input())
    if option == '0':
        print('Saindo...')
        exit(0)
    elif option == '1':
        print('Iniciando backup dos arquivos')
        BackupDir.start()
        print('Fim do programa')
    elif option == '2':
        print('Iniciando backup do banco de dados.')
        BackupMySQL.start()
        print('Fim do programa')
