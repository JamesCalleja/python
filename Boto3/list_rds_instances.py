from turtle import st
import boto3

client = boto3.client('rds')
response = client.describe_db_instances()

db_dictionary = {}

for db in response['DBInstances']:
   str = db['DBInstanceIdentifier']
   key_value = {'db_name': str}
   db_dictionary.update(key_value)

   str = db['DBInstanceClass']
   key_value = {'DBInstanceClass': str}
   db_dictionary.update(key_value)

   str = db['AllocatedStorage']
   key_value = {'AllocatedStorage': str}
   db_dictionary.update(key_value)

   str = db['Engine']
   key_value = {'Engine': str}
   db_dictionary.update(key_value)

   print(db_dictionary["db_name"], db_dictionary["AllocatedStorage"])
   print(db_dictionary)


# import boto3

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


new_lines = f"\n\n\n"
print(new_lines, db_list)