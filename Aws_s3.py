#!/bin/python3


import boto3
import os
from time import sleep

def Show():
    print("--- All buckets ---")
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print("Bucket name :",bucket.name)


def Directory():
    choose = input("Do you want to :\n(1) | Create directory inside bucket\n(2) | Delete directory inside bucket\n Your choice >:")
    if choose == "1" or choose == "create":
        buck = input("Enter the bucket name >:")
        create = input("Enter the directory name that you want to create >:")
        s3 = boto3.client('s3')
        bucket_name = buck
        directory_name = create
        s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))

    elif choose == "2":
        s3 = boto3.resource('s3')
        buck = input("Enter the bucket name >:")
        dir = input("Enter the directory that you want to delete >:")
        bucket = s3.Bucket(buck)
        for obj in bucket.objects.filter(Prefix=dir):
            s3.Object(bucket.name,obj.key).delete()

def Create_delete():
    choose = input("Do you want to :\n(1) | Create buckets\n(2) | Delete buckets\n Your choice >:")
    if choose == "1" or choose == 'create':
        a = int(input("How much buckets do you want to Create? :"))
        for i in range(a):
            c = input("Enter the new Bucket name >:")
            region = input("Enter the region >:")
            s3 = boto3.resource('s3')
            s3.create_bucket(Bucket=c, CreateBucketConfiguration={'LocationConstraint': region})

    elif choose == "2" or choose == 'delete':
        r = int(input("How much buckets do you want to Delete? :"))
        for i in range(r):
            name = input("Enter the bucket name to Delete >:")
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(name)
            bucket.delete()


def Upload():
    c = int(input("How many files do you want to upload? :"))
    for i in range(c):
        name = input("Enter the bucket name >:")
        file = input("Enter the file name")
        data = open(file, 'rb')
        s3 = boto3.client('s3')
        s3.put_object(Bucket=name, Key=file, Body=data)

os.system("clear")
while True:
    print("""
     ******                 ******
      ***** AWS S3 script ******
     ******                 ******
""")
    print("1| all AWS services from your account\n2| Show Buckets\n3| Create/delete buckets\n4| Delete/Create direcrory\n5| Upload Files\n6| Exit")
    sleep(0.5)
    choose = input("Enter your choice >>:")
    if choose == "1":
        os.system("aws configure")

    elif choose == "2":
        Show()

    elif choose == "3":
        Create_delete()

    elif choose == "4":
        Show()
        Directory()

    elif choose == "5":
        Show()
        Upload()

    elif choose == "6":
        print("ByeBye")
        break
