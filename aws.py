import boto3
from botocore.exceptions import ClientError
import boto3
from config import AWSConfig
from config import S3Config
import logging


class S3:

    def upload_file(file_name, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        # Config in config.py
        s3_client = boto3.client('s3', AWSConfig.region(),
                                 aws_access_key_id=AWSConfig.access_key(),
                                 aws_secret_access_key=AWSConfig.security_key())
        try:
            response = s3_client.upload_file(file_name, S3Config.bucket(), object_name)
            logging.info(response)
        except ClientError as e:
            logging.error(e)
            return False
        return True
