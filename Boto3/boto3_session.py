import boto3 as aws

import boto3.session
from boto3.session import Session

def session():
    sess = Session(profile_name='default', region_name='eu-west-1')
    return sess