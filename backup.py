class BackupDir:
    @classmethod
    def start(cls):
        import os
        from config import SystemConfig
        from aws import S3

        dir = SystemConfig.dir_to_upload()
        file_exceptions = SystemConfig.exceptions()

        # doing loop in directory
        for file in os.scandir(dir):
            # loop in exeptions for each file, verify extension exception
            ignore = False
            for extension_exception in file_exceptions:
                # if file extension equal any in exception, so ignore
                if file.path.endswith("." + extension_exception):
                    print('Arquivo ignorado (extenção na lista de exceção): ' + file.path)
                    ignore = True
                    continue
                # else go to upload files
            if not ignore and os.path.isfile(file.path) and S3.upload_file(file.path):
                print('Upload de ' + file.path + " realizado com sucesso.\n")
            elif not ignore:
                print('Erro na hora de fazer upload do arquivo: ' + file.path + "\n")


class BackupMySQL:
    @classmethod
    def start(cls):
        import os
        import time
        from config import SystemConfig
        from aws import S3
        from config import MySQLConfig

        DB_HOST = MySQLConfig.host()
        DB_USER = MySQLConfig.user()
        DB_USER_PASSWORD = MySQLConfig.password()
        DB_NAME = MySQLConfig.dbname()
        BACKUP_PATH = os.path.abspath(SystemConfig.dir_to_upload() + "database_backup")

        if not os.path.isdir(BACKUP_PATH):
            os.mkdir(BACKUP_PATH)

        # Getting current DateTime to create the separate backup folder like "20210530-123433".
        DATETIME = time.strftime('%Y%m%d-%H%M%S')
        bkp_file = (BACKUP_PATH + "\\" + DB_NAME + '-' + DATETIME + '.sql"')
        dumpcmd = 'mysqldump -h' + DB_HOST + ' -u' + DB_USER + ' -p' + DB_USER_PASSWORD + ' ' + DB_NAME + ' > "' + bkp_file
        os.system(dumpcmd)

        print('')
        print('Script de backup completo\n')
        print('Arquivo de backup criado com sucesso.')
        if SystemConfig.upload_to_s3_after_mysql_backup():
            print('Fazendo upload para AWS S3')
            S3.upload_file(SystemConfig.dir_to_upload() + "database_backup/" + DB_NAME + '-' + DATETIME + '.sql')
            print('Arquivo de backup enviado para S3');
