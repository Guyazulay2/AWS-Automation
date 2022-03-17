import boto3


client = boto3.client('ec2')
response = client.describe_instances(
    InstanceIds=[
        'i-0a793005d909ccefd',
    ],
)
for pythonins in response['Reservations']:
  for printout in pythonins['Instances']:
    print(printout['State']['Name'])
    
    
    
    
    
    
    
    
    
   ------------------------
  
  
  
  
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
  for printout in pythonins['Instances']:
    print(printout['InstanceId'])
    print(printout['InstanceType'])
    print(printout['State']['Name'])
