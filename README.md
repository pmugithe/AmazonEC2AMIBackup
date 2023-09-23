# Amazon EC2 AMI Backup Using Lambda Functions

## Overview

This project demonstrates how to automate Amazon Machine Image (AMI) backups for your Amazon Elastic Compute Cloud (EC2) instances using AWS Lambda functions. It includes logging and alerting features using Amazon Simple Notification Service (SNS) to enhance monitoring and notifications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Installation](#installation)
- [Contributing](#contributing)


## Prerequisites

Before setting up the AMI backup solution, make sure you have the following prerequisites in place:

- An AWS account with appropriate permissions to create and manage Lambda functions, CloudWatch Events, SNS topics, and EC2 resources.
- AWS CLI and AWS SAM CLI (Serverless Application Model CLI) installed and configured.
- Basic knowledge of AWS Lambda, CloudWatch Events, SNS, and EC2.

## Architecture

![Architecture Diagram]()![AWS Backup drawio](https://github.com/PradipMugithe/AutomationOfAmazonEC2AMIBackup/assets/78589162/2e5a38f2-8b95-4383-8d4e-6f40fcc1ccb7)


The architecture of this solution involves the following components:
- EC2 Instances: Your Amazon Elastic Compute Cloud instances running your applications.
-
## Installation
```
git clone https://github.com/PradipMugithe/AutomationOfAmazonEC2AMIBackup.git
cd ec2-ami-backup
Change the variable for your requirement: BACKUP_RETENTION_DAYS, EC2_INSTANCE_TAGS

```

## Contributing
-
-
-


