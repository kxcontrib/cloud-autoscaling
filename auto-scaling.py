import boto3


def get_metadata(asg_name):
    """
    Get meta data of an autoscaling group
    """
    asg = boto3.client('autoscaling')
    res = asg.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    return res['AutoScalingGroups'][0]


def get_desired_capacity(asg_name):
    """
    Find the current DesiredCapacity of an ASG
    """
    res = get_metadata(asg_name)
    return res['DesiredCapacity']


def set_desired_capacity(asg_name, desired_capacity):
    """
    Set the DesiredCapacity of an ASG
    Instances will either be terminated or launched once this is done
    """
    asg = boto3.client('autoscaling')
    res = asg.set_desired_capacity(AutoScalingGroupName=asg_name,
                                   DesiredCapacity=desired_capacity,
                                   HonorCooldown=False)
    return res


def increment_desired_capacity(asg_name):
    """
    Increase the DesiredCapacity of the ASG by 1
    """
    current = get_desired_capacity(asg_name)
    res = set_desired_capacity(asg_name, current + 1)
    return res


def terminate_instance_from_asg(instance_id):
    """
    Terminate the ec2 instance and reduce the DesiredCapacity
    """
    asg = boto3.client('autoscaling')
    res = asg.terminate_instance_in_auto_scaling_group(
        InstanceId=instance_id,
        ShouldDecrementDesiredCapacity=True
        )
    return res
