from importlib.resources import contents
from urllib import response
import boto3

from app import BUCKET

def upload(file_name, bucket, object_name):
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response


def download(file_name, bucket):
    s3 = boto3.resource('s3')
    output = f"download_files/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)
    return output

def buck_create(Bucketname):
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=Bucketname)

def delete(file_name, bucket):
    s3 = boto3.resource('s3')
    s3.delete_object(bucket,file_name)
    output = f"{file_name} is deleted"
    return output

def move():
    s3 = boto3.resource('s3')
    copy_source = {
        'Bucket': 'mybucket', # Source Bucket Name 
        'Key': 'mykey'        # Source File Name
    }
    #'otherbucket' - Destination Bucket Name
    #'otherkey' - Destination File Name
    s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')

def list_all_files(bucket):
    s3 = boto3.client('s3')
    contents = []
    for item in s3.list_objects_v2(Bucket=bucket)['Contents']:
        contents.append(item)
    return contents

def show_bucket():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    contents=[]
    for bucket in response['Buckets']:
        contents.append(bucket)
    return contents
