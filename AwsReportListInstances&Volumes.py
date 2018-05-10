# Author : Amit Suneja
# Dated : 10 May 2018
# Purpose : To generate Report of AWS Enviroment , It will list Instance ID and all the volumes attached to it.

import boto3

ec2 = boto3.client('ec2')
# Get list of regions
regions = ec2.describe_regions()
# extract from Dictionary for key 'Regions' & Store output in Variable
myRegionsList = regions['Regions']
# Select Particular region of list of regions myRegionsList
for region in myRegionsList:
    myReg = (region['RegionName'])
    # Connect to particular region
    ec2 = boto3.client('ec2', region_name=myReg)
    # Pick all the instances in particular region
    myInstances = ec2.describe_instance_status()
    # Pick Instance from the Dict and Store it in List
    myListOfInstances = myInstances['InstanceStatuses']
    # Pick One Instance from List of instances
    for myInstance in myListOfInstances:
        # Pick All volumes of particular instance
        volumesList = ec2.describe_instance_attribute(InstanceId=myInstance['InstanceId'], Attribute='blockDeviceMapping')
        # Pick Particular Volume of Particular Instance
        for myVol in volumesList['BlockDeviceMappings']:
            print(myInstance['InstanceId'], myVol['DeviceName'], myVol['Ebs']['DeleteOnTermination'], myVol['Ebs']['VolumeId'])
