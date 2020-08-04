__Author__ = 'Prameet Bisht'
__Version__ = "0.0.1"
__Email__ = "myprameet09@gmail.com"
__Github__ = "https://github.com/orgs/POC-AWS-services/dashboard"


import boto3


# Create CloudWatchEvents client
cloudwatch_events = boto3.client('events')

# Put an event rule
response = cloudwatch_events.put_rule(
    Name='DEMO_EVENT',
    RoleArn='IAM_ROLE_ARN',
    ScheduleExpression='rate(5 minutes)',
    State='ENABLED'
)
print(response['RuleArn'])