import boto3

iams = boto3.resource("iam")

roles = iams.roles.all()

count = 0 
for role in roles:
    print(role.role_name)
    count = count + 1 

msg = f"\nThere are {count} roles in the account"

print(msg)