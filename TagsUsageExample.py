import boto3
ec2_client = boto3.client("ec2", region_name="us-east-1")

description = ec2_client.describe_instances(
    Filters=[
        {'Name': 'tag-key', 'Values': ['Department']}, {'Name': 'tag-value', 'Values': ['HR']},
        {'Name': 'tag-key', 'Values': ['env']}, {'Name': 'tag-value', 'Values': ['dev']}
    ]
)
print(description)
