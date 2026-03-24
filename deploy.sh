#!/bin/bash

# EduQuiz Pro - AWS Deployment Script
# This script automates the deployment to AWS

set -e

echo "🚀 EduQuiz Pro - AWS Deployment Script"
echo "======================================="

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
AWS_REGION=${AWS_REGION:-us-east-1}
PROJECT_NAME="eduquiz-pro"
SERVICE_NAME="eduquiz-pro"

# Functions
print_step() {
    echo -e "${BLUE}→ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Step 1: Check prerequisites
print_step "Checking prerequisites..."

if ! command -v aws &> /dev/null; then
    print_warning "AWS CLI not found. Installing..."
    brew install awscli
fi

if ! command -v docker &> /dev/null; then
    print_warning "Docker not found. Installing..."
    brew install docker
fi

print_success "Prerequisites checked"

# Step 2: Get AWS account ID
print_step "Getting AWS account information..."
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
print_success "AWS Account ID: $AWS_ACCOUNT_ID"

# Step 3: Create ECR repository
print_step "Creating ECR repository..."
ECR_REPO_NAME="$PROJECT_NAME"

aws ecr describe-repositories --repository-names "$ECR_REPO_NAME" --region "$AWS_REGION" 2>/dev/null || {
    aws ecr create-repository \
        --repository-name "$ECR_REPO_NAME" \
        --region "$AWS_REGION" \
        --image-tag-mutability MUTABLE \
        --image-scanning-configuration scanOnPush=true
    print_success "ECR repository created"
}

ECR_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:latest"
print_success "ECR URL: $ECR_URL"

# Step 4: Build and push Docker image
print_step "Building Docker image..."
docker build -t "$PROJECT_NAME:latest" .
print_success "Docker image built"

print_step "Logging in to ECR..."
aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
print_success "Logged in to ECR"

print_step "Tagging Docker image..."
docker tag "$PROJECT_NAME:latest" "$ECR_URL"
print_success "Docker image tagged"

print_step "Pushing Docker image to ECR..."
docker push "$ECR_URL"
print_success "Docker image pushed to ECR"

# Step 5: Create CloudWatch Log Group
print_step "Creating CloudWatch Log Group..."
LOG_GROUP="/ecs/$PROJECT_NAME"
aws logs create-log-group --log-group-name "$LOG_GROUP" --region "$AWS_REGION" 2>/dev/null || true
aws logs put-retention-policy --log-group-name "$LOG_GROUP" --retention-in-days 7 --region "$AWS_REGION"
print_success "Log group configured"

# Step 6: Check for App Runner or ECS
print_step "Choose deployment method:"
echo "1. AWS App Runner (easiest)"
echo "2. AWS ECS Fargate (more control)"
read -p "Enter choice (1 or 2): " deployment_choice

case $deployment_choice in
    1)
        print_step "Deploying to AWS App Runner..."
        
        # Create App Runner service
        SERVICE_ROLE_ARN=$(aws iam get-role --role-name AppRunnerServiceRole 2>/dev/null | jq -r '.Role.Arn' || echo "")
        
        if [ -z "$SERVICE_ROLE_ARN" ]; then
            print_step "Creating IAM role for App Runner..."
            aws iam create-role --role-name AppRunnerServiceRole \
                --assume-role-policy-document '{
                    "Version": "2012-10-17",
                    "Statement": [{
                        "Effect": "Allow",
                        "Principal": {"Service": "apprunner.amazonaws.com"},
                        "Action": "sts:AssumeRole"
                    }]
                }'
            
            aws iam attach-role-policy --role-name AppRunnerServiceRole \
                --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
            
            SERVICE_ROLE_ARN="arn:aws:iam::$AWS_ACCOUNT_ID:role/AppRunnerServiceRole"
        fi
        
        # Check if service exists
        if aws apprunner describe-service --service-arn "arn:aws:apprunner:$AWS_REGION:$AWS_ACCOUNT_ID:service/$SERVICE_NAME" --region "$AWS_REGION" 2>/dev/null; then
            print_step "Updating existing App Runner service..."
            aws apprunner update-service \
                --service-arn "arn:aws:apprunner:$AWS_REGION:$AWS_ACCOUNT_ID:service/$SERVICE_NAME" \
                --source-configuration ImageRepository={ImageIdentifier="$ECR_URL",ImageRepositoryType=ECR,ImageConfiguration={Port=8501,RuntimeEnvironmentVariables={GROQ_API_KEY=$GROQ_API_KEY}}} \
                --region "$AWS_REGION"
        else
            print_step "Creating new App Runner service..."
            aws apprunner create-service \
                --service-name "$SERVICE_NAME" \
                --source-configuration ImageRepository={ImageIdentifier="$ECR_URL",ImageRepositoryType=ECR,ImageConfiguration={Port=8501,RuntimeEnvironmentVariables={GROQ_API_KEY=$GROQ_API_KEY}}} \
                --instance-configuration Cpu=1,Memory=2048 \
                --auto-scaling-configuration MaxSize=4,MinSize=1,MaxConcurrency=100 \
                --tags Key=Project,Value=EduQuizPro Key=Environment,Value=Production \
                --region "$AWS_REGION"
        fi
        
        print_success "App Runner deployment initiated"
        print_step "Getting service URL..."
        sleep 10
        SERVICE_URL=$(aws apprunner describe-service --service-arn "arn:aws:apprunner:$AWS_REGION:$AWS_ACCOUNT_ID:service/$SERVICE_NAME" --region "$AWS_REGION" | jq -r '.Service.ServiceUrl')
        print_success "Service URL: $SERVICE_URL"
        ;;
        
    2)
        print_step "ECS Fargate deployment not yet configured in this script"
        print_warning "Please follow the manual steps in AWS_DEPLOYMENT.md"
        ;;
        
    *)
        print_warning "Invalid choice"
        exit 1
        ;;
esac

# Step 7: Summary
print_step "Deployment Summary"
echo "===================="
echo "Project: $PROJECT_NAME"
echo "Region: $AWS_REGION"
echo "ECR URL: $ECR_URL"
echo "Log Group: $LOG_GROUP"
echo ""
print_success "Deployment complete! 🎉"
echo ""
echo "Next steps:"
echo "1. Add your Groq API key to the App Runner service environment variables"
echo "2. Set a custom domain (optional)"
echo "3. Monitor your application in AWS Console"
echo "4. Check CloudWatch logs: aws logs tail $LOG_GROUP --follow"
