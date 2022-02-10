import boto3

client = boto3.client('rds')
response = client.describe_db_instances()

db_list = []
for db in response['DBInstances']:
   str = db_instance_name = db['DBInstanceIdentifier']
   db_list.append(str)
   str = db_type = db['DBInstanceClass']
   db_list.append(str)
   str = db_storage = db['AllocatedStorage']
   db_list.append(str)
   str = db_engine = db['Engine']
   db_list.append(str)
   
print(db_list)