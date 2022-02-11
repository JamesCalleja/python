import json
import boto3


client = boto3.client('ec2')
response = client.describe_instances()

#print(response)

instance_dictionary = {}

count = 0
for i in response['Reservations']:
    for x in i['Instances']:
        str = x['InstanceId']
        key_value = {'InstanceId': str}
        instance_dictionary.update(key_value)
        count += 1 

    print(instance_dictionary)

msg = f'\nThere are {count} instances in the account.'
print(msg)

