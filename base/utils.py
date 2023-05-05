import boto3
from django.conf import settings

def generate_signed_url(file_key, expiration=3600):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

    url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': settings.AWS_PRIVATE_BUCKET_NAME, 'Key': file_key},
        ExpiresIn=expiration
    )

    return url