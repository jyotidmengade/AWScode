# AWScode
This script starts or stops EC2 instances based on a specific tag key and value using Boto3.
pip install boto3
# Start instances with tag Env=Dev
manage_ec2_instances('start', 'Env', 'Dev')

# Stop instances with tag Env=Test
manage_ec2_instances('stop', 'Env', 'Test')

Useful for auto-scaling, cost-saving schedules, or managing dev/test EC2 instances in bulk.
