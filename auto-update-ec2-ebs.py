import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    ec2_ids = []
    rds_ids = []
    ebs_ids = []
    detail = event['detail']
    print(detail)
    print(event)
    tags=[
        {
            'Key': 'Name',
            'Value': 'JJTECH'
        },
        {
            'Key': 'Name',
            'Value': 'JJTECH'
        }
    ]
    eventname = detail['eventName']
    if eventname == 'RunInstances':
        ec2_client = boto3.client('ec2')
        items = detail['responseElements']['instancesSet']['items']
        for item in items:
            ec2_ids.append(item['instanceId'])
            response = ec2_client.create_tags(
                Resources=ec2_ids,
                Tags=tags
            )
        print(response)
    if eventname == 'CreateDBInstance':
        rds_client = boto3.client('rds')
        db_instance_ARN = detail['responseElements']['dBInstanceArn']
        # db_instance_name = (detail['responseElements']['dBName'])
        rds_ids.append(db_instance_ARN)
        for id in rds_ids:
            response = rds_client.add_tags_to_resource(
                ResourceName=id,
                Tags=tags
            )
        print(response)

    if eventname == 'CreateVolume':
        ec2_client = boto3.client('ec2')
        ebs_ids.append(detail['responseElements']['volumeId'])
        for id in ebs_ids:
            response = ec2_client.create_tags(
                Resources=ec2_ids,
                Tags=tags
            )
        print(response)


    print(event)
