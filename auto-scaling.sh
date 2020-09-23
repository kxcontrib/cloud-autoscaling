aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name rdb-asg-1234ABCD

aws autoscaling set-desired-capacity --auto-scaling-group-name rdb-asg-1234ABCD --desired-capacity 2

aws autoscaling terminate-instance-in-auto-scaling-group --instance-id i-1234567890abcdef --should-decrement-desired-capacity
