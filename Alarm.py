__Author__ = 'Prameet Bisht'
__Version__ = "0.0.1"
__Email__ = "myprameet09@gmail.com"
__Github__ = "https://github.com/orgs/POC-AWS-services/dashboard"

import boto3

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# List alarms of insufficient data through the pagination interface
paginator = cloudwatch.get_paginator('describe_alarms')
for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
    print(response['MetricAlarms'])

# Create an alarm for a CloudWatch Metric alarm

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Create alarm
cloudwatch.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm when server CPU exceeds 70%',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
)

#Delete an alarm


# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Delete alarm
cloudwatch.delete_alarms(
  AlarmNames=['Web_Server_CPU_Utilization'],
)
