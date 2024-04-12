# Secure Static Web Application on AWS

This project demonstrates how to deploy a secure and scalable static web application on AWS using Infrastructure as Code (IaC) and Configuration Management tools. The application serves a simple "Hello World" page over HTTPS, with only the appropriate ports publicly exposed and HTTP traffic redirected to HTTPS.

## Architecture

The application architecture consists of the following components:

- **AWS CloudFormation**: Provisions the necessary infrastructure resources, including VPC, subnets, security groups, EC2 instances, Application Load Balancer, and SSL/TLS certificates.
- **Ansible**: Configures the web server instances, installs Apache, deploys the web content, configures SSL/TLS, and redirects HTTP traffic to HTTPS.
- **AWS CodePipeline, CodeBuild, and CodeDeploy**: Automates the deployment process using a CI/CD pipeline.
- **Automated Testing**: Validates the web server configuration using Ansible playbooks and the `ansible-lint` tool.

## Prerequisites

- AWS account
- AWS CLI
- Ansible

Deploy the CloudFormation stack:
aws cloudformation create-stack --stack-name SecureWebApp --template-body file://cloudformation.yml --parameters ParameterKey=EnvironmentName,ParameterValue=dev

This will provision the necessary infrastructure resources.

Update the Ansible inventory file  with the public IP or DNS name of the web server instance.

Run the Ansible playbook to configure the web server:

This will install Apache, deploy the web content, configure SSL/TLS, and redirect HTTP to HTTPS.

(Optional) Set up the CI/CD pipeline using AWS CodePipeline, CodeBuild, and CodeDeploy.

Access the web application using the DNS name of the Application Load Balancer (ALB) over HTTPS.

## Testing

The project includes automated tests to validate the web server configuration. To run the tests, execute the following command:
