import pulumi
import pulumi_aws as _aws

sg = _aws.ec2.SecurityGroup("web-app-sg",description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ])


ami = _aws.get_ami(most_recent="true",
                  owners=["amazon"],
                  filters=[{"name":"name","values":["amzn-ami-hvm-*"]}])

user_data = """
#!bin/bash
uname -n > index.html
nohup python -m SimpleHTTPServer 80 &
"""

instance = _aws.ec2.Instance(
    "my-web-app",instance_type="t2.micro",
    security_groups=[sg.name],
    ami=ami.id, user_data=user_data
)

pulumi.export('publicIp', instance.public_ip)
pulumi.export('publicHostName', instance.public_dns)
