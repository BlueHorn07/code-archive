from boto3 import client

s3_client = client('s3')

S3_BUCKET = "target-bucket-name"
PREFIX = "prefix-path/"

paginator = s3_client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=S3_BUCKET, Prefix=PREFIX)

BYTE_TO_GB = 1024 * 1024 * 1024
PRINT_PERIOD = 10000
total_size_gb = 0
total_count = 0

for page in pages:

    for key in page['Contents']:
        total_size_gb += (key['Size'] / BYTE_TO_GB)
    total_count += page['KeyCount']
    
    if total_count % PRINT_PERIOD == 0:
        print(f'{total_count:,} Objects')
        print(f'{total_size_gb:.3f} GB')


print(f'{total_count:,} Objects')
print(f'{total_size_gb:.3f} GB')
