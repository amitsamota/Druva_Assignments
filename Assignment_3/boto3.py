import boto3

#for s3 bucket
s3_resource  = boto3.resource('s3')


s3_client = boto3.client('s3')

#s3_client = s3_resource.meta.client()


