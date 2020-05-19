import boto3


def get_instance_ids(ec2_resource):
    id_list = list()
    for instance in ec2_resource.instances.all():
        id_list.append(instance.id)
    return id_list

def get_ebs_ids(ec2_resource):
    id_list = list()
    volume_iterator = ec2_resource.volumes.all()
    for v in volume_iterator:
        id_list.append(v.id)
    return id_list

def create_default_tags(ec2_client,ids,tags):
    response = ec2_client.create_tags(
            Resources=ids,
            Tags=tags
        )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Tags Created Successfully")

def lambda_handler(event,context):
    regions=['us-west-2','us-east-2','us-east-1']
    for region in regions:
        ec2_client = boto3.client('ec2', region)
        ec2_resource = boto3.resource('ec2', region)
        tags = [
            {
                'Key': 'BarometerIT',
                'Value': 'test'
            },
            {
                'Key': 'costcenter',
                'Value': 'test'
            },
            {
                'Key': 'Application',
                'Value': 'test'
            },
            {
                'Key': 'Owner Department',
                'Value': 'test'
            },
            {
                'Key': 'ResourceType',
                'Value': 'test'
            },
            {
                'Key': 'Environment',
                'Value': 'test'
            }
        ]
    instance_ids = get_instance_ids(ec2_resource)
    create_default_tags(ec2_client, instance_ids, tags)
    ebs_ids = get_ebs_ids(ec2_resource)
    create_default_tags(ec2_client, ebs_ids, tags)
