import boto3
import datetime

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
        myCurrentDateAndTime = datetime.datetime.now()
        createImageID = ec2.create_image(InstanceId=myInstance['InstanceId'], Name='AMI_' + myInstance['InstanceId'] + myCurrentDateAndTime.strftime('_%Y-%m-%d_%H-%M'), NoReboot=True)
