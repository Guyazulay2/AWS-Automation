#!/bin/python3

import boto3
import os
from time import sleep

def Install():
    print("<< Install packeges for AWS CLI >>")
    os.system("sudo apt-get update && sudo apt-get install python3-pip && sudo apt-get install awscli && sudo apt install python3-setuptools python3-pip")

def Deploy(id,num,type):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
    ImageId = id,
    MinCount = 1,
    MaxCount = num,
    InstanceType=type,
    SecurityGroupIds=["NVIDIA Deep Learning AMI-20-03-1-AutogenByAWSMP-"],
    KeyName="Newkey")
    print('New instanceID IS >>: ' + instance[0].id)

def Stop():
    s = int(input('how much instances do you want to Stop? :'))
    for i in range(s):
        id = input('Enter the id that you want to Stop >>:')
        ids = [id]
        ec2 = boto3.resource('ec2')
        ec2.instances.filter(InstanceIds = ids).stop()

def Start():
    x = int(input('how much instances do you want to Start? :'))
    for i in range(x):
        id = input('Enter the ID that you want to Start >>:')
        ids = [id]
        ec2 = boto3.resource('ec2')
        ec2.instances.filter(InstanceIds = ids).start()

def Reboot():
    a = int(input('how much instances do you want to Reboot? :'))
    for i in range(a):
        id = input('Enter the ID that you want to Reboot >>:')
        ids = [id]
        ec2 = boto3.resource('ec2')
        ec2.instances.filter(InstanceIds = ids).reboot()

def Terminate():
    r = int(input('how much instances do you want to Terminate? :'))
    for i in range(r):
        id = input('Enter the ID that you want to Terminate >>:')
        ids = [id]
        ec2 = boto3.resource('ec2')
        ec2.instances.filter(InstanceIds = ids).terminate()


def Show():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print("---------------------------")
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
                instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id,
                instance.state
            )
        )


def Get_key():
    print("""
   *******************
These are the keys :
""")
    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()
    for i in response['KeyPairs']:
        print("\nKey: " + i['KeyName'])
    return(response)


def Regions_name():
    client = boto3.client('ec2')
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    n = 0
    print("All regions available >>:\n")
    for i in regions:
        n = n + 1
        print(str(n) + ". " + i)
    return regions


####### Menu #########

os.system("clear")
while True:
    print("** Aws EC2 script **")
    print("""1| AWS CLI\n2| Deploy machines\n3| stop Instances\n4| start Instances\n5| reboot Instances\n
6| Terminate Instances\n7| Show instances\n8| Show keys\n9| Show regions\n10| Install Packages for AWS CLI\n11| Exit""")
    sleep(1)


    choose = input("Enter your choice >>:")
    if choose == "1":
        os.system("aws configure")

    elif choose == "2":
        print("    NVIDIA Deep Learning AMI : | ami-0bc1398a752880427\n    Ubuntu 18.04 AMI : | ami-07c1207a9d40bc3bd")
        print("    Instance type : g4dn.xlarge , g4dn.2xlarge , g4dn.4xlarge , p3.2xlarge")
        Deploy(input("Enter AMI id >>: "),int(input("Enter how many machines >>:")),input("Enter type >>: "))

    elif choose == "3":
        Show()
        Stop()

    elif choose == "4":
        Show()
        Start()

    elif choose == "5":
        Show()
        Reboot()

    elif choose == "6":
        Show()
        Terminate()

    elif choose == "7":
        Show()

    elif choose == "8":
        Get_key()

    elif choose == "9":
        Regions_name()

    elif choose == "10":
        Install()

    elif choose == "11":
        print("Exit")
        break

    else:
        print ("enter 1-10 only !")
