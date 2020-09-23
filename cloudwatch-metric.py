from boto3 import client
from datetime import datetime

def put_metric_data(namespace, asg_name, instance_id, name, unit, value):
    """
    Send Metric Data for an EC2 Instance in an AutoScaling group to Cloudwatch
    """
    cloudwatch = client('cloudwatch')
    # build the metric data dictionary
    data = {
       'MetricName': name,
       'Dimensions': [
           { 'Name': 'AutoScalingGroupName', 'Value': asg_name },
           { 'Name': 'InstanceId', 'Value': instance_id }
           ],
       'Timestamp': datetime.now(),
       'Value': value,
       'Unit': unit
       }
    # send the data to aws
    cloudwatch.put_metric_data(Namespace=namespace,
                               MetricData=[data])


put_metric_data('RdbCluster', 'rdb-asg-1234ABCDE', 'i-1234567890abcdef', 
    'MemoryUsage', 'bytes', 1000)
