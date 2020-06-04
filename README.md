# pulumi-project
Create a webserver with Pulumi and Python

Pre-requisites:
* Pulumi Account
* Python > 3.6
* AWS account and AWS CLI configured

How it works:

Pulumi is a multi-cloud Infra-as-a-code service provider. What sets it apart from others is that it maintains the state of your infrastructure. That means, after deploying the infrastructure via Pulumi, if something is manually changed from within the AWS console, it will be able to detect the changes. Also, you can check the revision history to the stack from the web interface.

You can run via the CommandLine:

 - pulumi preview : To see the changes to the stack

 - pulumi up : To deploy the changes to the cloud. A confirmation will be asked before deployment
    
 - pulumi destroy : To delete all the infra created from the stack

 - pulumi refresh : To detect any changes done manually to the infra