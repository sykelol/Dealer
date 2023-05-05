from storages.backends.s3boto3 import S3Boto3Storage
import os
from dotenv import load_dotenv
import boto3

load_dotenv()

class PublicS3Boto3Storage(S3Boto3Storage):
    bucket_name = os.environ.get('AWS_PUBLIC_BUCKET_NAME', '')
    default_acl = 'public-read'
    querystring_auth = False
    custom_domain = f'{bucket_name}.s3.amazonaws.com'
    location = 'static/'

class PrivateS3Boto3Storage(S3Boto3Storage):
    bucket_name = os.environ.get('AWS_PRIVATE_BUCKET_NAME', '')
    default_acl = 'private'
    custom_domain = False
    location = 'media/'
    file_overwrite = False
    querystring_auth = True  # This line ensures that the pre-signed URLs are generated
    querystring_expire = 3600  # The number of seconds the pre-signed URL is valid for