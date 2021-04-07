# Avi Networks CloudFormation Template
This template and Lambda package will deploy an Avi Vantage 20.1.4 3-node cluster into your region of choice.

## Pre-requsites
- You must have an SSH keypair in the region you wish to deploy into.
- The Avi Vantage product should be scribed to in the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B01ICD3R7E).

## Notes
- Deployment can take up to 30 minutes
- Currently the controllers do not have public IP enabled, so NAT to the internet is required for AWS Cloud Orchestration.
- A bastion host is deployed for demo purposes. RDP, username is admin, password is what was supplied for the Avi Controller.
- CFN completes after the cluster configuration is completed. It may take another 5 minutes for the cluster to initialize and be ready to accept configuration.