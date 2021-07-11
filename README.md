Installations and connection to aws service


# Centos
    Install Pip :
        yum -y update
        yum -y install python3-pip
    install AWSCLI :
        pip install awscli
    install boto3:
        pip3 install boto3






# Ubuntu
To get started with aws services you need to install python3, and boto3 :

    sudo apt-get update
    sudo apt-get install python3-pip
    pip3 install boto3
    pip3 install --upgrade awscli
    sudo apt install python3-setuptools python3-pip
    pip3 install --user pip
    pip install --user streamlink
    
    
    
    
    

Write in the command line : aws configure

And it will show you that 

To get services put your 


    aws_access_key_id = xxxxxxxxxxxxxxxxxxxxxxxx

    aws_secret_access_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    region= For example [us-east-2]
    
