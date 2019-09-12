import os

import boto3


def upload_file(file_name, bucket, object_name=None):
    region = os.environ.get('AWS_REGION', None)

    client = boto3.client('s3', region_name=region)
    transfer = boto3.s3.transfer.S3Transfer(client=client)
    transfer.upload_file(file_name, bucket, object_name)
    print('upload file ' + str(file_name) + ' to object' + str(object_name))
