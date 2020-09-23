aws cloudwatch put-metric-data --namespace RdbCluster \
    --dimensions AutoScalingGroupName=rdb-asg-1234ABCDE,InstanceId=i-1234567890abcdef \
    --metric-name MemoryUsage --unit Bytes --value 1000
