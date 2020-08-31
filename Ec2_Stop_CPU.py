import boto3
client = boto3.client('s3')

Buckets  = client.list_buckets()

for bucket in Buckets:
      response = client.put_bucket_encryption(Bucket= bucket, ContentMD5='ndah2', ServerSideEncryptionConfiguration={'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}},]})