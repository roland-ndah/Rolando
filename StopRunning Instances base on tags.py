from boto3.session import Session
from botocore.exceptions import ClientError

aws_access_key = 'AKIAX4YLV74NSB2TZYO2 '
aws_secret_key = '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'
region = 'us-east-1'

def lambda_handler(event, context):
   try:
       sess = Session(aws_access_key_id=aws_access_key,
                   aws_secret_access_key=aws_secret_key)
       ec2_conn = sess.client(service_name='ec2', region_name=region)

       instance_ids = []
       reservations = ec2_conn.describe_instances(
                                Filters=[
                                    {
                                                                                'Name': 'tag:Application',
                                        'Values': [
                                            'exampleName',
                                        ]
                                    },
                                    {
                                        'Name': 'tag:Vertical',
                                        'Values': [
                                            'exampleVertical',
                                        ]
                                    },
                                    {
                                        'Name': 'instance-state-name',
                                        'Values': [
                                            'running',
                                        ]
                                    },
                                ])['Reservations']
        for reservation in reservations:
          instances = reservation['Instances']
          for instance in instances:
              instance_ids.append(instance['InstanceId'])

      print("Stopping instances: {}".format(','.join(instance_ids)))

      stopped_instances_response = ec2_conn.stop_instances(
                             InstanceIds=instance_ids)

      print(stopped_instances_response)
  except ClientError as e:
     print(e)