#!/usr/bin/python
import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_images(
    Filters=[
        {
            "Name": "product-code",
            "Valules": [
                "a9e7i60gidrc5x9nd7z3qyjj5"
            ]
        }
    ]
)

print(response)