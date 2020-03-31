#!/bin/python3

#job1

import boto3
from time import sleep
import requests
import os

def deploy(id,num,type,key):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
    ImageId = id,
    MinCount = 1,
    MaxCount = num,
    InstanceType=type,
    KeyName=key,
    GroupName='ssh')
    print('New instanceID IS : ' + instance[0].id)


def stop():
    id = input('Enter the id that you want to stop : ')
    ids = [id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = ids).stop()


def start():
    id = input('Enter id that you want to start : ')
    ids = [id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = ids).start()


def reboot():
    id = input('Enter the ID that you want to reboot : ')
    ids = [id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = ids).reboot()


def terminate():
    id = input('Enter the ID that you want to terminate : ')
    ids = [id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = ids).terminate()

def go_back():
    a = 0
    while a == 0:
        back = input("Do you want to go back to the main menu?\n")
        if back == "yes" or back == "Yes" or back == "YES":
            print("Going back...")
            sleep(1)
            a = 1
            acc = 0
        elif back == "no" or back == "No" or back == "NO":
            print("that`s ok!")
            a = 1
            acc = 1
            account = 1
        else:
            print("Please choose yes or no")
            sleep(1)


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
    print("These are the keys :")
    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()
    for i in response['KeyPairs']:
        print("\nKey: " + i['KeyName'])
    return(response)



def regions_name():
    client = boto3.client('ec2')
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    n = 0
    print("All regions available: \n")
    for i in regions:
        n = n + 1
        print(str(n) + ". " + i)
    return regions


def get_services(aws_access_key,aws_secret_key,region_name):
    session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region_name)

    services = session.get_available_services()
    print("Available services for: " + region_name)
    n = 0
    for i in services:
        n = n + 1
        print(str(n) + ". " + i)


               ######### Menu #########


while True:
    print("------------------------")
    print("1.all AWS services from your account\n2.Deploy machines\n3.stop Instances\n4.start Instances\n5.reboot Instances\n6.Terminate Instances\n7.Show instances\n8.Show keys\n9.Show regions\n10.Exit")
    print("------------------------")
    sleep(1)
    choose = input("Enter 1 - 10 Pls :")
    if choose == "1":
        get_services(input("Enter aws_access_key:\n"),input("Enter aws_secret_key:\n"),input("Enter region name:\n"))


    elif choose == "2":
        get_key()
        deploy(input("Enter AMI id: "),int(input("Enter how many machines: ")),input("Enter type: "),input("Key type :"))


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
        print ("enter 1-10 only")

