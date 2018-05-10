# Author : Amit Suneja
# Dated : 10 May 2018
# Purpose : To generate Report of AWS Enviroment , It will list Instance ID and all the volumes attached to it.


import boto3

ec2 = boto3.client('ec2')
# Get list of regions
regions = ec2.describe_regions()
myRegionsList = (regions['Regions'])
for region in myRegionsList:
    myReg = (region['RegionName'])
    ec2 = boto3.client('ec2', region_name=myReg)
    myInstances = ec2.describe_instance_status()
    myListOfInstances = myInstances['InstanceStatuses']
    for myInstance in myListOfInstances:
        ec2 = boto3.resource('ec2', region_name=myReg)
        myParticularInstance = ec2.Instance(myInstance['InstanceId'])
        volumesOfMyParticularInstance = myParticularInstance.volumes.all()
        for volume in volumesOfMyParticularInstance:
            print(myInstance['InstanceId'], myReg, volume.id, volume.size
            
