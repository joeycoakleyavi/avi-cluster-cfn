# Avi Networks CloudFormation Template
This template and Lambda package will deploy an Avi Vantage 20.1.4 3-node cluster into your region of choice.

## Pre-requsites
- You must have an SSH keypair in the region you wish to deploy into.
- The Avi Vantage product should be subscribed to in the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B01ICD3R7E).

## Notes
- Deployment can take up to 30 minutes
- CFN completes after the cluster configuration is completed. It may take another 5 minutes for the cluster to initialize and be ready to accept configuration.
