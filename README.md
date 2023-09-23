# Amazon EC2 AMI Backup Using Lambda Functions

## Overview

This project demonstrates how to automate Amazon Machine Image (AMI) backups for your Amazon Elastic Compute Cloud (EC2) instances using AWS Lambda functions. It includes logging and alerting features using Amazon Simple Notification Service (SNS) to enhance monitoring and notifications. If you would like to check out the detailed explanation and coding part, please find the report. Thank you.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Installation](#installation)
- [Contributors](#contributors)


## Prerequisites

Before setting up the AMI backup solution, make sure you have the following prerequisites in place:

- An AWS account with appropriate permissions to create and manage Lambda functions, CloudWatch Events, SNS topics, and EC2 resources.
- AWS CLI and AWS SAM CLI (Serverless Application Model CLI) installed and configured.
- Basic knowledge of AWS Lambda, CloudWatch Events, SNS, and EC2.

## Architecture

![ ]()![AWS Backup drawio](https://github.com/PradipMugithe/AutomationOfAmazonEC2AMIBackup/assets/78589162/2e5a38f2-8b95-4383-8d4e-6f40fcc1ccb7)


The architecture of this solution involves the following components:

**Backup and cleanup of EC2 AMIs**

- This project's major goal is to automate the backup and cleaning of Amazon Machine Images (AMIs) for EC2 Instances. This automation is accomplished through the use of -Python-based AWS Lambda functions. The method starts by creating backups (AMIs) for each EC2 Instance. These backups are planned and carried out at regular intervals to ensure data consistency and availability. Furthermore, the project contains a cleanup process that detects and removes EC2 AMIs that are more than 30 days old. This automated technique decreases the need for manual intervention, reduces the danger of data loss, and optimizes AWS resource use.

**AWS SNS notification**
- The project leverages Amazon Simple Notification Service (SNS) to improve monitoring and alerting. When the cleanup procedure deletes older EC2 AMIs, an SNS notice is sent. This message, which contains critical information about the cleaning procedure, is delivered to a registered email address or other defined endpoints. AWS CloudWatch is used for auditing and troubleshooting by capturing logs and analytics. The project guarantees that important stakeholders receive timely warnings and notifications by including SNS in the design, enabling proactive reaction to backup and cleaning events.
## Installation
```
git clone https://github.com/PradipMugithe/AutomationOfAmazonEC2AMIBackup.git
cd ec2-ami-backup
Change the variable for your requirement: BACKUP_RETENTION_DAYS, EC2_INSTANCE_TAGS

```

## Contributors
- [Pradeep Mugithe](https://linkedin.com/in/pradeep-mugithe)


