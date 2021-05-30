class AWSConfig:
    __access_key = ''
    __security_key = ''
    __region = 'us-east-1'

    @classmethod
    def access_key(cls):
        return cls.__access_key

    @classmethod
    def security_key(cls):
        return cls.__security_key

    @classmethod
    def region(cls):
        return cls.__region


class S3Config:
    __bucket = 'upe-cloud-computing'

    @classmethod
    def bucket(cls):
        return cls.__bucket


class MySQLConfig:
    __host = 'localhost'
    __user = 'root'
    __password = 'root'
    __dbname = 'casadospobres'

    @classmethod
    def host(cls):
        return cls.__host

    @classmethod
    def user(cls):
        return cls.__user

    @classmethod
    def password(cls):
        return cls.__password

    @classmethod
    def dbname(cls):
        return cls.__dbname


class SystemConfig:
    __dir_to_upload = 'arquivos_para_upload/'
    __file_exceptions = ['exe', 'bat']
    __upload_to_s3_after_mysql_backup = False

    @classmethod
    def dir_to_upload(cls):
        return cls.__dir_to_upload

    @classmethod
    def exceptions(cls):
        return cls.__file_exceptions

    @classmethod
    def upload_to_s3_after_mysql_backup(cls):
        return cls.__upload_to_s3_after_mysql_backup
