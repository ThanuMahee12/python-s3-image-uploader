import boto3
from botocore.exceptions import NoCredentialsError
# Creating an S3 access object
s3= boto3.client("s3",)
