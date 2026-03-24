# 🚀 EduQuiz Pro - AWS Deployment Guide

Deploy your professional MCQ generator to AWS with this comprehensive guide.

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [AWS Services Overview](#aws-services-overview)
3. [Deployment Options](#deployment-options)
4. [Option 1: AWS App Runner (Easiest)](#option-1-aws-app-runner-easiest)
5. [Option 2: EC2 + Docker](#option-2-ec2--docker)
6. [Option 3: ECS Fargate](#option-3-ecs-fargate)
7. [Database Setup](#database-setup)
8. [Environment Variables](#environment-variables)
9. [Cost Estimation](#cost-estimation)

---

## Prerequisites

### AWS Account Setup
- ✅ Active AWS account
- ✅ AWS CLI installed: `brew install awscli` (macOS)
- ✅ Configure AWS credentials: `aws configure`
- ✅ AWS account with appropriate IAM permissions

### Tools Required
```bash
# Install AWS CLI
brew install awscli

# Install Docker
brew install docker

# Verify installations
aws --version
docker --version
```

### Local Setup
```bash
# Clone/backup your project
cd /Applications/mcq_generator_llama

# Ensure .env file exists with Groq API key
cat .env
```

---

## AWS Services Overview

| Service | Purpose | Cost |
|---------|---------|------|
| **App Runner** | Container deployment (easiest) | ~$1-5/month |
| **EC2** | Virtual server (more control) | ~$5-50/month |
| **RDS** | Managed database (optional) | ~$10-30/month |
| **S3** | File storage for PDFs | ~$0.50-2/month |
| **ALB** | Load balancer | ~$15-20/month |

---

## Deployment Options

### Quick Comparison

| Option | Ease | Cost | Control | Best For |
|--------|------|------|---------|----------|
| **App Runner** | ⭐⭐⭐⭐⭐ | Low | Low | Quick deployment |
| **EC2 + Docker** | ⭐⭐⭐ | Low-Medium | High | Full control |
| **ECS Fargate** | ⭐⭐⭐⭐ | Medium | Medium | Scalability |

---

## Option 1: AWS App Runner (Easiest)

### Step 1: Create Dockerfile

Create `Dockerfile` in your project root:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8501

# Set Streamlit config
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true

# Run app
CMD ["streamlit", "run", "app.py"]
```

### Step 2: Create .dockerignore

```
__pycache__
*.pyc
.git
.env
venv/
.DS_Store
*.db
outputs/
.streamlit/
```

### Step 3: Push to GitHub

```bash
# Initialize git (if not already)
cd /Applications/mcq_generator_llama
git init

# Add all files
git add .

# Commit
git commit -m "Add Docker deployment files"

# Push to GitHub (replace with your repo)
git remote add origin https://github.com/YOUR_USERNAME/mcq-generator-llama.git
git branch -M main
git push -u origin main
```

### Step 4: Deploy via AWS App Runner

**Via AWS Console:**

1. Go to AWS App Runner (https://console.aws.amazon.com/apprunner)
2. Click "Create service"
3. Select "Source code repository"
4. Connect GitHub account
5. Select your repository
6. Configure:
   - **Runtime**: Python 3.13
   - **Port**: 8501
   - **Environment variables**:
     ```
     GROQ_API_KEY=your_key_here
     STREAMLIT_SERVER_PORT=8501
     ```
7. Click "Deploy"

**Via AWS CLI:**

```bash
# Create App Runner service
aws apprunner create-service \
  --service-name eduquiz-pro \
  --source-configuration \
    RepositoryType=GITHUB,\
    GitHubConfiguration={RepositoryUrl=https://github.com/YOUR_USERNAME/mcq-generator-llama,Branch=main} \
  --instance-configuration \
    Cpu=1,\
    Memory=2048 \
  --tags \
    Key=Project,Value=EduQuiz
```

**Access your app:**
- URL will be provided in App Runner console
- Example: `https://abcd1234.us-east-1.apprunner.amazonaws.com`

---

## Option 2: EC2 + Docker

### Step 1: Launch EC2 Instance

```bash
# Via AWS CLI
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.small \
  --key-name your-key-pair \
  --security-groups streamlit-sg

# Or use AWS Console:
# - Launch Ubuntu 22.04 LTS
# - t3.small or t3.medium instance
# - Allow ports: 22 (SSH), 80 (HTTP), 443 (HTTPS), 8501 (Streamlit)
```

### Step 2: SSH into Instance

```bash
# Get instance IP from AWS Console
ssh -i /path/to/key.pem ubuntu@your-instance-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Step 3: Clone and Deploy

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/mcq-generator-llama.git
cd mcq-generator-llama

# Create .env file
cat > .env << EOF
GROQ_API_KEY=your_key_here
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
EOF

# Build Docker image
docker build -t eduquiz-pro .

# Run container
docker run -d \
  --name eduquiz \
  -p 8501:8501 \
  --env-file .env \
  eduquiz-pro
```

### Step 4: Setup Nginx Reverse Proxy

```bash
# Install Nginx
sudo apt install nginx -y

# Create Nginx config
sudo tee /etc/nginx/sites-available/eduquiz > /dev/null << EOF
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable site
sudo ln -s /etc/nginx/sites-available/eduquiz /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

### Step 5: Setup SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

---

## Option 3: ECS Fargate

### Step 1: Create ECR Repository

```bash
# Create ECR repository
aws ecr create-repository --repository-name eduquiz-pro

# Get login token
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# Build and push image
docker build -t eduquiz-pro .
docker tag eduquiz-pro:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/eduquiz-pro:latest
docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/eduquiz-pro:latest
```

### Step 2: Create ECS Task Definition

Create `task-definition.json`:

```json
{
  "family": "eduquiz-pro",
  "containerDefinitions": [
    {
      "name": "eduquiz-pro",
      "image": "YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/eduquiz-pro:latest",
      "portMappings": [
        {
          "containerPort": 8501,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "GROQ_API_KEY",
          "value": "your_key_here"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/eduquiz-pro",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "requiresCompatibilities": ["FARGATE"],
  "networkMode": "awsvpc",
  "cpu": "512",
  "memory": "1024"
}
```

### Step 3: Deploy ECS Service

```bash
# Register task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

# Create ECS cluster
aws ecs create-cluster --cluster-name eduquiz-cluster

# Create service
aws ecs create-service \
  --cluster eduquiz-cluster \
  --service-name eduquiz-pro \
  --task-definition eduquiz-pro \
  --desired-count 1 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-xxx],assignPublicIp=ENABLED}"
```

---

## Database Setup

### Option A: RDS PostgreSQL (Recommended for Production)

```bash
# Create RDS instance
aws rds create-db-instance \
  --db-instance-identifier eduquiz-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password YourSecurePassword123! \
  --allocated-storage 20
```

### Option B: Keep SQLite with S3 Backup

```bash
# Create S3 bucket for backups
aws s3 mb s3://eduquiz-backups-$(date +%s)

# Add backup script to cron
# 0 2 * * * aws s3 cp /app/users.db s3://eduquiz-backups/users.db
```

---

## Environment Variables

### Create AWS Secrets Manager Secret

```bash
# Create secret
aws secretsmanager create-secret \
  --name eduquiz-pro/config \
  --secret-string '{
    "GROQ_API_KEY":"your_key_here",
    "DATABASE_URL":"sqlite:///users.db",
    "STREAMLIT_SERVER_PORT":"8501"
  }'

# Reference in ECS task definition
```

### Or use Parameter Store

```bash
# Store parameters
aws ssm put-parameter \
  --name /eduquiz/groq-api-key \
  --value "your_key_here" \
  --type SecureString

aws ssm put-parameter \
  --name /eduquiz/streamlit-port \
  --value "8501" \
  --type String
```

---

## Cost Estimation

### Monthly Costs (Approximate)

**App Runner:**
- Compute: $1-5
- Data transfer: $0-2
- **Total: $1-7/month**

**EC2 + Docker:**
- t3.small instance: $7-10
- Elastic IP: $3-5
- Data transfer: $1-3
- **Total: $11-18/month**

**ECS Fargate:**
- vCPU: $0.04048/hour ≈ $30/month
- Memory: $0.004445/GB/hour ≈ $33/month (for 1GB)
- Data transfer: $1-3
- **Total: $64-66/month**

---

## Troubleshooting

### Common Issues

**1. Docker build fails**
```bash
# Check Docker logs
docker logs eduquiz

# Rebuild with verbose output
docker build --progress=plain -t eduquiz-pro .
```

**2. Streamlit connection issues**
```bash
# Check if port is open
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxx \
  --protocol tcp \
  --port 8501 \
  --cidr 0.0.0.0/0
```

**3. API key not loading**
```bash
# Verify environment variable
docker exec eduquiz env | grep GROQ_API_KEY

# Check .env file permissions
ls -la .env
```

**4. Database permission issues**
```bash
# Fix permissions in container
chmod 666 /app/users.db
chmod 755 /app/
```

---

## Next Steps

1. ✅ Choose deployment option
2. ✅ Prepare Dockerfile and configs
3. ✅ Set up AWS resources
4. ✅ Configure environment variables
5. ✅ Deploy application
6. ✅ Monitor and scale

## Support

For issues, check:
- AWS CloudWatch logs
- Container logs: `docker logs eduquiz`
- Application logs: Check Streamlit output

---

**Happy Deploying! 🚀**
