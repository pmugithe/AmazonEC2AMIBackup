import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    backup_time = datetime.utcnow() + timedelta(minutes=5)
    response = ec2.describe_instances()
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ami_name = f"{instance_id}-{backup_time.strftime('%Y-%m-%d-%H-%M-%S')}"
            print(ami_name)
            response = ec2.create_image(InstanceId=instance_id, Name=ami_name+"test", NoReboot=True)
            image_id = response['ImageId']
            ec2.create_tags(Resources=[image_id], Tags=[{'Key': 'backup', 'Value': 'true'}])

    response = ec2.describe_images(Filters=[{'Name': 'tag:backup', 'Values': ['true']}])
    for image in response['Images']:
        creation_time = datetime.strptime(image['CreationDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if (datetime.utcnow() - creation_time) > timedelta(day=30):
            ec2.deregister_image(ImageId=image['ImageId'])