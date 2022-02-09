from email.policy import default
import boto3 as aws

import boto3.session
from boto3.session import Session

sess = Session(profile_name=default region_name='eu-west-1')