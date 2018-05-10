import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
myAllImagesID = ec2.describe_images(Owners=['self'])
for image in myAllImagesID['Images']:
    print(image)
