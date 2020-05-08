#!/bin/python3

import boto3
import os
from time import sleep

def deploy(id,num,type):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
    ImageId = id,
    MinCount = 1,
    MaxCount = num,
    InstanceType=type,
    KeyName="guy")
    print('New instanceID IS >>: ' + instance[0].id)


def stop():
    id = input('Enter the ID that you want to stop >>:')
    ids = [id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = ids).stop()


def start():
    id = input('Enter the ID that you want to start >>:')
    ids = [id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = ids).start()


def reboot():
    id = input('Enter the ID that you want to reboot >>:')
    ids = [id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = ids).reboot()


def terminate():
    id = input('Enter the ID that you want to terminate >>:')
    ids = [id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = ids).terminate()


def show():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print("---------------------------")
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
                instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id,
                instance.state
            )
        )


def get_key():
    print("""

   *******************
These are the keys :

""")
    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()
    for i in response['KeyPairs']:
        print("\nKey: " + i['KeyName'])
    return(response)


def regions_name():
    client = boto3.client('ec2')
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    n = 0
    print("All regions available >>:\n")
    for i in regions:
        n = n + 1
        print(str(n) + ". " + i)
    return regions


               ######### Menu #########

os.system("clear")
while True:
    print("""

     *****                 ******
        ***** AWS Script *****
     *****                 ******

""")
    print("""1.all AWS services from your account\n2.Deploy machines\n3.stop Instances\n4.start Instances\n5.reboot Instances\n
6.Terminate Instances\n7.Show instances\n8.Show keys\n9.Show regions\n10.Exit""")
    sleep(1)
    choose = input("Enter your choice >>:")
    if choose == "1":
        os.system("aws configure")


    elif choose == "2":
        get_key()
        print(" Ubuntu 18.04 AMI: | ami-07c1207a9d40bc3bd\n Red Hat Enterprise Linux 8 AMI: | ami-0a54aef4ef3b5f881\n Microsoft Windows 2019 AMI: | ami-08db69d5de9dc9245")
        deploy(input("Enter AMI id >>: "),int(input("Enter how many machines >>:")),input("Enter type >>: "))

    elif choose == "3":
        show()
        stop()

    elif choose == "4":
        show()
        start()

    elif choose == "5":
        show()
        reboot()

    elif choose == "6":
        show()
        terminate()

    elif choose == "7":
        show()

    elif choose == "8":
        get_key()
        
    elif choose == "9":
        regions_name()

    elif choose == "10":
        print("Bye Bye")
        break

    else:
        print ("enter 1-10 only !")
