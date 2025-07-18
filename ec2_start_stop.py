import boto3

def manage_ec2_instances(action, tag_key, tag_value, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    filters = [{'Name': f'tag:{tag_key}', 'Values': [tag_value]}]
    instances = ec2.describe_instances(Filters=filters)

    instance_ids = [i['InstanceId'] for r in instances['Reservations'] for i in r['Instances']]
    if not instance_ids:
        print("No instances found.")
        return

    if action == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
        print(f'Started: {instance_ids}')
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f'Stopped: {instance_ids}')
    else:
        print("Invalid action")

# Example:
# manage_ec2_instances('start', 'Env', 'Dev')
