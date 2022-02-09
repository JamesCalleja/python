import boto3

s3 = boto3.resource('s3')

count = 0 
for bucket in s3.buckets.all():
    print(bucket.name)
    count = count + 1

msg = f"\nthere are {count} S3 buckets in the account"
print(msg) 