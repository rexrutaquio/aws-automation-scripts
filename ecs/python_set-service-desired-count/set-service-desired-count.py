#!/bin/bash

# Set AWS region
AWS_REGION="ap-southeast-2"

# Prompt for the ECS cluster name
read -p "Enter the ECS cluster name: " CLUSTER_NAME

# Prompt for the desired count
read -p "Enter the desired count for the services: " DESIRED_COUNT

# Fetch the list of services in the specified cluster
SERVICES=$(aws ecs list-services --region "$AWS_REGION" --cluster "$CLUSTER_NAME" --query "serviceArns[]" --output text)

if [ -z "$SERVICES" ]; then
  echo "No services found in the cluster $CLUSTER_NAME."
  exit 1
fi

# Iterate over each service and update the desired count
for SERVICE in $SERVICES; do
  SERVICE_NAME=$(basename "$SERVICE")
  echo "Updating service $SERVICE_NAME to desired count $DESIRED_COUNT..."
  aws ecs update-service --region "$AWS_REGION" --cluster "$CLUSTER_NAME" --service "$SERVICE_NAME" --desired-count "$DESIRED_COUNT"
  if [ $? -eq 0 ]; then
    echo "Successfully updated service $SERVICE_NAME."
  else
    echo "Failed to update service $SERVICE_NAME."
  fi
done

echo "All services in the cluster $CLUSTER_NAME have been updated to desired count $DESIRED_COUNT."
