# ECS Cluster Desired Count Updater

This script is designed to update the desired count for all services in a specified ECS cluster. It prompts the user to input the ECS cluster name and the desired count, then applies the desired count to all services in the cluster.

## Prerequisites

- **AWS CLI**: Ensure the AWS CLI is installed and configured on the machine where the script will be run.
  - Run `aws configure` to set up your AWS credentials and default region.
- **Bash**: The script is written in Bash and should be executed on a system with a Bash shell.
- **AWS IAM Permissions**: The user or role executing this script must have the following permissions:
  - `ecs:ListServices`
  - `ecs:UpdateService`

## Script Overview

### Features
1. Prompts for the ECS cluster name.
2. Prompts for the desired count for all services in the cluster.
3. Updates the desired count for each service in the specified ECS cluster.

### AWS Region
The script is configured to use the `ap-southeast-2` AWS region. You can modify this by changing the `AWS_REGION` variable in the script.

## How to Use

1. Clone or download this script to your local system.
2. Ensure the script has execution permissions:

   - <chmod +x set-service-desired-count.py>
   
3. Run the script:
   - <.\set-service-desired-count.py>
4. Follow the prompts to:
- Enter the ECS cluster name.
- Enter the desired count for the services in the cluster.


Script Workflow
1. Prompts the user for:
- The name of the ECS cluster.
- The desired count for the services.
2. Fetches the list of service ARNs in the specified cluster using aws ecs list-services.
3. Iterates through each service ARN, extracts the service name, and updates the desired count using aws ecs update-service.

  
*****  Example Usage: 

$ ./update_ecs_services.sh
Enter the ECS cluster name: TestCluster
Enter the desired count for the services: 3
Updating service service1 to desired count 3...
Successfully updated service service1.
Updating service service2 to desired count 3...
Successfully updated service service2.
All services in the cluster TestCluster have been updated to desired count 3.


Error Handling: 
 If no services are found in the specified cluster, the script will display:
  - No services found in the cluster <ClusterName>.
If an error occurs while updating a service, it will display:
  - Failed to update service <ServiceName>.



Notes:
- This script updates all services in the specified ECS cluster to the same desired count. To update specific services, the script will require modifications.
Always test scripts in a development or staging environment before using them in production.
